from youtube import youtube
from search import Search
from os import listdir
from dialog import Dialog
from tkinter import *

root = Tk()
listbox = Listbox(root)
listbox.pack()

values = listbox.get(ANCHOR)
print(values)

query = Search("metalica")
links = query.getResults()

#for item in links:
 #   print (links[item])
  #  audio = youtube(links[item])
#video = youtube("https://www.youtube.com/watch?v=5BAiDKOqfvc")
#video.download()

#files = listdir ("D:\\Documents\\youtube\\tracks")
files = links
for item in files:
    listbox.insert(END,item)


mainloop()

