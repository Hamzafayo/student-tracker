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

def save_students():
    #Write all students to students.txt as a CSV safely.
    # Writes rows to a CSV file with a header line.
    try:
        with open(STUDENTS_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            # Ref: csv.writer usage - https://docs.python.org/3/library/csv.html#csv.writer
            writer.writerow(["name", "age", "grade"])
            for s in students:
                writer.writerow([s["name"], s["age"], s["grade"]])
        messagebox.showinfo("Saved", f"Students saved to {STUDENTS_FILE}")
    except OSError as exc:
        messagebox.showerror("File Error", f"Could not save file: {exc}")

        def bubble_sort_students():
    #Sort students by grade with a bubble sort pass until sorted.
    # Swaps adjacent grades until the list is ordered.
    # Ref: bubble sort swap idea - https://en.wikipedia.org/wiki/Bubble_sort
    n = len(students)
   
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if students[j]["grade"] > students[j + 1]["grade"]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True
        if not swapped:
            break
    update_student_list()
    messagebox.showinfo("Sorted", "Students sorted by grade (ascending).")
def visualize_grades():
    #Display a bar chart of all student grades in Matplotlib.
    # Converts stored grades into a bar plot.
    # Ref: pyplot labels and title - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html
    # Ref: show warning box when data missing - https://docs.python.org/3/library/tkinter.messagebox.html
    if not students:
        messagebox.showerror("Error", "No students to visualize!")
        return

    names = [s["name"] for s in students]
    grades = [s["grade"] for s in students]

    plt.figure(figsize=(8, 5))
    # Ref: Matplotlib figure sizing - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.figure.html
    # Ref: Matplotlib bar usage - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.bar.html
    plt.bar(names, grades, color="#79a3f0")
    plt.xlabel("Students")
    plt.ylabel("Grades")
    plt.title("Student Grades")
    plt.ylim(0, 100)
    # Ref: clamp y-axis so 0-100 stays visible - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.ylim.html
    plt.tight_layout()
    # Ref: auto-fit margins to avoid overlap - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.tight_layout.html
    plt.show()
    # Ref: render the plot window - https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
 def recursive_average(grades, n=None):
    #Use recursion to calculate the average value across a list.
    # Combines prior sums with the new grade to find mean.
    # Ref: cumulative moving average formula - https://en.wikipedia.org/wiki/Moving_average#Cumulative_moving_average
    if n is None:
        n = len(grades)
    # Ref: handle empty list early - https://docs.python.org/3/library/stdtypes.html#truth-value-testing
    if n == 0:
        return 0
    if n == 1:
        return grades[0]
    return (recursive_average(grades, n - 1) * (n - 1) + grades[n - 1]) / n


def show_average():
    #Show the average grade of every stored student together.
    # Calculates and displays the current mean grade.
    if not students:
        messagebox.showinfo("Average", "No students to calculate average.")
        return

    grades = [s["grade"] for s in students]
    avg = recursive_average(grades)
    messagebox.showinfo("Average", f"Average grade: {avg:.2f}")
    def search_student():
def search_student():
    #Find a student by name without caring about letter case.
    # Looks for a matching name and shows details when found.
    # Ref: raise messagebox for missing input - https://docs.python.org/3/library/tkinter.messagebox.html#tkinter.messagebox.showerror
    name = get_entry_value(name_entry, NAME_PLACEHOLDER)
    if not name:
        messagebox.showerror("Error", "Enter a name to search in the Name field.")
        return

    for s in students:  
        if s["name"].lower() == name.lower():
            messagebox.showinfo(
                "Found",
                f"Found: {s['name']}  |  Age: {s['age']}  |  Grade: {s['grade']}",
            )
            return
    messagebox.showinfo("Not Found", f"No student found with name '{name}'.")
def update_student():
    #Change a student's age or grade when their name matches.
    # Replaces stored age or grade if new values are valid.
    name = get_entry_value(name_entry, NAME_PLACEHOLDER)
    if not name:
        messagebox.showerror("Error", "Enter the student's name you want to update.")
        return

    for s in students:
        if s["name"].lower() == name.lower():
            
            new_age_text = get_entry_value(age_entry, AGE_PLACEHOLDER)
            new_grade_text = get_entry_value(grade_entry, GRADE_PLACEHOLDER)

            if new_age_text:
                new_age = validate_age(new_age_text)
                if new_age is None:
                    return
                s["age"] = new_age

            if new_grade_text:
                new_grade = validate_grade(new_grade_text)
                if new_grade is None:
                    return
                s["grade"] = new_grade

            update_student_list()
            messagebox.showinfo("Updated", f"Student '{s['name']}' updated.")
            clear_entries()
            return

    messagebox.showinfo("Not Found", f"No student found with name '{name}'.")
def delete_student():
    #Remove a student from the list when the name matches.
    # Drops the matching student and refreshes the list.
    name = get_entry_value(name_entry, NAME_PLACEHOLDER)
    if not name:
        messagebox.showerror("Error", "Enter the student's name you want to delete.")
        return

    for i, s in enumerate(students):
        if s["name"].lower() == name.lower():
            students.pop(i)
            update_student_list()
            messagebox.showinfo("Deleted", f"Student '{s['name']}' deleted.")
            clear_entries()
            return

    messagebox.showinfo("Not Found", f"No student found with name '{name}'.")


    def add_placeholder(entry, text):
    #Add placeholder text that clears on focus and returns on blur.
    # Ref: Tkinter focus bindings - https://docs.python.org/3/library/tkinter.html#bindings-and-events
    # Ref: Entry insert default text - https://docs.python.org/3/library/tkinter.html#tkinter.Entry.insert
    entry.insert(0, text)
    entry.config(fg="#707070")

    def on_focus_in(event):
        if entry.get() == text:
            entry.delete(0, tk.END)
            entry.config(fg="#000000")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, text)
            entry.config(fg="#707070")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def restore_placeholder(entry, text):
    #Reapply placeholder text if an entry is empty.
    if not entry.get():
        entry.insert(0, text)
        entry.config(fg="#707070")


