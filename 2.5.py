import os
import subprocess

if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    images = os.listdir(os.path.join(directory, "Source"))
    for img in images:
        subprocess.run("convert.exe Source/{0} -resize 200 Results/{0}".format(img))
    pass
