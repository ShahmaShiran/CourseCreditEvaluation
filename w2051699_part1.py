#  I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
#  Any code taken from other sources is referenced within my code solution 
#  UOW Student ID: 20516992 IIT Student ID: 20230613
#  Date: 08.12.2023


credits_of_students = []
p_count = 0  # No. of students that have progressed
r_count = 0  # No. of students that have retrieved
t_count = 0  # No. of students that have trailered
e_count = 0  # No. of students that are excluded
total_no_of_students = 0  # Total number of students
total = 0  # Total credits

while True:
    user = input("Are you a student or staff: ")
    
    if user.lower() == "staff" or user.lower() == "student":
        print()
        break
    else:
        print("Invalid user")
prog_list = []  # List to save the credits of progress outcome
trai_list = []  # List to save the credits of trailer outcome
rete_list = []  # List to save the credits of retriever outcome
excl_list = []  # List to save the credits of exclude outcome

option = ''
while option.lower() != "q":

    def check_if_valid_input(credit):
        while True:
            try:
                value = int(input(credit))
                if value in range(0, 121, 20):
                    return value
                else:
                    print("Out of range")
            except ValueError:
                print("Integer required")

    pass_credits = check_if_valid_input("Please enter your credits at pass: ")
    defer_credits = check_if_valid_input("Please enter your credits at defer: ")
    fail_credits = check_if_valid_input("Please enter your credits at fail: ")

    total = pass_credits + fail_credits + defer_credits

    if total == 120:

        if pass_credits == 120:
            outcome = "Progress"
        elif pass_credits == 100:
            outcome = "Progress (module trailer)"
        elif (pass_credits, defer_credits) in [(40, 0), (20, 20), (20, 0), (0, 40), (0, 20), (0, 0)]:
            outcome = "Exclude"
        else:
            outcome = "Module retriever"

    # Only if the user is a staff the code should loop and count the number of students' credits entered.
        if user.lower() == "staff":

            cred_per_Student = [pass_credits, defer_credits, fail_credits]  # creates a credits list for each student
            total_no_of_students += 1
            credits_of_students.extend([cred_per_Student])  # Appends each list of a student into a big list

            if outcome == "Progress":
                p_count += 1
                prog_list.extend([cred_per_Student])
            elif outcome == "Progress (module trailer)":
                t_count += 1
                trai_list.extend([cred_per_Student])
            elif outcome == "Exclude":
                e_count += 1
                excl_list.extend([cred_per_Student])
            else:
                r_count += 1
                rete_list.extend([cred_per_Student])

        print(outcome, "\n")

        if user.lower() == "staff":
            print("Would you like to enter another set of data?")
            option = input("Enter 'y' for yes or 'q' to quit and view results: ")
            print()
            continue
        break

    else:
        print("Total incorrect")

sorted_cred_list = []
if option == "q":
    sorted_cred_list.extend(prog_list)
    sorted_cred_list.extend(trai_list)
    sorted_cred_list.extend(rete_list)
    sorted_cred_list.extend(excl_list)
