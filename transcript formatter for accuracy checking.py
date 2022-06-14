import glob


manual_filenames=[]
actual_filenames=[]

manual_path='C:/manual transcripts'#replace input and output path here
actual_path='C:/actual transcripts'
manaual_output_path='C:/transcripts_NTT'
actual_output_path='C:/transcript_actual'


filepaths_manual=glob.glob(f'{manual_path}/*txt')
filepaths_actual=glob.glob(f'{actual_path}/*txt')
for file in filepaths_manual:
    manual_filenames.append(file.lstrip(f"{manual_path}\\"))
print(manual_filenames)
for file in filepaths_actual:
    actual_filenames.append(file.lstrip(f"{manual_path}\\"))

def scrapper(path,stripper,output_path):
    filename=path.lstrip(f"{stripper}\\")
    print(filename)
    with open(path,'r') as feed:
        line=feed.read()
        mod =line.replace("\n"," ")
        mod = mod.lower()
        mod = mod.replace("agent: ", "")
        mod = mod.replace("customer: ", "")
        mod = mod.replace("\'", "")
        mod = mod.replace(",", "")
        mod=mod.replace("  "," ")

    print(mod)
    with open(f'{output_path}/{filename}',"w") as output:
        output.write(mod)
for path in filepaths_manual:
    scrapper(path,manual_path,manaual_output_path)
for path in filepaths_actual:
    scrapper(path,actual_path,actual_output_path)