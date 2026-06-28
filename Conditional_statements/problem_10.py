cart_total = int(input("cart total amount? "))
premium_member = input("Are you premium member? (yes/no) ").strip().lower()
coupon_available = input("Do you have coupon? (yes/no) ").strip().lower()

if cart_total >= 1000:
    if premium_member == "yes":
        if coupon_available == "yes":
            discount = cart_total / 100 * 20
            new_cart_total = float(cart_total - discount)
            print("Congratulation! you won '20%' discount. ", new_cart_total)
        else:
            discount = cart_total / 100 * 10
            new_cart_total = float(cart_total - discount)
            print("Congratulations! you won '10%' discount. ", new_cart_total) 
    else:
        if coupon_available == "yes":
            discount = cart_total / 100 * 5
            new_cart_total = float(cart_total - discount)
            print("congratulations! you won '5%' discount. ", new_cart_total)
        else:
            print("No discount")
else:
    print("order nor eligible")