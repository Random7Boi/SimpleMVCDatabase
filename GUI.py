from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image
from main import *
import os

# styling imports
from tkinter import ttk
from ttkthemes import themed_tk as tk 
#pip install ttkthemes before running code

os.system('cls') # clears the terminal from code, use 'clear' on linux/Mac

newPlaylist = []
filteredList = []
finalQueryList = []

root = tk.ThemedTk()
# Returns a list of all themes that can be set
root.get_themes()  
# Sets an available theme               
root.set_theme("black")         
root.title('Python SQLite3 Ktinker Project!')
root.iconbitmap('Images/queue-24px.ico')
root.geometry("700x750")
root.configure(bg = '#424242')

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar, bg = '#424242')

# create space
spaceFrame = ttk.Label(root, text="SQLite3 Database Viewer:", relief=GROOVE, anchor=CENTER, font = 'Times 12 italic')
spaceFrame.grid(row = 0, column = 2, pady = 10, ipadx = 10)

# Create Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=1, column=1, padx=20, pady=(10, 0))
l_name = Entry(root, width=30)
l_name.grid(row=2, column=1)
email = Entry(root, width=30)
email.grid(row=3, column=1)
income = Entry(root, width=30)
income.grid(row=4, column=1)
expenses = Entry(root, width=30)
expenses.grid(row=5, column=1)
revenue = Entry(root, width=30)
revenue.grid(row=6, column=1)
taxes = Entry(root, width=30)
taxes.grid(row=7, column=1)
delete_box = Entry(root, width=30)
delete_box.grid(row=7, column=4)

# Create Text Box Labels
f_name_label = Label(root, text="First Name", bg = '#424242', fg = '#FFFFFF')
f_name_label.grid(row=1, column=0, pady=(10, 0), padx = 10)
l_name_label = Label(root, text="Last Name", bg = '#424242', fg = '#FFFFFF')
l_name_label.grid(row=2, column=0, padx = 10)
email_label = Label(root, text="Email", bg = '#424242', fg = '#FFFFFF')
email_label.grid(row=3, column=0, padx = 10)
income_label = Label(root, text="Income", bg = '#424242', fg = '#FFFFFF')
income_label.grid(row=4, column=0, padx = 10)
expenses_label = Label(root, text="Expenses", bg = '#424242', fg = '#FFFFFF')
expenses_label.grid(row=5, column=0, padx = 10)
revenue_label = Label(root, text="Revenue", bg = '#424242', fg = '#FFFFFF')
revenue_label.grid(row=6, column=0, padx = 10)
taxes_label = Label(root, text="Taxes", bg = '#424242', fg = '#FFFFFF')
taxes_label.grid(row=7, column=0, padx = 10)
delete_box_label = Label(root, text="Delete a table by ID", bg = '#424242', fg = '#FFFFFF')
delete_box_label.grid(row=7, column=2, padx = 10)
queryLabel = Label(root, text="Records Table:", bg = '#424242', fg = '#FFFFFF', relief=RAISED, anchor=CENTER, font = 'Times 12 italic')
queryLabel.grid(row=14, column=0, pady=30, ipadx = 5, columnspan = 5)
editLabel = Label(root, text="Edit the Table:", bg = '#424242', fg = '#FFFFFF', relief=RAISED, anchor=CENTER, font = 'Times 12 italic')
editLabel.grid(row=1, column=3, ipadx = 5, columnspan = 5)

# create the list box
queryList = Listbox(root, bg = '#D8D8D8', fg = '#424242', width = 70, height = 20)
queryList.grid(row = 15, column = 0, columnspan = 5, padx = 30)

# add items to record from GUI
def addToRecord():

    # call insert function from database script
    firstName = f_name.get()
    lastName = l_name.get()
    emailAddress = email.get()
    _income = income.get()
    _expenses = expenses.get()
    _revenue = revenue.get()
    _taxes = taxes.get()
    insert(firstName, lastName, emailAddress, _income, _expenses, _revenue, _taxes)

    # Clear The Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    email.delete(0, END)
    income.delete(0, END)
    expenses.delete(0, END)
    revenue.delete(0, END)
    taxes.delete(0, END)

# query the items for display to GUI
def Query():

    queryList.delete(0, END)
    delete_box.delete(0, END)

    index = 0

    output = show_query()

    for items in output:
        newPlaylist.extend(items.split(" \n"))

    filteredList = list(filter(None, newPlaylist))

    for items in filteredList:
        queryList.insert(index, items)
        finalQueryList.insert(index, items)
        index += 1
    
    del newPlaylist[:]
    del filteredList[:]

    #print(filteredList)
    print(finalQueryList)
    #print(output)
    # query_label = Label(root, text=output, bg = '#424242', fg = '#FFFFFF')
    # query_label.grid(row=13, column=0, columnspan=2)

# insert the delete record ID from GUI to delete function
def Remove():

    removalNumber = delete_box.get()
    delete(removalNumber)
    queryList.delete(0, END)
    delete_box.delete(0, END)

