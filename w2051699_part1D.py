#  I declare that my work contains no examples of misconduct, such as plagiarism, or collusion
#  Any code taken from other sources is referenced within my code solution
#  UOW Student ID: 20516992 IIT Student ID: 20230613
#  Date: 08.12.2023


from graphics import *
from w2051699_part1 import p_count, t_count, r_count, e_count, total_no_of_students, option, user

try:
    # To generate the histogram if only a staff enters the value and when q is entered
    if user.lower() == "staff" and option.lower() == "q":
        histogram_window = GraphWin("Histogram", 750, 900)
        histogram_window.setBackground("black")
        xaxis = Line(Point(30, 703), Point(700, 703))
        xaxis.setFill("white")
        xaxis.setWidth(2)

        #  TITLE
        title = Text(Point(180, 50), "Histogram Results")
        title.setStyle("bold")
        title.setSize(24)
        title.setTextColor("white")
        title.draw(histogram_window)

        #  PARAMETERS IN THE FUNCTION

        # noOfStudents - the no. of students per progression outcome
        # x1 - bottom left x-cordinate of the bar
        # y - center point of the bar_name and no_of_students
        # z - height increase in the bar for no_of_student


        def construct_bar(noOfStudents, bar_name, x1, colour):
            y = (2 * x1 + 150) / 2
            z = noOfStudents*10

            bar = Rectangle(Point(x1, 702), Point(x1+150, (702 - z)))
            bar_title = Text(Point(y, 722), bar_name)
            number_of_students_per_outcome = Text(Point(y, 690 - z), noOfStudents)

            bar.setFill(colour)
            bar.setOutline("white")
            bar.setWidth(2)

            bar_title.setStyle("bold")
            bar_title.setTextColor("white")
            bar_title.setSize(14)

            number_of_students_per_outcome.setStyle("bold")
            number_of_students_per_outcome.setTextColor("white")
            number_of_students_per_outcome.setSize(14)

            bar.draw(histogram_window)
            bar_title.draw(histogram_window)
            number_of_students_per_outcome.draw(histogram_window)


        construct_bar(p_count, "Progress", 50, "forestgreen")  # progress bar
        construct_bar(t_count, "Trailer", 210, "limegreen")  # trailer bar
        construct_bar(r_count, "Retriever", 370, "darkorange")  # retriever bar
        construct_bar(e_count, "Exclude", 530, "orange")  # exclude bar

        #  PRINTING THE TOTAL NO. OF STUDENTS
        no_of_students = Text(Point(120, 750), str(total_no_of_students) + " outcomes in total")
        no_of_students.setStyle("bold")
        no_of_students.setTextColor("white")
        no_of_students.setSize(16)
        no_of_students.draw(histogram_window)

        #  PRINTING THE X-AXIS
        xaxis.draw(histogram_window)

        #  PAUSES THE WINDOW TILL THE MOUSE IS CLICKED ON THE WINDOW
        histogram_window.getMouse()
        histogram_window.close()

except GraphicsError:
    pass
