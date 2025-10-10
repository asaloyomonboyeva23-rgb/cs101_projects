
celsius = float(input(" enter the temperature :"))
fahreheit = (celsius * 9/5 )+ 32 
kelvin = celsius + 273.15 
print(f" celsius temperature :{ celsius:.2f} ")
print(f" fahrenheit temperature : {fahreheit:.2f}")
print(f" kelvin temperature : {kelvin:.2f} ")

2
r = float(input("enter the radius : "))
pi = 3.14159
Area = pi * r**2
Circumference = 2 * pi * r
print(f" the area  :{ Area:.2f} ")
print(f" the circumference :{ Circumference:.2f} ")
3 

student_name = input("Enter your name  : ")
gpa = float(input(" enter your gpa :"))
credit_hours =int(input("enter tour creadit hours :"))
deans_list = gpa >= 3.5 and credit_hours >=12

print(f"student information : {student_name} , {gpa} , {credit_hours}")
print(f" Deans_status : {"true" if deans_list else " False"}")
print(f" how many gpa status needed :{"no need" if gpa >= 3.5 else 3.5 - gpa}")
print(f" how many more credits needed : {"no need" if credit_hours >= 12 else 12 - credit_hours}")
