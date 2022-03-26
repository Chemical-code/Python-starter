with open("info.txt", "r") as file:
    for line in file:
        # Declare variables
        (name, weight, height) = line.strip().split(", ")

        # Check data with error: if there is problem, pass it
        if (not name) or (not weight) or (not height):
            continue
        # Calculate result
        bmi = int(weight) / ((int(height) / 100) **2)
        result = ""
        if 25 <= bmi:
            result = "Overweight"
        elif 18.5 <= bmi:
            result = "Regular weight"
        else:
            result = "Low weight"
        
        # Print
        print('\n'.join([
            "name: {}",
            "weight: {}",
            "height: {}",
            "BMI: {}",
            "result: {}"
        ]).format(name, weight, height, bmi, result))
        print()
