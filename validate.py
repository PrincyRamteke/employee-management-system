# Validate name and mobile no. .isaplha all should be alphabets
from random import randint
import re
from datetime import datetime, date

def valid_empid(empid):
    exp = '^[A-Z]{3}[0-9]{3}$'
    if re.match(exp,empid):
        return True
    else:
        return False

def valid_empname(empname):
    l=empname.split()
    if len(l)==3:
        if len(l[0]) > 1 and l[0].isalpha() and len(l[1]) > 1 and l[1].isalpha() and len(l[2]) > 1 and l[2].isalpha():
            # added one more check constraint to check that the name should not be single letter
            return True
    return False

def valid_salary(salary):
    if salary > 0:
        return True
    else:
        return False

def valid_increment(inc):
    if inc > 0:
        return True
    else:
        return False

def valid_age(age):
    if 20 <= age <= 80:
        return True
    return False

def valid_gender(gender):
    valid_gender = {"Male", "Female"}
    if gender in valid_gender:
        return True
    else:
        return False

# not working
def valid_address(address):
    if len(address) > 20:
        d = address.split(',')
        pincode = d[-1].strip()
        if pincode.isdigit() and len(pincode)==6:
            return True
        else:
            return False
    else:
        return False

# error
def valid_state(state):
    sc = {"Maharashtra":{"Mumbai","Pune","Nashik"},"Haryana":{"Gurugram","Noida"}}
    if state in sc:
        return True
    else:
        return False

def valid_city(state,city):
    sc = {"Maharashtra":{"Mumbai","Pune","Nashik"},"Haryana":{"Gurugram","Noida"}}
    if state in sc:
        v = sc[state]
        if city in v:
            return True
        else:
            return False
    else:
        return False

def valid_dob(dob):
    if valid_doj(dob):
        age = calculate_age(dob)
        if age > 20:
            return True
        else:
            return False
    else:
        return False

def valid_doj(doj):
    date_parts = doj.split('-')

    if len(date_parts) != 3:
        return False

    day, month, year = date_parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year, month, day = int(year), int(month), int(day)

    if 1960 <= year <= 2023 and 1 <= month <= 12 and 1 <= day <= 31:
        current_date = date.today()
        if year < current_date.year or (year == current_date.year and month <= current_date.month and day <= current_date.day):
            return True
        else:
            return False

def valid_dep(department):
    valid_departments = {"IT","HR","Finance","Accounts"}
    if department in valid_departments:
        return True
    else:
        return False

def valid_des(designation):
    valid_designations = {"Business Analyst","Software Engineer Associate","Java Developer","HR"}
    if designation in valid_designations:
        return True
    else:
        return False

def valid_mobileno(mobileno):
    if len(mobileno) == 10 and mobileno.isdigit():
        return True
    else:
        return False

def valid_pan(pan):
    exp = '^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if re.match(exp,pan):
        return True
    else:
        return False

def valid_aadhaar(aadhaar):
    if len(aadhaar)==12 and aadhaar.isdigit():
            return True
    else:
        return False

def calculate_age(date_of_birth):
    current_date = datetime.now()
    dob = datetime.strptime(date_of_birth, "%d-%m-%Y")
    age = current_date.year - dob.year - ((current_date.month, current_date.day) < (dob.month, dob.day))
    return age

def create_empid(emp_name):
    names = emp_name.split()
    empid = names[0][0].upper() + names[1][0].upper() + names[2][0].upper() + str(randint(100, 999))
    return empid
