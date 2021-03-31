NumberString = '100.21'

if NumberString.isdigit():
    Number = int(NumberString)
    Number = float(Number)
else:
    Number = float(NumberString)


print(float(Number))