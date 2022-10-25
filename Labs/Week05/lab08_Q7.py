#Filename: lab08_Q7.py
#Author: Deirdre
#Description: using selection statements

wavelength1 = "violet"
wavelength2 = "blue"
wavelength3 = "green"
wavelength4 = "yellow"
wavelength5 = "orange"
wavelength6 = "red"

x = int(input("Enter a wavelength of light: "))

if 380 <= x <= 450:
    print(wavelength1)
elif 450 <= x <= 495:
    print(wavelength2)
elif 495 <= x <= 570:
    print(wavelength3)
elif 570 <= x <= 590:
    print(wavelength4)
elif 590 <= x <= 620:
    print(wavelength5)
elif 620 <= x <= 750:
    print(wavelength6)
else:
    print("This wavelength is outside the visible colour spectrum.")



