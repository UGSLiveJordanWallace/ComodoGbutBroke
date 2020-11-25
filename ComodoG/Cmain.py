from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
import time
import datetime
import pytz
from PIL import ImageTk,Image
from tkinter import filedialog

global c

#Databas
conn = sqlite3.connect("Notes.db")

#connect
c = conn.cursor()

#Create
conn.commit()

#Another Databas
connect = sqlite3.connect("Users.db")

#connect
cur = connect.cursor()

#Commiting
connect.commit

# Another DATABAS
recon = sqlite3.connect("numbers.db")

mes = recon.cursor()

recon.commit()

# def callback(input):
#     if input.isinstance():
#         print(input)
#         return True
#
#     elif input is "":
#         print(input)
#         return True
#
#     else:
#         print(input)
#         return False

def preloging():
    screen6 = Toplevel(root)
    screen6.title("List of Entries")
    screen6.iconbitmap("download.ico")
    # Designate height and width of our app
    app_width = 400
    app_height = 735
    screen_width = screen6.winfo_screenwidth()
    screen_height = screen6.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    screen6.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

    cur.execute("SELECT *, oid FROM users")
    ids = cur.fetchall()

    mes.execute("SELECT *, oid FROM numbers")
    numbers = mes.fetchall()

    # Create a main frame
    main_frame = Frame(screen6)
    main_frame.pack(fill = BOTH, expand = 10)

    # Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = 10)

    # add scrollbar to canves
    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    # Configure the Canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame Inside the Canvas
    second_frame = Frame(my_canvas)

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window = second_frame, anchor = "nw")

    #
    print_ids = ""
    print_number = ""
    #
    for id in ids:
        print_ids += "Your Username: " + str(id[0]) + ":\n" + "Your Password: " + str(id[1]) + "\n\n"
    for num in numbers:
        print_number += "Your Phone Number is " + str(num[0]) + "\n\n"

    global users_label
    global user_numbers

    #
    users_label = Label(second_frame, text = print_ids, font = ("Helvetica", 13))
    users_label.pack(pady = 6)

    user_numbers = Label(second_frame, text=print_number, font=("Helvetica", 16))
    user_numbers.pack(pady=2)

    #
    Button(second_frame, text="Clear", bg = "grey", width=12, height=2, command=del_and_update2).pack(pady = 30)

def Submit():
    thedigits = phone_number.get()

    if thedigits >= 2000000000:
        mes.execute("INSERT INTO numbers VALUES (:phone_number)", {'phone_number': thedigits})

    mes.execute("SELECT * FROM numbers")

    recon.commit()

    actual_user = username.get()
    actual_password = passwordEnter.get()

    cur.execute("SELECT * FROM users")
    print(cur.fetchone())

    # if e not actual_user:
    #     root.quit()

    cur.execute("INSERT INTO users VALUES (:userId, :passId)", {'userId': actual_user, 'passId': actual_password})
    e.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

    step()

    connect.commit()

def GetandUpload():

    fln = filedialog.askopenfilename(initialdir = "C:/Documents", title = "Select a file", filetypes = (("JPG File", "*.jpg"), ("png", "*.png"), ("docx files", "*.docx"), ("pdf", "*.pdf"), ("text", "*.txt"), ("all files", "*.*")))
    my_label = Label(second_frame, text=fln)
    my_label.pack()

    img = Image.open(fln)
    img.thumbnail((350,350))
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img

    # frame = Frame(second_frame, borderwidth=12, bg="green")
    # frame.pack(pady=13)

def del_and_update2():
    cur.execute("SELECT * FROM users")
    [print(row) for row in cur.fetchall()]

    cur.execute('DELETE FROM users')
    connect.commit()

    mes.execute('DELETE FROM numbers')
    recon.commit()

    label = users_label
    num_label = user_numbers

    label["text"] = ""
    num_label["text"] = ""

