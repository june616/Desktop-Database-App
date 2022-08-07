from tkinter import *
# In order to refer to functions in back_end script
import back_end


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


# This function will grab the data from view() and insert them to the listbox
def view_command():
    # Make sure it is an empty listbox when we press the button
    # (0, END) to ensure deleting rows from index 0 to the end
    list1.delete(0, END)
    for row in back_end.view():
        list1.insert(END, row)


def search_command():
    # empty the list first
    list1.delete(0, END)
    for row in back_end.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        # Insert the new values at the end of listbox
        list1.insert(END, row)


# When user press "add entry" button, expect that the data they typed in 4 entryboxes will be stored somewhere, and they will be able to retrieve them
def add_command():
    back_end.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


# When user select a row, press "delete selected" button, and expect this row will disappear from the database
# And when they select a row, they want to see the data show in entryboxes
def delete_command():
    back_end.delete(selected_tuple[0])


def update_command():
    back_end.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())


window = Tk()

window.wm_title("BookStore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)


title_text = StringVar()

e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

# Meaning that the vertical scrollbar (along the y-axis) will be set to list
list1.configure(yscrollcommand=sb1.set)
# Meaning that when scroll the bar, the vertical view of list will change
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)


b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

# Pass id of the selected tuple to the delete function
b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
