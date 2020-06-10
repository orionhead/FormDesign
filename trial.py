from tkinter import *
#
# root = Tk()
# root.geometry('500x500')
# root.title("Registration Form")
# label_0 = Label(root, text="Registration form", width=20, font=("bold", 20))
# label_0.place(x=90, y=53)
#
# label_1 = Label(root, text="FullName", width=20, font=("bold", 10))
# label_1.place(x=80, y=130)
# entry_1 = Entry(root)
# entry_1.place(x=240, y=130)
#
# label_2 = Label(root, text="Email", width=20, font=("bold", 10))
# label_2.place(x=68, y=180)
# entry_2 = Entry(root)
# entry_2.place(x=240, y=180)
#
# label_3 = Label(root, text="Gender", width=20, font=("bold", 10))
# label_3.place(x=70, y=230)
# var = IntVar()
# Radiobutton(root, text="Male", padx=5, variable=var, value=1).place(x=235, y=230)
# Radiobutton(root, text="Female", padx=20, variable=var, value=2).place(x=290, y=230)
#
# label_4 = Label(root, text="Age:", width=20, font=("bold", 10))
# label_4.place(x=70, y=280)
# entry_2 = Entry(root)
# entry_2.place(x=240, y=280)
# Button(root, text='Submit', width=20, bg='brown', fg='white').place(x=180, y=380)
# # it is use for display the registration form on the window
# root.mainloop()
# print("registration form  successfully created...")


from tkinter import *  # Import tkinter
import tkinter.messagebox  # Import tkinter.messagebox
from tkinter.filedialog import askopenfilename


def showResult():
    analyzeFile(filename.get())


def analyzeFile(filename):
    try:
        infile = open(filename, "r")

        counts = 26 * [0]  # Create and initialize counts
        for line in infile:
            countLetters(line.lower(), counts)

        # Display results
        for i in range(len(counts)):
            if counts[i] != 0:
                text.insert(END, chr(ord('a') + i) + " appears " + str(counts[i])
                            + (" time" if counts[i] == 1 else " times") + "\n")

        infile.close()  # Close file
    except IOError:
        tkinter.messagebox.showwarning("Analyze File",
                                       "File " + filename + " does not exist")

    # Count each letter in the string


def countLetters(line, counts):
    for ch in line:
        if ch.isalpha():
            counts[ord(ch) - ord('a')] += 1


def openFile():
    filenameforReading = askopenfilename()

    filename.set(filenameforReading)


window = Tk()  # Create a window
window.title("Occurrence of Letters")  # Set title

frame1 = Frame(window)  # Hold four labels for displaying cards
frame1.pack()

scrollbar = Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=Y)
text = Text(frame1, width=40, height=30, wrap=WORD,
            yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config(command=text.yview)

frame2 = Frame(window)  # Hold four labels for displaying cards
frame2.pack()

Label(frame2, text="Enter a filename: ").pack(side=LEFT)
filename = StringVar()
Entry(frame2, width=20, textvariable=filename).pack(side=LEFT)
Button(frame2, text="Browse", command=openFile).pack(side=LEFT)
Button(frame2, text="Show Result", command=showResult).pack(side=LEFT)

window.mainloop()  # Create an event loop
