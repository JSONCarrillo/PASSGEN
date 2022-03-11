import random
#imports ttk as well as messagebox
from tkinter import *
from ttkbootstrap import *
import webbrowser

class Window:
    # list of all characters
    lower_case = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
        'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
    upper_case = [x.upper() for x in lower_case]
    special_char = [
        '@', '#', '$', '%', '=', ':', '?', '.', '/', '|',
        '~', '>', '*', '<', '!'
        ]

    def genPassword(self):
        password = ''
        i = 0

        while i < pass_length:
            char_choice = random.randint(0,3)

            if char_choice == 0:
                password += self.lower_case[random.randint(0, len(self.lower_case) - 1)]

            elif char_choice == 1:
                password += str(random.randint(0,9))

            elif char_choice == 2:
                password += self.upper_case[random.randint(0, len(self.upper_case) - 1)]

            else: 
                password += self.special_char[random.randint(0, len(self.special_char) - 1)]

            i+= 1

        return password

    def help(self):
        webbrowser.open('help.html')
    
    def view(self):
        pass

    def update(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass
    
    def select(self):
        pass

    def clearTable(self):
        pass

    def clearInputs(self):
        pass
    
    def refresh(self):
        pass
    
    def insert(self):
        pass
    
    def rightClickMenu(self, event):
        self.menu.tk_popup(event.x_root+12, event.y_root)

    def __init__(self, root, title, winsize):
        self.root = root
        self.root.title(title)
        self.root.geometry(winsize)
        self.root.resizable(width=False, height=False)

        self.passwd = StringVar()
        self.username = StringVar()
        self.website = StringVar()
        self.length = StringVar()

        # Username label and text entry
        Label(self.root, text="Username").grid(
            row=0, column=0, padx=10, pady=10
        )
        ttk.Entry(
            self.root, width=30, textvariable=self.username,
        ).grid(row=0, column=1, padx=10, pady=10)

        # Password label and text entry
        Label(self.root, text="Password").grid(
            row=1, column=0, padx=10, pady=10
        )
        ttk.Entry(
            self.root, width=30, textvariable=self.passwd,
        ).grid(row=1, column=1, padx=10, pady=10)

        # Website label and text entry
        Label(self.root, text="Website").grid(
            row=2, column=0, padx=10, pady=10
        )
        ttk.Entry(
            self.root, width=30, textvariable=self.website,
        ).grid(row=2, column=1, padx=10, pady=10)

        passlen = ttk.Combobox(
            self.root, values=['4', '8', '12', '16', '18', '20', '24'],
            textvariable=self.length
            )
        passlen.grid(row=0, column=2)
        passlen['state'] = 'readonly'
        self.length.set('Set Password Length')

        ttk.Button(
            self.root, text='Generate Password', style='success.TButton', width=20, padding=5, 
            command=self.genPassword
            ).grid(row=1, column=2)

        ttk.Button(
            self.root, text='Save', style='success.TButton', width=20, padding=5, 
            command=self.save
            ).grid(row=3, column=2)

        ttk.Button(
        self.root, text='Delete', style='danger.TButton', width=20, padding=5, 
        command=self.delete
        ).grid(row=3, column=0)

        ttk.Button(
        self.root, text='View All Passwords', width=20, padding=5, 
        command=self.view
        ).grid(row=3, column=0)
        
        ttk.Button(
        self.root, text='Update Password', width=20, padding=5, 
        command=self.view
        ).grid(row=3, column=1)

        # Table to display usernames, passwords, and sites
        self.tree = ttk.Treeview(self.root, height=5)
        self.tree['columns'] = ('site', 'user', 'pass')
        self.tree.column('#0', width=0, stretch=NO)
        self.tree.column('site', width=160, anchor=W)
        self.tree.column('user', width=140, anchor=W)
        self.tree.column('pass', width=180, anchor=W)
        
        self.tree.heading('#0', text='')
        self.tree.heading('site', text='Website')
        self.tree.heading('user', text='Username')
        self.tree.heading('pass', text='Password')

        self.tree.grid(row=4, column=0, columnspan=3, pady=10)
        # this calls the 'select' function
        # that takes the row and fills its respective data to inputs
        self.tree.bind("<ButtonRelease-1>", self.select)


        # creates the right-click popup menu
        self.menu = Menu(self.root, tearoff=False)
        self.menu.add_command(label='Refresh', command=self.refresh)
        self.menu.add_command(label='Update', command=self.update)
        self.menu.add_command(label='Insert', command=self.insert)
        self.menu.add_separator()

        self.menu.add_command(label='Show All', command=self.view)
        self.menu.add_command(label='Clear Table', command=self.clearTable)
        self.menu.add_command(label='Clear Fields', command=self.clearInputs)
        self.menu.add_separator()

        self.menu.add_command(label='Delete', command=self.delete)
        self.menu.add_command(label='Help', command=self.help)
        self.menu.add_separator()

        self.menu.add_command(label='Exit', command=self.root.quit)
        # this binds the right mouse button to a function that creates the popup
        self.root.bind("<Button-3>", self.rightClickMenu)
        

w = Style(theme='darkly').master
name = 'FPG: FOSS Password Generator'
dimension = '720x480'

app = Window(w, name, dimension)
w.mainloop()