def reset_placeholders():
    #Restore placeholder text for every entry box that is empty.
    restore_placeholder(name_entry, NAME_PLACEHOLDER)
    restore_placeholder(age_entry, AGE_PLACEHOLDER)
    restore_placeholder(grade_entry, GRADE_PLACEHOLDER)
    # Ref: DRY reuse of helper functions - https://docs.python.org/3/glossary.html#term-dry
def exit_app():
    #Close the application window and end the program.
    # Ref: closing a Tk app with destroy - https://docs.python.org/3/library/tkinter.html#tkinter.Tk.destroy
    # Ref: common exit button pattern - https://tkdocs.com/tutorial/windows.html#dialogs
    root.destroy()
 root = tk.Tk()
root.title("Student Tracker")
root.configure(bg="#eef6ff") 
root.option_add("*Font", ("Helvetica", 13))
root.option_add("*Button.Font", ("Helvetica", 12, "bold"))
root.option_add("*Entry.Font", ("Helvetica", 13))
root.grid_columnconfigure(0, weight=1)  # spacer column
root.grid_columnconfigure(1, weight=3)  # input column
root.grid_columnconfigure(2, weight=2)  # buttons column
root.grid_rowconfigure(5, weight=1)  # allow list area to grow
# Ref: grid weight to stretch widgets - https://docs.python.org/3/library/tkinter.html#the-grid-geometry-manager
title_label = tk.Label(
    root, text="Student Tracker", bg="#eef6ff", fg="#0f172a", font=("Helvetica", 20, "bold")
)
title_label.grid(row=0, column=0, columnspan=3, pady=(12, 6), sticky="n")
# Ref: headline label across the top - https://tkdocs.com/tutorial/grid.html#grid-basics
#  Input area 
name_entry = tk.Entry(root, width=25, bg="#f3f4f6", fg="black")
age_entry = tk.Entry(root, width=25, bg="#f3f4f6", fg="black")
grade_entry = tk.Entry(root, width=25, bg="#f3f4f6", fg="black")

name_entry.grid(row=1, column=1, padx=15, pady=8, sticky="we")
age_entry.grid(row=2, column=1, padx=15, pady=8, sticky="we")
grade_entry.grid(row=3, column=1, padx=15, pady=8, sticky="we")

add_placeholder(name_entry, NAME_PLACEHOLDER)
add_placeholder(age_entry, AGE_PLACEHOLDER)
add_placeholder(grade_entry, GRADE_PLACEHOLDER)
button_frame = tk.Frame(root, bg="#eef6ff")
button_frame.grid(row=1, column=2, rowspan=4, padx=20, pady=5, sticky="n")
# Ref: vertical button stack with grid - https://docs.python.org/3/library/tkinter.html#the-packer-and-grid

button_specs = [
    ("Add Student", add_student),
    ("Save Students", save_students),
    ("Sort by Grade", bubble_sort_students),
    ("Visualize Grades", visualize_grades),
    ("Show Average", show_average),
    ("Search Student", search_student),
    ("Update Student", update_student),
    ("Delete Student", delete_student),
    ("Exit", exit_app),
]

for i, (text, cmd) in enumerate(button_specs):
    tk.Button(
        button_frame,
        text=text,
        command=cmd,
        bg="#cde4ff",
        fg="#0f172a",
        activebackground="#b7d3f5",
        relief="ridge",
        padx=6,
        pady=4,
    ).grid(
        row=i, column=0, sticky="we", pady=3
    )
    # Ref: grid each button with padding - https://tkdocs.com/tutorial/grid.html#grid-basics


list_frame = tk.Frame(root, bg="#eef6ff")
list_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")
list_frame.grid_columnconfigure(0, weight=1)

scrollbar = tk.Scrollbar(list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

student_listbox = tk.Listbox(
    list_frame,
    width=70,
    yscrollcommand=scrollbar.set,
    bg="white",
    fg="#0f172a",
    highlightthickness=1,
    selectbackground="#cde4ff",
)
student_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
# Ref: Listbox + Scrollbar pack expand - https://tkdocs.com/tutorial/morewidgets.html#listbox

scrollbar.config(command=student_listbox.yview)
# Ref: configure scrollbar command to sync scrolling - https://docs.python.org/3/library/tkinter.html#tkinter.Scrollbar.config


root.mainloop()
# Ref: Tk main loop to run the UI - https://docs.python.org/3/library/tkinter.html#tkinter.Tk.mainloop

