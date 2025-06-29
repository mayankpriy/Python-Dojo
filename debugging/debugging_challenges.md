# 🐛 Python Debugging Challenges

## Master the Art of Debugging Across All Python Concepts

---

### 🎯 Learning Objectives

- Master debugging techniques across all Python concepts
- Identify common bugs in real-world scenarios
- Practice systematic debugging approaches
- Build confidence in fixing complex issues

---

## 🔧 Debugging Fundamentals

### **Level 1: Basic Syntax & Logic Errors** ⭐

#### **Challenge 1: Variable Scope Confusion**

```python
# Buggy Code
def calculate_total():
    price = 100
    tax_rate = 0.1
    total = price + (price * tax_rate)
    return total

def display_receipt():
    print(f"Price: ${price}")  # ❌ NameError
    print(f"Tax: ${price * tax_rate}")  # ❌ NameError
    print(f"Total: ${total}")  # ❌ NameError

# Expected Output: Receipt with price, tax, and total
```

**🐛 Bug Type:** Variable Scope Error  
**💡 Hint:** Variables defined inside functions are local  
**🔧 Fix Strategy:** Pass variables as parameters or use global variables

---

#### **Challenge 2: Type Conversion Issues**

```python
# Buggy Code
def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average

# Test cases
scores = ["85", "92", "78", "95"]  # Strings instead of integers
result = calculate_average(scores)  # ❌ TypeError

# Expected Output: 87.5
```

**🐛 Bug Type:** Type Error  
**💡 Hint:** Check data types before operations  
**🔧 Fix Strategy:** Convert strings to integers before calculation

---

#### **Challenge 3: List Index Out of Bounds**

```python
# Buggy Code
def get_middle_element(lst):
    middle_index = len(lst) // 2
    return lst[middle_index]

# Test cases
empty_list = []
result = get_middle_element(empty_list)  # ❌ IndexError

# Expected Output: Handle empty list gracefully
```

**🐛 Bug Type:** Index Error  
**💡 Hint:** Always check list length before accessing indices  
**🔧 Fix Strategy:** Add boundary checks

---

### **Level 2: Control Flow & Functions** ⭐⭐

#### **Challenge 4: Infinite Loop**

```python
# Buggy Code
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1  # Missing this line would cause infinite loop
    print("Blast off!")

# Test case
countdown(5)  # Should print: 5, 4, 3, 2, 1, Blast off!
```

**🐛 Bug Type:** Logic Error  
**💡 Hint:** Check loop termination conditions  
**🔧 Fix Strategy:** Ensure loop variable is properly updated

---

#### **Challenge 5: Function Return Value**

```python
# Buggy Code
def find_maximum(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    # Missing return statement

# Test case
result = find_maximum([3, 7, 2, 9, 1])  # Returns None instead of 9
```

**🐛 Bug Type:** Missing Return  
**💡 Hint:** Check if function returns expected value  
**🔧 Fix Strategy:** Add return statement

---

#### **Challenge 6: Recursion Base Case**

```python
# Buggy Code
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)  # Missing base case for negative numbers

# Test case
result = factorial(-1)  # ❌ RecursionError
```

**🐛 Bug Type:** Recursion Error  
**💡 Hint:** Check base cases for edge conditions  
**🔧 Fix Strategy:** Add validation for negative numbers

---

### **Level 3: Data Structures** ⭐⭐⭐

#### **Challenge 7: Dictionary Key Error**

```python
# Buggy Code
def get_user_info(user_data, key):
    return user_data[key]  # ❌ KeyError if key doesn't exist

# Test case
user = {"name": "Alice", "age": 30}
email = get_user_info(user, "email")  # ❌ KeyError
```

**🐛 Bug Type:** Key Error  
**💡 Hint:** Use .get() method or check key existence  
**🔧 Fix Strategy:** Use .get() with default value

---

#### **Challenge 8: List Mutation**

```python
# Buggy Code
def remove_duplicates(lst):
    for i in range(len(lst)):
        if lst.count(lst[i]) > 1:
            lst.remove(lst[i])  # ❌ Modifying list while iterating
    return lst

# Test case
numbers = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(numbers)  # Unexpected behavior
```

**🐛 Bug Type:** List Mutation Error  
**💡 Hint:** Don't modify list while iterating over it  
**🔧 Fix Strategy:** Use list comprehension or create new list

