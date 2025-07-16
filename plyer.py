from tkinter import Tk,Listbox,PhotoImage,Frame,Button,Menu,filedialog,Label,Scrollbar,Listbox
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



def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end",song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]
song_label = Label(root,text="No Song Playing",font=("Arial",14),fg="orange")
song_label.pack(pady=5)

def play_music():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory,current_song))
        pygame.mixer.music.play()
        song_label.config(text=f"Playing : {current_song}")
        root.title(f"{current_song}")
    else:
        pygame.mixer.music.unpause()
        paused = False
        song_label.config(text=f"Playing : {current_song}")
        root.title(f"{current_song}")

def play_pause():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_play():
    global current_song,paused
    try:
        songlist.selection_clear(0,"end")
        songlist.selection_set(songs.index(current_song)+1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

def pre_play():
    global current_song,paused
    try:
        songlist.selection_clear(0,"end")
        songlist.selection_set(songs.index(current_song)-1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass



organize_menu = Menu(menuBar,tearoff=False)
organize_menu.add_command(label="Select Folder",command=load_music)
menuBar.add_cascade(label="Organize",menu=organize_menu)



play_btn_image  = PhotoImage(file='play.png')
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