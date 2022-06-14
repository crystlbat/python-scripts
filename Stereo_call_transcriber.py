import os
import glob
import datetime
import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
from multiprocessing import Process
import json
import time
from threading import Thread

model=Model('big_model_hmm')

audio_files=glob.glob('C:\FOR STT AUDIO')

def batchprocesor(filename):

    wav_file = filename
    txt_file = filename.strip('.wav') + '.txt'
    wf = wave.open(wav_file, "rb")
    print(f"transcribing {wav_file}")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    transcription = []

    while True:
        data = wf.readframes(1500)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # Convert json output to dict
            result_dict = json.loads(rec.Result())
            # Extract text values and append them to transcription list
            transcription.append(result_dict.get("text", ""))
            #print(f"Agent:{transcription[-1]}")

    final_result = json.loads(rec.FinalResult())
    transcription.append(final_result.get("text", ""))

    # merge or join all list elements to one big string
    #transcription_text = '\n Speaker:'.join(transcription)

    #print(transcription_text)
    with open(txt_file, 'w') as output:
        for list in transcription:
            output.write(f"Speaker:{list}\n")


def file_conv(filename):
    file=os.path.basename(filename)
    channels=['Left','Right']
    output_path="C:/CALLS_TEMP/"
    current_dir = os.getcwd()
    os.chdir('C:/Program Files (x86)/sox-14-4-2')
    sox_command_left = f'sox {filename} -b 16 -r 8k {output_path + channels[1] + "_" + file} remix 1'
    sox_command_right = f'sox {filename} -b 16 -r 8k {output_path + channels[0] + "_" + file} remix 2'
    os.system(f'cmd /C "{sox_command_right}"')
    os.system(f'cmd /C "{sox_command_left}"')
    os.chdir(current_dir)
    filenames=glob.glob(f'{output_path}*.wav')
    print(filenames)
    return filenames

file_list=file_conv(r'C:\input_files\196737382996.wav')

print(file_list)

#for file in file_list:
    #batchprocesor(file)
current_time=datetime.datetime.now()
t1 = Thread(target=batchprocesor,args=(file_list[0],))
t2 = Thread(target=batchprocesor,args=(file_list[1],))

t1.start()
t2.start()

if __name__=='__main__':
    print(datetime.datetime.now()-current_time)
