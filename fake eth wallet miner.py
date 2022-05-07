#basic fake eth wallet miner by drak-o


import random
import os
from os import system, name
import time
website = "(Your website)" #put your website here
def clear():
  
    # for windows
    if name == "nt":
        _ = system("cls")
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")

count1 = 0
count2 = 0
eth_ammount = str(round(random.uniform(0.5, 1), 2)) #generates fake eth ammount
random_id = ''
list_ = str('A''B''C''D''E''F''G''H''I''J''K''L''M''N''O''P''Q''R''S''T''U''V''W''X''Y''Z''a''b''c''d''e''f''g''h''i''j''k''l''m''n''o''p''q''r''s''t''u''v''w''x''y''z''1''2''3''4''5''6''7''8''9''0')

print("ETH wallet miner by Drak-o") #you can delete this and add your own tag/name
time.sleep(5)
      


os.system('color 4')
while count1<random.randint(1000000,1500000): #number of tries until you get a fake win
    
    while count2<40:
        random_id = random_id + (random.choice(list_)) #makes random fake eth adress
        count2 = count2+1
    count2 = 0
    print(">  0x" + random_id + "   |   ETH 0.0")
    count1 = count1 + 1
    random_id2 = random_id
    random_id = ''
    

clear()    
os.system('color 2')
print(">  0x"+random_id2 + "   |   ETH " + eth_ammount + "  Go on " + website + " to claim it")
os.system('pause')
