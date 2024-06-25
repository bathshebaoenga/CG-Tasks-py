cycling= int(input("please enter completion time of cycling event :"))
running =int(input("please enter completion time of the running event:"))
swimming=int(input("please enter completion time of the swimming event:"))

triatholon_completion_time = swimming+cycling+running
print("total completion time: ",triatholon_completion_time,"minute")

if triatholon_completion_time>= 111:
    print("no award !better luck next time")
elif triatholon_completion_time>=106 or triatholon_completion_time==110:
    print("congratulations you have won a provinical scroll !! woop !")
elif triatholon_completion_time>=101 or triatholon_completion_time==105:
    print("congratulations you have won a provincial half colours award !!") 
else:
    print("congratulations you have won a provincial colours award !") 
