from tkinter import *
from openpyxl import workbook
from openpyxl import load_workbook
import os
import glob
import datetime
import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
import json


#model = Model("model")

screen = Tk()
screen.title('Call Transcriber')
screen.minsize(width=500,height=200)
screen.config(padx=20,pady=10)


fileinfo=Label(text="Enter folderpath: ",font=("Arial",10,"bold"))
fileinfo.grid(row=0,column=0)
fileinfo=Label(text="enter filename: ",font=("Arial",10,"bold"))
fileinfo.grid(row=1,column=0)
filepath=Entry(width='50')
fileinput=Entry(width='50')
file_name=fileinput.get()
file_path=filepath.get()
filepath.grid(row=0,column=1)
fileinput.grid(row=1,column=1)
print(file_name)


def batchprocesor(filename):
    wav_file = filename
    txt_file = filename.strip('.wav') + '.txt'
    wf = wave.open(wav_file, "rb")


    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    transcription = []

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # Convert json output to dict
            result_dict = json.loads(rec.Result())
            # Extract text values and append them to transcription list
            transcription.append(result_dict.get("text", ""))
            print(f"Agent:{transcription[-1]}")

    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result.get("text", ""))

    # merge or join all list elements to one big string
    transcription_text = '\n Speaker:'.join(transcription)

    print(transcription_text)
    with open(txt_file, 'w') as output:
        for list in transcription:
            output.write(f"Speaker:{list}\n")


def file_conv(filename):
    file=os.path.basename(filename)
    channels=['speaker_1','speaker_2']
    output_path="C:/CALLS_TEMP/"
    current_dir = os.getcwd()
    os.chdir('C:/Program Files (x86)/sox-14-4-2')
    sox_command_left = f'sox {filename} -b 16 -r 8k {output_path + channels[1] + "_" + file} remix 1'
    sox_command_right = f'sox {filename} -b 16 -r 8k {output_path + channels[0] + "_" + file} remix 2'
    os.system(f'cmd /C "{sox_command_right}"')
    os.system(f'cmd /C "{sox_command_left}"')
    os.chdir(current_dir)
    filenames=glob.glob(f'{output_path}*.wav')
    return filenames


def getfile():
    file_name = fileinput.get()
    file_path=filepath.get()
    filename=f'{file_path}\{file_name}.wav'
    filenames=file_conv(filename)

    processinfo=Label(text=f"Transcribing:{filename}",font=("Arial",10,"bold"))
    processinfo.grid(column=1,row=3)
    print(filenames)
    #for name in filenames:
        #batchprocesor(name)
    processinfo['text']=f"Transcribed:{filename}"




button=Button(text='Transcribe',command=getfile)
button.grid(row=2,column=1)



screen.mainloop()