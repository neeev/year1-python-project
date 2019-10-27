# program initiated with definition of global, empty dictionaries & creation of
# frequently reused templates
emp_dict = {}
pos_dict = {}
header = "{:5}{:30}{:5}{:20}{:10}{:6}".format(
    "No.", "Name", "Age", "Position", "Salary", "Length")


# takes user input for initial, required user-action
def main():
    file_open()
    main_menu()
    print("*" * 76 + "\n")
    menu_select = gci("Enter an option from the menu:\t", int, 1)
    menu_nav(menu_select)
# end of main()


# populate the dictionary with the data read from the data set, and closes file
def file_open():
    dataset = open("CW2_Emp_Dataset.txt", "r")
    for rcrd in dataset.readlines()[1:]:
        emp = rcrd.rstrip().split('\n')
        for attrs in emp:
            attr = attrs.rstrip().split(', ')
            emp_dict[attr[0]] = (attr[1], attr[2], attr[3], attr[4], attr[5])
        # end of for loop
    # end of for loop
    dataset.close()
# end of function file_open()


# shows the main menu text
def main_menu():
    print("\n" + "*" * 76, "{:>16}".format("MENU"),
          "{:>3}".format("1) Summary"),
          "{:>3}".format("2) Employee Details"),
          "{:>3}".format("3) Total Salary Bill"),
          "{:>3}".format("4) Average Salary"),
          "{:>3}".format("5) Add New Employee"),
          "{:>3}".format("6) Delete Employee"),
          "{:>3}".format("7) Employees by Position"),
          "{:>3}".format("8) Salary Threshold"),
          "{:>3}".format("9) Quit"), sep="\n", end="\n")
# end of main_menu()


# globally controls and validates user inputs
def gci(inp, dt=None, lim=None):
    while True:
        ui = input(inp)
        if inp == 'Num:\t' and (len(ui) != 3):
            if len(ui) != 3:
                print("Must be 3 characters long.")
                continue
        if '[Y/N]:\t' in inp:
            if ui not in ['Y', 'y', 'N', 'n']:
                print("Please enter [Y] or [N].")
                continue
        if lim is not None and len(ui) > lim:
            print("Max {} character(s) allowed.".format(lim))
            continue
        if dt is not None:
            if dt == int and not all(nums.isdigit() for nums in ui):
                print("Only numbers accepted in this field.")
                continue
            elif dt == str and not all(chars.isalpha() or chars.isspace()
                                       for chars in ui):
                print("Only letters and spaces accepted in this field.")
                continue
        return ui
# end of gci()



# takes value inputted by user and executes function according to user input
def menu_nav(menu_select):
    # if user enters '8' upon prompt, the program will quit.
    while menu_select != '9':
        if menu_select == '1':
            task_1()
        elif menu_select == '2':
            task_2()
        elif menu_select == '3':
            task_3()
        elif menu_select == '4':
            task_4()
        elif menu_select == '5':
            task_5()
        elif menu_select == '6':
            add_feat()
        elif menu_select == '7':
            task_6()
        elif menu_select == '8':
            task_7()
        elif menu_select == '9':
            break
        else:
            print("INPUT ERROR: Not a valid option from the menu.")
        # end of if-elif-else statement

        # provides the user the option to continue operations with or without
        # displaying the main menu
        print("\n"+"*"*76+"\n")
        show_menu = gci("Show menu? [Y/N]:\t", str, 1)
        if show_menu in ['Y', 'y']:
            main_menu()
            menu_select = gci("\nEnter an option from the menu:\t", int, 1)
        elif show_menu in ['N', 'n']:
            menu_select = gci("\nEnter an option from the menu:\t", int, 1)
        # end of if-elif-else statement
    # end of while loop
    print("Any unsaved changes will be lost.")
    sure = gci("Are you sure you want to quit? [Y/N]:\t", str, 1)
    if sure in ['Y', 'y']:
        print("QUITTING THE PROGRAM . . .")
    elif sure in ['N', 'n']:
        menu_select = gci("Enter an option from the menu:\t", int, 1)
        menu_nav(menu_select)
# end of menu_nav(menu_select)


# displays a list of employees in the program and their respective details
def task_2():
    print("\n"+"*"*29, "EMPLOYEE DETAILS", "*"*29+"\n")
    print(header+"\n"+"-"*76)
    for key, att in emp_dict.items():
        print("{:5}{:30}{:5}{:20}{:10}{:6}".format(
            key, att[0], att[1], att[2], att[3], att[4]))
# end of task_2()


# stores and calculates numbers used frequently by the program
def file_stats():
    no_emps = len(emp_dict)
    sal_lst = []
    for attr in emp_dict.values():
        sal_lst.append(int(attr[3]))
    # end of for loop
    tot_sal_bill = sum(sal_lst)
    avg_sal = tot_sal_bill/no_emps
    return no_emps, tot_sal_bill, avg_sal
# end of file_stats()


