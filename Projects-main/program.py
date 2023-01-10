import mysql.connector as mysql

db = mysql.connect(host="beetle",user="root",password="ashique",database="college")
command_handler = db.cursor()

#Insert details Function
def studentEntry():
    print("Register New Student")
    reg_no = int(input("Enter reg no : "))
    name = input(str("Enter your full name: "))
    dob = input(str("Enter your birth date (YYYY-MM-DD) : "))
    phone = input("Enter your phone number : ")
    email = input(str("Enter email : "))
    password = input(str("Student password : "))
    address = input(str("Enter your Address : "))
    course = input(str("Enter your Course : "))
    query_vals = (reg_no,name,dob,phone,email,password,address,course)
    command_handler.execute("INSERT INTO studentDets VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",query_vals)
    db.commit()
    print(name + " has been registered as a student")
def teacherEntry():
    print("Register New Teacher")
    reg_no = int(input("Enter reg no : "))
    name = input(str("Enter your full name: "))
    dob = input(str("Enter your birth date (YYYY-MM-DD) : "))
    phone = input("Enter your phone number : ")
    email = input(str("Enter email : "))
    password = input(str("Enter your Password : "))
    address = input(str("Enter your Address : "))
    course = input(str("Enter your Course : "))
    query_vals = (reg_no,name,dob,phone,email,password,address,course)
    command_handler.execute("INSERT INTO teacherDets VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",query_vals)
    db.commit()
    print(name + " has been registered as a teacher")


