#Khristel Perez Newton's law of universal gravitation
print("Newton Law of universal gravitation")
import math
#This is the Gravitational Measurement 
print("Start by positioning our units")
#make sure the mass is in Kg and in thoundsands (50000)
mass_of_object_1    =	float (input("m1(kg): "))
mass_of_object_2	=	float (input("m2(kg): "))

#and distance between mass be in tenths (10)
distance = float(input(' r(m): '))

G = 6.673*(10**-11)

# Calculating Gravitational Force
F = (G*mass_of_object_1*mass_of_object_2)/(distance*2)

# Result
print('Gravitational Force = %f Newton' %(F))