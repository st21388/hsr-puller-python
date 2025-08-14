"""
Written by: Surya.A
Component 3: Version 1:
Create the GUI for the frame that shows what characters you have pulled after 
pressing pull buttons. Use the json file from version 1 component 1 so the
program knows what to show on the rewards frame.

Component 3: Version 2:
Changes the way the program grabs from the json file. Since the json file
changed to store lists instead of single numbers in the history list, this
program looks for index[0] of the items in that list. This is so that it only
gets the rarities of the items.
"""
from tkinter import *
import json

class reward_frame:
    
    def __init__(self, root):
        '''Initialisation frame'''
        self.root = root
        root.title("Reward Frame")
        root.geometry("1280x720") # set the dimensions of the window
        root.resizable(0,0) # make the window not resizeable
        
        #configure the root window to take up the space of the whole window so the frames also do that
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        
        # create the frames
        self.button_frame = Frame(root, bg='black')
        self.single_frame = Frame(root, bg="black")
        self.ten_frame = Frame(root, bg="black")
        
        # place the frames in grids
        self.button_frame.grid(row=0, column=0, sticky='nsew')
        
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
        
        # Add content to button_frame
        button_single = Button(self.button_frame, text="1x\n160 gems",
                               command=lambda: self.show_frame('single'))
        button_single.pack(padx=20)
        button_ten = Button(self.button_frame, text="10x\n1600 gems",
                            command=lambda: self.show_frame('ten'))
        button_ten.pack(padx=20)
        
        # load the information (dictionary) in the json and place it in a variable
        with open("history.json") as f:
            data = json.load(f)
        
        # Add content to single_frame
        if data['history'][-1][0] == 3: # 3 star
            Label(self.single_frame, text='3 star',
                  bg='lightblue').grid(row=1, column=1, sticky='nswe', padx=67)
        elif data['history'][-1][0] == 4: # 4 star
            Label(self.single_frame, text='4 star',
                  bg='#CBC3E3').grid(row=1, column=1, sticky='nswe', padx=67)
        elif data['history'][-1][0] == 5: # 5 star
            Label(self.single_frame, text='5 star',
                  bg='yellow').grid(row=1, column=1, sticky='nswe', padx=67)
        
        Button(self.single_frame, text="Back",
               command=lambda: self.show_frame('button')).grid(row=2, column=1)

        # Add content to ten_frame 
        past_ten = [] # create an empty list
        for i in range(0,11,1): # for 11 times (because the first one is 0, so we discard it)
            if i > 0: # don't include the first pull that's in the list
                past_ten.append(data['history'][-i][0]) # append to list
        past_ten.reverse() # reverse the list so instead of last->first it goes first->last

        z = 0 # create another variable z to represent which number item in the array it is in [0,1,2,3,4,5,6,7,8,9]
        for x in range(0,2,1): # first two rows
            for y in range(0,4,1): # each column (4 columns)
                if past_ten[z] == 3: # 3 star
                    Label(self.ten_frame, text='3 star',
                          bg='lightblue').grid(row=x, column=y, sticky='nswe')
                elif past_ten[z] == 4: # 4 star
                    Label(self.ten_frame, text='4 star',
                          bg='#CBC3E3').grid(row=x, column=y, sticky='nswe')
                elif past_ten[z] == 5: # 5 star
                    Label(self.ten_frame, text='5 star',
                          bg='yellow').grid(row=x, column=y, sticky='nswe')
                z+=1 # increment z's count by 1
        
        for i in range(0,2,1): # last row two columns
            if (past_ten[i+8]) == 3:
                Label(self.ten_frame, text='3 star',
                      bg='lightblue').grid(row=2, column=i+1, sticky='nswe')
            elif (past_ten[i+8]) == 4:
                Label(self.ten_frame, text='4 star',
                      bg='#CBC3E3').grid(row=2, column=i+1, sticky='nswe')
            elif (past_ten[i+8]) == 5:
                Label(self.ten_frame, text='5 star',
                      bg='yellow').grid(row=2, column=i+1, sticky='nswe')

        Button(self.ten_frame, text="Back", command=lambda: self.show_frame('button')).grid(row=2, column=0)

        # Initially show button_frame
        self.button_frame.tkraise()

    def show_frame(self, frame_choice):
        '''method to put the selected frame on the front of window'''
        if frame_choice == "button":
            self.button_frame.tkraise()
        elif frame_choice == 'single':
            self.single_frame.tkraise()
        elif frame_choice == 'ten':
            self.ten_frame.tkraise()

root = Tk() # establish the root of the window
app = reward_frame(root) # create the app object using class converter
root.mainloop() # run/create the window