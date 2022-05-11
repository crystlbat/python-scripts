import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
import json
import winsound
import glob


# open audio file


path_TXT='C:/Processed_Transcipts/'
path_WAV='C:/output_files_splitted/' #change here wrt your input audio files
filenames=[]


filelist=glob.glob('C:/output_files_splitted/Agent_*.wav')
for file in filelist:
    filenames.append(file.strip("C:/output_files_splitted\\"))


model = Model("model")

def batchprocesor(filename):
    wav_file = path_WAV + filename
    txt_file = path_TXT+ filename.strip('.wav') + '.txt'
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
    transcription_text = '\n Agent:'.join(transcription)

    print(transcription_text)
    with open(txt_file, 'w') as output:
        for list in transcription:
            output.write(f"Agent:{list}\n")


for file in filenames:
    print(f"now processing {file}")
    batchprocesor(file)
    winsound.Beep(200, 200)
    print(f"Processed {file}\n")

