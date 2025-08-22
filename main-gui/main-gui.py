"""
Written by: Surya.A
Component 2: Version 1:
Create a base layout of the main Gui in the design. Using tkinter objects, make
a non-functional main frame for the program. Buttons will be added but will lead
to nowhere.

Component 2: Version 2:
After completing every single component's version two, add those components to
this main gui and make the program functional. The updated json will also be
used and stored with this program's file.

Component 2: Version 3:
After c1-v3, the json file has been modified to consider the history of pulling
on different banners. c2-v3 has been modified to have functionality with this
new json and has updated components to function with the format of this new
json.
"""

from tkinter import *
import json
import random

"""main gui that opens when program is run"""
class main_frame(Tk): # parameter Tk is used to create the window in super()
    
    def __init__(self):
        '''Initialisation method'''
        # defining the Tk() window
        super().__init__() # this is necessary for creating history frame
        '''super().__init__() is the same as doing self.root = root from version
        1. Difference is that we do not need to use root, we are putting Tk as a
        parameter in the class - main_frame(Tk): and super calls from that.'''
        '''source where I learned this information:
        https://www.geeksforgeeks.org/python/python-super-with-__init__-method/
        https://stackoverflow.com/questions/576169/understanding-python-super-with-init-methods'''
        self.title("Main Window")
        self.geometry("1280x720") # set the dimensions of the window
        self.resizable(0,0) # make the window not resizeable
        self.configure(bg='black') # set the background
        
        # instantiating variables
        self.current_banner = 0 # which banner the GUI is currently on
        
        '''for pull error windows'''
        self.currency_error = False # is there currently a currency error?
        self.banner_error = True # has the user selected a banner?
        self.err_window_creation = False # does an error window currently exist? for the pull() and pull_error_window() methods
        self.new_window = None # initialise the new window creation so we can call it in pull() and pull_error_window()
        self.error_type = 'banner' # what type of error is currently occuring?
        
        '''for history window''' # this is the instance of the history window
        self.history_window_instance = None # variable that stores the object
        self.history_window_open = False # boolean that says if its open or not
        
        # open and load the list in the json into variable named self.data
        with open("history.json") as f:
            self.data = json.load(f)               
        
        '''for rewards frame'''
        # configure the root window to take up the space of the whole window, so frames also do that
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # place the entire gui in a grid, so we can pull up reward frame when pull button is pressed
        self.gui_frame = Frame(self, bg='black')
        
        # create the other frames
        self.single_frame = Frame(self, bg='black')
        self.ten_frame = Frame(self, bg='black')
        
        # place the frames in grids
        self.gui_frame.grid(row=0, column=0, sticky='nswe')
        
        # configure size of single_frame row and column
        # 1280/3=426.67, 720/3=240 going to be 3x3 because only 1 box
        self.single_frame.grid(row=0, column=0, sticky='nsew')
        for i in range(3):
            self.single_frame.grid_rowconfigure(i, weight=0, minsize=240)
        for i in range(4):
            self.single_frame.grid_columnconfigure(i, weight=0, minsize=426.67)        
        
        # configure the size of ten_frame row and column
        # 1280/4=320, 720/3=240 because 4 boxes horizontal, 3 boxes vertical
        self.ten_frame.grid(row=0, column=0, sticky='nswe')
        for i in range(3):
            self.ten_frame.grid_rowconfigure(i, weight=0, minsize=240)
        for i in range(4):
            self.ten_frame.grid_columnconfigure(i, weight=0, minsize=320)
        
        # add content for the main-gui        
        '''LEFT SIDE PANEL'''
        left_panel = Frame(self.gui_frame, bg='black', width=300)
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
        
        self.button_history = Button(left_panel, text="History", width=12,
                                     command=self.open_history_window)
        self.button_history.pack(side='bottom', padx=20, pady=20)
        
        '''RIGHT SIDE PANEL'''
        self.right_panel = Frame(self.gui_frame, bg='lightcoral', width=980, height=720)
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
        
        '''PULLING FRAMES'''        
        # add content to single_frame
        self.single_label = Label(self.single_frame) # create the label
        self.single_label.grid(row=1, column=1, sticky='nswe', padx=67) # pack it in the a grid
        self.update_single_frame() # add information to the label
                
        Button(self.single_frame, text="Back", # add a back button
               command=lambda: self.show_frame('main-gui')).grid(row=2, column=1)
        
        # add content to ten_frame        
        self.ten_labels = {}
        i = 0
        for x in range(0,2,1): # first 2 rows
            for y in range(0,4,1): # each column (4 columns)
                # create the label
                self.ten_labels[f"label{i}"] = Label(self.ten_frame)
                # pack it in a grid
                self.ten_labels[f"label{i}"].grid(row=x, column=y, sticky='nsew')
                i+=1 # increment i by 1
        
        for z in range(0,2,1): # last row two columns
            self.ten_labels[f"label{z+8}"] = Label(self.ten_frame)
            self.ten_labels[f"label{z+8}"].grid(row=2, column=z+1, sticky='nswe')
        
        Button(self.ten_frame, text="Back",
               command=lambda: self.show_frame('main-gui')).grid(row=2, column=0)

        # initially show main-gui frame
        self.show_frame('main-gui')
    
    def update_single_frame(self):
        '''method to update single pull frame with latest info from json file'''
        # add content to single_frame
        if self.current_banner == 0: # hasn't selected banner yet
            self.single_label.config(bg='black')
        elif self.data[self.current_banner]['history'][-1][0] == 3: # 3 star
            self.single_label.config(text ='3 star', bg='lightblue')
        elif self.data[self.current_banner]['history'][-1][0] == 4: # 4 star
            self.single_label.config(text='4 star', bg='#CBC3E3')
        elif self.data[self.current_banner]['history'][-1][0] == 5: # 5 star
            self.single_label.config(text='5 star', bg='yellow')
    
    def update_ten_frame(self):
        '''method to update ten pull frame with latest info from json file'''
        # add content to ten_frame
        past_ten = []
        for i in range(0,11,1): # for 11 times (because the first one is 0, so we discard it)
            if i > 0: # don't include the first pull that's in the list
                past_ten.append(self.data[self.current_banner]['history'][-i][0]) # append to list
        
        past_ten.reverse() # reverse the list so instead of last->first it goes first->last        
        
        z = 0 # create another variable z to represent which number item in the array it is in [0,1,2,3,4,5,6,7,8,9]
        for i in range(0,10,1):
            if past_ten[z] == 3: # 3 star
                self.ten_labels[f"label{i}"].config(text='3 star', bg='lightblue')
            elif past_ten[z] == 4: # 4 star
                self.ten_labels[f"label{i}"].config(text='4 star', bg='#CBC3E3')
            elif past_ten[z] == 5: # 5 star
                self.ten_labels[f"label{i}"].config(text= '5 star', bg='yellow')
            z+=1 # increment z's count by 1
    
    def show_frame(self, frame_choice):
        '''method to put the selected frame on the top of the window'''
        if frame_choice == 'main-gui': # original name was button, decided to keep as that
            self.gui_frame.tkraise()
        elif frame_choice == 'single':
            self.single_frame.tkraise()
        elif frame_choice == 'ten':
            self.ten_frame.tkraise()
        
    def banner_one(self): # display banner 1
        self.data['banner'] = '1' # change the variable in the json to the current banner
        with open('history.json', 'w') as f:
            json.dump(self.data, f, indent=1) # dump this info into the json so that history window knows
        
        self.current_banner = self.data['banner'] # change the variable in the python program
        self.right_panel.config(bg='blue') # change bg
        self.label_banner.config(text="Banner 1") # change title text
        self.pull_frame.config(bg='blue') # change pull button's bg
        self.label_banner_content.config(text="CharArt 1", bg='blue') # change img of char (right now just placeholder text)

    def banner_two(self): # display banner 2
        self.data['banner'] = '2'
        with open('history.json', 'w') as f:
            json.dump(self.data, f, indent=1)
        
        self.current_banner = self.data['banner']
        self.right_panel.config(bg='green')
        self.label_banner.config(text="Banner 2")
        self.pull_frame.config(bg='green')
        self.label_banner_content.config(text="CharArt 2", bg='green')
        
    def banner_three(self): # display banner 3
        self.data['banner'] = '3'
        with open('history.json', 'w') as f:
            json.dump(self.data, f, indent=1)        
        
        self.current_banner = self.data['banner']
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
        
    def get_rate_4_star(self, warp):
        if warp == 10: # 10 pulls is guaranteed 4 star
            return 1.1
        else:
            return 0.051
        
    def get_rate_5_star(self, warp):
        # base rate same until we reach 74th pull
        if warp < 74:
            return 0.006
        
        # after 73th pull, the rate increase 6% per pull until 90 pull
        elif warp <= 90 and warp >= 74:
            return (warp - 73) * 0.06 + 0.006
    
    def roll(self, rate_four, rate_five): # the current rate (account for pity) and the type of rarity (4* or 5*)
        if (rate_four*100) > random.uniform(0.0,100.0) and (rate_five*100) > random.uniform(0.0,100.0):
            return "5&4"
        elif (rate_five*100) > random.uniform(0.0,100.0):
            return "5"
        elif (rate_four*100) > random.uniform(0.0,100.0):
            return "4"
    
    def pull_append(self): # function for pulling
        self.data[self.current_banner]["warp_4"] += 1 # increment 4 & 5 star pity count by 1
        self.data[self.current_banner]["warp_5"] += 1
        rate_4 = self.get_rate_4_star(self.data[self.current_banner]["warp_4"]) # calculate the rates
        rate_5 = self.get_rate_5_star(self.data[self.current_banner]["warp_5"])
        
        outcome = self.roll(rate_4,rate_5) # roll the dice
        if outcome == "5&4": # if both 5 and 4 star win, discard 4 star
            '''append self.data as (rarity, 5* pity, 4* pity)'''
            self.data[self.current_banner]["history"].append([5,
                                                              self.data[self.current_banner]["warp_5"],
                                                              self.data[self.current_banner]["warp_4"]])
            self.data[self.current_banner]["warp_5"] = 0
            self.data[self.current_banner]["warp_4"] = 0
        elif outcome == "5": # if 5 star win, reset 5* pity not 4 star
            self.data[self.current_banner]["history"].append([5,
                                         self.data[self.current_banner]["warp_5"],
                                         self.data[self.current_banner]["warp_4"]])
            self.data[self.current_banner]["warp_5"] = 0
        elif outcome == "4": # if 4 star win, reset 4* pity not 5 star
            self.data[self.current_banner]["history"].append([4,
                                                              self.data[self.current_banner]["warp_5"],
                                                              self.data[self.current_banner]["warp_4"]])
            self.data[self.current_banner]["warp_4"] = 0
        else: # else, then 3 star was won
            self.data[self.current_banner]["history"].append([3,
                                                              self.data[self.current_banner]["warp_5"],
                                                              self.data[self.current_banner]["warp_4"]])
        
        if len(self.data[self.current_banner]["history"]) == 301:
            self.data[self.current_banner]["history"].pop(0) # history can not store over 300 pulls
    
    def pull(self, option):
        '''runs when the pull buttons are pressed (in future versions, this will
        change to the pull frame as well as subtract currency'''
        err_window_creation = False # set a boolean to determine if the error window exists (so that multiple windows don't just exist if the user spams the button)
        
        if self.current_banner == 0: # if a banner has not been selected
            self.error_type = 'banner'
            if self.err_window_creation == False: # if error window doesn't exist
                self.err_window_creation = True # set it to True
                self.pull_error_window() # create err_window
            else: # destroys old window and pulls up another new one
                '''this is so that lots of windows don't clog up the pc screen,
                destroying the old one and creating a new one helps to bring
                the error message to the user's screen instead of just keeping
                the old one which could be under another window.'''
                self.new_window.destroy() # destroy old window
                self.pull_error_window() # create new one
        
        elif option == "single": # if single pull button pressed
            if int(self.varLabel_currency.cget('text')) >= 160: # if able to afford 160 gems
                calculation = int(self.varLabel_currency.cget("text")) - 160 # calculate current currency - 160
                self.varLabel_currency.config(text=str(calculation)) # update currency
                if self.err_window_creation == True: # if err_window exists
                    self.err_window_creation = False
                    self.new_window.destroy() # destroy it
                
                if self.history_window_instance: # if history window exist
                    self.on_history_window_close() # destroy window
                
                self.pull_append() # run the pulling method that does rate calculation
                with open("history.json", "w") as f:
                    json.dump(self.data, f, indent=1) # append list to json for rewards frame
                
                self.update_single_frame() # update the frame with latest info
                self.show_frame('single') # tkraise() the single pull frame
                
            else: # cannot afford 160 gems
                self.error_type = 'currency'
                if self.err_window_creation == False:
                    self.err_window_creation = True
                    self.pull_error_window()
                else:
                    self.new_window.destroy()
                    self.pull_error_window()
        
        elif option == "ten":
            if int(self.varLabel_currency.cget('text')) >= 1600: # if able to afford 1600 gems
                calculation = int(self.varLabel_currency.cget('text')) - 1600
                self.varLabel_currency.config(text=str(calculation))
                if self.err_window_creation == True:
                    self.err_window_creation = False
                    self.new_window.destroy()
                
                if self.history_window_instance: # if history window exist
                    self.on_history_window_close() # destroy window                    
                
                for i in range(0,10,1): # run rate calculation 10 times
                    self.pull_append()
                with open('history.json', 'w') as f: # append to json
                    json.dump(self.data, f, indent=1)
                
                self.update_ten_frame() # update the list to show newer information
                self.show_frame('ten') # tkraise() the ten pull frame
            
            else: # cannot afford 1600 gems
                self.error_type = 'currency'
                if self.err_window_creation == False:
                    self.err_window_creation = True
                    self.pull_error_window()
                else:
                    self.new_window.destroy()
                    self.pull_error_window()
    
    def open_history_window(self):
        '''Create an instance of the history_frame class'''
        if self.current_banner == 0: # if a banner has not been selected
            if self.err_window_creation == False:
                self.err_window_creation = True
                self.pull_error_window()
            
            else:
                self.new_window.destroy()
                self.pull_error_window()
        
        elif not self.history_window_instance: # if history window doesn't already exist
            self.history_window_creator()
        else:
            self.on_history_window_close() # destroy window
            self.history_window_creator() # reopen the window
    
    def history_window_creator(self):
        self.history_window_instance = history_frame(self) # create the window's instance
        self.history_window_open = True # set boolean to true now that window is open
        '''source: https://www.reddit.com/r/Tkinter/comments/vrxzuz/i_dont_understand_how_protocolwm_delete_window/'''
        # protocol sets it so when history_frame is closed, it replaces its own close window method with the on_history_window_close method from main_frame class
        self.history_window_instance.protocol("WM_DELETE_WINDOW", self.on_history_window_close)
    
    def on_history_window_close(self): # when history_frame is closed
        self.history_window_open = False # set the variable ot false
        if self.history_window_instance: # if the instance is open (it will be open)
            self.history_window_instance.destroy() # destroy window
            self.history_window_instance = None # set object to none    
    
    def pull_error_window(self):
        '''error window that shows when you don't have enough gems to afford a
        pull, credit to: https://www.geeksforgeeks.org/python/open-a-new-window-with-a-button-in-python-tkinter/'''
        if self.error_type == 'banner':
            self.new_window = Toplevel(self) # Create a new window
            self.new_window.title("Banner Error")
            self.new_window.geometry('250x150')
            
            Label(self.new_window, text='Error, please select a banner first.').pack(pady=20)
        
        elif self.error_type == 'currency':
            self.new_window = Toplevel(self)
            self.new_window.title("Currency Error")
            self.new_window.geometry('250x150')
            
            Label(self.new_window, text="Error, not enough currency to afford pull.").pack(pady=20)

