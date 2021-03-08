#!/usr/bin/env python
# coding: utf-8

# In[107]:


from datetime import datetime
now = datetime.now()
print ("Run timestamp: "+"%02d/%02d/%04d %02d:%02d:%02d" % (now.month,now.day,now.year,now.hour,now.minute,now.second))

import requests
import urllib.request

from urllib.request import urlopen
html = urlopen("https://weatherology.com/weather-word-of-the-day/")
page_content = html.read()
with open('page_content.html', 'wb') as fid:
     fid.write(page_content)
type(page_content)
#print(page_content)

word=input("What's the word? ")
worddict=requests.get("https://www.dictionaryapi.com/api/v3/references/collegiate/json/"+str(word)+"?key=ab07ff10-f65e-440e-85b5-2ec6d067158b")

bank=worddict.json()
#print(len(bank))
print(" ")
print(" ")
print("---------------------------------------------------------------")
print("---------------------------------------------------------------")
print(" ")
print(" ")

defines=[]
actual=[]
DEFINITIONS=[]

for first in bank:
    part=first['fl']
    define=first['def']
    wordy=first['meta']['id'].upper()
    if ':' in wordy:
        wordy=wordy[:wordy.find(':')]
    print(wordy)
    print(" ")
    print(" ")
    print("Part of speech:",part)
    #print("Number of Definitions:",len(define))
    
    for piece in define:
        #print("KEYS:",piece.keys())
        #print("PIECE:",type(piece),len(piece),piece)
        print(" ")
        try: sseq=piece['sseq']
        except:print("No sseq")
        #print("SSEQ:",sseq)
        for deff in sseq:
            #print("DEFF:",type(deff), len(deff))
            for deffy in deff:
                #print("DEFFY:",deffy)
                SN=deffy[1]
                #print(SN)
                try : sense=SN['sn']
                except:sense=0
                if sense != 0:
                    print("SENSE:",sense)
                
                try:
                    actual=SN['dt']
                    actually=actual[0][1]
                    isinstance(actually,str)
                except:
                    continue

                
                if actual is None: continue

                
                if actually.startswith('{'):
                    actually=actually[4:]
                    if actually.startswith('{'):
                        actually=actually[4:]
                        actually=actually[:actually.find('|')]
                
                if SN.get('sdsense'):
                    sensy1=SN['sdsense']['sd']
                    sensy2=SN['sdsense']['dt']
                    #print("SENSY:", sensy1, sensy2)
                    
                    actually1=sensy1
                    actually2=sensy2[0][1]
                    if actually2.startswith('{'):
                        actually2=actually2[4:]
                        if actually2.startswith('{'):
                            actually2=actually2[4:]
                            actually2=actually2[:actually2.find('|')]
                    actually=actually+", "+actually1+" "+actually2
                print("-",actually)
                print(" ")

    print("---------------------------------------------------------------")
    print(" ")




ID=bank[0]['meta']['id']

defs=[]


#for y in range(len(dict[0]['def'][0]['sseq'])):
 #   for z in range(len(dict[0]['def'][0]['sseq'][y][0])-1):
  #      try:
   #         dict[0]['def'][0]['sseq'][y][0][z+1]['dt']
    #    except NameError:
     #       defs1=dict[0]['def'][0]['sseq'][y][0][z+1]['sls'][0][1]
      #  else:
       #     defs1=dict[0]['def'][0]['sseq'][y][0][z+1]['dt'][0][1]
        #    print(defs1)
         #   defs.append(defs1)
    
#for x in range(len(dict)):
 #   L1=dict[x]['def'][0]['sseq'][0][0][1]['dt'][0][1]
  #  defs.append(L1)
   # print(L1)
    #for y in range(len(dict)
 #   L1=dict[x]['def']
    
    
#len(dict)
#dict
#print(defs)


#for x in range(len(page_content)):
#bytearray([page_content [(x)]])
#for line in urllib.request.urlopen("https://weatherology.com/weather-word-of-the-day/"):
 #   print(line.decode('utf-8'))
#txt = urllib.request.urlopen("https://weatherology.com/weather-word-of-the-day/").read()
#from html.parser import HTMLParser
#HTMLParser.feed('data')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




