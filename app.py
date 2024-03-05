def divide_numbers(a, b):
    """
    Divides two numbers, handling division by zero.

    Parameters:
    a (float): The numerator.
    b (float): The denominator.

    Returns:
    float: The result of the division if b is not zero.
    str: An error message if b is zero.
    """
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

def main():
    print("Basic Division Application")
    
    # Get user input
    a = float(input("Enter the first number (numerator): "))
    b = float(input("Enter the second number (denominator): "))
    
    # Perform division and handle potential division by zero
    result = divide_numbers(a, b)
    
    # Display the result or error message
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
