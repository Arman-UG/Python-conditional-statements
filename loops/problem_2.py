


for inspection in range(10):
    product_id = input("enter the product Id: ").strip().lower()
    quality_inspection = input("Did the product pass quality inspection? (yes/no) ").strip().lower()
    if quality_inspection == "yes" and len(product_id) == 6:
        print("Product : ", product_id ,"approved")
    else:
        print("Product : ", product_id ,"rejected")