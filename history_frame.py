"""
Written by: Surya.A
Component 4: Version 1:
Create the GUI for the frame that shows the history of all characters pulled.
The frame will display the history list in the json file from component 1. This
version 1 program will use placeholder data to display on the history frame The
frame will show the rarity of the pull, the 5* pity and 4* pity at that pull for
all 300 previous individual pulls.
"""
from tkinter import *
import json

'''each array has 10 items, in each item is (rarity, 5* pity, 4* pity) i wrote
this data by hand and it is accurate as pity counts up from the last 4*/5*
pulled. Page 1 (index[0]) holds most recent pulls. Version 2 will have code to
replicate this type of list based on information pulled from the json file'''
placeholder_data = [
    [('3 star', 3, 2), ('3 star', 2, 1), ('4 star', 1, 3), ('5 star', 4, 2),
     ('3 star', 3, 1), ('4 star', 2, 1), ('4 star', 1, 5), ('5 star', 3, 4),
     ('3 star', 2, 3), ('3 star', 1, 2)],
    [('5 star', 80, 1), ('4 star', 79, 5), ('3 star', 78, 4), ('3 star', 76, 3),
     ('3 star', 75, 2), ('3 star', 74, 1), ('4 star', 73, 8), ('3 star', 72, 7),
     ('3 star', 71, 6), ('3 star', 70, 5)],
    [('3 star', 69, 4), ('3 star', 68, 3), ('3 star', 67, 2), ('3 star', 66, 1),
     ('4 star', 65, 9), ('3 star', 64, 8), ('3 star', 63, 7), ('3 star', 62, 6),
     ('3 star', 61, 5), ('3 star', 60, 4)]
]

class history_frame:
    
    def __init__(self, root):
        '''Initialisation frame'''
        self.root = root
        root.title("History Frame")
        root.geometry("1280x720") # set the dimensions of the window
        root.resizable(0,0) # make the window not resizeable
        root.configure(bg='black') # set the background colour
        
        # instantiating variables
        self.current_banner = 1 # which banner the GUI needs to get info for (for version 2)
        self.current_page = 0 # the current page that the history gui is on
        
        '''TOP SIDE PANEL'''
        top_panel = Frame(root, bg='black', height=90)
        top_panel.pack(side='top', fill='x')
        
        # current banner label        
        self.label_current_banner = Label(top_panel,
                                          text= f"History - Banner {str(self.current_banner)}",
                                          fg='white', bg='black', font=('Arial', 28))
        self.label_current_banner.pack(pady=20)
        
        '''MIDDLE PANEL'''
        self.middle_panel = Frame(root, bg='black', height=470,
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
        page_frame = Frame(root, bg='black')
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
        
        self.update_display() # add content to the display
        
    def update_display(self):
        pulls = placeholder_data[self.current_page] # get the current page's pulls to display
        
        '''going through the pulls array, enumerate each indice to store
        (rarity, pity5, pity4) and ...... add more comments and info'''
        for i, (rarity, pity5, pity4) in enumerate(pulls):
            if rarity=='5 star':
                colour = "yellow"
            elif rarity=='4 star':
                colour = "#CBC3E3"
            else:
                colour = "lightblue"
            
            self.entries[i].configure(
                text=f"{rarity}      5* Pity: {pity5} | 4* Pity: {pity4}",
                bg=colour
            )
    
    def prev_page(self):
        if (self.current_page + 1) > 1:
            self.current_page -= 1
            self.page_label.config(text=f"Page {self.current_page + 1}")
            self.update_display()
    
    def next_page(self):
        if (self.current_page + 1) < len(placeholder_data):
            self.current_page += 1
            self.page_label.config(text=f"Page {self.current_page + 1}")
            self.update_display()

root = Tk() # establish the root of the window
app = history_frame(root) # create the app object using class converter
root.mainloop() # run/create the window