"""history gui window that opens when history button is pressed"""
class history_frame(Toplevel): # toplevel is used here instead of tk as that is the tkinter module for opening an extra window
    
    def __init__(self, parent):
        '''Initialisation method'''
        '''source for learning how to make a parent class open child class:
        https://python-forum.io/thread-32514.html'''
        # parent parameter is used to refer to parameter self that is passed from main-frame method
        # history_window_creator(self) in code self.history_window_instance = history_frame(self)
        super().__init__(parent)
        self.title("History Window")
        self.geometry("1280x720") # set the dimensions of the window
        self.resizable(0,0) # make the window not resizeable
        self.configure(bg='black') # set the background colour
        
        # instantiating variables
        
        # load the information (dictionary) in the json and place it in a self.var
        with open("history.json") as f:
            self.data = json.load(f)        
        
        self.current_banner = self.data['banner'] # which banner the GUI needs to get info for
        self.current_page = 0 # the current page that the history gui is on
        self.pull_info = [] # list that stores pages and each page's info
        
        '''TOP SIDE PANEL'''
        top_panel = Frame(self, bg='black', height=90)
        top_panel.pack(side='top', fill='x')
        
        # current banner label
        self.label_current_banner = Label(top_panel,
                                          text= f"History - Banner {self.current_banner}",
                                          fg='white', bg='black', font=('Arial', 28))
        self.label_current_banner.pack(pady=20)
        
        '''MIDDLE PANEL'''
        self.middle_panel = Frame(self, bg='black', height=470,
                             highlightbackground='white', highlightthickness=2)
        self.middle_panel.pack(side='top', fill='x', padx=35, pady=25)
        
        # entry widgets
        
        self.entries = [] # store entry widgets
        
        for i in range(10): # 10 entry widgets
            entry = Label(self.middle_panel, text='', font=('Arial', 16),
                          width=80, anchor='w') # create the label
            entry.grid(row=i, column=0, pady=10) # pack it in the grid
            self.entries.append(entry) # add this label to the list
        
        '''PAGE BUTTON PANEL'''
        page_frame = Frame(self, bg='black')
        page_frame.pack(pady=20)
        
        self.prev_button = Button(page_frame, text='<-- Previous', font=('Arial',14),
                                  command=self.prev_page) # previous page button
        self.prev_button.grid(row=0,column=0,padx=20)
        
        self.page_label = Label(page_frame,text=f"Page {self.current_page + 1}", font=("Arial",14),
                                fg='white',bg='black') # label to display page
        self.page_label.grid(row=0,column=1)
        
        self.next_button = Button(page_frame, text='Next -->', font=('Arial',14),
                                  command=self.next_page) # next page button
        self.next_button.grid(row=0,column=2,padx=20)
        
        self.load_info() # load info into the list pull_info
        self.update_display() # add content to the display
    
    def load_info(self):
        '''organising information from json to a list. each array has 10 items,
        in each item is (rarity, 5* pity, 4* pity). Page 1 (index[0]) holds most
        recent pulls.'''
        self.data[self.current_banner]['history'].reverse() # reverse info in the self.data history list so last pull appears as first
        pages = (len(self.data[self.current_banner]['history'])//10) # if theres 78 pulls, this shows 7
        self.ones = len(self.data[self.current_banner]['history']) - (pages*10) # if theres 78 pulls this shows 8
        
        foo_list = [] # temporary list to store each page's info for the nested for loop below
        
        z = 0 # create another variable z to represent the index of items in self.data[self.current_banner]['history']
        for x in range(1, (pages) + 1, 1): # looping for each page
            for y in range(1, 11, 1): # looping 10 times for 10 items in each page
                temp = (self.data[self.current_banner]['history'][z][0],
                        self.data[self.current_banner]['history'][z][1],
                        self.data[self.current_banner]['history'][z][2])
                foo_list.append(temp) # append self.data to foo_list
                z += 1 # increment z by 1, moves to the next item; z is saved even when loop ends
            self.pull_info.append(foo_list) # append the page to pull_info
            foo_list = [] # clear foo_list
        
        if self.ones > 0: # if there have been 10, 20, 30 pulls, self.ones would be 0 and every item would already be in the list
            for i in range(1, (self.ones) + 1, 1): # appending the last couple of items
                temp = (self.data[self.current_banner]['history'][z][0],
                        self.data[self.current_banner]['history'][z][1],
                        self.data[self.current_banner]['history'][z][2])
                foo_list.append(temp)
                z+=1
            self.pull_info.append(foo_list)        
    
    def update_display(self):
        if len(self.pull_info) == 0: # if there is no pull history
            for i in range(0, 10, 1): # repeat 10 times
                self.entries[i].configure(bg='black') # make blank entries
            # text to show no pulls have been made yet
            self.entries[0].configure(text="No pulls currently made on this banner.",
                                      fg='white', bg='black', font=("Arial", 19, "bold"))
            self.prev_button.config(state='disabled') # disable the buttons
            self.next_button.config(state='disabled')        
        else: # if there is pull history for the current banner
            pulls = self.pull_info[self.current_page] # get the current page's pulls to display
            
            '''going through the pulls array, enumerate each indice to store
            (rarity, pity5, pity4) and ...... add more comments and info'''
            for i, (rarity, pity5, pity4) in enumerate(pulls): # for every pull (loops ten times unless last page doesn't have 10)
                if rarity==5: # 5*=yellow, 4*=purple, 3*=blue
                    colour = "yellow"
                elif rarity==4:
                    colour = "#CBC3E3"
                else:
                    colour = "lightblue"
                self.entries[i].configure( # update the corresponding entry (1, 2, 3, 4...) to store the correct info
                    text=f"{rarity}      5* Pity: {pity5} | 4* Pity: {pity4}",
                    bg=colour)
            
                if self.ones > 0 and (self.current_page + 1) == len(self.pull_info): # if it is the last page and the total number of pulls done is not a multiple of 10
                    # make the remaining entries blank (if there is 78 pulls, this will loop 2 times and the last 2 entries will be black)
                    for i in range(self.ones, 10, 1):
                        self.entries[i].configure(
                            bg='black')
            
            if self.current_page == 0: # if first page, disable prev, enable next
                self.prev_button.config(state='disabled')
                self.next_button.config(state='normal')
            elif (self.current_page + 1) == len(self.pull_info): # if last page, enable prev, disable next
                self.prev_button.config(state='normal')
                self.next_button.config(state='disabled')
            else: # if not first or last, enable both
                self.prev_button.config(state='normal')
                self.next_button.config(state='normal')
    
    def prev_page(self): # button for previous page
        if (self.current_page + 1) > 1: # if not at first page
            self.current_page -= 1 # minus page by 1
            self.page_label.config(text=f"Page {self.current_page + 1}") # change label
            self.update_display() # update labels to show new pulls
    
    def next_page(self): # button for next page
        if (self.current_page + 1) < len(self.pull_info): # if not at last page
            self.current_page += 1 # add page by 1
            self.page_label.config(text=f"Page {self.current_page + 1}") # update label
            self.update_display() # update labels in center

if __name__ == "__main__":
    app = main_frame()
    app.mainloop()