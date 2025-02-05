wieght = float( input("Enter your wieght in kg:"))
height = float( input("Enter your height in cm:"))

bmi = wieght / height 



print(f"Your BMI is: {bmi:.2f}")


if bmi < 60:
  print("You are overwieght you need to work out more and watch your diet.")

elif bmi > 50:
  print("You are fit & healthy.")

else:
  print("You are underweight. Watch your health.")