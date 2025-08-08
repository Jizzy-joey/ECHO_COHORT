# whileloop
num = 0 

while num  <= 5:
    num = num + 1
    # print(num, "do something")

    # guess the number

    # while True:
    #     number = int(input("guess the number from one to 20:"))

    #     if (number >= 6 and number <= 11) or (number >= 13 and number <= 16) :
    #         print(f"{"--" * 24}\nwild guess. try again.\n{"--" * 24}")
    #     elif number == 12:
    #         print(f"{"--" * 24}\nwild guess. try again.\n{"--" * 24}")
    #     else:
    #         print(f"{"--" * 24}\nwild guess. try again.\n{"--" * 24}")

    # list_of_items = []

    # while True:
    #     if len(list_of_items) == 5:
    #         print("you have gotten to the maximum number of items", len(list_of_items))
    #         break

    #     input_value = input("write an item: ")
    #     list_of_items.append(input_value)


# name_body = ("")

# while True:
#     input_value = input("write your name: ")
#     if len(input_value) >= 5:
#         print("name entered successfully")
#         break

# user_info = {}

# while True:
#     input_name = input("Name: ")
#     input_password = input("password: ")
#     user_info["name"] = input_name
#     user_info["password"] = input_password

#     if len(input_password) <= 5:
#         print("password must be more than 5.")
#         continue

#     print("user information is successful")
#     print(user_info)   
    





# while True:
#     number = float(input("enter number from one to 20:"))
#     if (number % 2):
#         print("this is an odd number")
#     else:
#         print("this is an even number")


# Function---
# A function is a block of code that perform specific tasks

# def sum(num1, num2, num3): #argument
#     print(num1, num2, num3, "INSIDE FUNCTION")
#     add = num1 + num2 + num3
#     return add


# run_function = sum(1, 2, 3) #Argument

# print(run_function, sum(4,11,9), "FROM print")


# def introduction(name):
#     return f"hi my name is {name}"

# run_function = introduction("Joseph")
# print(introduction("Joseph"))


# def evenNumbers(number):
#     return number if number % 2 == 0 else None

# print(
#     evenNumbers(13),
#     evenNumbers(4),
#     evenNumbers(12)
# )

# TYPES OF ARGUMENTS;
# - positional argument
def func1(first, second, third):
    return first, second, third # this will print a type of the parameter values

# print(func1)

# - Keyword argument

def func2(name,location, gender):
    return name, location, gender

# print(
#     func2(name="joseph", location="lagos", gender="male")
# )

# default argument
def func3(name, mode="easy"):
    return (name, mode)

# print(
#     func3("indiana jones", 'hard')
# )


# - variable length argument

def func4(*colors):
    return colors

# print(
#     func4("red", "blue", "orange", "green")  #variable length argument returns a tuple 
# )

# keyword as an argument

def func5(**user_info):
    return user_info

print(
    func5(name= "joseph", gender= "male", is_available=True)
    )