import wave
import glob

input_path=str('C:\\output_files_splitted\\')
path=input_path.replace("\\","/")
filenames=[]
mono_calls=[]
filelist=glob.glob('C:/output_files_splitted/*.wav')
def mono_checker(filelist):
    for file in filelist:
        ch=wave.open(file)
        if int(ch.getnchannels())==1:
            mono_calls.append(file.replace('C:/output_files_splitted\\',""))
    with open(f'{path}monocalls.txt',"w") as output:
        for calls in mono_calls:
            output.write(f'{calls}\n')
mono_checker(filelist)