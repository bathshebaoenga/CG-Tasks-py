user_input= str(input("please enter a sentence:"))

split_string= user_input.split()

final_string =" "

for i in range(len(split_string)):
    if i % 2 == 0:
        final_string += split_string[i].upper()+" "
    else:
        final_string += split_string[i].lower()+ " "

print(final_string)



user_input1= input("please enter a greeting:")

letter_split = user_input1.split()

alternative_string = ""


for i , chr in enumerate (user_input1):
    if i % 2 == 0:
        alternative_string += chr.upper()
    else:
        alternative_string += chr.lower()

print(alternative_string)

