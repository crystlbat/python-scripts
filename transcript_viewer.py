#now temp file for transcipt combiner
from tkinter import *
import glob
import os



text=[]

screen = Tk()
screen.resizable(True, True)
screen.columnconfigure(0, weight=1)
screen.columnconfigure(1, weight=1)
screen.rowconfigure(0, weight=1)
screen.rowconfigure(1, weight=1)
screen.title('Transcripts YAAAY!')
screen.minsize(width=600,height=600)
screen.config(padx=20,pady=10)
screen.config(bg='#103d4d')
transcripts_files=[os.path.basename(file).lstrip('Left_') for file in glob.glob(r'C:\stt_calls_splitted\Transcripts\Left_*.txt')]

#print(transcripts_files)

variable = StringVar(screen)
variable.set(transcripts_files[0])

drop = OptionMenu( screen, variable, *transcripts_files)
drop.grid(row=0,column=0)




text_box_left = Text(
    screen,
    height=30,
    width=40,
    background='#4d4946',
    foreground='#d9d1cc')

def rightclick(event):
    try:
        text.append(str(text_box_left.selection_get())+'\n')
    except:
        text.append(text_box_left.selection_get())
    text_box_inside.delete("1.0", "end")
    for t in text:
        text_box_inside.insert(END, '\n')
        text_box_inside.insert(END, t)

text_box_left.grid(row=1,column=0,sticky="NSEW")
text_box_left.configure(font=("Segoe UI", 9, "bold"))
text_box_left.insert('end', "lol")



text_box_right = Text(
    screen,
    height=30,
    width=40,
    background='#c2ecfc',
    foreground='#695870')
text_box_right.configure(font=("Segoe UI", 9, "bold"))
text_box_right.grid(row=1,column=1,sticky="NSEW")
text_box_right.insert(END, "Yo,the paths are  hardcoded,contact the creator to tweak!!!")



def get_value():
    filename=str(variable.get())
    text_box_inside.delete("1.0", "end")
    text.clear()
    #print(filename)
    with open(f'C:\stt_calls_splitted\Transcripts\Left_{filename}','r') as left_text:
        content=left_text.read()
        content=content.replace('\n',"\n \n").replace("Speaker","Agent")
        #print(content)
    text_box_left.delete("1.0","end")
    text_box_left.insert(END,content)
    with open(f'C:\stt_calls_splitted\Transcripts\Right_{filename}','r') as right_text:
        content_ol=right_text.read()
        content_ol = content_ol.replace('\n', "\n \n").replace("Speaker","Customer")
        #print(content_ol)
    text_box_right.delete("1.0","end")
    text_box_right.insert(END,content_ol)


button = Button(screen, text="select", command=get_value)
text_box_left.bind("<Button-3>", rightclick)
text_box_right.bind("<Button-3>", rightclick)
button.grid(row=0,column=1)

screen.update()

screen_clip=Tk()
screen_clip.resizable(True, True)
screen_clip.columnconfigure(1, weight=1)
screen_clip.rowconfigure(1, weight=1)
screen_clip.title('Transcripts YAAAY!')
screen_clip.minsize(width=100, height=200)
screen_clip.config(padx=20, pady=10)
screen_clip.config(bg='#103d4d')

text_box_inside = Text(
    screen_clip,
    height=20,
    width=40,
    background='#c2ecfc',
    foreground='#695870')
text_box_inside.configure(font=("Segoe UI", 9, "bold"))
text_box_inside.grid(row=1,column=1,sticky="NSEW")
text_box_inside.insert(END, "Selected items will come here!")

screen_clip.update()
screen_clip.mainloop()
screen.mainloop()
