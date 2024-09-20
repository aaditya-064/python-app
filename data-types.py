# x = 1
# if x == 1 :
#     print('x is 1')


# a = 7.0
# print(a)
# a = float(7)
# print(a)
# both of this brint the same result while printing

myWord = "Hello World!"
# print(myWord)
# Well, I ofcourse am familiar with this

# x = 1
# y = 2
# z = x + y
# print(z)


# a = "hello"
# b = "world"
# c = a + " " + b
# print(c)

# a, b = 1, 2
# print(a + b)


firstWord, secondWord = "Hello", "World!"
output = firstWord + " " + secondWord
# print(output)


myString = "hello"
myFloat = 10.0
myInt = 20

# if myString == "hello" :
#     print("String: %s" % myString)
# if isinstance(myFloat, float) and myFloat == 10.0:
#     print("Float: %f" % myFloat)
# # else:
#     print("Not the correct type")
# if isinstance(myInt, int) and myInt == 20:
#     print("Int: %d" % myInt)
# else:
#     print("Not the correct type")


myList = []
myList.append("First Index")
myList.append("Second Index")
# print(myList[0])

# for x in myList:
#     print(x)


# numbers = []
# strings = []

# inputWord = "Hello World!"
# inputInt = 1.5

# if isinstance(inputInt, int):
#     numbers.append(inputInt)
#     print(numbers)
# else:
#     strings.append(inputWord)
#     print(strings)

lotsofapple = "apple " * 10
# print(lotsofapple)

even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
# print(all_numbers)
# print(all_numbers * 10)

# x = object()
# x_list = [x]
# big_list = []
# print(len(x_list))
# print("x_list contains %d objects" % len(x_list))

# name = "Aaditya"
# print("Hello, %s" % name)
# age = 16
# print("%s is %d years old" % (name, age))

myAnotherList = [1, 2, 3]
# print("The list is: %s" % myAnotherList)

firstName = "John"
lastName = "Doe"
balance = 53.44
format_string = "Hello"
# print("%s, %s %s, Your Balance is: %f" % (format_string, firstName, lastName, balance))

aString = "Pedophile"
# print(len(aString)) # len doesn't count spaces in terms of string
# print(aString.index("o"))
# print(aString.count("d"))
# print(aString[2:7])
# print(aString[2:7:3]) #didn't understand this one any better than I understood other things.
# print(aString[::-1]) #to reverse a string
# print(aString.upper())
# print(aString.lower())
# print(aString.startswith("Pedo"))
# print(aString.endswith("Aaditya"))

bString = "Hello World"
# print(bString.split(" "))
# print("l occurs %d times in %s" %(bString.count("l"), bString))

# if firstName == "John" and lastName == "Doe":
#     print("Your name is John Doe")
# if firstName == "John" or firstName =="Ram":
#     print("Your first name is either John or Ram")
# else:
#     print("You're a kind with no name")


# if firstName in ["John", "Rick"]:
#     print("Your name is either John or Rick")
# else:
#     print("You're none of Ram or Rick")

# a = [1, 2, 3]
# b = [3, 5, 6]
# print(a == b)
# print(a is b)

primes = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
# for prime in primes:
#     print(prime)

count = 1
# while count <= 5:
#     print(count)
#     count +=1

# while True:
#     print(count)
#     count += 1
#     if count >= 5:
#         break #acts like return
#         print("done")


# for x in range(10):
#     if x%2 == 0:
#         continue
#     print(x)


# def my_function(name, age):
#     print("%s is %d years old" % (name, age))

# my_function("Ram", 15)

# def sum_two_numbers(a, b):
#     return a + b
# sum_two_numbers(10, 15)

phoneBoook = {}
phoneBoook["John"] = 12345
phoneBoook["Purna"] = 2311
phoneBoook["Aaditya"] = 69696969
phoneBoook["Elon"] = 7070707070
# print(phoneBoook)

# OR

phoneBoook = {
    "John": 12345,
    "Purna": 2311,
    "Aaditya": 69696969,
    "Elon": 7070707070,
}
# del phoneBoook["Purna"]
# print(phoneBoook)


# for name, number in phoneBoook.items():
#     print(f"{name}'s phone number is {number}")


# if "John" in phoneBoook:
#     print("John is listed in the phonebook")

# if "Ram" not in phoneBoook:
#     print("Ram is not in phoneBook")


# from draw import *


# def play_game(): ...


# def main():
#     result = play_game()
#     draw_game(result)
