# 🎯 Solution Submission Guidelines

> **How to submit your solutions to Python practice questions**

Welcome to the Python Atelier! This guide will help you submit your solutions to practice questions and contribute to this collaborative learning atelier.

---

## 📁 Solution Structure

Each topic folder contains a `solutions/` directory where you'll submit your answers:

```
topic_folder/
├── questions.md          # Practice questions
├── README.md            # Topic overview
└── solutions/           # Your solutions go here
    ├── question_01.py
    ├── question_02.py
    └── ...
```

---

## 📝 How to Submit Your Solution

### 1. **Choose a Question**

- Browse through any topic folder (e.g., `01_variables_and_data_types/`)
- Open `questions.md` to see all practice questions
- Pick a question you want to solve

### 2. **Create Your Solution File**

- Navigate to the `solutions/` folder in that topic
- Create a new Python file: `question_XX.py` (replace XX with question number)
- Use the appropriate template below based on what you know

### 3. **Solution File Templates**

Choose the template based on your current Python knowledge level:

#### 🟢 **Template A: Absolute Beginner**

```python
"""
Question X: [Question Title]
Difficulty: ⭐
Category: [Category]

[Copy the full question text here]

This solution uses only variables and print statements.
Use this template if you have only learned about variables.
"""

# ===========================================
# STEP 1: Create your variables
# ===========================================

# Create variables with the data you want to work with
my_number = 42
my_text = "hello"
my_decimal = 3.14

# ===========================================
# STEP 2: Print your variables
# ===========================================

print("My variables contain:")
print("my_number =", my_number)
print("my_text =", my_text)
print("my_decimal =", my_decimal)

# ===========================================
# STEP 3: Try to solve the question
# ===========================================

# Add your solution logic here
# Use print() to show your results
print("\nMy solution:")
# Write your answer here
```

#### 🟡 **Template B: Intermediate**

```python
"""
Question X: [Question Title]
Difficulty: ⭐⭐⭐
Category: [Category]

[Copy the full question text here]

Example:
    function_name("input") -> "expected_output"
"""

def your_function_name():
    """
    TODO: Write what your function does
    """
    # TODO: Write your solution here
    pass

# Test your solution
if __name__ == "__main__":
    print("Testing your solution...")
    # TODO: Add test cases here
    # Example: result = your_function_name("test_input")
    # Example: print(f"Result: {result}")
```

#### 🔴 **Template C: Expert**

```python
"""
Question X: [Question Title]
Difficulty: ⭐⭐⭐⭐⭐
Category: [Category]

[Copy the full question text here]

Example:
    function_name("input") -> "expected_output"
"""

from typing import Any, Optional

def your_function_name(param: Any) -> str:
    """
    Detailed description of what your function does.

    Args:
        param: Description of the parameter

    Returns:
        Description of the return value

    Raises:
        ValueError: When something goes wrong

    Examples:
        >>> your_function_name("test")
        'expected_output'
    """
    # TODO: Write your solution here
    pass

# Comprehensive testing
if __name__ == "__main__":
    print("Running comprehensive tests...")

    # Test cases
    test_cases = [
        ("input1", "expected1"),
        ("input2", "expected2"),
    ]

    for test_input, expected in test_cases:
        result = your_function_name(test_input)
        status = "✅" if result == expected else "❌"
        print(f"{status} {test_input} -> {result} (expected: {expected})")
```

### 4. **Code Quality Requirements**

#### 🟢 **Template A (Absolute Beginner):**

✅ **Must Include:**

- Variables with meaningful names
- Print statements to show your work
- Comments explaining what you're doing

✅ **Code Style:**

- Use clear variable names
- Add comments to explain your steps
- Test your code by running it

#### 🟡 **Template B (Intermediate):**

✅ **Must Include:**

- Clear function names
- Basic docstrings
- Simple test cases
- Comments explaining complex logic

✅ **Code Style:**

- Follow basic Python conventions
- Use meaningful variable names
- Add comments for complex logic

#### 🔴 **Template C (Expert):**

✅ **Must Include:**

- Type hints
- Comprehensive docstrings
- Extensive test cases
- Error handling
- Performance considerations

✅ **Code Style:**

- Follow all PEP 8 guidelines
- Use type hints throughout
- Write production-ready code
- Include performance optimizations

❌ **Avoid (All Levels):**

- Hardcoded values without explanation
- Overly complex one-liners
- Missing error handling (where appropriate)
- Poor variable naming

---

## 🚀 Submission Process

1. **Fork the Repository**

   ```bash
   # Fork on GitHub, then clone your fork
   git clone https://github.com/Python-Atelier/python-core.git
   cd python-core
   ```

2. **Create Your Solution**

   ```bash
   # Navigate to the topic folder
   cd 01_variables_and_data_types/solutions/

   # Create your solution file
   touch question_01.py
   # Edit the file with your solution
   ```

3. **Test Your Solution**

   ```bash
   # Run your solution to make sure it works
   python question_01.py
   ```

4. **Commit and Push**

   ```bash
   git add .
   git commit -m "feat: Add solution for question 01 - Variables"
   git push origin main
   ```

5. **Create Pull Request**
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Add description: "Solution for Question X in Topic Y"
   - Submit PR

---

## 🏆 Best Solution Selection

### **Evaluation Criteria:**

1. **Correctness (40%)**

   - Solution produces correct output
   - Handles edge cases properly
   - No runtime errors

2. **Code Quality (30%)**

   - Clean, readable code
   - Proper documentation
   - Follows Python best practices

3. **Efficiency (20%)**

   - Optimal time/space complexity
   - Efficient algorithms
   - Minimal resource usage

4. **Creativity (10%)**
   - Unique approach
   - Elegant solutions
   - Learning value

### **Selection Process:**

- Solutions are reviewed by maintainers
- Best solution gets merged to main branch
- Other good solutions may be kept as alternatives
- Students receive feedback on their submissions

---

## 📋 Naming Conventions

### **Solution Files:**

- `question_01.py` - Standard format (include your name in the file header)
- `question_01_alternative.py` - Alternative approaches (if you have multiple solutions)

### **Commit Messages:**

- `feat: Add solution for question 01 - Variables`
- `feat: Add solution for question 02 - Control Flow`
- `feat: Add solution for question 03 - Functions`

---

## 🎯 Template Selection Guidelines

### **Template A: Absolute Beginner**

Use this template when you have learned:

- Variable creation and assignment
- Basic data types (int, float, str, bool)
- Print statements
- Basic comments

### **Template B: Intermediate**

Use this template when you have learned:

- All concepts from Template A
- Function definition and calling
- Parameters and return values
- Basic docstrings
- Main guard pattern

### **Template C: Expert**

Use this template when you have learned:

- All concepts from Template B
- Type hints
- Advanced docstrings
- Comprehensive testing
- Error handling
- Performance optimization

---

## 💡 Tips for Success

1. **Start Simple** - Don't try to use concepts you haven't learned yet
2. **Test Often** - Run your code frequently to catch errors early
3. **Ask Questions** - Use the Discussions section if you get stuck
4. **Learn from Others** - Look at other solutions after you've tried yourself
5. **Have Fun** - Learning to code should be enjoyable!

---

**Remember: There's no rush! Take your time and learn at your own pace. Every solution, no matter how simple, is valuable! 🐍✨**
