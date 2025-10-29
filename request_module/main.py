from flask import Flask, request, jsonify, session, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import requests

# ==================== CONFIG ====================
BASE = "https://crudcrud.com/api/b65db85c9ea349b083c7a7295d32349f"
USER_RESOURCE = "Users"
STUDENT_RESOURCE = "Std_data"
USERS_URL = f"{BASE}/{USER_RESOURCE}"
STUDENTS_URL = f"{BASE}/{STUDENT_RESOURCE}"

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Change this in production


# ==================== HELPER FUNCTIONS ====================
def find_user(email):
    res = requests.get(USERS_URL)
    if res.status_code != 200:
        return None
    for user in res.json():
        if user.get("email") == email:
            return user
    return None


def login_required():
    return "user_id" in session


# ==================== AUTH ROUTES ====================
@app.route("/")
def home():
    return render_template_string("""
    <h2>Welcome to CRUD + Login App</h2>
    <a href="/signup">Signup</a> | <a href="/login">Login</a>
    """)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template_string(SIGNUP_HTML)
    data = request.json
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")

    if not email or not password:
        return jsonify({"error": "Email and Password required"}), 400

    if find_user(email):
        return jsonify({"error": "User already exists"}), 400

    hashed = generate_password_hash(password)
    user_data = {"email": email, "password_hash": hashed, "name": name}
    r = requests.post(USERS_URL, json=user_data)

    if r.status_code in (200, 201):
        return jsonify({"message": "Signup successful"}), 201
    return jsonify({"error": r.text}), 500


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template_string(LOGIN_HTML)
    data = request.json
    email = data.get("email")
    password = data.get("password")

    user = find_user(email)
    if not user:
        return jsonify({"error": "User not found"}), 401

    if not check_password_hash(user.get("password_hash", ""), password):
        return jsonify({"error": "Invalid credentials"}), 401

    session["user_id"] = user["_id"]
    session["email"] = user["email"]
    return jsonify({"message": "Login successful"})


@app.route("/logout")
def logout():
    session.clear()
    return "<h3>Logged out successfully!</h3><a href='/login'>Login again</a>"


# ==================== STUDENT CRUD ROUTES ====================
@app.route("/dashboard")
def dashboard():
    if not login_required():
        return "<h3>Please login first.</h3><a href='/login'>Login</a>"
    return render_template_string(DASHBOARD_HTML)


@app.route("/api/students", methods=["GET", "POST"])
def students():
    if not login_required():
        return jsonify({"error": "Login required"}), 401

    if request.method == "GET":
        res = requests.get(STUDENTS_URL)
        return jsonify(res.json())

    data = request.json
    r = requests.post(STUDENTS_URL, json=data)
    return jsonify(r.json()), r.status_code


@app.route("/api/students/<id>", methods=["PUT", "DELETE"])
def student_item(id):
    if not login_required():
        return jsonify({"error": "Login required"}), 401

    if request.method == "PUT":
        r = requests.put(f"{STUDENTS_URL}/{id}", json=request.json)
        return jsonify({"message": "Updated"}), r.status_code

    if request.method == "DELETE":
        r = requests.delete(f"{STUDENTS_URL}/{id}")
        return jsonify({"message": "Deleted"}), r.status_code


