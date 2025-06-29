# 🐍 Variables and Data Types - Questions

> **Master Python's fundamental building blocks!** 🧱

---

## 🏷️ **Question Categories**

- 🟢 **🟢 Basic** - Foundational concepts
- 🟡 **🟡 Intermediate** - Practical applications
- 🟠 **🟠 Advanced** - Complex scenarios
- 🔴 **🔴 Expert** - Real-world challenges

---

## 🟢 **Basic Level Questions** (1-6)

### Question 1: Variable Declaration and Assignment ⭐

**⏱️ Time Estimate:** 5 minutes  
**🎯 Category:** Basic Types  
**📝 Skills Tested:** Variable naming, data types

**Task:** Create variables to store different types of information about a person.

**Real-life Scenario:** You're building a user profile system for a website:

- Store person's name (text)
- Store person's age (whole number)
- Store person's height (decimal number)
- Store whether person is a student (true/false)

**Think about:**

- What types of data are you storing and how do they differ?
- How do you choose appropriate names for your variables?
- What happens when you need to store different kinds of information?

**Challenge yourself:**

- Can you create variables for additional person information (email, phone, address)?
- What if you need to store multiple people's information?

**If you can't solve this, review:** Variable naming rules, basic data types (str, int, float, bool)

**💡 Pro Tip:** Use snake_case for variable names in Python!

---

### Question 2: Understanding Data Type Conversion ⭐

**⏱️ Time Estimate:** 8 minutes  
**🎯 Category:** Type Conversion  
**📝 Skills Tested:** Type casting, conversion methods

**Task:** Demonstrate type conversion between different data types.

**Real-life Scenario:** You're processing user input from a web form:

- Convert user age input (string) to a number
- Convert price calculations (float) to display format (string)
- Handle different data formats safely

**Think about:**

- What happens when you try to use different types together?
- How can you safely convert between different data types?
- What might go wrong during type conversion?

**Challenge yourself:**

- Can you handle conversion errors gracefully?
- What if you need to validate the converted data?

**If you can't solve this, review:** Type conversion functions, implicit vs explicit conversion

**⚠️ Common Mistake:** Forgetting that `int("3.14")` will raise a ValueError!

---

### Question 3: Working with Numbers ⭐

**⏱️ Time Estimate:** 10 minutes  
**🎯 Category:** Basic Types  
**📝 Skills Tested:** Arithmetic operations, numeric types

**Task:** Perform various mathematical operations and understand numeric data types.

**Real-life Scenario:** You're building a simple calculator for a retail store:

- Calculate total prices with tax
- Determine change from customer payments
- Track inventory quantities
- Calculate discounts and sales

**Think about:**

- What mathematical operations do you need for basic calculations?
- How do different number types behave in calculations?
- What happens when you divide numbers?

**Challenge yourself:**

- Can you implement a tip calculator with different percentages?
- What if you need to handle currency formatting?

**If you can't solve this, review:** Numeric types, arithmetic operators, division in Python

**🔢 Quick Reference:** `//` = floor division, `/` = true division

---

### Question 4: String Operations and Methods ⭐⭐

**⏱️ Time Estimate:** 12 minutes  
**🎯 Category:** String Manipulation  
**📝 Skills Tested:** String methods, immutability

**Task:** Manipulate strings using various string methods and operations.

**Real-life Scenario:** You're building a text processing system for a content management platform:

- Format user names consistently
- Clean up user input data
- Extract information from text
- Validate text formats

**Think about:**

- How can you change the appearance of text without losing the original?
- What operations help you find and extract parts of text?
- How do you combine or split text data?

**Challenge yourself:**

- Can you implement a simple text search function?
- What if you need to handle text in different languages?

**If you can't solve this, review:** String methods, string immutability, slicing

**📝 Remember:** Strings are immutable - methods return new strings!

---

### Question 5: Boolean Logic and Comparisons ⭐⭐

**⏱️ Time Estimate:** 10 minutes  
**🎯 Category:** Logic & Control  
**📝 Skills Tested:** Boolean operations, comparison operators

**Task:** Work with boolean values and comparison operators.

**Real-life Scenario:** You're building a user authentication system:

- Check if user is logged in
- Validate user permissions
- Determine access levels
- Handle conditional logic

**Think about:**

- How do you compare values to make decisions?
- What happens when you combine multiple conditions?
- How do you check if something is true or false?

**Challenge yourself:**

- Can you implement a simple access control system?
- What if you need to handle complex permission combinations?

**If you can't solve this, review:** Boolean logic, comparison operators, truthy/falsy values

**🎯 Key Difference:** `=` assigns, `==` compares!

---

### Question 6: Complex Data Types Introduction ⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Data Structures  
**📝 Skills Tested:** Lists, tuples, dictionaries

**Task:** Create and understand basic complex data types.

**Real-life Scenario:** You're building a simple contact management system:

- Store multiple phone numbers for a person
- Keep track of person's location coordinates
- Store person's personal information (name, age, email)

**Think about:**

