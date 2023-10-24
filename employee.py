class employee:
    def __init__(self, empid, empname, salary, age, gender, address, city, dob, doj, depname, designation, mobileno,
                 pan,
                 aadhaar):
        self.empid = empid
        self.empname = empname
        self.salary = salary
        self.age = age
        self.gender = gender
        self.address = address
        self.city = city
        self.dob = dob
        self.doj = doj
        self.depname = depname
        self.designation = designation
        self.mobileno = mobileno
        self.pan = pan
        self.aadhaar = aadhaar

    def display(self):
        print("\033[93m {}\033[00m".format(' Emp Id:'),"\033[92m {}\033[00m".format(self.empid),
              "\n", "\033[93m {}\033[00m".format('Name:'),"\033[92m {}\033[00m".format(self.empname),
              "\n", "\033[93m {}\033[00m".format('Salary:'),"\033[92m {}\033[00m".format(self.salary),
              "\n", "\033[93m {}\033[00m".format('Age:'),"\033[92m {}\033[00m".format(self.age),
              "\n", "\033[93m {}\033[00m".format('Gender:'),"\033[92m {}\033[00m".format(self.gender),
              "\n", "\033[93m {}\033[00m".format('Address:'),"\033[92m {}\033[00m".format(self.address),
              "\n", "\033[93m {}\033[00m".format('City:'),"\033[92m {}\033[00m".format(self.city),
              "\n", "\033[93m {}\033[00m".format('DOB:'),"\033[92m {}\033[00m".format(self.dob),
              "\n", "\033[93m {}\033[00m".format('DOJ:'),"\033[92m {}\033[00m".format(self.doj),
              "\n", "\033[93m {}\033[00m".format('Department:'),"\033[92m {}\033[00m".format(self.depname),
              "\n", "\033[93m {}\033[00m".format('Designation:'),"\033[92m {}\033[00m".format(self.designation),
              "\n", "\033[93m {}\033[00m".format('PAN:'),"\033[92m {}\033[00m".format(self.pan),
              "\n", "\033[93m {}\033[00m".format('Mobile Number:'),"\033[92m {}\033[00m".format(self.mobileno),
              "\n", "\033[93m {}\033[00m".format('Aadhhar:'),"\033[92m {}\033[00m".format(self.aadhaar))