def del_and_update():
    c.execute('SELECT * FROM notes')
    [print(row) for row in c.fetchall()]
    # c.execute('UPDATE notes SET value = CSAwesome WHERE value = User')
    # conn.commit()
    #
    # c.execute('SELECT * FROM notes')
    # [print(row) for row in c.fetchall()]

    c.execute('DELETE FROM notes')
    conn.commit()

    c.execute("INSERT INTO notes VALUES (:tNote, :bNote)", {'tNote': "Put your notes Here", 'bNote': "They will show up In this database: "})
    conn.commit()
    print(50*'#')

    c.execute('SELECT * FROM notes')
    [print(row) for row in c.fetchall()]

    query_label["text"] = ""

#Save function for database
def Save():
    labelofQuery = query_label

    # Getting text
    global note
    global BodyOfNote

    note = noteN.get()
    BodyOfNote = notes.get()
    # Table
    # c.execute("""CREATE TABLE notes (
    #         noteTitle text,
    #         noteWrittenBody text
    #         )""")
    c.execute("INSERT INTO notes VALUES (:tNote, :bNote)", {'tNote': note, 'bNote': BodyOfNote})

    notesNameEnter.delete(0, END)
    notesEntered.delete(0, END)
    labelofQuery.destroy()

def ExitOnClose3():
    saveScreen = screen4
    saveScreen.destroy()

def ExitOnClose2():
    saveScreen = screen
    saveScreen.destroy()

def ExitOnClose1():
    saveScreen = n_screen
    saveScreen.destroy()

def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("Completed")
    # Designate height and width of our app
    app_width = 285
    app_height = 295
    screen_width = pop.winfo_screenwidth()
    screen_height = pop.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    pop.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
    pop.config(bg="cyan")

    global me
    me = PhotoImage(file="gui_file_png.png")

    pop_label = Label(pop, text="You have completed my app.", bg="cyan", fg = "white", font=("helvetica", 15))
    pop_label.pack(pady = 15)

    my_frame = Frame(pop, bg = "cyan")
    my_frame.pack(pady = 10)

    me_pic = Label(my_frame, image = me, borderwidth = 0)
    me_pic.grid(row=0, column=0, padx=15)

    Label(my_frame, text="This app is ridiculous", bg="cyan").grid(row=1, column=0)

def step():
    my_progress["value"] += 33.5
    Label(root, text=str(int(my_progress["value"])) + "%").grid(row=14, column=1)
    if my_progress["value"] > 98:
        clicker()

def query():
    global n_screen

    n_screen = Toplevel(root)
    # Designate height and width of our app
    app_width2 = 685
    app_height2 = 650
    screen_width2 = n_screen.winfo_screenwidth()
    screen_height2 = n_screen.winfo_screenheight()
    x2 = (screen_width2 / 2) - (app_width2 / 2)
    y2 = (screen_height2 / 2) - (app_height2 / 2)
    n_screen.geometry(f"{app_width2}x{app_height2}+{int(x2)}+{int(y2)}")
    n_screen.title("Your Notes")
    n_screen.iconbitmap("C:\\Users\\jjbos\\Desktop\\Code\\ComodoG\\Save.ico")

    #Create a main frame
    main_frame = Frame(n_screen)
    main_frame.pack(fill=BOTH, expand = 10)

    #Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=10)

    #add scrollbar to canves
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    #Configure the Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    #Create ANOTHER Frame Inside the Canvas
    second_frame = Frame(my_canvas)

    #Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

    c.execute("SELECT *, oid FROM notes")
    records = c.fetchall()
    #print(records)

    global print_records
    global query_label

    print_records = ""

    #status_bar = ttk.Progressbar(n_screen, orient = HORIZONTAL, length = 250, mode = "indeterminate").pack()

    for record in records:
        print_records += str(record[0]) + ":\n" + str(record[1]) + "\n\n"

    query_label = Label(second_frame, text=print_records, font=("Helvetica", 13))
    query_label.pack(pady = 6)

    Button(second_frame, text="Clear", bg="lightgrey", command=del_and_update).pack(pady = 7)

    conn.commit()
    #Close
    #conn.close()

    Button(second_frame, text = "EXIT", bg="black", fg = "red", borderwidth=5, width=12, height=2, command = ExitOnClose1).pack()

