import math

from employee import employee
from validate import valid_empid, valid_empname, valid_salary, valid_increment, valid_age, valid_gender, valid_address, valid_city, valid_state, \
    valid_dob, valid_doj, valid_dep, valid_des, valid_mobileno, valid_pan, valid_aadhaar, calculate_age, create_empid

Emp = []
while True:
    print("1: Add the Record ")
    print("2: Display the Record ")
    print("3: Search the Record ")
    print("4: Update the Record ")
    print("5: Delete the Record ")
    print("6: Display the details of employee with highest salary")
    print("7: Display the details of employee with lowest salary")
    print("8: Exit ")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        while True:
            empname = input("Enter your Name: ")
            if valid_empname(empname.upper()):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter Name in the format First Middle Surname: "))
        while True:
            salary = int(input("Enter your Salary: "))
            if valid_salary(salary):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct salary: "))
        while True:
            gender = input("Enter your Gender: ")
            if valid_gender(gender.title()):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct gender: "))
        while True:
            address = input("Enter your Address: ")
            if valid_address(address):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter address with pincode: "))
        while True:
            state = input("Enter your State: ")
            if valid_state(state.title()):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct state: "))
        while True:
            city = input("Enter your City: ")
            if valid_city(state.title(), city.title()):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct city: "))
        while True:
            dob = input("Enter your Date of Birth in DD-MM-YYYY format: ")
            if valid_dob(dob):
                age = calculate_age(dob)
                if valid_age(age):
                    break
                else:
                    print("\033[091m {}\033[00m".format("Age should be greater than 20"))
            else:
                print("\033[091m {}\033[00m".format("Age should be greater than 20"))
        while True:
            doj = input("Enter your Date of Joining in DD-MM-YYYY format: ")
            if valid_doj(doj):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct date of joining"))
        while True:
            depname = input("Enter your Department Name: ")
            if valid_dep(depname):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct department"))
        while True:
            designation = input("Enter your Designation: ")
            if valid_des(designation):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct designation"))
        while True:
            mobileno = input("Enter your Mobile Number without country code: ")
            if valid_mobileno(mobileno):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct 10 digit mobile number"))
        while True:
            pan = input("Enter your PAN card number: ")
            if valid_pan(pan):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct PAN number"))
        while True:
            aadhaar = input("Enter your Aadhaar card number: ")
            if valid_aadhaar(aadhaar):
                break
            else:
                print("\033[091m {}\033[00m".format("Please enter correct aadhaar number"))
        while True:
            empid = create_empid(empname)
            if not valid_empid(empid):
                print("\033[091m {}\033[00m".format("Error generating a valid employee id. Please try again."))
            else:
                break
        e = employee(
            empid=empid,
            empname=empname,
            salary=salary,
            age=age,
            gender=gender,
            address=address,
            city=city,
            dob=dob,
            doj=doj,
            depname=depname,
            designation=designation,
            mobileno=mobileno,
            pan=pan,
            aadhaar=aadhaar,
        )
        Emp.append(e)
    elif choice == 2:
        print("Details of the Employee")
        for i in Emp:
            i.display()
    elif choice == 3:
        print("Press A to search by Name")
        print("Press B to search by Employee ID")
        print("Press C to search by Department Name")
        ch = input("Enter your choice: ")
        if ch == "A":
            nm = input("Enter the name to be searched: ")
            for i in Emp:
                if i.empname == nm:
                    i.display()
        elif ch == "B":
            e = input("Enter the Employee ID to be searched: ")
            for i in Emp:
                if i.empid == e:
                    i.display()
        elif ch == "C":
            dp = input("Enter the Department name to be searched: ")
            for i in Emp:
                if i.depname == dp:
                    i.display()
    elif choice == 4:
        print("Press i to update Name")
        print("Press ii to update Salary")
        print("Press iii to update Address")
        print("Press iv to update Mobile Number")
        ch = input("Enter your choice: ")
        if ch == 'i':
            while True:
                emp = input("Enter the Employee ID: ")
                nm = input("Enter the updated Name: ")
                if valid_empname(nm) and valid_empid(emp):
                    for i in Emp:
                        if i.empid == emp:
                            i.empname = nm
                            break
                else:
                    print("\033[091m {}\033[00m".format("Please enter Name in the format First Middle Surname"))
        elif ch == 'ii':
            print("Press 1 to update salary of specific Employee by Employee ID")
            print("Press 2 to update salary of all Employees working in specific department")
            print("Press 3 to update salary of all Employees")
            cho = int(input("Enter your choice: "))
            if cho == 1:
                is_internal_break = False
                while True:
                    emp = input("Enter the Employee ID: ")
                    inc = float(input("Enter the salary increment percentage: "))
                    if valid_empid(emp) and valid_increment(inc):
                        for i in Emp:
                            if i.empid == emp:
                                i.salary += inc*i.salary/100
                                is_internal_break = True
                                break
                    else:
                        print("\033[091m {}\033[00m".format("Please enter valid Employee ID or valid salary"))
            elif cho == 2:
                while True:
                    dep = input("Enter the Department: ")
                    inc = float(input("Enter the salary increment percentage: "))
                    if valid_dep(dep) and valid_increment(inc):
                        for i in Emp:
                            if i.depname == dep:
                                i.salary += inc*i.salary/100
                    else:
                        print("\033[091m {}\033[00m".format("Please enter valid department name or valid salary"))
            elif cho == 3:
                while True:
                    inc = float(input("Enter the salary increment percentage: "))
                    if valid_increment(inc):
                        for i in Emp:
                            i.salary += inc*i.salary/100
                    else:
                        print("\033[091m {}\033[00m".format("Please enter valid salary"))
            else:
                print("\033[091m {}\033[00m".format("Salary should be greater than 0"))

        elif ch == 'iii':
            while True:
                emp = input("Enter the Employee ID: ")
                ad = input("Enter the updated Address: ")
                if valid_empid(emp) and valid_address(ad):
                    for i in Emp:
                        if i.empid == emp:
                            i.address = ad
                            break
                else:
                    print("\033[091m {}\033[00m".format("Please enter correct address"))
        elif ch == 'iv':
            while True:
                emp = input("Enter the Employee ID: ")
                m = input("Enter the updated Mobile number: ")
                if valid_empid(emp) and valid_mobileno(m):
                    for i in Emp:
                        if i.empid == emp:
                            i.mobileno = m
                            break
                else:
                    print("\033[091m {}\033[00m".format("Please enter dob in DD-MM-YYYY format"))
        else:
            print("\033[091m {}\033[00m".format("Invalid choice"))

    elif choice == 5:
        e = input("Enter the Employee ID to delete the record: ")
        for i in Emp:
            if i.empid == e:
                Emp.remove(i)

    elif choice == 6:
        max_salary = 0
        e = None
        for i in Emp:
            if i.salary > max_salary:
                max_salary = i.salary
                e = i
        if e is not None:
            e.display()
        else:
            print("\033[091m {}\033[00m".format("No max salary"))

    elif choice == 7:
        min_salary = math.inf
        e = None
        for i in Emp:
            if i.salary < min_salary:
                min_salary = i.salary
                e = i
        if e is not None:
            e.display()
        else:
            print("\033[091m {}\033[00m".format("No min salary"))

    elif choice == 8:
        break
    else:
        print("\033[091m {}\033[00m".format("Invalid choice"))