# function to create a second GUI to use the update function with
def Modify():

    #root.withdraw()
    global editor
    editor = tk.ThemedTk()
    editor.get_themes()
    editor.set_theme("black")  
    editor.title('Update A Record')
    editor.iconbitmap('Images/queue-24px.ico')
    editor.geometry("400x300")
    editor.configure(bg = '#424242')

    #Create Global Variables for text box names
    global f_name_editor
    global l_name_editor
    global email_editor
    global income_editor
    global expenses_editor
    global revenue_editor
    global taxes_editor
    global editor_delete_box

    # Create Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=2, column=1, padx = 20)
    email_editor = Entry(editor, width=30)
    email_editor.grid(row=3, column=1, padx = 20)
    income_editor = Entry(editor, width=30)
    income_editor.grid(row=4, column=1, padx = 20)
    expenses_editor = Entry(editor, width=30)
    expenses_editor.grid(row=5, column=1, padx = 20)
    revenue_editor = Entry(editor, width=30)
    revenue_editor.grid(row=6, column=1, padx = 20)
    taxes_editor = Entry(editor, width=30)
    taxes_editor.grid(row=7, column=1, padx = 20)

    # Create Text Box Labels
    f_name_label = Label(editor, text="First Name", bg = '#424242', fg = '#FFFFFF')
    f_name_label.grid(row=1, column=0, pady=(10, 0), padx = 20)
    l_name_label = Label(editor, text="Last Name", bg = '#424242', fg = '#FFFFFF')
    l_name_label.grid(row=2, column=0, padx = 20)
    email_label = Label(editor, text="Email", bg = '#424242', fg = '#FFFFFF')
    email_label.grid(row=3, column=0, padx = 20)
    income_label = Label(editor, text="Income", bg = '#424242', fg = '#FFFFFF')
    income_label.grid(row=4, column=0, padx = 20)
    expenses_label = Label(editor, text="Expenses", bg = '#424242', fg = '#FFFFFF')
    expenses_label.grid(row=5, column=0, padx = 20)
    revenue_label = Label(editor, text="Revenue", bg = '#424242', fg = '#FFFFFF')
    revenue_label.grid(row=6, column=0, padx = 20)
    taxes_label = Label(editor, text="Taxes", bg = '#424242', fg = '#FFFFFF')
    taxes_label.grid(row=7, column=0, padx = 20)

    # create an order ID entry and label
    editor_delete_box = Entry(editor, width=30)
    editor_delete_box.grid(row=0, column=1, pady=10, padx = 20)
    editor_delete_box_label = Label(editor, text="Select Table by ID", bg = '#424242', fg = '#FFFFFF')
    editor_delete_box_label.grid(row=0, column=0, pady=10, padx = 20)

    # Create a Save Button To Save edited record
    edit_btn = Button(editor, text="Save Record", bg = '#0B3861', fg = '#FFFFFF', activebackground = '#F3F781', command=Modifier)
    edit_btn.grid(row=10, column=0, columnspan=5, pady=20, padx=160, ipadx=10)

    # when closing window:
    editor.protocol("WM_DELETE_WINDOW", editorClose)

# function to call the update function and close the second window
def Modifier():

    update(editor_delete_box.get(), f_name_editor.get(), l_name_editor.get(), email_editor.get(), income_editor.get(), expenses_editor.get(), revenue_editor.get(), taxes_editor.get())
    editor.destroy()
    root.deiconify()

# function to close editor window but not update anything
def editorClose():
    editor.destroy()
    root.deiconify()

# menu functions:
def createNewDatabase():
    createDatabase()

# destroy window function
def closeWindow():
    root.destroy()

def about_us():
    tkinter.messagebox.showinfo('About SQLite3 Database Manager!', 'This is a database manager used to create and query databases using a GUI frontend.')

# Create Submit Button 
submit_btn = Button(root, text="Add Record To Database", bg = '#0B3861', fg = '#FFFFFF', activebackground = '#F3F781', command = addToRecord)
submit_btn.grid(row=8, column=1, columnspan=1, pady=10, padx=10, ipadx=5)

# Create a Query 
query_btn = Button(root, text="Show Records", bg = '#0B3861', fg = '#FFFFFF', activebackground = '#F3F781', command = Query)
query_btn.grid(row=16, column=0, columnspan=5, pady=10, padx=10, ipadx=5)

#Create A Delete Button
delete_btn = Button(root, text="Delete Record", bg = '#0B3861', fg = '#FFFFFF', activebackground = '#F3F781', command = Remove)
delete_btn.grid(row=8, column=3, columnspan=2, pady=10, padx=10, ipadx=5)

# Create an Update Button
edit_btn = Button(root, text="Edit Record", bg = '#0B3861', fg = '#FFFFFF', activebackground = '#F3F781', command = Modify)
edit_btn.grid(row=3, column=3, columnspan = 2, padx=10, ipadx = 5)

# Menus, used for creating database and secondary window close button
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Create Database", command=createNewDatabase)
subMenu.add_command(label = "Exit", command = closeWindow)

# Secondary menu to show info on this GUI
subMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=subMenu)
subMenu.add_command(label="About Us", command=about_us)

# when closing window:
root.protocol("WM_DELETE_WINDOW", closeWindow)

root.mainloop()