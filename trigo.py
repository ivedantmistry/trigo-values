import math

unit = input("Enter the unit (degree or radian): ").lower()
angle = float(input("Enter the angle: "))

if unit == 'degree':
    angle = math.radians(angle)

# Calculate the trigonometric functions
sin_value = math.sin(angle)
cos_value = math.cos(angle)
tan_value = math.tan(angle)
cosec_value = 1 / sin_value
sec_value = 1 / cos_value
cot_value = 1 / tan_value

# Print the results
print("sin({}) = {}".format(angle, sin_value))
print("cos({}) = {}".format(angle, cos_value))
print("tan({}) = {}".format(angle, tan_value))
print("cosec({}) = {}".format(angle, cosec_value))
print("sec({}) = {}".format(angle, sec_value))
print("cot({}) = {}".format(angle, cot_value))
