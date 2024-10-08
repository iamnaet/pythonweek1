def calculate_discount(price, discount_percent):
    # Calculate the discount amount
    discount_amount = (discount_percent / 100) * price

    # Calculate the final price
    final_price = price - discount_amount

    return final_price
    # Check if the discount is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if final_price == original_price:
    print(f"No discount applied. The original price is: ${original_price:.2f}")
else:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
