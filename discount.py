def calculate_discount(price, discount_percent):
    if discount_percent >= 20:  # Apply discount only if it's 20% or higher
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price  # Return the original price if the discount is less than 20%

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price using the function
final_price = calculate_discount(original_price, discount_percent)

# Display the result
if discount_percent >= 20:
    print(f"🎉 Discount applied! Final price: ${final_price:.2f}")
else:
    print(f"🚫 No discount applied. Original price: ${original_price:.2f}")
