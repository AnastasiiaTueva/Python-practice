username = input("Write your username: ")

if len(username) < 2:
    print("Your username cannot be less than 2 characters")
elif len(username) > 12:
    print("Your username cannot be more than 12 characters")
else:
    print(f"Your username is {username}")

mail = input("Write your e-mail: ")
print("Your e-mail:")
print(mail.replace(" ", ""))

phone_number = input("Your phone number: ")
if phone_number.startswith("0"):
    
    phone_number = "+359" + phone_number[1:]
elif phone_number.startswith("+359"):
    
    pass
elif phone_number.startswith("00359"):
    
    phone_number = "+359" + phone_number[5:]
print(f"Your phone number is: {phone_number}")

password = input("Write your password: ")
if len(password) < 6:
    print("Your password cannot be less than 6 characters.")
else:
    print("Your password:")
    print(password)

password_again = input("Write your password again: ")

if password_again == password:
    print(f"Welcome {username}!\n Your e-mail is: {mail}\n Your phone number is: {phone_number}\n Your password is: {password}")
else:
    print("There is an error in password")
