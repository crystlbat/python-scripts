import librosa
import glob

import os
import pandas as pd

cd=librosa.get_duration(filename='C:/input_files/198094049878.wav')/60
print(cd)

files=glob.glob(r'C:\input_files\*.wav')
print(files)

filenames=[]
duration=[]
dict={}

for file in files:
    cs=librosa.get_duration(filename=file)/60
    print(f'{os.path.basename(file)}:duration-{cs}')
    filenames.append(os.path.basename(file))
    duration.append(round(cs,2))

dict={'filenames':filenames,
      'duration in min':duration}

print(dict)
df=pd.DataFrame.from_dict(dict)
print(df)
df.to_csv(r'C:\input_files\duration.csv',index=False)
