import requests
import json

url = "https://fakestoreapi.com"

# 🎨 Helper for color output (works in most terminals)
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# 🧩 Pretty print JSON safely
def print_json(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))

# 1️⃣ READ — Get all products
def get_all_products():
    response = requests.get(f"{url}/products")
    if response.status_code == 200:
        data = response.json()
        print(f"\n{CYAN}--- All Products ({len(data)}) ---{RESET}")

        for item in data:
            print(f"""
🆔 ID: {item['id']}
📦 Title: {item['title']}
💰 Price: ${item['price']}
📂 Category: {item['category']}
🖼️ Image: {item['image']}
📝 Description: {item['description']}
{'-'*80}
""")

    else:
        print(f"{RED}Error:{RESET} {response.status_code}")


# 2️⃣ READ — Get single product
def get_product():
    try:
        pid = int(input("Enter Product ID: "))
    except ValueError:
        print(f"{RED}Invalid ID! Please enter a number.{RESET}")
        return

    response = requests.get(f"{url}/products/{pid}")
    if response.status_code == 200:
        print(f"\n{CYAN}--- Product Details ---{RESET}")
        print_json(response.json())
    elif response.status_code == 404:
        print(f"{RED}❌ Product not found.{RESET}")
    else:
        print(f"{RED}Error:{RESET} {response.status_code}")

# 3️⃣ CREATE — Add a new product
def create_product():
    print("\nEnter product details:")
    title = input("Title: ").strip()
    if not title:
        print(f"{RED}Title cannot be empty.{RESET}")
        return
    try:
        price = float(input("Price: "))
    except ValueError:
        print(f"{RED}Invalid price! Enter a number.{RESET}")
        return
    description = input("Description: ").strip() or "No description"
    image = input("Image URL (press Enter for default): ").strip() or "https://i.pravatar.cc"
    category = input("Category: ").strip() or "general"

    new_product = {
        "title": title,
        "price": price,
        "description": description,
        "image": image,
        "category": category
    }

    response = requests.post(f"{url}/products", json=new_product)
    if response.status_code in (200, 201):
        print(f"{GREEN}✅ Product created successfully!{RESET}")
        print_json(response.json())
    else:
        print(f"{RED}Error:{RESET} {response.status_code}")

# 4️⃣ UPDATE — Modify existing product
def update_product():
    try:
        pid = int(input("Enter Product ID to update: "))
    except ValueError:
        print(f"{RED}Invalid ID! Please enter a number.{RESET}")
        return

    print("Enter new details (leave blank to skip):")
    title = input("New Title: ").strip()
    price = input("New Price: ").strip()

    updated_data = {}
    if title:
        updated_data["title"] = title
    if price:
        try:
            updated_data["price"] = float(price)
        except ValueError:
            print(f"{RED}Invalid price! Update cancelled.{RESET}")
            return

    if not updated_data:
        print(f"{YELLOW}No changes entered. Nothing to update.{RESET}")
        return

    response = requests.patch(f"{url}/products/{pid}", json=updated_data)
    if response.status_code == 200:
        print(f"{GREEN}✅ Product updated successfully!{RESET}")
        print_json(response.json())
    else:
        print(f"{RED}Error:{RESET} {response.status_code}")

# 5️⃣ DELETE — Remove a product
def delete_product():
    try:
        pid = int(input("Enter Product ID to delete: "))
    except ValueError:
        print(f"{RED}Invalid ID! Please enter a number.{RESET}")
        return

    confirm = input(f"⚠️  Are you sure you want to delete product {pid}? (y/n): ").lower()
    if confirm != "y":
        print(f"{YELLOW}Delete cancelled.{RESET}")
        return

    response = requests.delete(f"{url}/products/{pid}")
    if response.status_code == 200:
        print(f"{GREEN}✅ Product deleted successfully!{RESET}")
    else:
        print(f"{RED}Error:{RESET} {response.status_code}")

# 6️⃣ Menu System
def menu():
    while True:
        print(f"""
{CYAN}========== FakeStore API CRUD =========={RESET}
1️⃣  View all products
2️⃣  View single product by ID
3️⃣  Add a new product
4️⃣  Update an existing product
5️⃣  Delete a product
6️⃣  Exit
""")
        choice = input("Enter your choice (1–6): ").strip()

        if choice == "1":
            get_all_products()
        elif choice == "2":
            get_product()
        elif choice == "3":
            create_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            print(f"{GREEN}👋 Exiting program... Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice! Please enter a number 1–6.{RESET}")

# Entry point
if __name__ == "__main__":
    menu()
