import os
import subprocess
import queue

if __name__ == "__main__":
    directory = os.path.abspath(os.path.dirname(__file__))
    images = os.listdir(os.path.join(directory, "Source"))
    q = queue.Queue()
    for img in images:
        q.put(img)
        subprocess.run("convert.exe Source/{0} -resize 200 Results/{0}".format(q.get()))
    pass