- How do you organize multiple related pieces of information?
- What happens when you need to group data together?
- How do you access specific information from a collection?

**Challenge yourself:**

- Can you create a system that stores multiple contacts?
- What if you need to search through the contact information?

**If you can't solve this, review:** Lists, tuples, dictionaries, indexing

**📊 Quick Guide:** Lists = mutable, Tuples = immutable, Dicts = key-value pairs

---

## 🟡 **Intermediate Level Questions** (7-12)

### Question 7: Variable Scope and Lifetime ⭐⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Advanced Concepts  
**📝 Skills Tested:** Scope rules, variable lifetime

**Task:** Understand how variables work in different scopes.

**What to do:**

- Create variables in global scope and demonstrate how they can be accessed
- Show the difference between local and global variables, and understand variable lifetime

**What NOT to do:**

- Don't assume all variables are accessible everywhere
- Don't forget to use the 'global' keyword when modifying global variables inside functions
- Don't create variables with the same name in different scopes without understanding shadowing

**If you can't solve this, review:** Variable scope, global vs local variables, lifetime of variables

**🌍 Scope Rule:** LEGB (Local → Enclosing → Global → Built-in)

---

### Question 8: Type Checking and Validation ⭐⭐⭐

**⏱️ Time Estimate:** 18 minutes  
**🎯 Category:** Type Safety  
**📝 Skills Tested:** Type checking, validation

**Task:** Check and validate data types of variables.

**What to do:**

- Use type() function and isinstance() function to check data types
- Create a function that validates if a variable is of a specific type and returns appropriate boolean values

**What NOT to do:**

- Don't rely solely on type() for type checking
- Don't forget that isinstance() is preferred for type checking
- Don't ignore that some objects can be instances of multiple types

**If you can't solve this, review:** type(), isinstance(), type validation

**🔍 Best Practice:** Use `isinstance()` over `type()` for type checking!

---

### Question 9: Memory and Object Identity ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Memory Management  
**📝 Skills Tested:** Object identity, memory concepts

**Task:** Understand object identity and memory management.

**What to do:**

- Use the 'is' operator to compare object identity vs the '==' operator for value equality
- Demonstrate how Python handles small integers and string interning

**What NOT to do:**

- Don't use 'is' for value comparison
- Don't assume all equal values have the same identity
- Don't forget that 'is' checks for the same object in memory

**If you can't solve this, review:** Object identity, 'is' vs '==', memory management basics

**🧠 Memory Tip:** Small integers (-5 to 256) are cached for performance!

---

### Question 10: Advanced Data Types and Special Values ⭐⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Special Values  
**📝 Skills Tested:** None, True, False handling

**Task:** Work with special values and understand their behavior.

**What to do:**

- Create variables with None, True, False, and demonstrate their behavior in different contexts
- Show how to check for these special values and understand their boolean interpretation

**What NOT to do:**

- Don't use None as a default parameter value without understanding mutable default arguments
- Don't forget that None is a singleton object
- Don't confuse None with empty containers or zero values

**If you can't solve this, review:** None, True, False, boolean context, special values

**🎭 Special Values:** None = absence of value, True/False = boolean constants

---

### Question 11: Variable Naming Pitfalls in Real Projects ⭐⭐

**⏱️ Time Estimate:** 15 minutes  
**🎯 Category:** Best Practices  
**📝 Skills Tested:** Naming conventions, code quality

**Task:** Refactor a set of poorly named variables from a real-life script (e.g., x1, y2, z3) to meaningful names.

**What to do:**

- Identify unclear variable names and rename them to reflect their purpose in a real-world context (e.g., user_age, product_price)

**What NOT to do:**

- Don't use abbreviations that are not obvious
- Don't use single-letter names except for counters

**If you can't solve this, review:** Naming conventions, code readability, PEP8 guidelines

**📝 PEP8 Rule:** Use descriptive names that reveal intent!

---

### Question 12: Debugging Type Errors in User Input ⭐⭐

**⏱️ Time Estimate:** 12 minutes  
**🎯 Category:** Error Handling  
**📝 Skills Tested:** Input validation, error handling

**Task:** Simulate a scenario where user input is always a string, but you need an integer for calculations.

**What to do:**

- Convert user input to the correct type and handle possible conversion errors

**What NOT to do:**

- Don't assume input() returns the correct type
- Don't ignore ValueError exceptions

**If you can't solve this, review:** input(), type conversion, exception handling basics

**🛡️ Defensive Programming:** Always validate user input!

---

## 🟠 **Advanced Level Questions** (13-17)

### Question 13: Floating Point Precision in Financial Calculations ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Precision & Accuracy  
**📝 Skills Tested:** Decimal arithmetic, financial calculations

**Task:** Calculate the total price for a list of items with floating point prices and quantities.

**What to do:**

- Use the decimal module to avoid floating point rounding errors in financial calculations

**What NOT to do:**

- Don't use float for money
- Don't ignore rounding issues

**If you can't solve this, review:** float vs decimal, rounding, financial calculations in Python

**💰 Financial Rule:** Never use float for money - use Decimal!

