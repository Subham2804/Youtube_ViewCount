import pandas as pd
import requests
import datetime
import numpy as np
from bs4 import BeautifulSoup

f=open('youtube_data.csv','w')
f.close()
f=open('youtube_data.csv','a')



while(True):
    page=requests.get("https://www.youtube.com/watch?v=TcMBFSGVi1c&t=6s")
    soup=BeautifulSoup(page.content,'html.parser')

    now=datetime.datetime.now()

    
    views=soup.find_all(class_='watch-view-count')[0].get_text()
    views2=views[0:int(len(views))-6]
    views2=views2.replace(',','')
    views=int(views2)
    
    likes=soup.find_all(class_='yt-uix-button-content')[25].get_text()
    likes=likes.replace(',','')
    


    dislikes=soup.find_all(class_='yt-uix-button-content')[23].get_text()
    dislikes=dislikes.replace(',','')
    


    subscribers=soup.find_all(class_='yt-uix-button-content')[23].get_text()
    subscribers=subscribers.replace(',','')


    a=np.asarray([[now.month,now.day,now.hour,now.minute,views,likes,dislikes,subscribers]])
    np.savetxt(f,a,fmt='%i',delimiter=",")
  
