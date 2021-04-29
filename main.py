from dearpygui import core,simple
import subprocess
import configparser
import os

##Basic configuration

config = configparser.ConfigParser()
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config.read(os.path.join(path, 'config.ini'))
##User specifies where youtube dl is installed to depending on operating system

installdir = config['youtubedlinstall']['path']

core.set_main_window_title("YouTube Downloader V0.1")
core.set_theme("Cherry") #cherry theme looks pretty cool

def myfunction(sender,data):
    youtubelink = (core.get_value("YouTube Link"))
    subprocess.Popen(f'{installdir} -x --audio-format mp3 'f'{youtubelink}') #f-strings allow the passing of variables to a command

##youtube download
with simple.window("YouTube Downloader", width=600, height=200, no_close = True):
    core.add_input_text(name="YouTube Link", on_enter=True, callback=myfunction)
    core.add_button("Click here..", callback = myfunction)
    core.set_main_window_size(1200,600)
core.start_dearpygui()
