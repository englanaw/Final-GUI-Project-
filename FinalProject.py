"""

Author:  Student Name
Date written: mm/dd/yy
Assignment:   Module# exercise# part# (1 or 2), etc.
Short Desc:   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


"""
import tkinter as tk

def mmWindow():
    #Sets up the window and the color
    Window = tk.Tk()
    Window.geometry('750x500')
    Frame = tk.Frame(Window, bg = "lime green")
    Frame.place(relwidth = 1, relheight = 1)


    Que1 = tk.Label(Window, text = "ARE YOU ON THE GREEN?", font = ("Helvetica",12), fg = "white", bg = "lightcoral"
                    , padx = 55, pady = 25)
    Que1.place(x=100, y=200)
    

    exit_button = tk.Button(Window, text = "EXIT", height = 2, width = 8,fg = "white", bg = "lightcoral")
    exit_button.place(x = 675, y = 18)
   




    Yes_button = tk.Button(Window, text = "yes", height = 5, width = 15, fg = "white", bg = "lightcoral" )
    Yes_button.place(x=100, y = 300)

    No_button = tk.Button(Window, text = "No", height = 5, width = 15, fg = "white", bg = "lightcoral")
    No_button.place(x=300, y = 300)










    Window.mainloop()



    

mmWindow()

       
