cars = 100 
#number of cars
space_in_a_car = 4.0 
#why is there .0? 
drivers = 30 
# no. of drivers
passengers = 90
#amount of people who needs rides
cars_not_driven = cars - drivers 
#difference
cars_driven = drivers 
#tru
car_pool_capacity = cars_driven * space_in_a_car 
# Amount of space in the cars
average_passengers_per_car = passengers / cars_driven 
# # of passengers in the car - the drivers


print "There are", cars , "cars available." 
print "There are only", drivers , "drivers available." 
print "There will be", cars_not_driven, "empty cars today." 
print "we can transport" , car_pool_capacity, "people today." 
print "We have", passengers , "to carpool today." 
print "We need to put about", average_passengers_per_car , "in each car." 