# Student Tracker Application
# Author: Hamza Fayo
# Course: IY499
# ID number: P484205

import csv
import tkinter as tk
from tkinter import messagebox

import matplotlib.pyplot as plt

STUDENTS_FILE = "students.txt"
NAME_PLACEHOLDER = "Name"
AGE_PLACEHOLDER = "Age"
GRADE_PLACEHOLDER = "Grade"

students = []


def validate_age(age_text):
    #Check age text is digits and above zero.
    # Checks that age input is a positive whole number only.
    # Ref: Tkinter messagebox for errors - https://docs.python.org/3/library/tkinter.messagebox.html
    if not age_text.isdigit():
        messagebox.showerror("Error", "Age must be a positive whole number!")
        return None
    age = int(age_text)
    if age <= 0:
        messagebox.showerror("Error", "Age must be a positive whole number!")
        return None
    return age


def validate_grade(grade_text):
    #Check grade text is digits between zero and one hundred.
    # Checks that grade input is within the 0-100 range.
    # Ref: Python str.isdigit for numeric check - https://docs.python.org/3/library/stdtypes.html#str.isdigit
    if not grade_text.isdigit():
        messagebox.showerror("Error", "Grade must be a number between 0 and 100!")
        return None
    grade = int(grade_text)
    if grade < 0 or grade > 100:
        messagebox.showerror("Error", "Grade must be between 0 and 100!")
        return None
    return grade

def update_student_list():
    #Refresh the listbox with every student's name, age, and grade.
    # Keeps the on-screen list in sync with the students data.
    # Ref: Tkinter Listbox insert pattern - https://docs.python.org/3/library/tkinter.html#tkinter.Listbox.insert
    student_listbox.delete(0, tk.END)
    for s in students:
        student_listbox.insert(
            tk.END,
            f"{s['name']}  |  Age: {s['age']}  |  Grade: {s['grade']}",
        )


def get_entry_value(entry, placeholder):
    #Return entry value unless it equals the placeholder text shown.
    # Pulls user text but ignores placeholder prompts.
    # Ref: strip whitespace - https://docs.python.org/3/library/stdtypes.html#str.strip
    value = entry.get().strip()
    if value == placeholder:
        return ""
    return value

def clear_entries():
    #Wipe entry boxes and restore placeholder text after actions finish.
    # Empties fields so the next action starts clean.
    # Ref: Entry.delete clears text - https://docs.python.org/3/library/tkinter.html#tkinter.Entry.delete
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    grade_entry.delete(0, tk.END)
    reset_placeholders()


    def add_student():
    #Add a new student using entered name, age, and grade values.
    # Validates inputs, prevents duplicates, then stores the student.
    name = get_entry_value(name_entry, NAME_PLACEHOLDER)
    age_text = get_entry_value(age_entry, AGE_PLACEHOLDER)
    grade_text = get_entry_value(grade_entry, GRADE_PLACEHOLDER)

    if not name or not age_text or not grade_text:
        messagebox.showerror("Error", "All fields (Name, Age, Grade) are required!")
        return

    # Ref: avoid duplicate names by comparing lowered strings - https://docs.python.org/3/library/stdtypes.html#str.lower
    if any(s["name"].lower() == name.lower() for s in students):
        messagebox.showerror("Error", f"A student named '{name}' already exists.")
        return
    
age = validate_age(age_text)
    grade = validate_grade(grade_text)
    if age is None or grade is None:
        return  

    students.append({"name": name, "age": age, "grade": grade})
    messagebox.showinfo("Success", f"Student '{name}' added!")

    clear_entries()
    update_student_list()

