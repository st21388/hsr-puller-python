"""
Written by: Surya.A
Component 3: Version 1:
Create the GUI for the frame that shows what characters you have pulled after 
pressing pull buttons. Use the json file from version 1 component 1 so the
program knows what to show on the rewards frame.
"""
from tkinter import *
import json
import random

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
        self.single_frame.grid(row=0, column=0, sticky='nsew')
        
        # configure the size of row and grid (1280/4=320, 720/3=240 because 4 boxes horizontal, 3 boxes vertical)
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
        
        # Add content to single_frame
        result = Label(self.single_frame, text='3 star', width=320, height=240,
                       bg='lightblue')
        result.pack(padx=480, pady=240)
        Button(self.single_frame, text="Back", command=lambda: self.show_frame('button')).pack()

        # Add content to ten_frame
        result1 = Label(self.ten_frame, text='3 star', width=320, height=240,
                        bg='lightblue')
        result1.grid(row=0, column=0)
        
        result2= Label(self.ten_frame, text='3 star', width=320, height=240,
                        bg='lightblue')
        result2.grid(row=0, column=1)        
        
        result3 = Label(self.ten_frame, text='3 star', width=320, height=240,
                        bg='lightblue')
        result3.grid(row=0, column=2)
        
        Button(self.ten_frame, text="Back", command=lambda: self.show_frame('button')).grid(row=3, column=1, sticky='nswe')

        # Initially show button_frame
        self.button_frame.tkraise() 

    def show_frame(self, frame_choice):
        '''methods to put the selected frame on the front of window'''
        if frame_choice == "button":
            self.button_frame.tkraise()
        elif frame_choice == 'single':
            self.single_frame.tkraise()
        elif frame_choice == 'ten':
            self.ten_frame.tkraise()

root = Tk() # establish the root of the window
app = reward_frame(root) # create the app object using class converter
root.mainloop() # run/create the window