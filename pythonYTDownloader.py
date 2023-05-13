import PySimpleGUI as sg
from pytube import YouTube
import os

resolutions = ["360p","480p","720p","Max"]

def getVideo(link, resolution, audio):
    
    savePath = "./" #Download Path
    
    try:
        yt = YouTube(link)
        
        if(audio == True):  #If Audio just download audio
            video = yt.streams.filter(only_audio=True).first()
        else: 
            if(resolution == "Max"): #If resolution max then download video at its max quality 
                video = yt.streams.get_highest_resolution()
            else:
                video = yt.streams.filter(res=resolution).first() #Download video at specified resolution
       
        #video.set_filename(yt.title + "_Download")
        video.download(savePath)
    except:
        print("Could Not Find Video")

sg.theme('DarkTeal9')   # Add a touch of color

# All the stuff inside your window.
layout =    [
    
  
            [sg.Text('Enter Url:',pad=(0,10)), sg.InputText(do_not_clear=False)],
            [sg.Text('Just Audio',pad=(0,10)),sg.Checkbox("",k='-AUDIO-')],
            [[sg.Text('Resolution:',pad=(0,10)),sg.Combo(resolutions, default_value="Max" ,k='-COMBO-')]],
            [sg.Button('Download',pad=(0,10))] 
            ]

# Create the Window
window = sg.Window('Youtube Downloader', layout, font=("Arial",12) )
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    resolution = window['-COMBO-'].get()
    audio = window['-AUDIO-'].get()
    getVideo(values[0],resolution,audio)
 


window.close()

