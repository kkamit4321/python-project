all_data={}
choice = 0
while choice != 7:
    print("-----------------------menu button------------------------------")
    print("press 1 for insert the data")
    print("press 2 for update the data")
    print("press 3 for delete the data ")
    print("press 4 for show all data")
    print("press 5 for show roll no wise data")
    print("press 6 for exit")
    choice = int(input("enter choice"))
    if choice == 1:
        Student_name = input("Student name:")
        Father_name = input("father name of student:")
        Mother_name = input("Mother name of student")
        Address = input("Address of student")
        Mobile_no = int(input("enter mobile no"))
        Email_id = input("enter email_id")
        Roll_no = int(input("enter roll no:"))
        Course = input("Enter course")
        Institute_name = input("enter institute name") #Amit buddhu hai
        all_data.update({Roll_no: [Student_name, Father_name,Mother_name,Address,Mobile_no,Email_id,Course,Institute_name]})
        print("successfully insert data")
    if choice == 2:
        print(all_data)
        info_update_rollno = int(input("enter roll no which change the data of the student"))
        if  info_update_rollno == Roll_no:
            input_update_name = int(input("press 1 for update Student name\npress 2 for update father name "))
            match input_update_name:
                case 1:
                    info_update_Student = input("enter new name of Student :")
                    Student_name = info_update_Student
                    all_data.update({Roll_no: [Student_name, Father_name]})
                case 2:
                    info_update_Father = input("enter new name of father ")
                    Father_name = info_update_Father
                    all_data.update({Roll_no: [Student_name, Father_name]})
                case 3:
                    print("invalid input")
            print("update successfully")
        else:
            print("invalid roll no")
    if choice == 3:
        info_delete_rollno = int(input("enter roll no which delete the data of the student:"))
        if info_delete_rollno == Roll_no:
            del all_data[Roll_no]
        print("delete data successfully")
    if choice == 4:
        print(all_data)
    if choice == 5:
        check_rollno=int(input("enter roll no which you want to check data"))
        if(check_rollno==Roll_no):
            print(all_data[Roll_no])
    if choice == 6:
        pass
        print("you are successfully exit")

