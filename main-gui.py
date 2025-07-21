"""
Written by: Surya.A
Component 2: Version 1:
Create a base layout of the main Gui in the design. Using tkinter objects, make
a non-functional main frame for the program. Buttons will be added but will lead
to nowhere.
"""

from tkinter import *

class main_frame:
    
    def __init__(self, root):
        '''Initialisation method'''
        # defining the Tk() window
        self.root = root
        root.title("Main Frame")
        root.geometry("1280x720") # set the dimensions of the window
        root.resizable(0,0) # make the window not resizeable
        root.configure(bg='black') # set the background
        
        '''LEFT SIDE PANEL'''
        left_panel = Frame(root, bg='black', width=300)
        left_panel.pack(side='left', fill='y')
        
        # banner select label
        banner_select = Label(left_panel, text='Banner Select', bg='skyblue', width=25)
        banner_select.pack(pady=10)
        
        # banner select buttons
        button_1 = Button(left_panel, text="Banner 1", width=25)
        button_1.pack(pady=5)
        
        button_2 = Button(left_panel, text="Banner 2", width=25)
        button_2.pack(pady=5)
        
        button_3 = Button(left_panel, text="Banner 2", width=25)
        button_3.pack(pady=5)
        
        # empty space to push currency frame down
        ## might replace this section with something more useful like a help button
        empty_frame = Frame(left_panel, bg='black')
        empty_frame.pack(pady=70)
        
        # currency input frame
        currency_frame = Frame(left_panel, bg='skyblue', borderwidth=2)
        currency_frame.pack(padx=20,pady=20)
        
        currency_label = Label(currency_frame, text="Input Currency", bg='skyblue', width=25)
        currency_label.pack(pady=10)
        
        currency_entry = Entry(currency_frame, width=25)
        currency_entry.pack(pady=10)
        
        currency_button_add = Button(currency_frame, text="Add")
        currency_button_add.pack(padx=25, side="left")
        
        currency_button_subtract = Button(currency_frame, text="Subtract")
        currency_button_subtract.pack(padx=25, side="right")
        
        # details and history buttons
        details_button = Button(left_panel, text="Details", width=12)
        details_button.pack(side='bottom', padx=20, pady=20)
        
        history_button = Button(left_panel, text="History", width=12)
        history_button.pack(side='bottom', padx=20, pady=20)
        
        '''RIGHT SIDE PANEL'''
        right_panel = Frame(root, bg='lightcoral', width=1048, height=720)
        right_panel.pack(side='left', fill='both')
        

root = Tk()
app = main_frame(root)
root.mainloop()