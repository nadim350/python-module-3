
gender = input("Enter your biological gender (male/female): ").strip().lower()
hemoglobin = float(input("Enter your hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif 117 <= hemoglobin <= 155:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
elif gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif 134 <= hemoglobin <= 167:
        print("Your hemoglobin level is normal.")
    else:
        print("Your hemoglobin level is high.")
else:
    print("Invalid input for gender. Please enter 'male' or 'female'.")
