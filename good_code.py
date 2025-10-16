# bad_code.py

# 1️⃣ Unused import
import os

# 2️⃣ Bad variable naming
x = 123
y = 456
z = x + y

# 3️⃣ Function too complex / bad formatting
def do_stuff(a,b,c):
  result = 0
  for i in range(a):
      if i % 2 == 0:
          result += b
      else:
          result += c
  return result

# 4️⃣ Function with no docstring
def no_doc(x,y):
  return x*y

# 5️⃣ Duplicate code
def duplicate1():
    print("Hello")
    print("Hello")

def duplicate2():
    print("Hello")
    print("Hello")

# 6️⃣ Bad practice: bare except
try:
    1/0
except:
    pass