def student_session(regNo):
    reg_no = int(regNo)
    while 1:
        print("\nWELCOME\n")
        print("1. Update Your Name")
        print("2. Update Your Phone Number")
        print("3. Change Your Password")
        print("4. Change Your Date Of Birth")
        print("5. Update Your Address")
        print("6. Update Your Email Address")
        print("7. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            new_name = input("Enter your new name : ")
            sql = "UPDATE studentDets set name = %s where reg_no = %s "
            command_handler.execute(sql,(new_name,reg_no))
            db.commit()
            print("\nYour name has been Updated!\n")

        elif user_option == "2":
            print("")
            new_phoneNum = input("Enter your new phone number : ")
            sql = "UPDATE studentDets set phoneNo = %s where reg_no = %s"
            command_handler.execute(sql,(new_phoneNum,reg_no))
            db.commit()
            print("\nYour phone number has been Updated!")

        elif user_option == "3":
            print("")
            new_password = input("Enter your new password : ")
            sql = "UPDATE studentDets set password = %s where reg_no = %s "
            command_handler.execute(sql,(new_password,reg_no))
            db.commit()
            print("\nYour password has been Updated!")

        elif user_option == "4":
            print("")
            new_dob = input("Enter your date of birth : ")
            sql = "UPDATE studentDets set dateOfBirth = %s where reg_no = %s "
            command_handler.execute(sql,(new_dob,reg_no))
            db.commit()
            print("\nYour Date Of Birth has been Updated!")

        elif user_option == "5":
            print("")
            new_address = input("Enter your new address : ")
            sql = "UPDATE studentDets set address = %s where reg_no = %s"
            command_handler.execute(sql,(new_address,reg_no))
            db.commit()
            print("\nYour address has been Updated!")
        
        elif user_option == "6":
            print("")
            new_emailAdd = input("Enter your new email address : ")
            sql = "UPDATE studentDets set emailAdd = %s where reg_no = %s "
            command_handler.execute(sql,(new_emailAdd,reg_no))
            db.commit()
            print("\nYour Email address has been Updated!")
        elif user_option == "7":
            break
def teacher_session(regNo):
    reg_no = int(regNo)
    while 1:
        print("\nWELCOME\n")
        print("1. Update Your Name")
        print("2. Update Your Phone Number")
        print("3. Change Your Password")
        print("4. Change Your Date Of Birth")
        print("5. Update Your Address")
        print("6. Update Your Email Address")
        print("7. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            new_name = input("Enter your new name : ")
            sql = "UPDATE teacherDets set name = %s where reg_no = %s "
            command_handler.execute(sql,(new_name,reg_no))
            db.commit()
            print("Your name has been Updated!\n")

        elif user_option == "2":
            print("")
            new_phoneNum = input("Enter your new phone number : ")
            sql = "UPDATE teacherDets set phoneNo = %s where reg_no = %s"
            command_handler.execute(sql,(new_phoneNum,reg_no))
            db.commit()
            print("\nYour phone number has been Updated!")

        elif user_option == "3":
            print("")
            new_password = input("Enter your new password : ")
            sql = "UPDATE teacherDets set password = %s where reg_no = %s "
            command_handler.execute(sql,(new_password,reg_no))
            db.commit()
            print("\nYour password has been Updated!")

        elif user_option == "4":
            print("")
            new_dob = input("Enter your date of birth : ")
            sql = "UPDATE teacherDets set dateOfBirth = %s where reg_no = %s "
            command_handler.execute(sql,(new_dob,reg_no))
            db.commit()
            print("\nYour Date Of Birth has been Updated!")

        elif user_option == "5":
            print("")
            new_address = input("Enter your new address : ")
            sql = "UPDATE teacherDets set address = %s where reg_no = %s"
            command_handler.execute(sql,(new_address,reg_no))
            db.commit()
            print("\nYour address has been Updated!")
        
        elif user_option == "6":
            print("")
            new_emailAdd = input("Enter your new email address : ")
            sql = "UPDATE teacherDets set emailAdd = %s where reg_no = %s "
            command_handler.execute(sql,(new_emailAdd,reg_no))
            db.commit()
            print("\nYour Email address has been Updated!")
        
        elif user_option =="7":
            break
def admin_session():
    while 1:
        print("\nWELCOME\n")
        print("Admin Menu") 
        print("1. Register new Student")
        print("2. Register new Teacher")
        print("3. Delete Existing Student")
        print("4. Delete Existing Teacher")
        print("5. List of Students")
        print("6. List of Teachers")
        print("7. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("")
            studentEntry()
        
        elif user_option == "2":
            print("")
            teacherEntry()
    
        elif user_option == "3":
            print("")
            print("Delete Existing Student Account")
            reg_no = int(input("Enter your Registration Number : "))
            command_handler.execute("DELETE FROM studentDets WHERE reg_no = %s",(reg_no,))
            db.commit()
            if command_handler.rowcount < 1:
                print("User not found")
            else:
                print("User with Registration Number " + str(reg_no) + " has been deleted")
        
        elif user_option == "4":
            print("")
            print("Delete Existing Teacher Account")
            reg_no = input("Enter the registration number: ")
            sql = "DELETE FROM teacherDets WHERE reg_no = %s"
            command_handler.execute(sql,(reg_no,))
            db.commit()
            if command_handler.rowcount < 1:
              print("User not found")
            else:
                print("User with Registration Number " + str(reg_no) + " has been deleted!")
        
        elif user_option == "5":
            print("")
            print("List of Student")
            sql = "SELECT reg_no,name from studentDets"
            command_handler.execute(sql)
            listOfStu = command_handler.fetchall()
            for x in listOfStu:
                print(x)
            db.commit()

        elif user_option == "6":
            print("")
            print("List of Teacher")
            sql = "SELECT reg_no,name from teacherDets"
            command_handler.execute(sql)
            listOfTeach = command_handler.fetchall()
            for x in listOfTeach:
                print(x)
            db.commit()

        elif user_option == "7":
            break
        else:
            print("No valid option selected")

#Login Details Check
def student_auth():
    print("")
    print("Student Login")
    print("")
    reg_no = int(input("Registration Number : "))
    password = input("Password : ")
    sql = "Select password from users where reg_no = %s and privilege = %s"
    command_handler.execute(sql,(reg_no,'Student'))
    check_password = command_handler.fetchone()
    for x in check_password:
        if password == str(x):
            student_session(reg_no)
        else:
           print("Login details not recognized")
def teacher_auth():
    print("")
    print("Teacher Login")
    print("")
    reg_no = int(input("Registration Number : "))
    password = input("Password : ")
    sql = "Select password from users where reg_no = %s and privilege = %s"
    command_handler.execute(sql,(reg_no,'Teacher'))
    check_password = command_handler.fetchone()
    for x in check_password:
        if password == str(x):
            teacher_session(reg_no)
        else:
           print("Login details not recognized")
def admin_auth():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username : "))
    password = input(str("Password : "))
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("Incorrect password !")
    else:
        print("Login details not recognized") 

def main():
    while 1:
        print(" Welcome to the college system ")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")
        print("4. Exit")

        user_option = input(str("Option : "))
        if user_option == "1":
            student_auth()
        elif user_option == "2":
            teacher_auth()  
        elif user_option == "3":
            admin_auth()
        elif user_option == "4":
            break
        else:
            print("No valid option was selected")
main()