# summary statement detailing number of records successfully read into program
def task_1():
    no_emps = file_stats()[0]
    print("\n"+"*"*31, "READ SUMMARY", "*"*31+"\n")
    if no_emps == 1:
        print("Successfully read 1 employee record.")
    elif no_emps > 1:
        print("Successfully read", no_emps, "employee records.")
    else:
        print("File read incorrectly.")
    # end of if-elif-else statements
# end of task_1()


# total salary bill of all employees currently in the program
def task_3():
    total = file_stats()[1]
    print("\n"+"*"*28, "TOTAL SALARY BILL", "*"*29+"\n")
    print("Total salary bill: £", format(total, ',.2f'), sep="", end=".\n")
# end of task_3()


# average salary bill based on no of employees
def task_4():
    avg_sal = file_stats()[2]
    print("\n" + "*" * 30, "AVERAGE SALARY", "*" * 30 + "\n")
    print("Average salary: £", format(avg_sal, ',.2f'), sep="", end="\n")
# end of task_4()


# adds new employee to the current list
def task_5():
    new_emp = {}
    print("\n" + "*" * 32, "ADD EMPLOYEE", "*" * 32 + "\n")
    add_new = gci("\nAdd new employee record? [Y/N]:\t", str, 1)
    while add_new in ['Y', 'y']:
        while True:
            num = gci("Num:\t", int, 3)
            if num in emp_dict.keys():
                print("That number is not available.")
                continue
            else:
                break
            # end of if-else statement
        # end of while loop
        name = gci("Name:\t", str, 30)
        age = gci("Age:\t", int, 2)
        pos = gci("Position:\t", str, 15)
        sal = gci("Salary:\t", int, 7)
        yrs = gci("Years:\t", int, 2)
        new_emp[num] = (name, age, pos, sal, yrs)
        emp_dict.update(new_emp)
        add_new = gci("\nAdd new employee record? [Y/N]:\t", str, 1)
    # end of while loop
# end of task_5()


# choose a method by which to search for employee record to delete
def add_feat():
    print("\n" + "*" * 30, "DELETE EMPLOYEE", "*" * 31 + "\n")
    dele_rec = gci("Delete an employee record? [Y/N]:\t", str, 1)
    while dele_rec in ['Y', 'y']:
        print("""\nSEARCH BY:
            a) Employee Number
            b) Fullname
            c) Position""")
        search = gci("\nChoose a criteria to search by [A/B/C]:\t", str, 1)
        if search in ['A', 'a']:
            num = gci("Num:\t", int, 3)
            search_delete(num)
        elif search in ['B', 'b']:
            name = gci("Name:\t", str, 30)
            search_delete(name)
        elif search in ['C', 'c']:
            pos = gci("Position:\t", str, 15)
            search_delete(pos)
        else:
            print("INPUT ERROR: [A], [B] or [C]")
            continue
        # end of if-elif-else statement
        dele_rec = gci("\nDelete an employee record? [Y/N]:\t", str, 1)
    # end of while loop
# end of add_feat()


# find all records according to input and allows user to delete a single record
def search_delete(crit):
    not_found_count = 0
    print(header)
    for key, att in emp_dict.items():
        if crit in [key, att[0], att[1], att[2], att[3], att[4]]:
            print("{:5}{:30}{:5}{:20}{:10}{:6}".format(
                key, att[0], att[1], att[2], att[3], att[4]))
        else:
            not_found_count += 1
        # end of if-else statement
    # end of for loop
    if not_found_count == len(emp_dict):
        print("No records found!")
    else:
        num = gci("Num:\t", int, 3)
        dele_opt = gci("Delete this record? [Y/N]:\t", str, 1)
        if dele_opt in ['Y', 'y']:
            del emp_dict[num]
        else:
            add_feat()
        # end of if-else statement
    # end of if-elif statement
# end of search_delete(crit)


# tallies the number of employees, grouped by position
def task_6():
    # populates the position dictionary with all existing position type titles
    print("\n" + "*" * 33, "POSITIONS", "*" * 34 + "\n")
    for att in emp_dict.values():
        pos_dict[att[2]] = 0
    for att in emp_dict.values():
        if att[2] in pos_dict.keys():
            pos_dict[att[2]] += 1
    for pos, num in pos_dict.items():
        print(pos+":", num, sep=" ", end="\n")
    # end of for loop
# end of task_6()


# query list via salary threshold, returning employees above the threshold
def task_7():
    print("\n" + "*" * 30, "SALARY THRESHOLD", "*" * 30 + "\n")
    sal_thresh = int(gci("\nEnter minimum salary:\t", int, 7))
    print(header)
    for key, att in emp_dict.items():
        if sal_thresh < int(att[3]):
            print("{:5}{:30}{:5}{:20}{:10}{:6}".format(
                key, att[0], att[1], att[2], att[3], att[4]))
        # end of if statement
    # end of for loop
# end of task_7()


main()
