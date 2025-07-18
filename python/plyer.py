from tkinter import Tk,Listbox,PhotoImage,Frame,Button,Menu,filedialog,Label,Scrollbar,Listbox,messagebox
import pygame
from tkinter import ttk
import os

root = Tk()
style = ttk.Style()
style.theme_use('default')
root.geometry('500x300')
root.resizable(False,False)

pygame.mixer.init()


menuBar = Menu()
root.config(menu=menuBar)

songs = []
current_song = " "
paused = False

def load_single_music():
    global current_song
    file_paths = filedialog.askopenfilenames(filetypes=[("MP3 Files","*.mp3")])
    if not file_paths:
        messagebox.showwarning("No MP3 Found","No mp3 files are selected")
        return
    songs.clear()
    songlist.delete(0,"end")
    for file_path in file_paths:
            song = os.path.basename(file_path)
            songs.append(file_path)
            songlist.insert("end",os.path.basename(file_path))
        
    songlist.selection_set(0)
    current_song = songs[0]

def load_music():
    global current_song
    directory = filedialog.askdirectory()
    if not directory:
        return
    songs.clear()
    songlist.delete(0,"end")
    found = False
    for song in os.listdir(directory):
            name, ext = os.path.splitext(song)
            if ext == '.mp3':
                full_path = os.path.join(directory,song)
                songs.append(full_path)
                songlist.insert("end",song)
                found = True
            if not found:
                messagebox.showwarning("No MP3 Found","No mp3 files found in the selected folder")
    songlist.selection_set(0)
    current_song = songs[0]

song_label = Label(root,text="No Song Playing",font=("Arial",14),fg="orange")
song_label.pack(pady=5)

def play_music():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
        song_label.config(text=f"Playing : {current_song}")
        root.title(f"{os.path.basename(current_song)}")
    else:
        pygame.mixer.music.unpause()
        paused = False
        song_label.config(text=f"Playing : {current_song}")
        root.title(f"{os.path.basename(current_song)}")

def play_pause():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_play():
    global current_song,paused
    try:
        idx = songs.index(current_song)
        if idx < len(songs) - 1:
            songlist.selection_clear(0,"end")
            songlist.selection_set(idx + 1)
            current_song = songs[idx+1]
            play_music()
    except:
        pass

def pre_play():
    global current_song,paused
    try:
        idx = songs.index(current_song)
        if idx > 0:
            songlist.selection_clear(0,"end")
            songlist.selection_set(idx - 1)
            current_song = songs[idx-1]
            play_music()
    except:
        pass



organize_menu = Menu(menuBar,tearoff=False)
organize_menu.add_command(label="Add mp3",command=load_single_music)
organize_menu.add_command(label="Select Folder",command=load_music)
menuBar.add_cascade(label="Organize",menu=organize_menu)



play_btn_image  = PhotoImage(file='play.gif')
pause_btn_image  = PhotoImage(file='pause.png')
nex_btn_image  = PhotoImage(file='next.png')
pre_btn_image  = PhotoImage(file='previous.png')


control_fram = Frame(root)
control_fram.pack(side="bottom")

scrollbar = Scrollbar(root)
scrollbar.pack(side="right",fill="y")
songlist = Listbox(root,bg='#222244',fg='#FFFFFF',font=("Arial",12),width=100,height=15,yscrollcommand=scrollbar.set)
songlist.pack(side="left",fill="both")


scrollbar.config(command=songlist.yview)

status_bar = Label(root,text="Welcome to Ravi Music",bd=1, relief="sunken",anchor="w")
status_bar.pack(side="bottom",fill="x")

def on_song_double_click(event):
    global current_song
    selection = songlist.curselection()
    if selection:
        current_song = songs[selection[0]]
        play_music()

songlist.bind("<Double-Button-1>", on_song_double_click)

play_btn = Button(control_fram,image=play_btn_image,borderwidth=0,command=play_music)
pause_btn = Button(control_fram,image=pause_btn_image,borderwidth=0,command=play_pause)
next_btn = Button(control_fram,image=nex_btn_image,borderwidth=0,command=next_play)
pre_btn = Button(control_fram,image=pre_btn_image,borderwidth=0,command=pre_play)

play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
next_btn.grid(row=0,column=3,padx=7,pady=10)
pre_btn.grid(row=0,column=0,padx=7,pady=10)
root.title("Ravi Music Player")
root.mainloop()