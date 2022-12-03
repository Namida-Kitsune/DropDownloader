# import all function from class tkinter
from tkinter import *

# import function YouTube from class pytube
from pytube import YouTube

# create screen
app = Tk()

# set width and height screen
app.geometry("500x200")

# set the screen to be inflexible
app.resizable(width=False,height=False)

# set background color
app.config(bg="#fff")

# set title application
app.title("Drop Downloader")

# set icon application
app_logo = PhotoImage(file="icon.png")
app.iconphoto(False, app_logo)

# create label header application
Label(app, text="Drop Downloader", font=("Courier 30 bold"),
      fg="#007bff",bg="#fff").place(x=75,y=20)

# create entry for input link video
link_from_user = StringVar()
input_link = Entry(app,textvariable=link_from_user,
                   font=("Courier 10 bold"),justify=LEFT,bd=0,
                   highlightthickness=2,highlightbackground="#007bff",
                   highlightcolor="#007bff")
input_link.place(x=75,y=100,width=250,height=30)

# create function video_download for process download video
def video_download() :
    try :
        video_url = YouTube(str(link_from_user.get()))
        videos = video_url.streams.get_highest_resolution().download()
        status_change_text.set("Completed.")
    except :
        status_change_text.set("Paste your video link.")

# create button
btn_download = Button(app,font=("Courier 14 bold"),text="Download",
                      bd=0,fg="#fff",bg="#007bff",activebackground="#0065d1",
                      activeforeground="#fff",command=video_download)
btn_download.place(x=325,y=100,width=100,height=30)

# create label status
status_change_text = StringVar()
status_change_text.set("Paste your video link.")
status_change_label = Label(app,textvariable = status_change_text,font=("Courier 12 bold"),
                            fg="red",bg="#fff")
status_change_label.place(x=75,y=150)

# run application
app.mainloop()

