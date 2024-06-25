f =open('reg_form.txt','a')
studentid=" "

# w passed as second arguement to open file in write mode .
number_students=int(input("how many students do wish to register:"))
for i in range(number_students):
 while True: 
    studentid = input("please enter a student id :")
    if studentid ==0:
      print("please print another student id :")
    else:
        break

#loop created to run for the number of students to be be registered . e.g loop will run 4 times if 4 students wish to be registered.

with open ("reg_form.txt", "w") as file:
   file.write("studentid id :\n"+ f" {studentid}")