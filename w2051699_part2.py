#  I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
#  Any code taken from other sources is referenced within my code solution
#  UOW Student ID: 20516992 IIT Student ID: 20230613
#  Date: 08.12.2023


#  THIS CODE PRINTS THE HISTOGRAM AND LIST OUTPUT

from w2051699_part1 import credits_of_students, sorted_cred_list
from w2051699_part1D import *

if user.lower() == "staff":
    print("Part 2 - Getting the outputs from a list\n")

    def check_credits(student_cr):
        if student_cr[0:3] == [120, 0, 0]:
            prog_outcome = "Progress"
        elif student_cr[0:3] in ([100, 20, 0], [100, 0, 20]):
            prog_outcome = "Progress (module trailer)"
        elif student_cr[0:3] in ([40, 0, 80], [20, 20, 80], [20, 0, 100], [0, 40, 80], [0, 20, 100], [0, 0, 120]):
            prog_outcome = "Exclude"
        else:
            prog_outcome = "Module retriever"
        return prog_outcome

    while True:
        user_need = input("Enter A for printing the sorted list of outcomes according to credits, B for printing the sorted list according to progression or C for printing the outcomes in the entered order : ")
        if user_need.upper() == "A":
            credits_of_students = sorted(credits_of_students, reverse=True)
            break
        elif user_need.upper() == "B":
            credits_of_students = sorted_cred_list
            break
        elif user_need.upper() == "C":
            break
        else:
            print("Invalid option has been entered.")

for cr_per_Student in credits_of_students:
    prog_output = check_credits(cr_per_Student)

    print(f'{prog_output} - {cr_per_Student[0]}, {cr_per_Student[1]}, {cr_per_Student[2]}')
