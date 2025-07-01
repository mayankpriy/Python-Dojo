"""
Question X: [Question Title]
Difficulty: ⭐⭐⭐
Category: [Category Name]

[Copy the full question text here, including:
- Task description
- Requirements
- Examples
- Constraints]

Example:
    function_name("input") -> "expected_output"
    function_name([1, 2, 3]) -> 6
"""

# =============================================================================
# YOUR SOLUTION STARTS HERE
# =============================================================================


def your_function_name(param1: str, param2: int) -> str:
    """
    Brief description of what your function does.

    Args:
        param1 (str): Description of first parameter
        param2 (int): Description of second parameter

    Returns:
        str: Description of what the function returns

    Raises:
        ValueError: When invalid input is provided

    Example:
        >>> your_function_name("Alice", 25)
        "Name: Alice, Age: 25"
    """
    # Add your solution logic here
    # Use clear variable names
    # Add comments for complex logic

    # Input validation
    if not param1 or param2 < 0:
        raise ValueError("Invalid input parameters")

    # Main logic
    result = f"Name: {param1}, Age: {param2}"

    return result


# =============================================================================
# ALTERNATIVE SOLUTIONS (if you have multiple approaches)
# =============================================================================


def alternative_solution(param1: str, param2: int) -> str:
    """
    Alternative approach using different method.

    This solution demonstrates a different way to solve the same problem.
    """
    # Alternative implementation
    return "Name: {}, Age: {}".format(param1, param2)


# =============================================================================
# TESTING YOUR SOLUTION
# =============================================================================

if __name__ == "__main__":
    print("🧪 Testing your solution...")
    print("=" * 50)

    # Test case 1: Basic functionality
    try:
        result1 = your_function_name("Alice", 25)
        print(f"✅ Test 1 PASSED: {result1}")
        assert result1 == "Name: Alice, Age: 25"
    except Exception as e:
        print(f"❌ Test 1 FAILED: {e}")

    # Test case 2: Edge case
    try:
        result2 = your_function_name("Bob", 0)
        print(f"✅ Test 2 PASSED: {result2}")
        assert result2 == "Name: Bob, Age: 0"
    except Exception as e:
        print(f"❌ Test 2 FAILED: {e}")

    # Test case 3: Error handling
    try:
        result3 = your_function_name("", -5)
        print(f"❌ Test 3 FAILED: Should have raised ValueError")
    except ValueError:
        print(f"✅ Test 3 PASSED: Correctly raised ValueError for invalid input")
    except Exception as e:
        print(f"❌ Test 3 FAILED: Unexpected error: {e}")

    # Test case 4: Alternative solution
    try:
        result4 = alternative_solution("Charlie", 30)
        print(f"✅ Test 4 PASSED: {result4}")
        assert result4 == "Name: Charlie, Age: 30"
    except Exception as e:
        print(f"❌ Test 4 FAILED: {e}")

    print("=" * 50)
    print("🎉 All tests completed!")

    # Performance test (if applicable)
    import time

    start_time = time.time()
    for _ in range(1000):
        your_function_name("Test", 25)
    end_time = time.time()

    print(f"⏱️ Performance: {1000} calls in {end_time - start_time:.4f} seconds")


# =============================================================================
# LEARNING NOTES (optional)
# =============================================================================

"""
📚 What I learned from this problem:

1. Key Concept: [What concept this problem taught you]
2. Challenge: [What was most challenging]
3. Solution: [How you approached the problem]
4. Improvement: [How you could improve the solution]

🔍 Time Complexity: O(n) - explain why
💾 Space Complexity: O(1) - explain why

💡 Pro Tips:
- Always validate inputs
- Use type hints for clarity
- Test edge cases
- Consider multiple approaches
"""
