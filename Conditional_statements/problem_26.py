identity = input("who are you? (hr/admin/employee) ").strip().lower()

if identity == "hr" or identity == "admin":
    print("Access to Salary Records")
else:
    print("Access Denied")  