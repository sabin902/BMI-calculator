

print("++++++++++++++")
print("BMI CALCULATOR")
print("++++++++++++++")



def bmi_calculation(weight,height):
	
	try:
		height = int(height)
		weight = int(weight)
		bmi = weight / ((height/100) ** 2)
		return bmi
	except:
		return "wrong input"
	
def bmi_status(func):
	try:
		a = func + 10
		if func < 18.5:
			return "underweight"
		elif func >= 18.5 and func <= 24.9:
			return "normal"
		elif func >= 25 and func < 30:
			return "over weight"
		elif func >= 30:
			return "obese"
	except:
		return "something went wrong"
		
while True:
	print()
	inp = input("do you want to check your BMI(y/n): ").lower()
	if inp == 'n':
		print("Thank  you")
		break
	print()
	height = input("Enter your height in centimeter: ")
	weight = input("Enter weight in kilogram: ")
	bmi = bmi_calculation(weight,height)
	print()
	print("BMI : ",bmi)
	print("BMI status: ",bmi_status(bmi))
