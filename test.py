from pytube import YouTube
import pytube
import os
import urllib.request
import json
import urllib
from tkinter import *
from tkinter import messagebox
import re


def download():
    if len(link.get()) != 0:
        params = {"format": "json", "url": "%s" % link.get()}
        url = "https://www.youtube.com/oembed"
        query_string = urllib.parse.urlencode(params)
        url = url + "?" + query_string


        try:
            with urllib.request.urlopen(url) as response:
                response_text = response.read()
                data = json.loads(response_text.decode())
                title = (data['title'])
        except urllib.error.HTTPError as exception:
            messagebox.showwarning(title="Error", message="Requested URL not found")
            ui.mainloop()

        #downloading the video
        name = pytube.extract.video_id(link.get())
        YouTube(link.get()).streams.filter(only_audio=True).first().download(filename=name)

        #grabbing the current working directory
        path = os.getcwd() + '\\'

        #get the location and name of the downloaded file
        location = path + name
        fmtitle = re.sub(r"[^a-zA-Z0-9]","",title)
        nwname = path + fmtitle + '.mp3'

        #renaming existing file to mp3
        os.rename(location, nwname)

    else:
        messagebox.showinfo("info", "Please enter a valid URL to continue")


ui = Tk()
ui.title("YouTube audio downloader")
ui.config(padx=50, pady=50, bg="#383e56")

title1 = Label(text="YouTube audio downloader", bg="#383e56", fg="#c5d7bd", font=("Arial", 35, "bold"))
title1.pack()

#Taking the link of the video
label_before_input = Label(text="Enter the youtube video link",bg="#383e56",fg="#c5d7bd",font=("Arial", 15, "bold"))
label_before_input.pack()
link = Entry(bg="#fb743e")
link.pack()

download_button = Button(ui, text="Enter the video link!", state=NORMAL, bg="#fb743e", height=4, width=55, command=download)
download_button.pack()

ui.mainloop()