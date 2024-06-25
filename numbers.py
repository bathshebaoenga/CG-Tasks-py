#ask user to enter 3 different integers

Num1= int(input("please enter the first integer :"))
Num2= int(input("please enter the second interger:"))
Num3= int(input("please enter the third integer:"))

# the sumof all the numbers
sum_of_num = Num1+ Num2 + Num3
print(sum_of_num)

#the first number minus the second number 
subtract = Num1 - Num2
print(subtract)

#the third number multiplied by the first number 
multiply = Num3 * Num1
print(multiply)

# the sum of all 3 numbers divided by the 3rd number 
divide = sum_of_num / Num3
print(divide)
