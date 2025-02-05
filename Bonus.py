wieght = float( input("Enter your wieght in kg:"))
height = float( input("Enter your height in cm:"))

bmi = wieght / (height / 100) **2



print(f"Your BMI is: {bmi:.2f}")


if bmi >= 25:
  print("You are overwieght you need to work out more and watch your diet.")

elif 18.5 <= bmi < 25 :
  print("You are fit & healthy.")

else:
  print("You are underweight. Watch your health.")