# slicing
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

slicing_numbers = list [0:6]

slicing_numbers_from_end = list [-4:]

# print(slicing_numbers_from_end)

# Basic operation with "list"
len_in_list = len(list)

# print(len_in_list)

concat = [1,2,3,4] + [5,6,7,8,9]
# print(concat)

# repitiion

repeat = ["yes"] * 4
# print(repeat)

# Membership
checking = 6 in list
# print(checking)

# ---- List built in methods ---
premier_league_clubs = ["liverpool", "arsenal", "manchester united", "chelsea", "manchester city"]

premier_league_clubs.append("newcastle united")

premier_league_clubs.pop(3)

premier_league_clubs.insert(3, "brighton")

premier_league_clubs.remove("brighton")

# print(premier_league_clubs)

# tuple
tuple_data = (1,2,3,4,5,6)
checking = 5 in tuple_data
# print(checking)
slicing_data = tuple_data [0:4]
# print(slicing_data)

# ---- set ----
# collection_of-numbers = {1,2,3,4,5,6}
# print(collection_of_numbers)
setA = {1,9}
setB = {1,3,9,6}

union = setA.union(setB) #setA / setB
intersection = setA.intersection(setB) #setA & setB

# print("set A:",setA)
# print("set B:",setB)
# print("union:",union)
# print("intersection:",intersection)
# print("membership:",1 in setA, 14 not in setB)

concat_set = {1,2,3}

concat_set.add(5) #add item to a set

concat_set.remove(1) #removes specific item
concat_set.pop() #takes out the first one
concat_set.update([9,10,11,12]) # for join two set together or adding the items in a list to a set

# print(concat_set)

#-- conditional statement --
# if statement
# if False:
#     print("it's true")
# else:
#     print("it's not true")    

score = 80
# if score >= 80:
#     print("excellent effort. Well done!!")

# elif score > 60:
#     print("fair. you tried ")    
# else:
#     print("oops. try again")    
# a=0
# print("yes") if True else print("no")

# ---- loops ---
'''
examples of iterables
-list
-strings
-tuple
-dictionary
-set
'''
numbers = [1,2,3,4,5,6,7,8]

# for num in numbers:
#     if num == 6:
#         print("i have the number 6")
#         continue
#     print(num)

students = ["adam", "bob", "sam"]

for index, stud in enumerate(students):
    if stud == "bob":
        students[index] = "sam"

# print(students)

random_numbers = [4, 14, 12, 8, 22, 19]
lowest_numbers = 50

for number in random_numbers:
    if number < lowest_numbers:
        lowest_numbers = number

# print(lowest_numbers)

users = ["dapo", "tunde", "jesse", "joseph"]
emails = []

for index, user in enumerate(users):
    users[index] = user + "@gmail.com"

# print(users) 

str_of_numbers = "124682937"

new_str = ""

for index, num in enumerate(str_of_numbers):
    if int(num) > 5:
        new_str = new_str + "*"
    else:
        new_str = new_str + num

# print(new_str) 

numbers = [1,2,3,4,5,6,7,8,9,12,13,14,15,16,17,18,19,20]
whole_num = []

for index, num in enumerate(numbers):
    if num % 2 == 0:
        whole_num.append(num)

# print(whole_num)

collections = ["book","pencil","text","biro"]
i = 0
while  i < len(collections):
#   print(collections[i])
  
  i += 1


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(*, x):
  print(x)

my_function(x = 3)

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)

x = lambda a : a + 10
print(x(5))

a = 33
b = 20
if b > a:
  print("b is greater than a")


  i = 1
while i < 6:
  print(i)
  i += 1

#   i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1