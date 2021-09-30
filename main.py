
#Importing modules
import time
import random
import string



print('''

Welcome to BMI calculator...
Enter correct values of your weight and height in order to get your bmi
very quick
The source code was made by Hunar Bishnoi Copyrights 2021 claimed
Use not allowed without permission.
contact at : github.com/agrimbishnoi

''')

time.sleep(3)

name = input("Enter your full name : ")
print()
age = input("Enter your current age : ")
print()
w = float(input("Enter your weight : "))
wtype = input("Is your weight in (K)g or (L)bs : ")

if wtype.lower() == 'k':
     neww = w
elif wtype.lower() == 'l':
     neww = w * 0.45
     print("So your weight in kg is ",neww)

else:
     print("Your gave an non existing variable.")
print()

h = float(input("Enter your height : "))

htype = input("Is your weight in (M)eters or (C)enti-meters : ")

if htype.lower() == 'm':
     newh = h
elif htype.lower() == 'c':
     newh = h / 100
     print("So your height in meters is ",newh)

else:
     print("Your gave an non existing variable.")

print()
print("Processing your BMI..")

print()


time.sleep(3)



h2 = newh * newh
bmi = neww / h2
print("Your Bmi value is",bmi)




if bmi >=15 and bmi < 18.5 :
     nvalue = "You fall within the underweight range"
     comment = "You sholud start eating healthy food in respectable amount"
elif bmi >= 18.5 and bmi < 25 :
     nvalue = "You fall within the normal range"
     comment = "You sholud maintain your diet with slight exercise."
elif bmi >= 25 and bmi < 30 :
     nvalue = "You fall within the overweight range"
     comment = "You sholud lose weight by extercise and limiting your
diet to healthy and less amount of food"
elif bmi <= 30 :
     nvalue = "You fall within the obesity range"
     comment = "You sholud focus on losing a lot of weight for
betterment of your heath."
else:
     nvalue = "hmm.. your bmi value",bmi,"was not expected. Seems you
gave wrong values of yourself."
     comment = "You sholud reconsider entering correct values to system. "
print()

print("Prepairing your report by our extremly qualified doctor -Dr Agrim
Bishnoi")
time.sleep(4)
print()
print("Your report: ")
print()
print("Name : "+name)
print("Age : ",age)
print("BMI value : ",bmi)
print("Value calculated : "+nvalue)
print("Doctor's comment : "+comment)

print()
time.sleep(10)
print("Thank you for using the script")
print("Now pay our doctor's fee i.e. $120.99 LOL")
