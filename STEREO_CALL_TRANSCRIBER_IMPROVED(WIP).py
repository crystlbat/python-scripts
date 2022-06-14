import glob
import os
import datetime
import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
from multiprocessing import Process,Pool,cpu_count
import json






model=Model('big_model_hmm')



audio_files=[os.path.basename(file) for file in glob.glob(r'C:\FOR_STT_AUDIO\*.wav')]
audio_file_with_path=glob.glob(r'C:\FOR_STT_AUDIO\*.wav')
print(audio_files)
print(audio_file_with_path)
files_for_transcription=[]

def batchprocesor(filename):

    wav_file = filename
    txt_file = filename.strip('.wav') + '.txt'
    wf = wave.open(wav_file, "rb")
    print(f"transcribing {wav_file}")

    rec = KaldiRecognizer(model, wf.getframerate())
    rec.SetWords(True)

    transcription = []

    while True:
        data = wf.readframes(500)
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
    print(filename)
    file=os.path.basename(filename)
    print(file)
    channels=['Left','Right']
    output_path="C:/stt_calls_splitted/"
    current_dir = os.getcwd()
    os.chdir('C:/Program Files (x86)/sox-14-4-2')
    sox_command_left = f'sox {filename} -b 16 -r 16k {output_path + channels[1] + "_" + file} remix 1'
    sox_command_right = f'sox {filename} -b 16 -r 16k {output_path + channels[0] + "_" + file} remix 2'
    os.system(f'cmd /C "{sox_command_right}"')
    os.system(f'cmd /C "{sox_command_left}"')
    os.chdir(current_dir)


if __name__=='__main__':
    for file in audio_file_with_path:
        file_conv(file)

    pool = Pool(processes=(cpu_count() - 2))
    for file in audio_files:
        file_left = f'C:/stt_calls_splitted/Left_{file}'
        file_right=f'C:/stt_calls_splitted/Right_{file}'
        print(file_left)
        print(file_right)
        pool.map(batchprocesor,[file_left,file_right])
    pool.close()
    pool.join()

    file_list_audios = glob.glob(r'C:\stt_calls_splitted\*.wav')
    print(file_list_audios)
    os.chdir('C:/stt_calls_splitted/')
    for file in file_list_audios:
        os.system(f'cmd /C "del {file}"')
