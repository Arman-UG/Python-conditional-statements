name = input("Enter your name: ")
country = input("Enter your country name: ")

# Let's make these inputs dynamic so you can test different amounts!
total_amount = float(input("Enter your total cart amount: "))

# Step 1: Immediate Security Block
if "North Korea" in country:
    print("Sorry!", name, "We cannot ship to this destination due to our policies.")

# Step 2: If it passes security, proceed to shipping calculation
else:
    print("\n--- Order Summary ---")
    print("Country:", country)
    
    # Nested Branch A: Domestic Shipping
    if "India" in country:
        if total_amount >= 500:
            shipping = 0
            print("Shipping Cost: Free")
        else:
            shipping = 50
            print("Shipping Cost: ₹50")
        print("Final Total: ₹", total_amount + shipping, name)
        
    # Nested Branch B: International Shipping
    else:
        if total_amount >= 100:
            shipping = 10
            print("Shipping Cost: $10")
        else:
            shipping = 25
            print("Shipping Cost: $25")
        print("Final Total: $", total_amount + shipping, name)