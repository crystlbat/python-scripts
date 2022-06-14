import requests
from requests.structures import CaseInsensitiveDict
import json
import time

time_list=[]
start_time='20:22:24'
startdate='2022-05-25'
enddate='2022-05-26'

url = "https://api-c6.incontact.com/inContactAPI/services/v24.0/contacts/completed"
headers = CaseInsensitiveDict()
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpY0JVSWQiOjQ1OTMyOTksIm5hbWUiOiJwcmF0aGFtZXNoLnNhcm9kZUB1bmlwaG9yZS5jb20iLCJpc3MiOiJodHRwczovL2FwaS5pbmNvbnRhY3QuY29tIiwic3ViIjoidXNlcjozMDI5NDA2NCIsImF1ZCI6IlVuaXBob3JlQFVuaXBob3JlIiwiZXhwIjoxNjU0MTc4MjMxLCJpYXQiOjE2NTQxNzQ2MzIsImljU2NvcGUiOiI4IiwiaWNDbHVzdGVySWQiOiJDNiIsImljQWdlbnRJZCI6MzAyOTQwNjQsImljU1BJZCI6MjE0NSwiZ2l2ZW5fbmFtZSI6IlByYXRoYW1lc2giLCJmYW1pbHlfbmFtZSI6IlNhcm9kZSIsInRlbmFudElkIjoiMTFlOWVmZDEtNGQ3Ny1mNjE3LTgwZWEtMDA1MDU2YTEwYzlkIiwibmJmIjoxNjU0MTc0NjMxfQ.4oDxi7-_FOaAKd3-I2WWU_6SfrjWCkVuyM7bVgJ4K-8AEBaofSB5O73E5mL5jvs-k66IDY6LW7NQkJywc0yf_nJ_pKENPQ7ufgX02nHf74cd-MECwWDzXCV4H4GBvYo-bfag6-OVgVySdR6XVqvu2p14bGE29jyEG2doP1Lc4XW7POHU0ov3Mb4tOUdVqMWjP0KZ9TVXSmXmVgMnhJQbkFXXmdaV2FbEZbpux9MRPvTi9YXtU_1utKU0rI4ITugrTN3r8B4eaErKcHmPASmGi9Cu-tuCKSdESfz9tVS51eYNRmq1fEpaIYfNvV3Xh6EC4CD33rMA8jnGRRwK8DsBMg"
headers["accept"] = "application/json"

s=int(start_time[:2])
for i in range(25):
    if s+i<24:
        if s+i<10:
            time_list.append(f'{startdate}T0{s+i}{start_time[-6:]}.760Z')
        else:
            time_list.append(f'{startdate}T{s+i}{start_time[-6:]}.760Z')

    else:
        if (s+i-24)<10:
            time_list.append(f'{enddate}T0{s + i-24}{start_time[-6:]}.760Z')
        else:
            time_list.append(f'{enddate}T{s + i-24}{start_time[-6:]}.760Z')
print(time_list)
batches={
        'batch1':time_list[:3],
        'batch2':time_list[2:5],
        'batch3':time_list[4:7],
        'batch4':time_list[6:9],
        'batch5':time_list[8:11],
        'batch6':time_list[10:13],
        'batch7':time_list[12:25],
        'batch8':time_list[14:17],
        'batch9':time_list[16:19],
        'batch10':time_list[18:21],
        'batch11':time_list[20:23],
        'batch12':time_list[22:25],
        }

for batch in batches:
    dict_param = {'isLogged': 'true',
                  'startDate': batches[batch][0],
                  'endDate': batches[batch][-1], }
    print(dict_param)

    try:
        response = requests.get(url, params=dict_param, headers=headers)
        res = response.json()

    except:
        print(response.status_code)

    else:
        with open(f"C:\CALLS_TEMP\output_{batch}.json", "w") as outfile:
            json.dump(res, outfile)
