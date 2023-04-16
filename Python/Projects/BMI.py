Height = float(input(" Enter your height in centimeters : "))
Weight = float(input(" Enter your height in Kg : "))
Height = Height / 100
BMI = Weight / (Height * Height)
print (" Your BMI is : " , BMI)
if (BMI > 0) :
            if (BMI <= 18.5) :
                    print(" Underweight ")
            elif (BMI <= 23) :
                    print(" Healthy ")
            elif (BMI <= 25) :
                    print(" Overweight ")
            elif (BMI <= 30) :
                    print(" Mild obesity ")
            else : 
                    print(" Excessive obesity ")
        