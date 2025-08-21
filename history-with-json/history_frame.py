"""
Written by: Surya.A
Component 4: Version 1:
Create the GUI for the frame that shows the history of all characters pulled.
The frame will display the history list in the json file from component 1. This
version 1 program will use placeholder data to display on the history frame The
frame will show the rarity of the pull, the 5* pity and 4* pity at that pull for
all 300 previous individual pulls.

Component 4: Version 2:
Instead of using placeholder data, the json has been updated to store pity in
the list like the json, this version just works with the new json by not calling
the placeholder list whenever grabbing rarity and pull pity data.

Component 4: Version 3:
The program is modified to read from the new json format introduced in component
1 version 3. The program will accurately show which banner it is reading history
from in the title (E.g, Banner 1, Banner 2 or Banner 3) and also display the
correct information from that banner.
"""
from tkinter import *
import json

'''organising information from json to a list.
each array has 10 items, in each item is (rarity, 5* pity, 4* pity). Page 1
(index[0]) holds most recent pulls.'''
# store pulling information dictionary in variable data
with open("history.json") as f:
    data = json.load(f)

curr_banner = data['banner']

data[curr_banner]['history'].reverse() # reverse info in the data history list so last pull appears as first
pages = (len(data[curr_banner]['history'])//10) # if theres 78 pulls, this shows 7
ones = len(data[curr_banner]['history']) - (pages*10) # if theres 78 pulls this shows 8

pull_info = [] # list that stores pages and each page's info
foo_list = [] # temporary list to store each page's info for the nested for loop below

z = 0 # create another variable z to represent the index of items in data['history']
for x in range(1, (pages) + 1, 1): # looping for each page
    for y in range(1, 11, 1): # looping 10 times for 10 items in each page
        temp = (data[curr_banner]['history'][z][0],
                data[curr_banner]['history'][z][1],
                data[curr_banner]['history'][z][2]) # temporary variable to store information to append
        foo_list.append(temp) # append data to foo_list
        z += 1 # increment z by 1, moves to the next item; z is saved even when loop ends
    pull_info.append(foo_list) # append the page to pull_info
    foo_list = [] # clear foo_list

if ones > 0: # if there have been 10, 20, 30 pulls, ones would be 0 and every item would already be in the list
    for i in range(1, (ones) + 1, 1): # appending the last couple of items
        temp = (data[curr_banner]['history'][z][0],
                data[curr_banner]['history'][z][1],
                data[curr_banner]['history'][z][2])
        foo_list.append(temp)
        z+=1
    pull_info.append(foo_list)

class history_frame:
    
    def __init__(self, root):
        '''Initialisation frame'''
        self.root = root
        root.title("History Frame")
        root.geometry("1280x720") # set the dimensions of the window
        root.resizable(0,0) # make the window not resizeable
        root.configure(bg='black') # set the background colour
        
        # instantiating variables
        self.current_page = 0 # the current page that the history gui is on
        
        '''TOP SIDE PANEL'''
        top_panel = Frame(root, bg='black', height=90)
        top_panel.pack(side='top', fill='x')
        
        # current banner label
        self.label_current_banner = Label(top_panel,
                                          text= f"History - Banner {curr_banner}",
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
        pulls = pull_info[self.current_page] # get the current page's pulls to display
        
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
        
            if ones > 0 and (self.current_page + 1) == len(pull_info): # if it is the last page and the total number of pulls done is not a multiple of 10
                # make the remaining entries blank (if there is 78 pulls, this will loop 2 times and the last 2 entries will be black)
                for i in range(ones, 10, 1):
                    self.entries[i].configure(
                        bg='black')
        
        if self.current_page == 0: # if first page, disable prev, enable next
            self.prev_button.config(state='disabled')
            self.next_button.config(state='normal')
        elif (self.current_page + 1) == len(pull_info): # if last page, enable prev, disable next
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
        if (self.current_page + 1) < len(pull_info): # if not at last page
            self.current_page += 1 # add page by 1
            self.page_label.config(text=f"Page {self.current_page + 1}") # update label
            self.update_display() # update labels in center

root = Tk() # establish the root of the window
app = history_frame(root) # create the app object using class converter
root.mainloop() # run/create the window