from datetime import datetime
from datetime import date

print("=" * 50)
print("Welcome To Age Calculator")
print("=" * 50)

def getDate():
    while True:
        try:
            dob = input("Enter date of birth (YYYY-MM-DD): ")
            birth_date = datetime.strptime(dob, "%Y-%m-%d").date()

            if birth_date > date.today():
                print("Date is in the future! Try again")
                continue

            return birth_date

        except ValueError:
            print("Invalid date format, use YYYY-MM-DD format!")

# get date for today from function
d_today = date.today()

print("=" * 50)

do = getDate()

print("=" * 50)

print("Birth Date: ", do)
print("Today's Date: ", d_today)

# age calculated
age = d_today.year - do.year

print("-" * 50)
print("Your age in years is: ", age)

print("=" * 50)
print("Fun Facts:")
print("Number of days since you were born(approximately): ", age*365)
print("Total hours lived since born(approximately): ", age*365*24)










