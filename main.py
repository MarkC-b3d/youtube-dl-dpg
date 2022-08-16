import dearpygui.dearpygui as dpg
import configparser
import os
import subprocess
config = configparser.ConfigParser()
path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
config.read(os.path.join(path, 'config.ini'))
font = (os.path.join(path, 'Gruppo-Regular.ttf'))
installdir = config['youtubedlinstall']['path']



print (installdir)

def downloadmp3():
    youtubelink = (dpg.get_value("link"))
    subprocess.Popen(f'{installdir} -x --audio-format mp3 'f'{youtubelink}') #f-strings allow the passing of variables to a command


dpg.create_context()
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font(font, 18)
    dpg.bind_font(default_font)
dpg.create_viewport(title='Custom Title', width=1280, height=720)

with dpg.window(label="Twip Mix Maker", width=640, height=360, no_close=True):
    dpg.add_text("Youtube Downloader")
    link = dpg.add_input_text(label="YouTube URL", default_value="", tag="link")
    dpg.add_button(label="Save", callback=downloadmp3)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()