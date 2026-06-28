for students in range(20):
    roll_no = int(input("enter your roll_no: "))
    marks = int(input("enter your marks: "))
    if marks >= 90:
        print("outstanding")
    elif marks >= 75 and marks <= 89:
        print("first division")
    elif marks >= 40 and marks <= 74:
        print("pass")
    else:
        print("fail")

