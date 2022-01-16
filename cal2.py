from tkinter import *
root=Tk()
First_no = eval(input("Enter First no. = "))  # it takes the first no.
Second_no = eval(input("Enter Second no. = "))  # it takes the second no.
operator_choice = input("Enter the operation (+, -, *, /)= ")  # Operation selection

exp = [First_no, operator_choice, Second_no]  # Expression created using above to be matched with given problems

# faults in the program

#  first faulty expression
if exp == [45, '*', 3]:
    print(555)

# second faulty expression
elif exp == [56, '+', 9]:
    print(77)

# third faulty expression
elif exp == [56, '/', 6]:
    print("4")

# Correct calculations  :-
elif operator_choice == '+':
    print(First_no + Second_no)

elif operator_choice == '-':
    print(First_no - Second_no)

elif operator_choice == '*':
    print(First_no * Second_no)

else:
    print(First_no / Second_no)
    root.mainloop()