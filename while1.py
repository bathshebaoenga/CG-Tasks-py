no_of_input= 0
sum= 0

while True:
    user_input= int(input("please enter a number :"))

    if user_input == -1:
     break

    no_of_input += 1
    sum += user_input
    Average= sum/no_of_input

    print(f"the average is {Average: 2f}")



