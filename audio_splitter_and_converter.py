import os
import glob
import datetime
import wave

mono=['Agent','Customer','converted_']#channels for naming
current_dir=os.getcwd()
print(current_dir)
input_path=str('C:\\input_files\\') #where calls for convertion has to be kept
output_path=str('C:\\output_files_splitted\\') #where splitted calls will be cumulated

start_time=datetime.datetime.timestamp(datetime.datetime.now())

input_filenames=[]
print(input_path)
filenames=[]
filelist=glob.glob('C:/input_files/*.wav')
for file in filelist:
    filenames.append(file.strip("C:/input_files\\"))
print(filenames)

os.chdir('C:/Program Files (x86)/sox-14-4-2')
for file in filenames:
    sox_command = f'sox --i {input_path+file}'
    sox_command_left = f'sox {input_path + file} -b 16 -r 8k {output_path+mono[1]+"_"+file} remix 1'
    sox_command_right = f'sox {input_path + file} -b 16 -r 8k {output_path+ mono[0]+"_" +file} remix 2'
    #sox_command_converted = f'sox {input_path + file} -b 16 -r 8k {output_path + mono[2] + file} '
    os.system(f'cmd /C "{sox_command}"')
    #os.system(f'cmd /C "{sox_command_converted}"')
    os.system(f'cmd /C "{sox_command_right}"')
    os.system(f'cmd /C "{sox_command_left}"')
endtime=datetime.datetime.timestamp(datetime.datetime.now())

print(f'Completed: Time taken=>{endtime-start_time}s')

filelist_conv=glob.glob('C:/output_files_splitted/*.wav')
def mono_checker(filelist):
    mono_calls=[]
    path = output_path.replace("\\", "/")
    for file in filelist:
        ch=wave.open(file)
        if int(ch.getnchannels())==1:
            mono_calls.append(file.replace('C:/output_files_splitted\\',""))
    with open(f'{path}monocalls.txt',"w") as output:
        for calls in mono_calls:
            output.write(f'{calls}\n')
mono_checker(filelist_conv)