def popup():
    global screen
    screen = Toplevel(root)
    # Designate height and width of our app
    app_width2 = 580
    app_height2 = 700
    screen_width2 = screen.winfo_screenwidth()
    screen_height2 = screen.winfo_screenheight()
    x2 = (screen_width2 / 2) - (app_width2 / 2)
    y2 = (screen_height2 / 2) - (app_height2 / 2)
    screen.geometry(f"{app_width2}x{app_height2}+{int(x2)}+{int(y2)}")
    screen.title("ComodoG")
    screen.iconbitmap("Thumbnail.ico")

    global noteN
    global notes
    global notesNameEnter
    global notesEntered
    noteN = StringVar()
    notes = StringVar()

    title_1 = Label(screen, text="Noto G", font=("Times", 35)).pack()
    Label(screen, text="Put your Notes Below").pack()
    Label(screen, text="").pack(pady = 2)
    Label(screen, text="It is suggested that you title your note so the program can locate it later").pack()
    Label(screen, text="Note Name").pack(pady=12)
    notesNameEnter = Entry(screen, textvariable=noteN)
    notesNameEnter.pack()
    Label(screen, text="").pack(pady=6)
    Label(screen, text="Notes").pack(pady=12)
    notesEntered = Entry(screen, textvariable=notes)
    notesEntered.pack()
    Label(screen, text="").pack(pady=10)
    Label(screen, text="Always View your notes or the program will not work").pack(pady=1)
    Button(screen, text="Save", width=10, height=2, command=Save).pack()
    Button(screen, text="View Written Notes", command = query).pack(pady=30)
    Button(screen, text = "EXIT", bg="black", fg = "red", borderwidth=5, width=12, height=2, command = ExitOnClose2).pack()

def open_txt():
    global files
    files = filedialog.askopenfilename(initialdir="C:/Documents", title="Open text file", filetypes=(("Text File (.txt)", "*.txt"), ))
    files = open(files, 'r')
    stuff = files.read()

    my_text.insert('1.0', stuff)
    files.close()

def save_txt():
    files = filedialog.askopenfilename(initialdir = "C:/Documents", title = "Open text file", filetypes = (("Text File (.txt)", "*.txt"),))
    file = open(files, 'w')
    file.write(my_text.get("1.0", END))

