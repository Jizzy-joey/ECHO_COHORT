# ================================
# Python Collections & Loops Assignment
# 20 Progressive Questions (Simple → Hard)
# ================================

# print("\n=== Level 1: Basic List Operations ===")
# 1. Create a list called 'fruits' containing "apple", "banana", and "cherry". Print it.
fruit = ["apple", "banana", "cherry"]
print(fruit)

# 2. Using slicing, extract the first two items from 'fruits'. Print the result.
slice_fruit = fruit [0:2]
print(slice_fruit)

# 3. Add "orange" to the end of the list and print the updated list.
fruit.append("orange")
print(fruit)

# 4. Create a tuple named 'colors' with "red", "green", and "blue". Print it.
colors = ("red", "green", "blue")
print(colors)

# 5. Check if "yellow" exists in the tuple. Print True or False.
checking = "yellow" in colors
print(checking)
# 6. Repeat the tuple 3 times and store it in 'repeated_colors'. Print it.
repeated_colors = colors * 3
print(repeated_colors)
# 7. Create two sets: setA = {1,2,3} and setB = {3,4,5}. Print both.
setA = {1,2,3}
setB = {3,4,5}
print(setA, setB)
# 8. Find and print the union of setA and setB.
union = setA.union(setB)
print(union)
# 9. Find and print the intersection of setA and setB.
intersection = setA.intersection(setB)
print(intersection)
# 10. Given the list: clubs = ["Chelsea","Arsenal","Liverpool"], insert "Man City" at position 1.
clubs = ["chelsea", "arsenal", "liverpool"]
clubs.insert((1), "man city")
print(clubs)
# 11. Remove "Arsenal" from the list and print the final list.
clubs.remove("arsenal")
print(clubs)
# 12. Check if the number 15 exists in this list: [10,20,30,40]. Print the result.
list = [10,20,30,40,]
checking = 15 in list
print(checking)
# 13. Classify a score of 85: 80+ = "A", 70+ = "B", else "C". Print the grade.
score = 85
if score  >= 80 :
    print("A", "excellent work!!")

if score <= 70 :
    print("B", "fair try")
else:
    print("C", "poor attempt")
# 14. Using a loop, print all even numbers between 1-10 (inclusive).
numbers = [1,2,3,4,5,6,7,8,9,10]
even_num = ()

for num in numbers:
    if num / 2: even_num

print(even_num)
    
# 15. Convert these names to email addresses: ["dapo","tunde"] → ["dapo@gmail.com", ...]
adj = ["dapo", "tunde"]
emails = ["@gmail.com"]
for x in adj:
    for y in emails:
        print(x,y)
# 16. Find and print the highest number in [4,14,12,8,22,19].
random_numbers = [4,14,12,8,22,19]
highest_number = 0
for number in random_numbers:
    if number > highest_number:
        highest_number = number
        print(highest_number)

# 17. In the string "124682937", replace all digits >5 with "*". Print result.


# 18. Create a dictionary from keys ["name","age"] and values ["Alice",25].


# 19. Flatten this 2D list: [[1,2],[3,4],[5,6]] → [1,2,3,4,5,6].


# 20. Find elements in {1,2,3,4} that aren't in {3,4,5,6} (set difference).