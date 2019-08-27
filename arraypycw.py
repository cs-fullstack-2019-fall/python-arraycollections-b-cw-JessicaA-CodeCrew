# # Problem 1:
# #
# # Create a function with the variable below. After you create the variable do the instructions below that.
# #
# # arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
#
# # a) Print the 3rd element of the numberList.
# # b) Print the size of the array
# # c) Delete the second element.
# # d) Print the 3rd element.
#
# def problem1():
#     variableBelow()
#
# def variableBelow():
#     arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
#     print(arrayForProblem2[2])
#     len(arrayForProblem2)
#     print(len(arrayForProblem2))
#     del(arrayForProblem2[1])
#     print(arrayForProblem2)
#     print(arrayForProblem2[2])
#
#
# problem1()
#
# # Problem 2:
# #
# # We will keep having this problem until EVERYONE gets it right without help
# #
# # Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
#
# def problem2():
#     userInput = ""
#     while(userInput != 'q'):
#         userInput = input("Try again")
#
# problem2()

# Problem 4:
#
# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function

# fiveNumbers = [10, 0, 5, 15, 20]
# for x in reversed(fiveNumbers):
#     print (x)

# Problem 5:
#
# Create a function that will have a hard coded array then ask the user for a number. Use the userInput to state how many numbers in an array are higher, lower, or equal to it.

def problem5():
    hardCodedArray()

def hardCodedArray():
    arrayOfNumbers = [1,2,3,4,5]
    for eachElement in arrayOfNumbers:
        if eachElement == 5:
            return arrayOfNumbers
        elif eachElement > 5:
            return arrayOfNumbers
        elif eachElement < 1:
            return arrayOfNumbers

problem5()