def filerCom():
    global my_text
    global lbl
    global second_frame
    global screen4

    screen4 = Toplevel(root)
    screen4.title("Files")
    screen4.geometry("600x750")
    screen4.iconbitmap("Files.ico")

    # Create a main frame
    main_frame = Frame(screen4)
    main_frame.pack(fill = BOTH, expand = 10)

    # Create a Canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side = LEFT, fill = BOTH, expand = 10)

    # add scrollbar to canves
    my_scrollbar = ttk.Scrollbar(main_frame, orient = VERTICAL, command = my_canvas.yview)
    my_scrollbar.pack(side = RIGHT, fill = Y)

    # Configure the Canvas
    my_canvas.configure(yscrollcommand = my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame Inside the Canvas
    second_frame = Frame(my_canvas)

    # Add that new frame to a window in the canvas
    my_canvas.create_window((0, 0), window = second_frame, anchor = "nw")

    title_2 = Label(second_frame, text="Filo G", font=("Times", 35))
    title_2.pack(padx=40)

    Label(second_frame, text="A directory Component").pack(pady = 10)

    Button(second_frame, text="Choose A File To Upload", command=GetandUpload).pack(padx=40)

    Label(second_frame, text = "").pack()

    Button(second_frame, text="EXIT", bg="black", fg="red", width=10, borderwidth=5, height=2, command=ExitOnClose3).pack(padx=210)

    lbl = Label(second_frame)
    lbl.pack()

    my_text = Text(second_frame, width=65, height = 18, font = ("Times", 12))
    my_text.pack(pady = 25, padx = 12)

    open_button = Button(second_frame, text="Open a text file (.txt)", command=open_txt)
    open_button.pack(pady=13)

    save_button = Button(second_frame, text="SAVE", borderwidth=10, width=12, height=2, command = save_txt)
    save_button.pack(pady = 15)

def screenOff():
    root.quit()

#The release_image function
def release_notes():
    if button["text"] == "NotoG":
        button["text"] = "Running"
        if button["text"] == "Running":
            root.update_idletasks()
            time.sleep(1)

    else:
        button["text"] = "Continue"
        if (button["text"] == "Continue"):
            time.sleep(1)
            step()
            popup()

def release_file():
    if button3["text"] == "FiloG":
        button3["text"] = "Running"
        if button3["text"] == "Running":
            time.sleep(1)
            filerCom()
    else:
        button3["text"] = "Continue"
        Label(root, text = "Click the continue button to resuse the component").grid(row = 11, column = 1)
        step()
        filerCom()

global root

#setting up the gui
root = Tk();
#Designate height and width of our app
app_width = 565
app_height = 790
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
root.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
root.title("ComodoG")
root.iconbitmap("Thumbnail.ico")

global Uname
global e
global Pname
global e2
global instruct

username = StringVar()
passwordEnter = StringVar()
phone_number = IntVar()

Uname = Label(root, text="Username*")
Uname.grid(row=9, column=1)

e = Entry(root, textvariable=username, width=30, borderwidth=3, bg="grey", fg="white")
e.get()
e.grid(row=10, column=1, pady=10)

Label(root, text=" ").grid(row=11, column=1)

Pname = Label(root, text="Password*")
Pname.grid(row=12, column=1)

e2 = Entry(root, textvariable=passwordEnter, borderwidth=3, bg="grey", fg="white")
e2.get()
e2.grid(row=13, column=1, pady=15)

Label(root, text="Phone Number*").grid(row=15, column=1, pady=12)

e3 = Entry(root, textvariable=phone_number, borderwidth=7, bg = "red", fg="white")
e3.insert(END, "XXX-XXX-XXXX")
e3.grid(row = 16, column = 1)

#The progress bar
my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length = 300, mode ="determinate")
my_progress.grid(row=17, column=1, pady=30)

#Year
tday = datetime.date.today()

title = Label(root, text=" COMODO G " + str(tday.year), font = ("Times", 20, "bold"))
title.grid(row=0, column=1, pady=5)

description = Label(root, text="A File, and Note processing Sorfware")
description.grid(row = 2, column=1, columnspan=1)

space = Label(root, text=" ")
space.grid(row=3, column=1, pady=10)

#Time
dt_eastern = datetime.datetime.now(tz=pytz.timezone('US/Eastern'))

label = Label(root, text=dt_eastern.strftime('%B %d, %Y'), font = ("Helvetica", 10))
label.grid(row=0, column=0)

t = datetime.datetime.now()

clockwork = Label(root, text="Current Time: " + t.strftime("%H:%M"))
clockwork.grid(row = 0, column = 3)

Submit = Button(root, text="Submit", width=15, height = 3, bg="green", fg="white", command=Submit)
Submit.grid(row=18, column=1)

reset = Button(root, text="Exit", font = ("Serif", 9), width=10, height=2, borderwidth=3, fg="Red", bg="black", command = screenOff)
reset.grid(row=19, column = 1, pady=16)

prelog = Button(root, text="See Previous Logins", width=20, height = 1, command = preloging)
prelog.grid(row=20, column=1, pady=5)

button = Button(root, text="Noto G", width = 16, height = 2, bg = "cyan", command = release_notes)
button.grid(row=4, column=1)

Label(root, text="").grid(row=5, column=1, pady=4)

button3 = Button(root, text="Filo G", width=16, height = 2, bg = "cyan", command = release_file)
button3.grid(row=6, column=1, pady = 8)

Label(root, text=" ").grid(row=7, column=1, pady=4)

root.mainloop()
#update_status(12)