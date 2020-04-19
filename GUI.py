from tkinter import *
from tkinter import ttk
from tkinter import filedialog

class Theme:
    background = "#000000"
    lightbackground = "#111111"
    lighterbackground = "#222222"
    font_0 = "#44ff11"
    font_1 = "#88aa11"
    font_2 = "#88aa11"
    h1 = 'Callibri 72 bold'
    h2 = 'Callibri 16 bold'
    h3 = 'Callibri 10'

class GUI:

    theme = Theme()
        
    def __init__(self):
        # setting up root windoww
        self.root = Tk()
        self.root.title("CHIFA Stats")
        self.root.geometry("350x431+450+50")
        self.root.resizable(False, False)
        self.root.overrideredirect(1)
        
        # setting up titlebar
        self.titlebar = Frame(self.root, height=25,
                    bg='#0f0f0f')

        def get_pos(event):
            xwin = self.root.winfo_x()
            ywin = self.root.winfo_y()
            startx = event.x_root
            starty = event.y_root

            ywin = ywin - starty
            xwin = xwin - startx


            def move_window(event):
                self.root.geometry('+{0}+{1}'.format(event.x_root + xwin, event.y_root + ywin))
            self.titlebar.bind('<B1-Motion>', move_window)

        self.titlebar.bind("<Button-1>", get_pos)
        
        self.exitbutton = Label(self.titlebar, 
            text='×', bg='#0f0f0f', fg='white',
            font='Arial 12 bold')
        self.exitbutton.pack(side='right', padx=5)
        self.exitbutton.bind("<Button-1>", lambda x: self.root.quit())
        self.titlebar.pack(side='top', expand=True, fill='x')
        # setting up main frames
        self.frame_top = ttk.Frame(self.root, height='200')
        self.frame_top.pack_propagate(0)
        self.frame_top.pack(side='top', fill='x',
                      padx=2, pady=2)

        self.frame_middle = ttk.Frame(self.root, height='200')
        self.frame_middle.pack_propagate(0)
        self.frame_middle.pack(side='top', fill='x',
                      padx=2, pady=0)

        self.frame_bottom = ttk.Frame(self.root, height='140')
        self.frame_bottom.pack_propagate(0)
        self.frame_bottom.pack(side='top', fill='x',
                      padx=2, pady=2)
        
        # setting up frame_top widgets
        self.title_top = ttk.Label(self.frame_top, text='Daily Statistics')
        self.title_top.pack(side='top', fill='x')

        self.container_top = ttk.Frame(self.frame_top)
        self.container_top.pack_propagate(0)
        self.container_top.pack(expand=True, fill='both', padx=20)

        self.label_todaytotal = ttk.Label(self.container_top, text='42', width=3)
        self.label_todaytotal.grid(row=0, column=0, rows=4)

        self.label_totalcnas = ttk.Label(self.container_top, text='CNAS: 24', justify='left', width=20)
        self.label_totalcnas.grid(row=0, column=1)

        self.label_totalcasnos = ttk.Label(self.container_top, text='CASNOS: 14', justify='left',
             width=20, foreground='#ff5500')
        self.label_totalcasnos.grid(row=1, column=1)

        self.label_totalhc = ttk.Label(self.container_top, text='Hors CHIFA: 4', justify='left',
             width=20, foreground='#00ff55')
        self.label_totalhc.grid(row=2, column=1)

        self.label_totalmt = ttk.Label(self.container_top, text='\nSales of today\n105420.10 DA', 
        justify='left', width=20, foreground='#00ffff')
        self.label_totalmt.grid(row=3, column=1)
        
        # setting up frame_middle widgets
        self.title_middle = ttk.Label(self.frame_middle, text='Stats per post')
        self.title_middle.pack(side='top', fill='x')

        self.container_middle = ttk.Frame(self.frame_middle)
        self.container_middle.pack(side='bottom', expand=True, fill='both', padx=4)

        self.label_post0title = ttk.Label(self.container_middle, text='Post 0', justify='center')
        self.label_post1title = ttk.Label(self.container_middle, text='Post 1', justify='center')

        self.label_post0label = ttk.Label(self.container_middle, text='23', width=3, justify='center')
        self.label_post1label = ttk.Label(self.container_middle, text='12', width=3, justify='center')

        self.label_post0title.grid(row=0, column=0)
        self.label_post1title.grid(row=0, column=1)
        self.label_post0label.grid(row=1, column=0, rowspan=5)
        self.label_post1label.grid(row=1, column=1, rowspan=5)


    def apply_theme(self):
        self.root.config(bg=self.theme.background)

        # configuring styles
        ttk.Style().configure("H1.TLabel", font=self.theme.h1,
            foreground=self.theme.font_0, background=self.theme.lightbackground)

        ttk.Style().configure("H2.TLabel", font=self.theme.h2,
            foreground=self.theme.font_1, background=self.theme.lightbackground)
        
        ttk.Style().configure("H3.TLabel", font=self.theme.h3,
            foreground=self.theme.font_1, background=self.theme.lightbackground)

        ttk.Style().configure("Title.TLabel", font=self.theme.h2,
            foreground=self.theme.font_1, background=self.theme.lighterbackground)

        ttk.Style().configure("T.TFrame", background=self.theme.lightbackground)

        # applying styles
        self.frame_bottom.config(style='T.TFrame')
        self.frame_middle.config(style='T.TFrame')
        self.frame_top.config(style='T.TFrame')
        self.container_middle.config(style='T.TFrame')
        self.container_top.config(style='T.TFrame')

        self.title_middle.config(style='Title.TLabel')
        self.title_top.config(style='Title.TLabel')

        self.label_todaytotal.config(style='H1.TLabel')
        self.label_post0label.config(style='H1.TLabel')
        self.label_post1label.config(style='H1.TLabel')

        self.label_post0title.config(style='H2.TLabel')
        self.label_post1title.config(style='H2.TLabel')

        self.label_totalcasnos.config(style='H3.TLabel')
        self.label_totalcnas.config(style='H3.TLabel')
        self.label_totalhc.config(style='H3.TLabel')
        self.label_totalmt.config(style='H2.TLabel')

    def start(self):
        self.root.mainloop()

    def set_todaytotal(self, n):
        self.label_todaytotal.config(text='{}'.format(n))
    
    def set_cnastotal(self, n):
        self.label_totalcnas.config(text='CNAS: {}'.format(n))
    
    def set_casnostotal(self, n):
        self.label_totalcasnos.config(text='CASNOS: {}'.format(n))
    
    def set_hctotal(self, n):
        self.label_totalhc.config(text='Hors CHIFA: {}'.format(n))
    
    def set_earnings(self, n):
        x = "{:.2f}".format(n)
        self.label_totalmt.config(text='\n\nSALES\n{} DA'.format(x))

    def set_post0(self, n):
        self.label_post0label.config(text='{}'.format(n))

    def set_post1(self, n):
        self.label_post1label.config(text='{}'.format(n))