---

### Question 14: Mutability Confusion in Lists vs Tuples ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Data Structures  
**📝 Skills Tested:** Mutability concepts

**Task:** Given a function that tries to modify both a list and a tuple, explain and fix the error.

**What to do:**

- Show which operations are allowed on lists but not on tuples, and refactor the code accordingly

**What NOT to do:**

- Don't try to append or modify tuples
- Don't confuse list and tuple methods

**If you can't solve this, review:** Mutability, list methods, tuple immutability

**🔄 Mutability:** Lists = changeable, Tuples = unchangeable

---

### Question 15: Chained Assignment and Unexpected Results ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Assignment Behavior  
**📝 Skills Tested:** Reference semantics, assignment behavior

**Task:** Investigate a bug where changing one variable unexpectedly changes another (e.g., a = b = []).

**What to do:**

- Explain why this happens and how to avoid it

**What NOT to do:**

- Don't use chained assignment for mutable objects unless intended

**If you can't solve this, review:** Assignment, references, mutability, Python memory model

**🔗 Reference Behavior:** Multiple variables can point to the same object!

---

### Question 16: Real-World Data Validation ⭐⭐⭐

**⏱️ Time Estimate:** 35 minutes  
**🎯 Category:** Data Validation  
**📝 Skills Tested:** Validation logic, error handling

**Task:** Validate a user profile dictionary to ensure all required fields are present and of the correct type.

**What to do:**

- Write a function that checks for missing or incorrectly typed fields and returns a helpful error message

**What NOT to do:**

- Don't assume all dictionary keys exist
- Don't skip type checks

**If you can't solve this, review:** Dictionaries, type checking, error handling

**✅ Validation:** Always check data before processing!

---

### Question 17: Handling None and Default Values in Functions ⭐⭐⭐

**⏱️ Time Estimate:** 25 minutes  
**🎯 Category:** Function Design  
**📝 Skills Tested:** Default arguments, None handling

**Task:** Write a function that takes an optional argument and uses None as a default. Explain the difference between None and other default values.

**What to do:**

- Show how to check for None and provide a fallback value

**What NOT to do:**

- Don't use mutable objects as default arguments
- Don't confuse None with 0 or empty string

**If you can't solve this, review:** Default arguments, None, function parameter best practices

**🎯 Default Values:** Use None for optional parameters, not mutable objects!

---

## 🔴 **Expert Level Questions** (18-20)

### Question 18: Detecting and Fixing Shadowed Variables ⭐⭐⭐

**⏱️ Time Estimate:** 30 minutes  
**🎯 Category:** Advanced Debugging  
**📝 Skills Tested:** Variable shadowing, scope debugging

**Task:** Debug a script where a local variable accidentally hides a global variable of the same name.

**What to do:**

- Identify the shadowing and refactor the code to avoid confusion

**What NOT to do:**

- Don't use the same name for local and global variables unless necessary

**If you can't solve this, review:** Variable scope, shadowing, global vs local variables

**👥 Shadowing:** Local variables can hide global ones with the same name!

---

### Question 19: Real-Life Logging and Data Types ⭐⭐

**⏱️ Time Estimate:** 20 minutes  
**🎯 Category:** Logging & Debugging  
**📝 Skills Tested:** Logging, type conversion

**Task:** Log user actions to a file, ensuring all data types are correctly converted to strings.

**What to do:**

- Safely convert and format different data types for logging

**What NOT to do:**

- Don't concatenate non-string types directly
- Don't ignore formatting errors

**If you can't solve this, review:** str(), string formatting, logging basics

**📝 Logging Tip:** Always convert data to strings before logging!

---

### Question 20: Debugging Identity vs Equality in Real Code ⭐⭐⭐⭐

**⏱️ Time Estimate:** 40 minutes  
**🎯 Category:** Advanced Debugging  
**📝 Skills Tested:** Identity vs equality, real-world debugging

**Task:** Fix a bug where 'is' is used instead of '==' to compare values from a database or API.

**What to do:**

- Explain the difference and refactor the code to use the correct operator

**What NOT to do:**

- Don't use 'is' for value comparison
- Don't assume identity means equality

**If you can't solve this, review:** 'is' vs '==', object identity, equality in Python

**🔍 Expert Tip:** 'is' checks identity, '==' checks value equality!

---

## 🎯 **Study Progress Summary**

### 📈 **Completion Status:**

- 🟢 **Basic Level:** 0/6 completed
- 🟡 **Intermediate Level:** 0/6 completed
- 🟠 **Advanced Level:** 0/5 completed
- 🔴 **Expert Level:** 0/3 completed

### ⏱️ **Total Estimated Time:** 6 hours 30 minutes

### 🎓 **Next Steps:**

1. Start with Basic Level questions (1-6)
2. Move to Intermediate when comfortable
3. Challenge yourself with Advanced concepts
4. Master Expert level for real-world scenarios

---

> **💡 Pro Tip:** Take your time with each question. Understanding the concepts deeply is more important than rushing through them!

---
