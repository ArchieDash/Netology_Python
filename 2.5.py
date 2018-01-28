import os
import subprocess
import queue

if __name__ == "__main__":

    def resize(images):
        q = queue.Queue()
        for img in images:
            q.put(img)
            subprocess.run("convert.exe Source/{0} -resize 200 Results/{0}".format(q.get()))
        pass

    def main():
        directory = os.path.abspath(os.path.dirname(__file__))
        images = os.listdir(os.path.join(directory, "Source"))
        try:
            os.mkdir(os.path.join(directory, "Results"))
        except:
            pass
        resize(images)

    main()
