import json
import tkinter as tk

FILENAME = "tasks.json"

def nameOfTask():

    newValueSTR = theRealName.get()
    theInputName.append(newValueSTR)
    indexOfRow = len(theInputName) 
    tk.Label(frameForTasks, text=newValueSTR).grid(row=indexOfRow, column=1,padx=10,pady=10)
    tk.Checkbutton(frameForTasks).grid(row=indexOfRow, column=0,padx=10,pady=10)



    return theInputName





theInputName = []


window = tk.Tk()
window.title("To-Do-List")


#tk.Label(window, text="Task:").grid(row=1,column=0, padx=10, pady=10)
theRealName = tk.Entry(window, width=100)
theRealName.grid(row=3,column=0,padx=10,pady=10)

tk.Label(window, text="Enter your Task:").grid(row=0, column=0, padx=10,pady=10)
tk.Button(window, text="Add new task", width = 100, command=nameOfTask).grid(row=1, column=0, padx=10,pady=10)


theName = tk.StringVar(value="")
frameForTasks = tk.Frame(window)


frameForTasks.grid(row=4, column=0,padx=10, pady=10, sticky = "w")
#These are how these are formatted
#tk.Label(frameForTasks, text="Task").grid(row=0, column=1, padx=10,pady=10)
#tk.Checkbutton(frameForTasks).grid(row=0, column=0, padx=10,pady=10)

window.mainloop()