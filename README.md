# CourseCreditEvaluation

**Description**<br>
This Python program helps evaluate course credits and progression for students and staff. It provides functionality for both students to check their progression status based on credits, and for staff to track multiple students' credit data and generate a report. The program includes validation checks and provides options for sorting and displaying data in different formats.

**Features**
Student Functionality:
The student enters their pass, defer, and refer credits.
The system evaluates whether the student has progressed, been deferred, or is excluded.
It validates the inputs and provides a progression status before exiting.

**Staff Functionality:**
The staff inputs the credits for multiple students, storing them in an array.
The program repeatedly prompts for input until the staff decides to quit.

A histogram is generated, displaying the number of students who:
Progressed
Got a module trailer
Are module retrievers
Are excluded
The staff can choose how to display the data: either in the order of entry or sorted by progression status.

**Data Output:**
The data is saved to an array and/or a text file and can be displayed in the console in either sorted or unsorted format.

**Example**
Student Workflow:
Input:
Pass Credits: 120
Defer Credits: 20
Refer Credits: 0

Output:
Progress

Staff Workflow:
Input:
Enter Credits (for multiple students) 
Quit to generate the histogram and view progression data.

Output:
Histogram showing the number of students who progressed, had a module trailer, were module retrievers, or were excluded.
Data displayed in the desired order: either sorted or in the original order.
