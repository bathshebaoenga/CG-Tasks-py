#ask the user to enter a sentce using the input method and save the response in a variable called str_manip
str_manip =input("please enter a sentence :")

# task 1 calculate and display the length of str_manip
print(len(str_manip))

#Task 2 - find the last letter of str_manip sentence. and replace every occurence of this letter with @

Last_letter = str_manip[-1]
str_manip_replace= str_manip.replace(Last_letter, "@")
print(str_manip_replace)

#Task 3-print the last 3 characters in str_manip backwards
print(str_manip[:-4:-1])

#Task 4-create a five letter word that is made up of the first three characters and last two character in str_manip.
string_slice= str_manip[0:4] +str_manip[-2:]
print(string_slice)