weight = int(input('Enter your weight in kgs: '))
height = int(input('Enter your height in cms: '))

bmi = int(weight/((height/100)**2))

print('Your BMI: '+str(bmi))
if bmi<18.5:
  print("You are underweight")
elif bmi<25:
   print("You weight is normal and good")
elif bmi<30:
   print("You are overweight")
elif bmi<35:
   print("You are obese")
else:
   print("You are very obese")