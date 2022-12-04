#establish GUI elements
import tkinter
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry

#create root window
root = tkinter.Tk()
root.configure(bg = "SteelBlue4")
root.title("ToDo List")
root.geometry("400x350")
#create empty lists
tasks = []
dates = []

def update_listbox():
    # clear the current listbox
    clear_listbox()
    # Populate listbox by appending each task to list
    for task in tasks:
        lb_tasks.insert("end", task)
    # Populate listbox by appending dates to list
    for date in dates:
        lb_dates.insert("end", date)

def clear_listbox():
    lb_tasks.delete(0, "end")
    lb_dates.delete(0,"end")

def add_task(event=None): # "event=None" so that enter key can add task without clicking the button
    #get user input(prompt)
    task = txt_input.get()
    # Ensure user has enetered a task
    if task !="":
      tasks.append(task)
      #capturing the date associated with entered task
      dates.append(cal.get_date())
      update_listbox()
    else:
        messagebox.showwarning("Note!", "Please enter a task")
    # Clear the textbox to avoid adding the same task twice accidentally
    txt_input.delete(0, "end")

root.bind('<Return>', add_task)# bind return key to add_task so that enter key can add task without clicking the button


def delete_task():

    # Get the text of the currently selected item
    task = lb_tasks.get("active")
    # Confirm task is in list
    if task in tasks:
        confirm_del = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete task:   ** {} ** ?".format(task))
        if confirm_del:# tkmessageBox.askyesno returns boolean
            #deletes the date at the same index of the task
            del dates[tasks.index(task)]
            tasks.remove(task)
    update_listbox()

#sorts dates and tasks by task name
def sort_list_up():
    #The dates list needs to be changes globally in response to the sort
    global dates 
    #Creates a temporary list of the dates sorted according to the sorted tasks
    tempdates = [x for _, x in sorted(zip(tasks,dates))]
    tasks.sort()
    #replaces the global date list with the temporary one created for sorting
    dates = tempdates
    update_listbox()

#sorts dates and tasks by reverse task name
def sort_list_down():
    #The dates list needs to be changes globally in response to the sort
    global dates
    #Creates a temporary list of the dates sorted according to the sorted tasks
    tempdates = [x for _, x in sorted(zip(tasks,dates))]
    tasks.sort()
    #replaces the global date list with the temporary one created for sorting
    dates = tempdates
    tasks.reverse()
    dates.reverse()
    update_listbox()

#sorts the tasks by the date associated with them
def sort_dates():
    global tasks
    temptasks = [x for _, x in sorted(zip(dates,tasks))]
    dates.sort()
    tasks = temptasks
    update_listbox()


def delete_all():
    # As list is being changed, it needs to be global.
    global tasks
    confirm_del = messagebox.askyesno("Delete All Confirmation", "Are you sure you want to delete all tasks?")
    if confirm_del:
      # Clears the lists.
      tasks = []
      dates = []
      # Update listbox
      update_listbox()

def exit():
    with open ('tasksfile.txt','w') as tf:
        for task in tasks:
           tf.write("%s\n" % task)
    with open ('datefile.txt','w') as df:
       for date in dates:
            df.write("%s\n" % date)           
    quit()

#Creating and formatting the GUI elemets

txt_input = tkinter.Entry(root, width = 15)
txt_input.grid(row=1 , column=1 )

btn_add_task = tkinter.Button(root, text="Add Task", fg="black", bg="SpringGreen3", command=add_task)
btn_add_task.grid(row= 1, column=0 )

btn_delete_task = tkinter.Button(root, text="Delete Task", fg="black", bg="indianred", command=delete_task)
btn_delete_task.grid(row=4 , column=0 )

btn_delete_all = tkinter.Button(root, text="Delete All", fg="black", bg="indianred", command=delete_all)
btn_delete_all.grid(row=5 , column= 0)

btn_sort_list_up = tkinter.Button(root, text="Sort List Ascending", fg="black", bg="LightSkyBlue1", command=sort_list_up)
btn_sort_list_up.grid(row=6 , column=0 )

btn_sort_list_down = tkinter.Button(root, text="Sort List Descending", fg="black", bg="LightSkyBlue1", command=sort_list_down)
btn_sort_list_down.grid(row=7 , column=0 )

btn_sort_dates_up = tkinter.Button(root, text="Sort by Date", fg="black", bg="LightSkyBlue1", command=sort_dates)
btn_sort_dates_up.grid(row=8 , column=0)

btn_quit_program = tkinter.Button(root, text="Exit", fg="black", bg="white", command=exit)
btn_quit_program.grid(row=9 , column=0 )

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=3 , column=1, rowspan=7 )

lb_dates = tkinter.Listbox(root)
lb_dates.grid(row=3 , column=3, rowspan=7 )

#Create calendar selector
cal = DateEntry(root, width= 12, background= "DodgerBlue4", foreground= "white",bd=2)
cal.grid(row=1, column=3)

#Populate listbox at program start
def show_listbox():
    global tasks
    global dates
    with open ('tasksfile.txt','r') as tf:
      for line in tf:
            x = line[:-1]
            tasks.append(x)
    with open ('datefile.txt','r') as df:
        for line in df:
            x = line[:-1]
            dates.append(x)
    for task in tasks:
        lb_tasks.insert("end", task)
    for date in dates:
        lb_dates.insert("end", date)
#Populate listbox at program start for future file io functionality
show_listbox()

# Start the main events loop
root.mainloop()
