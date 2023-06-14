Year = int(input("Enter year: "))
if Year % 400 == 0 and Year % 100 == 0:
    print("It is a leap year")
elif Year % 4 == 0 and Year % 100 != 0:
    print("It is a leap year")
else:
    print("It is not a leap year")