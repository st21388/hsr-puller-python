"""
Written by: Surya.A
Component 4: Version 1:
Create the GUI for the frame that shows the history of all characters pulled.
The frame will display the history list in the json file from component 1. The
json will be version 2 and will be modified to have dictionaries for different
banners. It will also be modified to show the 5* pity and 4* pity of the past
300 individual pulls as pity variable used for rate calculation discards pity
when encountering 5* or 4*. We need this info to show pulls past previous 5* in
history frame.
"""
from tkinter import *
import json

class history_frame:
    
    def __init__(self, root):
        '''Initialisation frame'''
        self.root = root
        root.title("History Frame")
        root.geometry("1280x720") # set the dimensions of the window
        root.resizable(0,0) # make the window not resizeable
        root.configure(bg='black') # set the background colour
        
        # instantiating variables
        current_banner = 1 # which banner the GUI needs to get info for
        
        '''TOP SIDE PANEL'''
        top_panel = Frame(root, bg='black', height=90)
        top_panel.pack(side='top', fill='x')
        
        # current banner label        
        self.label_current_banner = Label(top_panel,
                                          text= f"History - Banner {str(current_banner)}",
                                          fg='white', bg='black', font=('Arial', 28))
        self.label_current_banner.pack(pady=20)
        
        '''BOTTOM PANEL'''
        bottom_panel = Frame(root, bg='black', height=630,
                             highlightbackground='white', highlightthickness=2)
        bottom_panel.pack(side='top', fill='x', padx=35, pady=25)

root = Tk() # establish the root of the window
app = history_frame(root) # create the app object using class converter
root.mainloop() # run/create the window