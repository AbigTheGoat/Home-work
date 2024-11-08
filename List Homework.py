#Mark Hanherly Abig Cybersec yr1

#Create a list of 5 of your favorite fruits. Print the list.
Fruits = ['banana', 'orange', 'grapes', 'mango', 'apple']
print(Fruits)

#print the first, third, and last color in the list.
colors = ['red', 'blue', 'green', 'yellow', 'purple']
print(f" {colors[0]}\n {colors[2]}\n {colors[4]}")

#Change the second item to 25 and add 60 to the end of the list. Print the modified list.
numbers = [10, 20, 30, 40, 50]
numbers[1] = 25
numbers.append(60)
print(numbers)

#create a new list subset containing only the first three names. Print subset.
names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
print(names[0:3])

#Create a list of numbers from 1 to 10 and use a loop to print each number squared.
numbr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
snumbr = []
for x in numbr:
    snumbr.append( x **2 )
print(snumbr)

#reate an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list.
shopping_cart = []
shopping_cart.append(['milk', 'bread', 'eggs'])
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

#Write a program to find the maximum and minimum values in the list
numbers1 = [45, 22, 88, 56, 92, 33]
print(min(numbers1))
print(max(numbers1))

#count how many times the letter 'a' appears in the list.
letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
print('The letter a appears', letters.count('a'), 'times')

#Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.
squares = [0, 2, 4, 6, 8, 10]
squared = [numr ** 2 for numr in squares ]
print(squared)

#write a program to remove duplicates and print the unique elements only
nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
unique_nums = list(set(nums))
print(unique_nums)
