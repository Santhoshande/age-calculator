#agecalculator.py

from datetime import datetime

def calculate_age(birth_year):
    current_year = datetime.now().year
    age = current_year - birth_year
    return age

birth_year = int(input("Enter you Birth year: "))
print("you are", calculate_age(birth_year), "years old." )
