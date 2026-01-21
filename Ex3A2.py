def hemoglobin_value():
    sex = str(input("Enter your sex: "))
    hemoglobin = float(input("Enter your hemoglobin value: "))
    if sex == "male":
        if hemoglobin < 134:
            print("Your hemoglobin is low.")
        elif hemoglobin > 167:
            print("Your hemoglobin is high.")
        else:
            print("Your hemoglobin is normal.")
    elif sex == "female":
        if hemoglobin < 117:
            print("Your hemoglobin is low.")
        elif hemoglobin > 155:
            print("Your hemoglobin is high.")
        else:
            print("Your hemoglobin is normal.")
hemoglobin_value()