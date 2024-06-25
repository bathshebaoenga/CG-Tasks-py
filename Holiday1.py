cost_table= {'paris':150 ,'barcelona':95,'milan':78,'amsterdam':69,'lisbon':67,'budapest':52.99}
#cost table including city destinations and price of flights to the specific destination.

#functions to calculate the holiday cost (hotel cost+ plane cost + car rental cost )
def hotel_cost(nights):
    cost= 140 * int(nights)
    return cost

def plane_cost(city):
    return cost_table[city]

def car_rental_cost(days):
    cost_day= 40 * days
    return cost_day

def trip_cost(city, nights, rental_car):
    total= hotel_cost(nights)+plane_cost(city)+\
        car_rental_cost(rental_car)
    return total


#get input from user to calculate cost of holiday :)
city=None
while True:
    city=input("please select your city break destination:")
    if city not in cost_table:
        print("that's not a valid destination ,please try again")
    else:
        break

hotel_nights=input("please enter the number of days you wish to stay :")
rental_days=input(" please enter the number of days you require a car hire:")

total_trip_cost = hotel_cost(int(hotel_nights))+plane_cost(city)+car_rental_cost(int(rental_days))

print("the total cost with the trip is",total_trip_cost,"pounds")