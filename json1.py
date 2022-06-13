import json
import os

mediajson = json.load(open('./MediaCatalog.json'))
allfile = str(len(mediajson['Table']))
nowfile = 1

for i in mediajson['Table']:
    os.system('cls')
    newfile = str(mediajson['Table'][i]['path'])
    crc = '_' + str(mediajson['Table'][i]['Crc']) + '.dat'
    print(str(nowfile) + '/' + allfile)
    nowfile += 1
    for base, dirs, files in os.walk('./'):
        for name in files:
            if name.endswith(crc):
                fcrc = name.removesuffix(crc)
                if os.path.exists('./' + fcrc):
                    os.renames(fcrc, newfile)
                break

