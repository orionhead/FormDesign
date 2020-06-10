from tkinter import messagebox
from tkinter import filedialog
import tkinter as tk

filename = ""


def parseline(line):
    parse_line = line.strip()
    space_pos = parse_line.rfind(" ")
    new_text_line = parse_line[space_pos:] + " " + parse_line[:space_pos]
    return new_text_line.strip()


def save_file():
    global filename
    try:
        if filename:
            text_area = textArea.get("1.0", "end-1c")
            save_text = open(filename, "w")
            save_text.write(text_area)
            save_text.close()
            messagebox.showinfo("Saved", "FIle Saved")
        else:
            messagebox.showinfo("byatch", "You clicked cancel")
    except:
        messagebox.showinfo("Error", "Could not save file")


def open_file():
    global filename
    filename = filedialog.askopenfilename(initialdir="/",
                                          title="Open file",
                                          filetypes=(("Text Files", "*.txt"),
                                                     ("All Files", "*.*")))
    textArea.delete("1.0", tk.END)
    try:
        if filename:
            the_file = open(filename)
            for line in the_file.readlines():
                textline = parseline(line)
                textArea.insert(tk.END, textline + "\n")

            the_file.close()
        else:
            messagebox.showinfo("byatch", "You clicked cancel")
    except:
        messagebox.showinfo("Error", "Could not open file")
        # print(filename)


def save_file_as():
    try:
        save_text_as = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if save_text_as:
            text_area = textArea.get("1.0", "end-1c")
            save_text_as.write(text_area)
            save_text_as.close()
            messagebox.showinfo("Saved", "FIle Saved")
        else:
            messagebox.showinfo("byatch", "You clicked cancel")
    except:
        messagebox.showinfo("Error", "Could not save file")


def close_text_area():
    textArea.delete("1.0", tk.END)


form = tk.Tk()

form.title("Menus")

form.configure(background='thistle2')

menuBar = tk.Menu(form)

fileMenuItem = tk.Menu(menuBar, tearoff=0)
fileMenuItem.add_command(label="Open", command=open_file)
fileMenuItem.add_command(label="Save", command=save_file)
fileMenuItem.add_command(label="Save As", command=save_file_as)
fileMenuItem.add_command(label="Close", command=close_text_area)
fileMenuItem.add_separator()
fileMenuItem.add_command(label="Quit", command=form.quit)

menuBar.add_cascade(label="File", menu=fileMenuItem)
# cascade is add to main menu

editMenuItem = tk.Menu(menuBar, tearoff=0)
editMenuItem.add_command(label="Cut", command=open_file)
editMenuItem.add_command(label="Copy", command=open_file)
editMenuItem.add_command(label="Paste", command=open_file)
editMenuItem.add_command(label="Rename", command=open_file)

menuBar.add_cascade(label="Edit", menu=editMenuItem)

ViewMenuItem = tk.Menu(menuBar, tearoff=0)
ViewMenuItem.add_command(label="Appearance", command=open_file)
ViewMenuItem.add_command(label="Recent Files", command=open_file)
ViewMenuItem.add_command(label="Recent Changes", command=open_file)
ViewMenuItem.add_command(label="Type Info", command=open_file)

menuBar.add_cascade(label="View", menu=ViewMenuItem)

form.config(menu=menuBar)

textArea = tk.Text(form, height=12, width=80, wrap=tk.WORD)
textArea.insert(tk.END, "This is the default text")
textArea.config(font=(" Helvetica ", 14, "bold", "italic"), bg="bisque")

scrollV = tk.Scrollbar(form, orient=tk.VERTICAL)
scrollV.config(command=textArea.yview())
textArea.config(yscrollcommand=scrollV.set)
scrollV.pack(side=tk.RIGHT, fill=tk.Y)

scrollH = tk.Scrollbar(form, orient=tk.HORIZONTAL)
scrollH.config(command=textArea.xview)
textArea.config(xscrollcommand=scrollH.set)
scrollH.pack(side=tk.BOTTOM, fill=tk.X)

textArea.pack()
form.mainloop()
