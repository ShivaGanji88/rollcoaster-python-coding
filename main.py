print("Welcome to tollercoaster")
height = int(input("enter yout height: "))
bill = 0
if height > 120:
    print("You can ride rollercoaster")

    age = int(input("Enter your age: "))
    
    if age < 10 :
        bill = 100
        print("please pay INR 100")

    elif age < 18:
        bill = 200
        print("Please pay INR 200") 

    else:
        bill = 300
        print("Please pay 300")

    want_photo = input("Do want Photo? Y or N ")

    if want_photo == "Y":
        bill += 30   


    print(f"Your final bill INR {bill}")   
     
else:
    print("you are not eligible to ride")            
