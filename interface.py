import os
import random
from PIL import Image
from datetime import datetime



# If there are any errors please issue them:
# https://github.com/1tsIsaac/TrickClick/issues
# (or contact me | ItsIsaac#0001)



# The config, I don't recommend changing anything here unless you really have to
config = {
    "frame-delay": 1,  # 1 recommended
    "loops": 0,  # 0 required, changing will ruin the apng
    "auto-resize": True,  # If false, frames will require manual resizing
    "datetime-format": "%d-%m-%Y" # Change the date format if you are a weirdo American
}



# Generates the final image
def generateAPNG():
    os.system(
        "apngasm.exe completed/{0}.png frames/frame*.png 1 {1} -l{2} -f".format(
            datetime.now().strftime(config["datetime-format"]) + f".{random.randint(100000, 999999)}",
            config["frame-delay"],
            config["loops"]
        )
    )



# Resizes the source PNG files
def resizePNGs():
    frame1 = Image.open("frames/frame1.png")
    frame2 = Image.open("frames/frame2.png")

    frame1_size = frame1.size

    new_size = frame1_size[0], frame1_size[0]
    frame1 = frame1.resize(new_size)
    frame1.save("frames/frame1.png")
    frame2 = frame2.resize(new_size)
    frame2.save("frames/frame2.png")



resizePNGs()
generateAPNG()
