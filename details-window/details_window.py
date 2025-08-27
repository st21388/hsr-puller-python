"""
Written by: Surya.A
Component 5: Version 1:
Create the GUI for the window that explains the program to users. It will be
similar to the history-window in terms of format, but it will just have one page
of text that explains the program to users outside the target demographic, aka
people that have not played a gacha game before.
"""
from tkinter import *

class main_gui(Tk):
    
    def __init__(self):
        '''Initialisation method'''
        # defining the Tk() window
        super().__init__() # create the window
        self.title("Main Window")
        self.geometry("1280x720") # 150x100
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
        
        # first content
        Label(middle_panel, text='Gacha Simulator:',
              font=('Arial', 20), fg='white', bg='black',
              justify='left').grid(row=0, column=0, sticky='w') # header 1 label
        
        Label(middle_panel, text='''Do 1x or 10x pulls on individual banners! Test your luck! When a pull is done, you will earn either a 3 star, 4 star or a 5 star!''',
                            font=('Arial', 16), fg='white', bg='black',
                            justify='left', wraplength=1200).grid(row=1, column=0, sticky='w') # paragraph 1 label
        
        # second content
        Label(middle_panel, text='Rates:',
              font=('Arial', 20), fg='white', bg='black',
              justify='left').grid(row=2, column=0, sticky='w') # header 2 label
        
        Label(middle_panel, text=
              '''The rate for 4 stars is 5.1%. Four stars are guaranteed every 10 pulls. The rate for 5 stars is 0.6%. After 74 pulls, the rate increases by 6% until it overcaps at 90 pulls (at rate 102.6%). This makes the guarantee 89 pity but this is rare to come across as the chance to win increases after 74.''',
                            font=('Arial', 16), fg='white', bg='black',
                            justify='left', wraplength=1200).grid(row=3, column=0, sticky='w') # paragraph 2 label
        
        # third content
        Label(middle_panel, text='Currency:',
              font=('Arial', 20), fg='white', bg='black',
              justify='left').grid(row=4, column=0, sticky='w') # header 3 label
        
        Label(middle_panel, text=
              '''1x pulls cost 160 gems, 10x pulls cost 1600 gems. Reward yourself currency using the currency widget! Enter an integer larger than 0 and then select the add or subtract button, to affect your currency in that exact way!''',
                            font=('Arial', 16), fg='white', bg='black',
                            justify='left', wraplength=1200).grid(row=5, column=0, sticky='w')
        
        # fourth content
        Label(middle_panel, text='History',
              font=('Arial', 20), fg='white', bg='black',
              justify='left').grid(row=6, column=0, sticky='w') # header 4 label
        
        Label(middle_panel, text=
              '''Each banner has its own pity count and history. You can view these individual pities using the history window button. Simply select a banner, then click the history button to see all the pulls you have made on that banner! You can also clear the history for that banner with a clear button.''',
                            font=('Arial', 16), fg='white', bg='black',
                            justify='left', wraplength=1200).grid(row=7, column=0, sticky='w')
        
        # image
        global honkai_image
        honkai_image = PhotoImage(file='./download.png')
        Label(middle_panel, image=honkai_image, bg='black').grid(row=8, column=0, sticky='nswe')

if __name__ == "__main__":
    app = main_gui()
    app.mainloop()