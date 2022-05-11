import wave
from vosk import Model, KaldiRecognizer, SetLogLevel
import json
# open audio file


filename='MONO_196648281182'

wav_file='C:/Users/Bibin/Downloads/'+filename+'.wav'
txt_file='C:/Users/Bibin/Downloads/'+filename+'.txt'
wf = wave.open(wav_file, "rb")


model = Model("model")
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
with open(txt_file,'w') as output:
    for list in transcription:
        output.write(f"Agent:{list}\n")