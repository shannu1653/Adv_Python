#1. #print s
# rows=9
# for i in range(1,rows+1):
#     s=""
#     for j in range(1,rows+1):
#         if i==1 or i==rows or i==(rows//2)+1:
#             s+="* "
#         elif j==1 and i<(rows//2)+1:
#             s+="* "
#         elif j==rows and i>(rows//2)+1:
#             s+="* "
#         else:
#             s+="  "
#     print(s)

#2.print H
# rows=9
# for i in range(1,rows+1):
#     s=""
#     for j in range(1,rows+1):
#         if j==1 or j==rows or i==(rows//2)+1:
#             s+="* "
#         else:
#             s+="  "
#     print(s)

#3.print A
# rows=9
# for i in range(rows):
#     s=""
#     for j in range(rows):
#         if i == 0 and j > 0 and j < rows-1:
#             s += "* "
#         elif (j == 0 or j == rows-1) and i != 0:
#             s += "* "
#         elif i == rows//2:
#             s += "* "
#         else:
#             s += "  "
#     print(s)

#4.print N
# rows=5
# for i in range(rows):
#     s=""
#     for j in range(rows):
#         if j==0 or j==rows-1 or j==i:
#             s+="* "
#         else:
#             s+="  "
#     print(s)

#5.Solid Square Pattern
# Problem: Print a solid square of stars of size n.
# Input: n = 4
# Output:
# * * * *
# * * * *
# * * * *
# * * * *
# rows=4
# for i in range(rows):
#     s=""
#     for j in range(rows):
#         s+="* "
#     print(s)


# 2.Solid Rectangle Pattern
# Problem: Print a solid rectangle of m rows and n columns.
# Input: m = 3, n = 5
# Output:
# * * * * *
# * * * * *
# * * * * *
### m,n=3,5
# for i in range(m):
#     s=""
#     for j in range(n):
#         s+="* "
#     print(s)

# #3.Right-Angled Triangle (Left-Aligned)
# Problem: Print a left-aligned right-angled triangle.
# Input: n = 5
# Output:
# *
# * *
# * * *
# * * * *
# * * * * *
# r=5
# for i in range(1,r+1):
#     s=""
#     for j in range(1,i+1):
#         s+="* "
#     print(s)

# for i in range(1,r+1):
#     print("* "*i)

# ##4.Right-Angled Triangle (Right-Aligned)
# Input: n = 5
# Output:
#         *
#       * *
#     * * *
#   * * * *
# * * * * *
# r = 5
# for i in range(1,r+1):
#     s=""
#     for j in range(1,r-i+1):
#         s+="  "
#     for k in range(1,1+i):
#         s+="* "
#     print(s)


'''
# r = 5
# for i in range(r, 0, -1):
#     print(" " * i, "* " * (r - i))
'''

###5.Inverted Triangle (Left-Aligned)
# Input: n = 5
# Output:
# * * * * *
# * * * *
# * * *
# * *
# *
# r=5
# for i in range(1,r+1):
#     s=""
#     for j in range(1,r-i+2):
#         s+="* "
#     print(s)

# for i in range(r,0,-1):
#     print("* "*i)



###6.Inverted Triangle (Right-Aligned)
# Input: n = 5
# Output:
# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# n=5
# for i in range(n):
#     s=""
#     for j in range(n):
#         if j>=i:
#             s+="* "
#         else:
#             s+="  "
#     print(s)
# n=5
# for i in range(n):
#     s=""
#     for j in range(i):
#         s+="  "
#     for k in range(i,n):
#         s+="* "
#     print(s)
# n=5
# for i in range(n):
#     print("  "*i + "* "*(n-i))



# ##7.Centered Pyramid Pattern
# Input: n = 4
# Output:
#       *
#     * * *
#   * * * * *
# * * * * * * *
# n=4
# for i in range(n):
#     print("  "*(n-i-1) + "* "*(2*i+1))

##8.Diamond Pattern
# Input: n = 3
# Output:
#     *
#   * * *
# * * * * *
#   * * *
#     *

# n=5
# for i in range(n):
#     print("  "*(n-i-1)+ "* "*(2*i+1))
# for i in range(n-2,-1,-1):
#     print("  "*(n-i-1)+ "* "*(2*i+1))

# for i in range(n-2,-1,-1):
#     print(i)

# rows = 5
# mid = rows // 2        # center row & center column

# for i in range(rows):
#     s = ""
#     for j in range(rows):
#         # Diamond condition using Manhattan distance
#         if abs(i - mid) + abs(j - mid) <= mid:
#             s += "* "
#         else:
#             s += "  "
#     print(s)

###9. Butterfly Pattern
# Input: n = 4
# Output:
# *       *
# * *   * *
# * * * * *
# * *   * *
# *       *

rows = 30

for i in range(rows):
    s = ""
    for j in range(rows):
        # Left and right diagonal OR middle row
        if j == i or j == rows - i - 1 or i == rows // 2 or j==0 or j==rows-1:
            s += "* "
        else:
            s += "  "
    print(s)