# ==================== HTML TEMPLATES ====================
SIGNUP_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Signup</title>
    <style>
        body { font-family:Arial; background:#f0f4f8; display:flex; align-items:center; justify-content:center; height:100vh;}
        .card {background:white; padding:25px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.1);}
        input,button{width:100%;padding:10px;margin:8px 0;border-radius:6px;border:1px solid #ddd;}
        button{background:#007bff;color:white;border:0;}
    </style>
</head>
<body>
<div class="card">
<h3>Signup</h3>
<input id="name" placeholder="Full Name">
<input id="email" placeholder="Email">
<input id="password" placeholder="Password" type="password">
<button onclick="signup()">Signup</button>
<p id="msg"></p>
<a href="/login">Already have account? Login</a>
</div>
<script>
async function signup(){
 let name=document.getElementById('name').value;
 let email=document.getElementById('email').value;
 let password=document.getElementById('password').value;
 const res=await fetch('/signup',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({name,email,password})});
 const data=await res.json();
 document.getElementById('msg').innerText=data.message||data.error;
 if(res.ok){setTimeout(()=>window.location='/login',1000);}
}
</script>
</body>
</html>
"""

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Login</title>
    <style>
        body { font-family:Arial; background:#f0f4f8; display:flex; align-items:center; justify-content:center; height:100vh;}
        .card {background:white; padding:25px; border-radius:10px; box-shadow:0 4px 10px rgba(0,0,0,0.1);}
        input,button{width:100%;padding:10px;margin:8px 0;border-radius:6px;border:1px solid #ddd;}
        button{background:#28a745;color:white;border:0;}
    </style>
</head>
<body>
<div class="card">
<h3>Login</h3>
<input id="email" placeholder="Email">
<input id="password" placeholder="Password" type="password">
<button onclick="login()">Login</button>
<p id="msg"></p>
<a href="/signup">Create new account</a>
</div>
<script>
async function login(){
 let email=document.getElementById('email').value;
 let password=document.getElementById('password').value;
 const res=await fetch('/login',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({email,password})});
 const data=await res.json();
 document.getElementById('msg').innerText=data.message||data.error;
 if(res.ok){setTimeout(()=>window.location='/dashboard',1000);}
}
</script>
</body>
</html>
"""

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Student Dashboard</title>
<style>
body{font-family:Arial;background:#eef2f7;padding:20px;}
.card{background:white;padding:20px;border-radius:10px;box-shadow:0 2px 10px rgba(0,0,0,0.1);margin:10px;}
input,button{padding:10px;margin:5px;border-radius:6px;border:1px solid #ccc;}
button{cursor:pointer;background:#007bff;color:white;border:0;}
table{border-collapse:collapse;width:100%;}
th,td{border:1px solid #ddd;padding:8px;text-align:left;}
</style>
</head>
<body>
<h2>Student CRUD Dashboard</h2>
<button onclick="logout()">Logout</button>
<div class="card">
<h3>Add Student</h3>
<input id="id" placeholder="ID">
<input id="name1" placeholder="Name">
<input id="batch1" placeholder="Batch">
<input id="Phno" placeholder="Phone">
<input id="Role1" placeholder="Role">
<button onclick="addStudent()">Add</button>
</div>

<div class="card">
<h3>All Students</h3>
<table id="tbl"><tr><th>ID</th><th>Name</th><th>Batch</th><th>Phone</th><th>Role</th><th>Action</th></tr></table>
</div>

<script>
async function fetchStudents(){
 const res=await fetch('/api/students');
 const data=await res.json();
 const tbl=document.getElementById('tbl');
 tbl.innerHTML='<tr><th>ID</th><th>Name</th><th>Batch</th><th>Phone</th><th>Role</th><th>Action</th></tr>';
 data.forEach(s=>{
  tbl.innerHTML+=`<tr>
   <td>${s.id}</td><td>${s.name1}</td><td>${s.batch1}</td>
   <td>${s.Phno}</td><td>${s.Role1}</td>
   <td><button onclick="del('${s._id}')">Delete</button></td></tr>`;
 });
}
async function addStudent(){
 const student={id:document.getElementById('id').value,name1:document.getElementById('name1').value,batch1:document.getElementById('batch1').value,Phno:document.getElementById('Phno').value,Role1:document.getElementById('Role1').value};
 const res=await fetch('/api/students',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(student)});
 if(res.ok){alert('Added');fetchStudents();}
}
async function del(id){
 await fetch('/api/students/'+id,{method:'DELETE'});
 fetchStudents();
}
function logout(){window.location='/logout';}
fetchStudents();
</script>
</body>
</html>
"""

# ==================== MAIN ====================
if __name__ == "__main__":
    app.run(debug=True, port=5000)
