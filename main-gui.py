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
        
        # initialising constants
        self.currency = 0
        self.current_banner = 1
        
        '''LEFT SIDE PANEL'''
        left_panel = Frame(root, bg='black', width=300)
        left_panel.pack(side='left', fill='y')
        
        # banner select label
        label_select = Label(left_panel, text='Banner Select', bg='skyblue', width=25)
        label_select.pack(pady=10)
        
        # banner select buttons
        button_1 = Button(left_panel, text="Banner 1", width=25)
        button_1.pack(pady=5)
        
        button_2 = Button(left_panel, text="Banner 2", width=25)
        button_2.pack(pady=5)
        
        button_3 = Button(left_panel, text="Banner 2", width=25)
        button_3.pack(pady=5)
        
        # empty space to push currency frame down
        empty_frame = Frame(left_panel, bg='black')
        empty_frame.pack(pady=70)
        
        # currency input frame
        frame_currency = Frame(left_panel, bg='skyblue', borderwidth=2)
        frame_currency.pack(padx=20,pady=20)
        
        label_widget_currency = Label(frame_currency, text="Input Currency", bg='skyblue', width=25)
        label_widget_currency.pack(pady=10)
        
        entry_currency = Entry(frame_currency, width=25)
        entry_currency.pack(pady=10)
        
        button_add_currency = Button(frame_currency, text="Add")
        button_add_currency.pack(padx=25, side="left")
        
        button_subtract_currency = Button(frame_currency, text="Subtract")
        button_subtract_currency.pack(padx=25, side="right")
        
        # details and history buttons
        button_details = Button(left_panel, text="Details", width=12)
        button_details.pack(side='bottom', padx=20, pady=20)
        
        button_history = Button(left_panel, text="History", width=12)
        button_history.pack(side='bottom', padx=20, pady=20)
        
        '''RIGHT SIDE PANEL'''
        right_panel = Frame(root, bg='lightcoral', width=980, height=720)
        right_panel.pack(side='left', fill='both', expand=True)
        
        # black heading bar to store banner name and current currency
        heading_frame = Frame(right_panel, bg='black')
        heading_frame.pack(fill='x', pady=10)
        
        # banner_name and varlabel currency will change depending on variables
        label_banner = Label(heading_frame, text="Current Banner Name", fg='white', bg='black', font=("Arial", 16))
        label_banner.pack(side='left', padx=10)
        
        varLabel_currency = Label(heading_frame, text='0', fg='white', bg='black')
        varLabel_currency.pack(side='right')        
        
        label_currency = Label(heading_frame, text="Currency:", fg='white', bg='black')
        label_currency.pack(side='right', padx=5)
        
        # current banner content
        
        ## NEED TO ADD: pulls up different frames depending on what banner is currently on (e.g, phainon's banner, bronya's banner, etc) 
        
        # pull buttons
        pull_frame = Frame(right_panel, bg='black')
        pull_frame.pack(side='bottom', pady=20)

root = Tk() # establish the root of the window
app = main_frame(root) # create the app object using class converter
root.mainloop() # run/create the window