





identity = input("Are you library incharge (yes/no) ").strip().lower()
if identity == "no":
    print("Access denied")
else:
    
    library_open = "yes"
    while library_open == "yes":
        student_name = input("what is your name? ").strip().lower()
        book_name = input("What is the book name? ").strip().lower()
        book_issued = input("Was the book issued successfully? (yes/no) ").strip().lower()
        if book_issued == 'yes':
            print("Book issued successfully.")
        else:
            print("Issue failed.")

        library_open = input("Is the library still open? (yes/no) ").strip().lower()
        if library_open == "yes":
            print("next student")
        else:
            print("Library closed")