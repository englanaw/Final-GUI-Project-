"""

Author:  Adam England
Date written: 02/20/25
Assignment:   Final Project
Short Desc:   xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx


"""
import tkinter as tk

def mmWindow():
    #Sets up the window and the color
    Window = tk.Tk()
    Window.geometry('750x500')
    Frame = tk.Frame(Window, bg = "lime green")
    Frame.place(relwidth = 1, relheight = 1)

    Window.title("Golf Trainer")


    Que1 = tk.Label(Window, text = "ARE YOU ON THE GREEN?", font = ("Times",12), fg = "white", bg = "green"
                    , padx = 75, pady = 25)
    Que1.place(x=100, y=175)
    

    exit_button = tk.Button(Window, text = "EXIT", height = 2, width = 8, font = ("Times",12)
                            ,fg = "white", bg = "green",command = lambda: Exit(Window))
    exit_button.place(x = 655, y = 14)
   




    Yes_button = tk.Button(Window, text = "YES", height = 5, width = 15, font = ("Times",12)
                           ,fg = "white", bg = "green", command = lambda: Off_green(Window))
    Yes_button.place(x=100, y = 275)

    No_button = tk.Button(Window, text = "NO", height = 5, width = 15, font = ("Times",12)
                          ,fg = "white", bg = "green", command = lambda: On_green(Window))
    No_button.place(x=300, y = 275)


    image = tk.PhotoImage(file=r"C:\Users\epicc\Desktop\Second Sem\First 8\SDEV140\Final Project\PuttingGreen.png")
    smaller_image = image.subsample(10,7)
    label = tk.Label(Frame, image=smaller_image)
    label.image = smaller_image
    label.place(x=500,y=150)


def On_green(current_window):
    current_window.destroy()
    Distance()

def Off_green(current_window):
    current_window.destroy()
    Recommendation()

def Exit(current_window):
    current_window.destroy()
    
  
                
    
def Distance():
    Window = tk.Tk()
    Window.geometry('750x500')
    Frame = tk.Frame(Window, bg = "lime green")
    Frame.place(relwidth = 1, relheight = 1)

    Window.title('Distance')


    box = tk.Label(Window, text = "", font = ("Times",12), fg = "white", bg = "green"
                    , padx = 170, pady = 25)
    box.place(x=100, y=175)


    Que1 = tk.Label(Window, text = "ENTER THE DISTANCE FROM GREEN", font = ("Times",12), fg = "white", bg = "green"
                    , padx = 170, pady = 25)
    Que1.place(x=100, y=75)

    entry = tk.Entry(Window, width = 25)
    entry.place(x = 200, y = 200)
    

    exit_button = tk.Button(Window, text = "EXIT", height = 2, width = 8, font = ("Times",12)
                            ,fg = "white", bg = "green",command = lambda: Exit(Window))
    exit_button.place(x = 655, y = 14)

    back_button = tk.Button(Window, text = "BACK", height = 2, width = 8, font = ("Times",12),
                            fg = "white", bg = "green",command = lambda: Back(Window))
    back_button.place(x = 10, y = 14)
                            
   




    male_button = tk.Button(Window, text = "MALE", height = 5, width = 15, font = ("Times",12)
                           ,fg = "white", bg = "green", command = lambda: On_green(Window))
    male_button.place(x=100, y = 275)

    female_button = tk.Button(Window, text = "FEMALE", height = 5, width = 15, font = ("Times",12)
                          ,fg = "white", bg = "green")
    female_button.place(x=300, y = 275)


    image = tk.PhotoImage(file=r"C:\Users\epicc\Desktop\Second Sem\First 8\SDEV140\Final Project\PuttingGreen.png")
    smaller_image = image.subsample(10,7)
    label = tk.Label(Frame, image=smaller_image)
    label.image = smaller_image
    label.place(x=502,y=150)

def Back(current_window):
    current_window.destroy()
    mmWindow()

def Exit(current_window):
    current_window.destroy()
    

    
    


    


def Recommendation():
    Window = tk.Tk()
    Window.geometry('750x500')
    Frame = tk.Frame(Window, bg = "lime green")
    Frame.place(relwidth = 1, relheight = 1)

    Window.title("Recommendation")


    Que1 = tk.Label(Window, text = "I'D RECOMMEND USING THESE", font = ("Times",12), fg = "white", bg = "green"
                    , padx = 75, pady = 25)
    Que1.place(x=100, y=175)
    

    exit_button = tk.Button(Window, text = "EXIT", height = 2, width = 8, font = ("Times",12)
                            ,fg = "white", bg = "green",command = lambda: Exit(Window))
    exit_button.place(x = 655, y = 14)

    back_button = tk.Button(Window, text = "BACK", height = 2, width = 8, font = ("Times",12),
                            fg = "white", bg = "green",command = lambda: Back(Window))
    back_button.place(x = 10, y = 14)
   




    Yes_button = tk.Button(Window, text = "YES", height = 5, width = 15, font = ("Times",12)
                           ,fg = "white", bg = "green")
    Yes_button.place(x=100, y = 275)

    No_button = tk.Button(Window, text = "NO", height = 5, width = 15, font = ("Times",12)
                          ,fg = "white", bg = "green", command = lambda: On_green(Window))
    No_button.place(x=300, y = 275)


    image = tk.PhotoImage(file=r"C:\Users\epicc\Desktop\Second Sem\First 8\SDEV140\Final Project\clubs.png")
    smaller_image = image.subsample(10,7)
    label = tk.Label(Frame, image=smaller_image)
    label.image = smaller_image
    label.place(x=500,y=150)


def Back(current_window):
    current_window.destroy()
    mmWindow()

def Exit(current_window):
    current_window.destroy()





    Window.mainloop()



    

mmWindow()

       
