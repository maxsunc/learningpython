def test_function(func, test_cases):
    """
    Test the provided function against multiple test cases.
    
    Args:
        func: The function to test
        test_cases: List of tuples (inputs, expected_output)
                    inputs should be a tuple of arguments for the function
    """
    print(f"Testing function: {func.__name__}")
    print("-" * 50)
    
    passed = 0
    failed = 0
    
    for i, (inputs, expected) in enumerate(test_cases):
        try:
            # Convert inputs to a tuple if it's not already
            if not isinstance(inputs, tuple):
                inputs = (inputs,)
            
            # Call the function with the inputs
            result = func(*inputs)
            
            # Check if result matches expected output
            if result == expected:
                status = "PASSED"
                passed += 1
            else:
                status = "FAILED"
                failed += 1
                
            # Print test result
            print(f"Test {i+1}: {status}")
            print(f"  Input: {inputs}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            print()
            
        except Exception as e:
            print(f"Test {i+1}: ERROR")
            print(f"  Input: {inputs}")
            print(f"  Exception: {type(e).__name__}: {e}")
            print()