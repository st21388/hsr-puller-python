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
        
        # instantiating variables
        self.current_banner = 0 # which banner the GUI is currently on
        self.err_window_creation = False # does an error window currently exist? for the pull() and pull_error_window() methods
        self.new_window = None # initialise the new window creation so we can call it in pull() and pull_error_window()
        
        '''LEFT SIDE PANEL'''
        left_panel = Frame(root, bg='black', width=300)
        left_panel.pack(side='left', fill='y')
        
        # banner select label
        label_select = Label(left_panel, text='Banner Select', bg='skyblue', width=25)
        label_select.pack(pady=10)
        
        # banner select buttons
        button_1 = Button(left_panel, text="Banner 1", width=25,
                          command=lambda: self.banner_one())
        button_1.pack(pady=5)
        
        button_2 = Button(left_panel, text="Banner 2", width=25,
                          command=lambda: self.banner_two())
        button_2.pack(pady=5)
        
        button_3 = Button(left_panel, text="Banner 2", width=25,
                          command=lambda: self.banner_three())
        button_3.pack(pady=5)
        
        # empty space to push currency frame down
        empty_frame = Frame(left_panel, bg='black')
        empty_frame.pack(pady=70)
        
        # currency input frame
        frame_currency = Frame(left_panel, bg='skyblue', borderwidth=2)
        frame_currency.pack(padx=20,pady=20)
        
        label_widget_currency = Label(frame_currency, text="Input Currency", bg='skyblue', width=25)
        label_widget_currency.pack(pady=10)
        
        self.label_currency_help = Label(frame_currency, text="Enter an integer above 0.", bg='skyblue', width=20)
        self.label_currency_help.pack()
        
        self.entry_currency = Entry(frame_currency, width=25)
        self.entry_currency.pack(pady=10)
        
        button_add_currency = Button(frame_currency, text="Add",
                                     command=lambda: self.calc_currency("add"))
        button_add_currency.pack(padx=25, side="left")
        
        button_subtract_currency = Button(frame_currency, text="Subtract",
                                          command=lambda: self.calc_currency("subtract"))
        button_subtract_currency.pack(padx=25, side="right")
        
        # details and history buttons
        button_details = Button(left_panel, text="Details", width=12)
        button_details.pack(side='bottom', padx=20, pady=20)
        
        button_history = Button(left_panel, text="History", width=12)
        button_history.pack(side='bottom', padx=20, pady=20)
        
        '''RIGHT SIDE PANEL'''
        self.right_panel = Frame(root, bg='lightcoral', width=980, height=720)
        self.right_panel.pack(side='left', fill='both', expand=True)
        
        # black heading bar to store banner name and current currency
        heading_frame = Frame(self.right_panel, bg='black')
        heading_frame.pack(fill='x', pady=10)
        
        # banner_name and varlabel currency will change depending on variables
        self.label_banner = Label(heading_frame, text="Current Banner Name", fg='white', bg='black', font=("Arial", 16))
        self.label_banner.pack(side='left', padx=10)
        
        label_gems = Label(heading_frame, text='gems', fg='white', bg='black', font=('Arial', 16))
        label_gems.pack(side='right')
        
        self.varLabel_currency = Label(heading_frame, text='0', fg='white', bg='black', font=("Arial", 16))
        self.varLabel_currency.pack(side='right')        
        
        label_currency = Label(heading_frame, text="Currency:", fg='white', bg='black', font=("Arial", 16))
        label_currency.pack(side='right', padx=5)
        
        # placeholder banner content
        self.label_banner_content = Label(self.right_panel, text="Select a banner!", bg="lightcoral", font=("Arial", 24))
        self.label_banner_content.pack(expand=True)
        
        # pull buttons
        self.pull_frame = Frame(self.right_panel, bg='lightcoral')
        self.pull_frame.pack(side='bottom', pady=20)
        
        button_single = Button(self.pull_frame, text="1x\n160 gems", width=10, height=2,
                               command=lambda: self.pull('single'))
        button_single.pack(side="left", padx=20)
        button_ten = Button(self.pull_frame, text="10x\n1600 gems", width=10, height=2,
                            command=lambda: self.pull('ten'))
        button_ten.pack(side="left", padx=20)

    def banner_one(self): # display banner 1
        self.current_banner = 1 # change the variable to the current banner
        self.right_panel.config(bg='blue') # change bg
        self.label_banner.config(text="Banner 1") # change title text
        self.pull_frame.config(bg='blue') # change pull button's bg
        self.label_banner_content.config(text="CharArt 1", bg='blue') # change img of char (right now just placeholder text)

    def banner_two(self): # display banner 2
        self.current_banner = 2
        self.right_panel.config(bg='green')
        self.label_banner.config(text="Banner 2")
        self.pull_frame.config(bg='green')
        self.label_banner_content.config(text="CharArt 2", bg='green')
        
    def banner_three(self): # display banner 3
        self.current_banner = 3
        self.right_panel.config(bg='yellow')
        self.label_banner.config(text="Banner 3")
        self.pull_frame.config(bg='yellow')
        self.label_banner_content.config(text='CharArt 3', bg='yellow')

    def calc_currency(self, operation):
        '''calculate currency for currency widget (both add and subtract)'''
        if operation == "add": # when pressing the add button
            try: # try a series of tests to see if input is valid
                
                if int(self.entry_currency.get()) < 0: # if input is < 0 (we don't want negative currency)
                    raise ValueError # raise the error exception
                
                calculation = int(int(self.entry_currency.get()) + int(self.varLabel_currency.cget("text"))) # calculate entry + current_currency
                self.varLabel_currency.config(text=str(calculation)) # replace current_currency with new currency
                self.label_currency_help.config(text="Enter an integer above 0.", bg='skyblue', width=20) # reset the help text
            except ValueError: # error exception
                self.label_currency_help.config(text="Input must be an integer above 0.", bg="lightcoral", wraplength=160)
        
        if operation == "subtract": # when pressing the subtract button
            try:
                if int(self.entry_currency.get()) < 0:
                    raise ValueError
                
                calculation = int(int(self.varLabel_currency.cget("text")) - int(self.entry_currency.get())) # calculate current_currency - entry
                if calculation < 0: # if result is < 0 then raise new kind of error message
                    self.label_currency_help.config(text="Input must not be greater than current currency.", bg='lightcoral', wraplength=160)
                else: # else then replace the current_currency with new currency
                    self.varLabel_currency.config(text=str(calculation))
                    self.label_currency_help.config(text="Enter an integer above 0.", bg='skyblue', width=20) # reset the help text
            except ValueError:
                self.label_currency_help.config(text="Input must be an integer above 0.", bg="lightcoral", wraplength=160)
        
    def pull(self, option):
        '''runs when the pull buttons are pressed (in future versions, this will
        change to the pull frame as well as subtract currency'''
        err_window_creation = False # set a boolean to determine if the error window exists (so that multiple windows don't just exist if the user spams the button)
        
        if option == "single": # if single pull button pressed
            if int(self.varLabel_currency.cget('text')) >= 160: # if able to afford 160 gems
                calculation = int(self.varLabel_currency.cget("text")) - 160 # calculate current currency - 160
                self.varLabel_currency.config(text=str(calculation)) # update currency
                if self.err_window_creation == True: # if err_window exists
                    self.err_window_creation = False
                    self.new_window.destroy() # destroy it
            else:
                if self.err_window_creation == False: # if window doesn't exist
                    self.err_window_creation = True # set to true
                    self.pull_error_window() # create err_window
                else: # destroys old window and pulls up another new one
                    '''this is so that lots of windows don't clog up the pc screen,
                    destroying the old one and creating a new one helps to bring
                    the error message to the user's screen instead of just keeping
                    the old one which could be under another window.'''
                    self.new_window.destroy() # destroy old window
                    self.pull_error_window() # create new one
        elif option == "ten":
            if int(self.varLabel_currency.cget('text')) >= 1600: # if able to afford 1600 gems
                calculation = int(self.varLabel_currency.cget('text')) - 1600
                self.varLabel_currency.config(text=str(calculation))
            else:
                self.pull_error_window()
    
    def pull_error_window(self):
        '''error window that shows when you don't have enough gems to afford a
        pull, credit to: https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/'''
        self.new_window = Toplevel(root) # Create a new window
        self.new_window.title("Currency Error")
        self.new_window.geometry('250x150')
        
        Label(self.new_window, text="Error, not enough currency to afford pull.").pack(pady=20)

root = Tk() # establish the root of the window
app = main_frame(root) # create the app object using class converter
root.mainloop() # run/create the window