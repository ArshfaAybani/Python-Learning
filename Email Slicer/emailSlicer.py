# A simple email slicing program to enhance my understanding of functions and their usage  

email = input("Enter your email: ") 
index = email.index("@")

username = email[:index]
domain = email[index + 1 : ]

print(f"Your username is {username} and your domain is {domain}")
