password = input("Enter password: ") 

spl_char = "!@#$%&()"
num = "1234567890"

# Pre-checks for characters
has_spl = any(char in password for char in spl_char)
has_num = any(char in password for char in num)

if " " in password:
    print("Password is invalid: it must not contain spaces")
elif len(password) < 8:
    print("Password is invalid: it must be at least 8 characters long")
elif len(password) > 12:
    print("Password is invalid: it must be at most 12 characters long")
elif not has_spl or not has_num:
    print("Password invalid: it must contain at least one special character AND one number.")
else:
    print("Password is valid: ", password)