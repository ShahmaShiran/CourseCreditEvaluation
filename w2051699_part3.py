#  I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
#  Any code taken from other sources is referenced within my code solution
#  UOW Student ID: 20516992 IIT Student ID: 20230613
#  Date: 13.12.2023

#  THIS CODE PRINTS THE HISTOGRAM, LIST OUTCOME AND FILE OUTCOME
#  from w2051699part1 user, import credits_of_students and copy the function in part 2 (To get only file output)

from w2051699_part2 import *
from w2051699_part1 import credits_of_students, sorted_cred_list

while user.lower() == "student":
    break

if user.lower() == "staff":
    print("\nPart 3 - getting the output from a text file\n")

    while True:
        user_Need = input("Enter A for sorted list of outcomes according the credits, B for sorted list according to progression outcomes or C for unsorted list of outcomes: ")
        if user_Need.upper() == "A":
            credits_of_students = sorted(credits_of_students, reverse=True)
            break
        elif user_Need.upper() == "B":
            credits_of_students = sorted_cred_list
            break
        elif user_Need.upper() == "C":
            break
        else:
            print("Invalid option has been entered.")
    
    credits_file = open('credits.txt', 'w')

    for cr_per_student in credits_of_students:
        prog_output = check_credits(cr_per_student)
        credits_file.write(f'{prog_output} - {cr_per_student[0]},{cr_per_student[1]},{cr_per_student[2]} \n')

    credits_file.close()

    credits_file = open("credits.txt", "r")
    print()
    for line in credits_file:
        print(line, end="")
    credits_file.close()
