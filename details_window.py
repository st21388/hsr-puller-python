"""
Written by: Surya.A
Component 5: Version 1:
Create the GUI for the window that explains the program to users. It will be
similar to the history-window in terms of format, but it will just have one page
of text that explains the program to users outside the target demographic, aka
people that have not played a gacha game before.
"""
from tkinter import *
import json

class main_gui(Tk):
    
    def __init__(self):
        '''Initialisation method'''
        # defining the Tk() window
        super().__init__() # create the window
        self.title("Main Window")
        self.geometry("1280x720")
        self.resizable(0,0)
        
        # instantiating variables
        self.details_window_instance = None
        self.details_window_open = False
        
        self.button_details = Button(self, text='Details', width=12,
                                     command=self.open_details_window)
        self.button_details.pack(padx=20, pady=20)
        
    def open_details_window(self):
        if not self.details_window_instance:
            self.details_window_creator()
        else:
            self.on_details_window_close()
            self.details_window_creator()
    
    def details_window_creator(self):
        self.details_window_instance = details_window(self)
        self.details_window_open = True
        self.details_window_instance.protocol("WM_DELETE_WINDOW", self.on_details_window_close)
    
    def on_details_window_close(self):
        self.details_window_open = False
        if self.details_window_instance:
            self.details_window_instance.destroy()
            self.details_window_instance = None

'''details window that opens when button is pressed'''
class details_window(Toplevel):
    
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Details Window")
        self.geometry("1280x720")
        self.resizable(0,0)
        self.configure(bg='black')
        
        '''TOP SIDE PANEL'''
        top_panel = Frame(self, bg='black', height=90)
        top_panel.pack(side='top', fill='x') # pack the frame
        
        label_title = Label(top_panel, text='Details', fg='white', bg='black',
                            font=('Arial', 28))
        label_title.pack(pady=20) # the title
                
        
        '''MIDDLE PANEL'''
        middle_panel = Frame(self, bg='black', height=570, # the frame
                             highlightbackground='white', highlightthickness=2)
        middle_panel.pack(fill='x', padx=35, pady=25)
        
        Label(middle_panel, text='Gacha Simulator:',
              font=('Arial', 20), width=80, anchor='w',
              fg='white', bg='black').pack() # header 1 label
        
        Label(middle_panel, text='''Do 1x or 10x pulls on individual banners! Test your luck! When a pull is done, you will earn either a 3 star, 4 star or a 5 star!''',
                            font=('Arial', 16), fg='white', bg='black',
                            anchor='w').pack() # paragraph 1 label


if __name__ == "__main__":
    app = main_gui()
    app.mainloop()