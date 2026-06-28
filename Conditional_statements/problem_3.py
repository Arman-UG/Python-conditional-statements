user_role = "Admin"       # Can be: "Admin", "Developer", or "Guest"
server_type = "Large"         # Can be: "Small", "Medium", or "Large"
monthly_budget = 120.0        # Float value representing the client's budget limit

if user_role == "Guest":
     print("You do not have Permissions")

elif (user_role == "Developer") and (server_type == "Small"):
     server_cost = float(20)
     print("Your server type is: ", server_type, "and your cost of server is: ", server_cost)

elif (user_role == "Developer") and (server_type == "Medium"):
     server_cost = float(50)
     new_server_cost = server_cost / 100 * 10
     final_cost = server_cost - new_server_cost
     print("Your server type is: ", server_type, "and your cost of server is: ", final_cost)

elif (user_role == "Developer") and (server_type == "Large"):
     print("I do not have permission to create Large server, Please contact the Admin")

elif (user_role == "Admin") and (server_type == "Small"):
     server_cost = float(20)
     print("Your sever type is: ", server_type, "and your server cost is: ", server_cost)

elif (user_role == "Admin") and (server_type == "Medium"):
     server_cost = float(50)
     new_server_cost = server_cost / 100 * 10
     final_cost = server_cost - new_server_cost
     print("Your sever type is: ", server_type, "and your server cost is: ", final_cost)


elif (user_role == "Admin") and (server_type == "Large"):
     server_cost = float(100)
     new_server_cost = server_cost / 100 * 10
     final_cost = server_cost - new_server_cost
     print("Your sever type is: ", server_type, "and your server cost is: ", final_cost)
else:
     print("Sorry, at present we don't have server")