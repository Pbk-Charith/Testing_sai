def add(x, y=2):
    result = x + y
    if result > 10:
        print(f"The sum {result} is greater than 10.")
    else:
        print(f"The sum {result} is less than or equal to 10.")
    return result

def product(x, y=2):
    result = x * y
    if result > 10:
        print(f"The product {result} is greater than 10.")
    else:
        print(f"The product {result} is less than or equal to 10.")
    return result

# Testing the functions
add_result = add(5, 7)  # This will print that the sum is greater than 10.
product_result = product(3, 4)  # This will print that the product is greater than 10.

