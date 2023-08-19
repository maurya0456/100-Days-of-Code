height = float(input("Enter your height in m "))
weight = float(input("Enter your weight in Kg "))

bmi_val = round(weight / height ** 2, 2)

if bmi_val < 18.5:
    print("Your BMI value is {0}, you are underweight".format(bmi_val))
elif bmi_val < 25:
    print("Your BMI value is {0}, you are normal weight".format(bmi_val))
elif bmi_val < 30:
    print("Your BMI value is {0}, you are overweight".format(bmi_val))
elif bmi_val < 35:
    print("Your BMI value is {0}, you are obese".format(bmi_val))
else:
    print("Your BMI value is {0}, you are clinically obese".format(bmi_val))

# ans = 5
# x = ++ans
# print(x, ans)