---

#### **Challenge 9: Set Operations**

```python
# Buggy Code
def find_common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1.intersection(set2)  # Returns set, not list

# Test case
result = find_common_elements([1, 2, 3], [2, 3, 4])
print(result[0])  # ❌ TypeError: 'set' object is not subscriptable
```

**🐛 Bug Type:** Type Error  
**💡 Hint:** Convert set back to list if needed  
**🔧 Fix Strategy:** Use list() conversion

---

### **Level 4: Object-Oriented Programming** ⭐⭐⭐⭐

#### **Challenge 10: Class Inheritance**

```python
# Buggy Code
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

# Test case
dog = Dog("Buddy")
cat = Cat("Whiskers")
print(dog.speak())  # Works fine
print(cat.speak())  # Works fine

# But what if we try to access a non-existent attribute?
print(dog.breed)  # ❌ AttributeError
```

**🐛 Bug Type:** Attribute Error  
**💡 Hint:** Check if attributes exist before accessing  
**🔧 Fix Strategy:** Add attribute validation or use hasattr()

---

#### **Challenge 11: Method Overriding**

```python
# Buggy Code
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def area(self):
        return self.width ** 2  # Redundant calculation

# Test case
square = Square(5)
print(square.area())  # Works but inefficient
```

**🐛 Bug Type:** Design Issue  
**💡 Hint:** Consider if method override is necessary  
**🔧 Fix Strategy:** Remove redundant override or optimize calculation

---

#### **Challenge 12: Static Method**

```python
# Buggy Code
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    def divide(a, b):  # ❌ Missing @staticmethod decorator
        return a / b

# Test case
result = MathUtils.divide(10, 2)  # ❌ TypeError
```

**🐛 Bug Type:** Method Call Error  
**💡 Hint:** Check decorators for static methods  
**🔧 Fix Strategy:** Add @staticmethod decorator

---

### **Level 5: Advanced Concepts** ⭐⭐⭐⭐⭐

#### **Challenge 13: Generator Function**

```python
# Buggy Code
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Test case
fib = fibonacci_generator()
for i in range(10):
    print(next(fib))  # Works fine

# But what happens if we try to access as list?
fib_list = list(fibonacci_generator())  # ❌ Infinite loop
```

**🐛 Bug Type:** Infinite Loop  
**💡 Hint:** Generators can be infinite  
**🔧 Fix Strategy:** Limit the generator or use itertools.islice()

---

#### **Challenge 14: Decorator with Parameters**

```python
# Buggy Code
def retry(max_attempts):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
            return None
        return wrapper
    return decorator

@retry(3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ValueError("Random error")
    return "Success"

# Test case
result = unreliable_function()  # May raise exception
```

**🐛 Bug Type:** Exception Handling  
**💡 Hint:** Check exception handling logic  
**🔧 Fix Strategy:** Improve error handling and logging

---

#### **Challenge 15: Context Manager**

```python
# Buggy Code
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Test case
with FileManager("test.txt", "w") as f:
    f.write("Hello, World!")
    # What if an exception occurs here?
    raise ValueError("Something went wrong")
```

**🐛 Bug Type:** Resource Management  
**💡 Hint:** Check if context manager handles exceptions properly  
**🔧 Fix Strategy:** Ensure proper cleanup in **exit** method

---

## 🎯 Debugging Strategies

### **Systematic Approach:**

1. **🔍 Identify the Error Type**
2. **📍 Locate the Error Source**
3. **🧠 Understand the Root Cause**
4. **🔧 Apply the Fix**
5. **✅ Test the Solution**

### **Common Debugging Tools:**

- `print()` statements for tracing
- `pdb` debugger for step-by-step execution
- `logging` module for detailed logs
- IDE debuggers for visual debugging

### **Best Practices:**

- Always test with edge cases
- Use descriptive variable names
- Add proper error handling
- Document your assumptions
- Keep functions small and focused

---

## 🏆 Challenge Solutions

**Note:** Solutions are intentionally not provided to encourage independent problem-solving. Use the hints and strategies above to debug each challenge!

### **Need Help?**

- Review the specific topic in your learning materials
- Use Python's built-in `help()` function
- Consult the official Python documentation
- Practice with simpler examples first

---

_Happy Debugging! 🐛✨_
