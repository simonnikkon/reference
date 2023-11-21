index_price_v2_p.py

index_price_v2_linux.py












index_price_v2_p.py

#############################
########Download Data########
#############################
 





#check chromedriver ok or not
import time
import ctypes
import os
from collections import OrderedDict

# Import the SendInput object
SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBoardInput(ctypes.Structure):
    _fields_ = [
        ("wVk", ctypes.c_ushort),
        ("wScan", ctypes.c_ushort),
        ("dwFlags", ctypes.c_ulong),
        ("time", ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class HardwareInput(ctypes.Structure):
    _fields_ = [
        ("uMsg", ctypes.c_ulong),
        ("wParamL", ctypes.c_short),
        ("wParamH", ctypes.c_ushort)
    ]

class MouseInput(ctypes.Structure):
    _fields_ = [
        ("dx", ctypes.c_long),
        ("dy", ctypes.c_long),
        ("mouseData", ctypes.c_ulong),
        ("dwFlags", ctypes.c_ulong),
        ("time",ctypes.c_ulong),
        ("dwExtraInfo", PUL)
    ]

class Input_I(ctypes.Union):
    _fields_ = [
        ("ki", KeyBoardInput),
        ("mi", MouseInput),
        ("hi", HardwareInput)
    ]

class Input(ctypes.Structure):
    _fields_ = [
        ("type", ctypes.c_ulong),
        ("ii", Input_I)
    ]

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF

def key_down(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0, 0, ctypes.pointer(extra))
    x = Input( ctypes.c_ulong(1), ii_ )
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def key_up(keyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBoardInput(keyCode, 0x48, 0x0002, 0, ctypes.pointer(extra))
    x = Input(ctypes.c_ulong(1), ii_)
    SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
def key(key_code, length = 0):    
    key_down(key_code)
    time.sleep(length)
    key_up(key_code)
def volume_up():
    key(VK_VOLUME_UP)
def volume_down():
    key(VK_VOLUME_DOWN)
def set_volume(int):
    for _ in range(0, 50):
        volume_down()
    for _ in range(int / 2):
        volume_up()
        
from selenium import webdriver
chrome_driver_ok=True

try:
    #driver = webdriver.Chrome(executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_83.exe')#8003987
    driver = webdriver.Chrome(executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')#8003987
    driver.close()
except:
    chrome_driver_ok=False
    pass

            
if (chrome_driver_ok==False):
    
    #python send email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    mail_content = "email sent"
    #The mail addresses and password
    sender_address = 'ra'
    sender_pass = '95229522'
    receiver_address = 'daniel.chunyuwai@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'chromedriver not ok'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content))
    
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
    
    #adjust volumn to 0 first
    for i in range(0,100):
        volume_down()   
    #adjust up volume
    for i in range(0,7):
        volume_up()
    sound_path=r'C:\Users\danie_live_trade\Wecker-sound.mp3'
    os.system(sound_path)
































##connect wifi first

import subprocess
import requests
import zipfile
import io

#this bathch file will connect to the default wifi network
#filepath=r"C:\Users\daniellau\Dropbox\notebooks\index_analysis\mis\turn_on_wifi_connect_to_default_network.bat"
#p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)

#this will disconnect the exisiting one and then connect to another one
#filepath=r"C:\Users\daniellau\Dropbox\notebooks\index_analysis\mis\after_turn_on_connect_to_specific_wifi.bat"
#p = subprocess.Popen(filepath, shell=True, stdout = subprocess.PIPE)


#%reset -f
import os
import numpy as np
#os.chdir(r'C:\Users\daniellau\Desktop\python\WinPython-64bit-3.6.2.0Qt5\notebooks\index_analysis')
target_dir=r'C:\Users\daniellau\Dropbox\notebooks\index_analysis'

storage_reference=r'C:\Users\daniellau\storage_reference'

use_hsi_future_price=True

os.chdir(target_dir)

#import sys
#sys.path.append(r'C:\Users\daniellau\Desktop\python\boltons')
#from boltons import iterutils

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    
from pandas import read_excel
data = read_excel('index_table_v2_for_test.xlsx','Sheet1')


#python -m pip install pandas-datareader
#https://stackoverflow.com/questions/12433076/download-history-stock-prices-automatically-from-yahoo-finance-in-python
import pandas_datareader as pdr
from datetime import timedelta
from datetime import datetime as dt
import datetime
import pandas as pd
from time import sleep

from selenium import webdriver



#output stan out
import sys
import time
time_now_save=time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")
stan_out_log=os.path.join('log','stan_out_data_part_'+time_now_save+'_production'+'.log')
sys.stderr = open(stan_out_log, 'w')





#check internet
from urllib.request import urlopen
def internet_on():
    try:
        response = urlopen('https://www.google.com/', timeout=10)
        return True
    except: 
        return False

internet_check="connected" if internet_on() else "not connected"

eprint("internet connection is ",internet_check)
print("internet connection is ",internet_check)





#use_list=[data.Name_use_python[i]+'_change' for i in range(0,len(data.symbol)) if (data.Merge_tgh[i]=='Yes')&(pd.isnull(data.UseEMA[i]))]
#use_list_ema=['EMA_'+data.Name_use_python[i]+'_change' for i in range(0,len(data.symbol)) if (data.Merge_tgh[i]=='Yes')&(data.UseEMA[i]=='Yes')]
#if 'HSI_change' in use_list:
#    use_list.remove('HSI_change')
#    
#all_factor=use_list+use_list_ema+['CHRIS_com_CME_GC1_change_interact_CHRIS_com_ICE_B1_change','index_DJIA_wsj_greatless_mean_sd2_value_indicator']
#
##j='TWCCX_change'
#all_name=[]
#out=''
#for i in all_factor:
#    out=out+"'"+i+"',"
#out="["+out[0:(len(out)-1)]+"]"




#index_quote='0939.HK'
#index_quote='EWH'
#start_date=datetime(1991,1,1);end_date=datetime(2030,12,31)
#def get_quote(index_quote,start_date,end_date):
#    i = 0
#    print('Doing ',index_quote)
#    while i < 500:
#        i += 1
#        print(i,'\n')
#        try:
#            # do stuff
#            out=pdr.get_data_yahoo(symbols=index_quote, start=start_date, end=end_date)
#
#            break
#        except:
#            continue
#    return out
#help(pdr.get_data_yahoo)
#tt=get_quote('0939.HK')
#temp=get_quote('2819.HK',datetime(1991,1,1),datetime(2030,12,31))

#out=pdr.get_data_yahoo(symbols='^HSI', start=datetime(1991,1,1), end=datetime(2030,12,31),interval='m')


import os.path

#i=20
#download yahoo data and save to xlsx
#count=0
#yahoo_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='Yahoo'),:].shape[0]
#
#for i in range(0,len(data.symbol)):
#    if (data.Extract[i]=='Yes')&(data.Source[i]=='Yahoo'):
##        file_path=os.path.join(target_dir,data.Name_use_python[i]+'.xlsx')
##        if os.path.exists(file_path):
##            temp_old=read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
##            temp_old['Date2']=temp_old['Date'].dt.date
##            temp_old['Date2']=temp_old['Date2'].astype(str)
##            date_end=temp_old.Date2[temp_old.shape[0]-1]
##            date_end=datetime.strptime(date_end,'%Y-%m-%d')
#        
#        temp=get_quote(data.symbol[i],dt(1991,1,1),dt(2030,12,31))
#        # Create a Pandas Excel writer using XlsxWriter as the engine.
#        writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
#        
#        # Convert the dataframe to an XlsxWriter Excel object.
#        temp.to_excel(writer, sheet_name='Sheet1')
#        writer.save()
#        
#        #copy source as back up to daily_source_data_production
#        writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
#        temp.to_excel(writer, sheet_name='Sheet1')
#        writer.save()
#        
#        count=count+1
#        print('Yahoo Finance Data Extraction ',count,' (',data.symbol[i],')',' out of ',yahoo_source_total,'\n')
#        eprint('Yahoo Finance Data Extraction ',count,' (',data.symbol[i],')',' out of ',yahoo_source_total,'\n')

#extract data from quandl
        
        
import quandl
quandl.ApiConfig.api_key = "F71H5iBEAKKaL1YK6yLz"
#CHRIS/HKEX_HSI1
#mydata = quandl.get("WIKI/IBM", start_date="2000-01-01", end_date="2017-10-29", collapse="daily", returns="pandas")
#mydata1 = quandl.get("NBSC/A190101_M", start_date="1991-01-01", end_date="2017-11-30", collapse="minute", returns="pandas")
#mydata2 = quandl.get("USTREASURY/REALYIELD", start_date="1991-01-01", end_date="2017-11-07", collapse="daily", returns="pandas")
#help(quandl.get)
#BCHARTS/{ANXHK}{USD}


from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import csv

def get_quote_quandl(index_quote):
    return quandl.get(index_quote, start_date="1991-01-01", end_date="2030-12-31", collapse="daily", returns="pandas")

#i=75 i=322#2472  i=24 i=23  i=75 
#download data and save to xlsx
quandl_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='Quandl'),:].shape[0]
count=0
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='Quandl'):
        temp=pd.DataFrame([])
        for ii in range(0,5):
            try:
                temp=get_quote_quandl(data.symbol[i])
                
                if (data.symbol[i]=='USTREASURY/REALYIELD'):
                    url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2023/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2022&page&_format=csv'
                    webpage = urlopen(url)
                    datareader = csv.reader(io.TextIOWrapper(webpage))
                    us_yield = list(datareader)
                    
                    all_col_name=us_yield[0]
                    all_col_name_date=all_col_name.index('Date')
                    all_col_name_5=all_col_name.index('5 YR')
                    all_col_name_7=all_col_name.index('7 YR')
                    all_col_name_10=all_col_name.index('10 YR')
                    all_col_name_20=all_col_name.index('20 YR')
                    all_col_name_30=all_col_name.index('30 YR')
                    
                    us_yield_col1=[xx[all_col_name_date] for xx in us_yield[1:]]
                    us_yield_col2=[xx[all_col_name_5] for xx in us_yield[1:]]
                    us_yield_col3=[xx[all_col_name_7] for xx in us_yield[1:]]
                    us_yield_col4=[xx[all_col_name_10] for xx in us_yield[1:]]
                    us_yield_col5=[xx[all_col_name_20] for xx in us_yield[1:]]
                    us_yield_col6=[xx[all_col_name_30] for xx in us_yield[1:]]
                    
                    us_yield=pd.DataFrame({'Date':us_yield_col1,'5 YR':us_yield_col2,'7 YR':us_yield_col3,'10 YR':us_yield_col4,'20 YR':us_yield_col5,'30 YR':us_yield_col6})
                    us_yield['5 YR']=pd.to_numeric(us_yield['5 YR'], errors='coerce')
                    us_yield['7 YR']=pd.to_numeric(us_yield['7 YR'], errors='coerce')
                    us_yield['10 YR']=pd.to_numeric(us_yield['10 YR'], errors='coerce')
                    us_yield['20 YR']=pd.to_numeric(us_yield['20 YR'], errors='coerce')
                    us_yield['30 YR']=pd.to_numeric(us_yield['30 YR'], errors='coerce')
                    
                    
                    us_yield['Date']=us_yield['Date'].apply(lambda x: dt.strptime(x,'%m/%d/%Y'))
                    us_yield=us_yield.sort_values(by=['Date'],ascending=True)

                    temp=us_yield.reset_index(drop=True)
                    
                    
                if (data.symbol[i]=='USTREASURY/REALLONGTERM'):
                    url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2023/all?type=daily_treasury_real_long_term&field_tdr_date_value2022l&page&_format=csv'
                    webpage = urlopen(url)
                    datareader = csv.reader(io.TextIOWrapper(webpage))
                    us_yield = list(datareader)
                    
                    us_yield_col1=[xx[0] for xx in us_yield]
                    us_yield_col2=[xx[1] for xx in us_yield]
                    us_yield_col1=us_yield_col1[1:]
                    us_yield_col2=us_yield_col2[1:]
                    
                    us_yield=pd.DataFrame({'Date':us_yield_col1,'LT Real Average (>10Yrs)':us_yield_col2})
                    us_yield['LT Real Average (>10Yrs)']=pd.to_numeric(us_yield['LT Real Average (>10Yrs)'], errors='coerce')
                     
                    us_yield['Date']=us_yield['Date'].apply(lambda x: dt.strptime(x,'%m/%d/%Y'))
                    us_yield=us_yield.sort_values(by=['Date'],ascending=True)

                    temp=us_yield.reset_index(drop=True)
                
                if (data.symbol[i]=='AAII/AAII_SENTIMENT'):
                    if (dt.today().strftime('%A')=='Friday'):
                        count=count+1
                        for ii in range(0,2):
                            #clear_dir = r"C:\Users\daniellau\Dropbox\notebooks\index_analysis\wsj_csv\temp\*"
                            download_dir = r"C:\Users\daniellau\Dropbox\notebooks\index_analysis"

                            etract_link='https://www.aaii.com/files/surveys/sentiment.xls'
                            
                            if os.path.exists(os.path.join(download_dir,'sentiment.xls')):
                                os.remove(os.path.join(download_dir,'sentiment.xls')) 
                            
                            try:
                                #download file to folder
                                import requests
                                from lxml.html import fromstring
                        
                    
                                def get_proxies():
                                    url = 'https://free-proxy-list.net/'
                                    response = requests.get(url)
                                    parser = fromstring(response.text)
                                    proxies = set()
                                    #i=parser.xpath('//tbody/tr')[0]
                                    for i in parser.xpath('//tbody/tr'):
                                        if (i.xpath('.//td[7][contains(text(),"yes")]')):
                                            #Grabbing IP and corresponding PORT
                                            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                                            proxies.add(proxy)
                                    return proxies
                                
                                import requests
                                from itertools import cycle
                                import traceback
                                proxies = get_proxies()
                                proxy_pool = cycle(proxies)
                                url = 'https://httpbin.org/ip'
                                #iii=0
                                for iii in range(0,min(30,len(proxies))):
                                    #Get a proxy from the pool
                                    if not os.path.exists(os.path.join(download_dir,'sentiment.xls')):
                                        proxy_use = next(proxy_pool)
                                        print("Request #%d"%iii)
                                        chrome_options = webdriver.ChromeOptions()
                                        PROXY = proxy_use
                                        try:
                                            chrome_options.add_argument('--proxy-server=%s' % PROXY)
                                            preferences = {"download.default_directory": download_dir ,
                                                           "directory_upgrade": True,
                                                           "safebrowsing.enabled": True }
                                            chrome_options.add_experimental_option("prefs", preferences)
                                            
                                            driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')
                                            driver.set_page_load_timeout(30)
                                            driver.get(etract_link)
                                            
                                            count_time=0
                                            while (count_time<=30)&(not os.path.exists(os.path.join(download_dir,'sentiment.xls'))):
                                                time.sleep(2)
                                                count_time=count_time+2
                                                print('waiting '+str(count_time)+' seconds')
                                            sleep(2)
                                            driver.close()

        
                                            #move incompete download
                                            import shutil
                                            for filename in os.listdir(download_dir):
                                                f = os.path.join(download_dir, filename)
                                                if 'crdownload' in f:
                                                    #print(f)
                                                    shutil.move(f,os.path.join(download_dir,'can_delete',filename))
                                        
                                      
                                        except:
                                            driver.close()
                                            eprint("Oops!",sys.exc_info()[0],"occured when extracting ",'AAII sentiment','\n')
                                            print("Oops!",sys.exc_info()[0],"occured when extracting ",'AAII_sentiment','\n')
                                        if os.path.exists(os.path.join(download_dir,'sentiment.xls')):
                                            break

#                                #iii=2
#                                for iii in range(0,min(10,len(proxies))):
#                                    #Get a proxy from the pool
#
#                                    proxy_use = next(proxy_pool)
#                                    print("Request #%d"%iii)
#                                    chrome_options = webdriver.ChromeOptions()
#                                    PROXY = proxy_use
#                                    chrome_options.add_argument('--proxy-server=%s' % PROXY)
#                                    preferences = {"download.default_directory": download_dir ,
#                                                   "directory_upgrade": True,
#                                                   "safebrowsing.enabled": True }
#                                    chrome_options.add_experimental_option("prefs", preferences)
#
#                                    driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')
#                                    driver.set_page_load_timeout(30)                                            
#                                    driver.get('https://www.aaii.com/sentimentsurvey/sent_results')
#                                    html_string=driver.execute_script("return document.body.innerHTML")
# 
#                                    store=[]
#                                    soup = BeautifulSoup(html_string, 'lxml')
#                                    table = soup.find_all('table', {'class':'bordered'})[0] 
#                                    #row=table_1.find_all('tr')[1]
#
#                                    for row in table.find_all('tr'):
#                                        #row=table.find_all('tr')[1]
#                                        columns = row.find_all('td')
#                                        #print(len(columns))
#                                        store_temp=''
#                                        for column in columns:
#                                            print(column)
#                                            store_temp= store_temp+'|'+column.get_text()                    
#                                    
#                                        store.append(store_temp)
#                                        i=i+1
#                                    
#                                    temp_use=store[1]
#                                    temp_use_month=temp_use.split('|')[1].split(' ')[0].replace('\n','')
#                                    temp_use_day=temp_use.split('|')[1].split(' ')[1].replace(':\n','')
#                                    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
#                                    months_aaii=str(months.index(temp_use_month)+1)
#                                    date_aaii=dt()
#                                    day_aaii=str(temp_use_day)
#                                    if (months_aaii==dt.today().strftime('%m'))&(day_aaii==str(int(dt.today()-timedelta(days=4).strftime('%d'))-2)): # if it is wednesday
#                                        df_aaii=pd.DataFrame({'Date':[(dt.today()-timedelta(days=1)).strftime('%Y-%m-%d')],
#                                                              'Bullish':[float(temp_use.split('|')[2].replace('%','').replace(' ',''))/100],
#                                                              'Neutral':[float(temp_use.split('|')[3].replace('%','').replace(' ',''))/100],
#                                                              'Bearish':[float(temp_use.split('|')[4].replace('%','').replace(' ',''))/100]})
                                        


    
                                #find the file name under temp and read it
                                filename_temp=os.path.join(download_dir,'sentiment.xls')
                                df=pd.read_excel(filename_temp,dtype=str, sheetname='SENTIMENT', skiprows =1)
                                
                                colname=['Date','Bullish','Neutral','Bearish',
                                         'Total','Bullish 8-Week Mov Avg','Bull-Bear Spread',
                                         'Bullish Average','Bullish Average + St. Dev','Bullish Average - St. Dev','S&P 500 Weekly High',
                                         'S&P 500 Weekly Low','S&P 500 Weekly Close']
                                df.columns=colname
                                df=df[185:]
                                df=df.reset_index(drop=True)
                                remove=df.loc[df['Date']=='Observations over life of survey'].index[0]
                                df=df[0:remove]
                                df=df.loc[~(df['Date']=='nan'),:]
                                
                                df=df.reset_index(drop=True)
                                
                                df['Date']=df['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d %H:%M:%S"))
                                
                                temp=df.copy()                            
                                #df=df_connect.copy()
                                #make sure downloaded a complete csv file
                                if (df.shape[0]!=0)&(filename_temp[-3:]=='xls'): break
                            except:
                                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')
                                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')                
                
                
                if temp.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')

        no_of_trial=ii+1
        eprint(data.symbol[i],' tried ',no_of_trial,' times extraction with success','\n')
         

        
        if temp.shape[0]!=0:
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            temp.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(storage_reference,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
            temp.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            
            count=count+1
            eprint('Quandl Finance Data Extraction ',count,' out of ',quandl_source_total,'\n')
            print('Quandl Finance Data Extraction ',count,' out of ',quandl_source_total,'\n')
        else:
            eprint('Quandl Finance Data Extraction ',data.symbol[i],' not extracted','\n')
            print('Quandl Finance Data Extraction ',data.symbol[i],' not extracted','\n')



















#a=1
#for i in range(0,10):
#    try:
#        if a==1:break
#        print('doing')
#    except:
#        print('hi')


from bs4 import BeautifulSoup
import urllib.request as urllib2
from lxml import etree
import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict
import glob
import shutil


#i=2429#24142418 2425 i=2414  i=2462  i=2413  i=2468  i=2418 i=0  i=45  i=14   i=29  i=70 
#download WSJ data and save to xlsx
wsj_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='wsj'),:].shape[0]
count=0
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='wsj'):
        symbol_name=data.symbol[i]
        df=pd.DataFrame([])
        output_bigfrontbox=pd.DataFrame([])
        
        import requests
        import io
        
        count=count+1
        for ii in range(0,2):
            #clear_dir = r"C:\Users\daniellau\Dropbox\notebooks\index_analysis\wsj_csv\temp\*"
            download_dir = r"C:\Users\daniellau\Dropbox\notebooks\index_analysis\wsj_csv\temp"
            #remove this folder
            #shutil.rmtree(download_dir)
            
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            
            path_delete=r'C:\Users\daniellau\Dropbox\notebooks\index_analysis\wsj_csv\temp\HistoricalPrices.csv'
            
#            files = glob.glob(clear_dir)
#            for f in files:
#                os.remove(f)

 
            etract_link='https://www.wsj.com/market-data/quotes/'+symbol_name+'/historical-prices/download?MOD_VIEW=page&num_rows=100000&range_days=100000&startDate=01/01/1980&endDate=01/01/2100'
            try:
                if os.path.exists(path_delete):
                    os.remove(path_delete)                
                
                #download file to folder
                chrome_options = webdriver.ChromeOptions()
                preferences = {"download.default_directory": download_dir ,
                               "directory_upgrade": True,
                               "safebrowsing.enabled": True }
                chrome_options.add_experimental_option("prefs", preferences)
                driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')
                
                driver.get(etract_link)

                for iii in range(1,20):
                    sleep(1)
                    if os.path.exists(path_delete):
                        driver.close()
                        break

                #find the file name under temp and read it
                filename_temp=os.path.join(download_dir,'HistoricalPrices.csv')
                df=pd.read_csv(filename_temp)
                
                #df=df_connect.copy()
                #make sure downloaded a complete csv file
                if (df.shape[0]!=0)&(filename_temp[-3:]=='csv'): break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",symbol_name,'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",symbol_name,'\n')
        
        
        #find today price in front big box
        if (data.symbol[i][0:10]!='mutualfund'):
            for ii in range(0,2):
                etract_link='https://www.wsj.com/market-data/quotes/'+symbol_name+'/historical-prices'
                try:
    
                    #wsj is forbidden, need to use below.
                    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'none',
                           'Accept-Language': 'en-US,en;q=0.8',
                           'Connection': 'keep-alive'}
                    
                    req = urllib2.Request(etract_link, headers=hdr)
                    
                    page = urllib2.urlopen(req,timeout=7)
                    soup = BeautifulSoup(page, "html.parser")
    
    
                    if (data.Type[i]=='index'):
                        div = soup.find('span', {'class':"timestamp_value"})
                        date_value=div.text.split(' ')[-1]
                        
                        div = soup.find('li', {'class':"crinfo_quote"})
                        div = div.find('span', {'id':"quote_val"})
                        close_value=float(div.text)
        
                        div = soup.find('ul', {'class':"cr_data_collection cr_charts_info"})
                        low_value=float(div.text.split('     ')[0].replace('1 Day Range','').split('-')[0].strip())
                        high_value=float(div.text.split('     ')[0].replace('1 Day Range','').split('-')[1].strip())
                        
                        div = soup.find('div', {'class':"cr_compare_data"})
                        div=div.find('ul', {'class':"cr_data_collection"})
                        open_value=float(div.text.split('   ')[0].split(' ')[-1])
                        
                        output_bigfrontbox=pd.DataFrame(OrderedDict({'Date':[date_value],' Open':[open_value],' High':[high_value],' Low':[low_value],' Close':[close_value]}))
                    
                    if ((data.Type[i]=='stock_basic_material')|
                        (data.Type[i]=='stock_consumer_good')|
                        (data.Type[i]=='stock_financial')|
                        (data.Type[i]=='stock_service')|
                        (data.Type[i]=='stock_technology')|
                        (data.Type[i]=='ETF')|
                        (data.Type[i]=='HSI_component')|
                        (data.Type[i]=='HHI_component')):
                        
                        div = soup.find('span', {'class':"timestamp_value"})
                        date_value=div.text.split(' ')[-1]
                        
                        div = soup.find('li', {'class':"crinfo_quote"})
                        div = div.find('span', {'id':"quote_val"})
                        close_value=float(div.text)
                        
                        div = soup.find('ul', {'class':"cr_data_collection cr_charts_info"})
                        div = div.find('span', {'id':"quote_volume"})
                        volume_value=float(div.text.replace(',',''))                
        
                        div = soup.find('ul', {'class':"cr_data_collection cr_charts_info"})
                        low_value=float(div.text.split('     ')[2].replace('1 Day Range','').split('-')[0].strip())
                        high_value=float(div.text.split('     ')[2].replace('1 Day Range','').split('-')[1].strip())
                        
                        div = soup.find('div', {'class':"cr_compare_data"})
                        div=div.find('ul', {'class':"cr_data_collection"})
                        open_value=float(div.text.split('   ')[0].split(' ')[-1])                
                    
                        #note that it is very fake, wsj historical data has ' ' in Open so it is ' Open'
                        output_bigfrontbox=pd.DataFrame(OrderedDict({'Date':[date_value],' Open':[open_value],' High':[high_value],' Low':[low_value],' Close':[close_value],' Volume':[volume_value]}))
                        
                    #df=df_connect.copy()
                    #make sure downloaded a complete csv file
                    if (output_bigfrontbox.shape[0]!=0): break
                except:
                    eprint("Oops!",sys.exc_info()[0],"occured when extracting wsj bigfrontbox",symbol_name,'\n')
                    print("Oops!",sys.exc_info()[0],"occured when extracting wsj bigfrontbox",symbol_name,'\n')
        
        if output_bigfrontbox.shape[0]!=0:
            if output_bigfrontbox.Date.values[-1] not in df.Date.values.tolist():
                df=df.append(output_bigfrontbox)
                output_msg='error '+symbol_name+' , wsj historical csv has no today data so appended bigfrontbox with Date '+output_bigfrontbox.Date.values[-1]+' Open '+str(output_bigfrontbox[' Open'].values[-1])+' Close '+str(output_bigfrontbox[' Close'].values[-1])
                print(output_msg)
                eprint(output_msg)
        
    
        no_of_trial=ii+1
        eprint(symbol_name,' tried ',no_of_trial,' times extraction with success','\n')
        print(symbol_name,' tried ',no_of_trial,' times extraction with success','\n')
        
            
        if df.shape[0]!=0:
            #in wsj, there is a space before'Open'
            df.columns = df.columns.str.strip()
            
            df['Date']=df['Date'].apply(lambda x:dt.strptime(x,'%m/%d/%y'))#convert string (need to tell python string format) to datetime
            df=df.sort_values(by=['Date'],ascending=[True])
            df=df.reset_index(drop=True)
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(storage_reference,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
            df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            eprint('WSJ Finance Data Extraction ',count,' out of ',wsj_source_total,'\n')
            print('WSJ Finance Data Extraction ',count,' out of ',wsj_source_total,'\n')
        else:
            eprint('WSJ Finance Data Extraction ',symbol_name,' not extracted','\n')
            print('WSJ Finance Data Extraction ',symbol_name,' not extracted','\n')
        
        
    #dji something no data in historical wsj, so use market watch price  i=29
    if (data.Extract[i]=='Yes')&(data.Name_use_python[i]=='index_DJIA_wsj')&(data.use_cnbc[i]=='Yes'):
     #if (data.Extract[i]=='Yes')&(data.use_cnbc[i]=='Yes')&(not pd.isnull(data.use_cnbc[i])):
        output_df=pd.DataFrame([])
        for ii in range(0,2):
            try:
#                url = 'https://www.marketwatch.com/investing/'+data.market_watch_symbol[i]
#                r = requests.get(url)
#                root = LH.fromstring(r.content)
#                price_value=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]')[0].text_content() #[0] because under this xpath list only 1 element
#                price_value=float(price_value.replace(',',''))
#                
#                #read open
#                open_price_value=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "kv__item", " " ))]')[0].text_content()
#                open_price_value=float(open_price_value.replace(" ","").replace("\n","").replace("Open","").replace(",",""))
#
#                low_high_price_value=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "kv__item", " " ))]')[1].text_content()
#                low_price_value=float(low_high_price_value.replace(" ","").replace("\n","").replace("DayRange","").replace(",","").split("-")[0])
#                high_price_value=float(low_high_price_value.replace(" ","").replace("\n","").replace("DayRange","").replace(",","").split("-")[1])
#
#                
#                #format like this "Last Updated: Jan 3, 2019 4:08 p.m. HKST"
#                updated_time_raw=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "timestamp__time", " " ))]')[0].text_content()
#                result = re.search('Last Updated: (.*)', updated_time_raw).group(1)
#                result_split=result.split(",")
#                
#                year=int(result_split[1].strip()[0:4])
#                def month_converter(month):
#                    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#                    return months.index(month) + 1
#                month=month_converter(result_split[0].strip()[0:3])
#                day=[int(s) for s in result_split[0].split() if s.isdigit()][0]
#                dt_new = dt(year, month, day)
#                date_updated=dt_new.strftime('%Y-%m-%d')                
                #url='https://www.cnbc.com/quotes/?symbol='+data.cnbc_symbol[i]
                url='https://www.cnbc.com/quotes/?symbol=.DJI'
                #url='https://www.cnbc.com/quotes/?symbol=.NYA'
                
                
                page = urllib2.urlopen(url,timeout=7)
                soup = BeautifulSoup(page, "html.parser")
                
                div = soup.find('div', {'class':"Summary-subsection"})
                div=div.find_all('li')
                open_price_value=float(div[0].text.replace('Open','').replace(',',''))
                high_price_value=float(div[1].text.replace('Day High','').replace(',',''))
                low_price_value=float(div[2].text.replace('Day Low','').replace(',',''))
                price_value=float(div[3].text.replace('Prev Close','').replace(',',''))
                
                
                url='https://apps.cnbc.com/view.asp?symbol=.DJI&uid=stocks/summary'
                page = urllib2.urlopen(url,timeout=7)
                soup = BeautifulSoup(page, "html.parser")

                
                div = soup.find('div', {'class':"fontSm"})

                d_temp=div.find_all('span')[0].text
                months_all = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                find_temp_m=[x for x in months_all if x in d_temp][0]
                year_all=range(2021,2200)
                find_temp_y=[str(x) for x in year_all if str(x) in d_temp][0]
                d_temp=d_temp[d_temp.find(find_temp_m):d_temp.find(find_temp_y)+4]
                
                date_raw=d_temp.replace(',','')                
              
                date_updated=date_raw  #string
                dt_new=dt.strptime(date_updated,'%b %d %Y') #string to dt
                date_updated=dt_new.strftime('%Y-%m-%d')  #dt to string

                        
                output_df=pd.DataFrame(OrderedDict({'Date':[date_updated],'Open':[open_price_value],'High':[high_price_value],'Low':[low_price_value],'Close':[price_value]}))
                print(data.Name_use_python[i].replace('_wsj',''),'\n')
                print(output_df,'\n')
                eprint(data.Name_use_python[i].replace('_wsj',''),'\n')
                eprint(output_df,'\n')
                if output_df.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')

        no_of_trial=ii+1
        eprint(data.Name_use_python[i].replace('_wsj',''),' with backup in cnbc tried ',no_of_trial,' times extraction with success','\n')         
        print(data.Name_use_python[i].replace('_wsj',''),' with backup in cnbc tried ',no_of_trial,' times extraction with success','\n')          

        
        if output_df.shape[0]!=0:        
            #save a back up of this market watch price
            writer = pd.ExcelWriter(data.Name_use_python[i].replace('_wsj','')+'_from_cnbc.xlsx', engine='xlsxwriter')
            output_df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(storage_reference,'daily_source_data_production',data.Name_use_python[i].replace('_wsj','')+'_'+time_now_save+'_from_cnbc.xlsx'), engine='xlsxwriter')
            output_df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            
            vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
            #check2=vars()[data.Name_use_python[i]].copy()
            
            #date_updated='2019-05-23'
            #if the date in cnbc is already in wsj, then keep using wsj
            if sum(vars()[data.Name_use_python[i]]['Date2'].isin([date_updated]))>=1:
                print(data.Name_use_python[i]," wsj already have today data",'\n')
                eprint(data.Name_use_python[i]," wsj already have today data",'\n')
            else: #if not in wsj, append to wsj
                print(data.Name_use_python[i]," wsj don't have today data, now append prices from cnbc",'\n')
                eprint(data.Name_use_python[i]," wsj don't have today data, now append prices from cnbc",'\n')
                #copy last row and append it
                new_data = pd.DataFrame(vars()[data.Name_use_python[i]][-1:].values, columns=vars()[data.Name_use_python[i]].columns)
                vars()[data.Name_use_python[i]] = vars()[data.Name_use_python[i]].append(new_data)
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
                #replace last row value with market watch value
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date2']]=date_updated
                #check=vars()[data.Name_use_python[i]].copy()
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Open','High','Low','Close']]=[open_price_value,high_price_value,low_price_value,price_value]
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date']]=dt_new
            
            del vars()[data.Name_use_python[i]]['Date2']
            #check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].sort_values(by=['Date'],ascending=[True])
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            
            # Convert the dataframe to an XlsxWriter Excel object.
            vars()[data.Name_use_python[i]].to_excel(writer, sheet_name='Sheet1')
            
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
        else:
            eprint(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')
            print(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')   
















#this part is deal with 6 mutual fund, which may not be timely from wsj at morning 8:30am
#so use market watch.com, https://www.marketwatch.com
#if the date in market watch is already in wsj, then replace the price in wsj with market watch price
#if not in wsj, append to it (copy last row and replicate in wsj and then revise date,open,high...)
from bs4 import BeautifulSoup
import urllib.request as urllib2
from lxml import etree
import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict

mutual_fund_list=['OTPSX_wsj','FBGKX_wsj','HJPNX_wsj','FJSCX_wsj','TBGVX_wsj']

#i=2462  i=64
#url = 'https://w...content-available-to-author-only...h.com/investing/fund/OTPSX'
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Name_use_python[i] in mutual_fund_list)&(data.use_cnbc[i]=='Yes'):
        output_df=pd.DataFrame([])
        for ii in range(0,20):
            try:
                #url = 'https://www.marketwatch.com/investing/fund/'+data.Name_use_python[i].replace('_wsj','')

                url='https://www.cnbc.com/quotes/'+data.Name_use_python[i].replace('_wsj','')
                

                page = urllib2.urlopen(url,timeout=7)
                soup = BeautifulSoup(page, "html.parser")
                #div = soup.find('div', {'id':"structured-data"})
                div = soup.find('span', {'class':"QuoteStrip-lastPrice"})
                price_value=div.text
                price_value=float(price_value)
                
                div = soup.find('div', {'class':"QuoteStrip-lastTradeTime"})
                date_raw=div.text.split(' ')[2]
                date_updated=date_raw  #string
                dt_new=dt.strptime(date_updated,'%m/%d/%y') #dt
                date_updated=dt_new.strftime('%Y-%m-%d')
                
                

#                #use market watch price
#                price_value=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]')[0].text_content() #[0] because under this xpath list only 1 element
#                price_value=float(price_value.replace(',',''))
#                 
#                #                      '//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]'
#                #/html/body/div[2]/div[2]/div[2]/div/div/div[2]/h3/span
#                
#                #format like this "Last Updated: Jan 3, 2019 4:08 p.m. HKST"
#                updated_time_raw=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "timestamp__time", " " ))]')[0].text_content()
#                result = re.search('Last Updated: (.*)', updated_time_raw).group(1)
#                result_split=result.split(",")
#                
#                year=int(result_split[1].strip()[0:4])
#                def month_converter(month):
#                    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#                    return months.index(month) + 1
#                month=month_converter(result_split[0].strip()[0:3])
#                day=[int(s) for s in result_split[0].split() if s.isdigit()][0]
#                dt_new = dt(year, month, day)
#                date_updated=dt_new.strftime('%Y-%m-%d')
                 
                output_df=pd.DataFrame(OrderedDict({'Date':[date_updated],'Close':[price_value]}))
                print(data.Name_use_python[i].replace('_wsj',''))
                print(output_df)
                eprint(data.Name_use_python[i].replace('_wsj',''))
                eprint(output_df)
                
                if output_df.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')

        no_of_trial=ii+1
        eprint(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')         
        print(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')          

        
        if output_df.shape[0]!=0:        
            #save a back up of this cnbc price
            writer = pd.ExcelWriter(data.Name_use_python[i].replace('_wsj','')+'_from_cnbc.xlsx', engine='xlsxwriter')
            output_df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(storage_reference,'daily_source_data_production',data.Name_use_python[i].replace('_wsj','')+'_'+time_now_save+'_from_cnbc.xlsx'), engine='xlsxwriter')
            output_df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            
            vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
            #check2=vars()[data.Name_use_python[i]].copy()
            
            #date_updated='2018-12-31'
            #if the date in cnbc is already in wsj, then replace the price in wsj with cnbc price
            if sum(vars()[data.Name_use_python[i]]['Date2'].isin([date_updated]))>=1:
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Date2']==date_updated,['Open','High','Low','Close']]=price_value
            else: #if not in wsj, append to wsj
                #copy last row and append it
                new_data = pd.DataFrame(vars()[data.Name_use_python[i]][-1:].values, columns=vars()[data.Name_use_python[i]].columns)
                vars()[data.Name_use_python[i]] = vars()[data.Name_use_python[i]].append(new_data)
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
                #replace last row value with market watch value
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date2']]=date_updated
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Open','High','Low','Close']]=price_value
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date']]=dt_new
            
            del vars()[data.Name_use_python[i]]['Date2']
            #check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].sort_values(by=['Date'],ascending=[True])
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            
            # Convert the dataframe to an XlsxWriter Excel object.
            vars()[data.Name_use_python[i]].to_excel(writer, sheet_name='Sheet1')
            
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            eprint(data.Name_use_python[i].replace('_wsj',''),'from cnbc replaced wsj or merged to wsj','\n')
            print(data.Name_use_python[i].replace('_wsj',''),'from cnbc replaced wsj or merged to wsj','\n')
        else:
            eprint(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')
            print(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')            






#download data from investing.com
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd




investingdotcom_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='investing_com'),:].shape[0]
count=0
#i=2469;ii=0;i=2469  i=71
#asset='commodities/brent-oil-historical-data'
for i in range(0,len(data.symbol)):
#for i in range(2468,2472):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='investing_com'):
        final_output=pd.DataFrame([])
        asset_name=data.Name_use_python[i]
        count=count+1
        

        def extract_from_investing(start_date,end_date,asset):
#                    start_date='11/25/2009';start_date='12/31/2002';end_date='11/25/1975'
#                    start_date='12/31/2014';end_date='11/25/2019';
#                    start_date='01/01/1990';end_date='12/31/2002'
#                    start_date='12/31/2018';end_date='12/31/2040'
#                    asset='rates-bonds/euro-bobl-historical-data';asset='commodities/brent-oil-historical-data'
#                    asset=data.symbol[i];start_date='12/31/2018';end_date='12/31/2040'
            df_output=pd.DataFrame([])
            for ii in range(0,2): #max try 20 times, if one time successful, it will quit this for loop
                #because pop up window may appear faster than clicking signin button, so error occure, so need to use try, except
                aa=''
                aa_replace_all=''

                try:
                    try:
                        #browser = webdriver.Chrome(executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver79039.exe')
                        browser = webdriver.Chrome(executable_path=r'C:\Users\daniellau\Dropbox\notebooks\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')

                    except:
                        browser = webdriver.Chrome(executable_path=r'C:\Users\daniellau\Desktop\python\chromedriver770286510.exe')
                    #browser = webdriver.PhantomJS(r"C:\Users\daniellau\Desktop\python\phantomjs.exe")
                    #because if running selenium in terminal/command prompt, will get this error (chrome will hang and wait so long)
                    #ERROR:latency_info.cc(144) Surface::TakeLatencyInfoFromFrame, LatencyInfo vector size 102 is too big.
                    #but run at console, no error
                    #so set this timeout at 10s, so if hang 10s, will appear timeout error
                    #then can go to exception handling(no need wait too long)
                    browser.set_page_load_timeout(80)

                    
                    link='https://www.investing.com/ad-free-subscription/?source=desktop&medium=header_button'
                    browser.get(link)
                    

                    #webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
                    wait = WebDriverWait(browser, 30)
                    

                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userAccount"]/div/a[1]'))).click()
                    #use email to login
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginFormUser_email"]'))).send_keys('daniel.chunyuwai@gmail.com')
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm_password"]'))).send_keys('wertrolj')
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signup"]/a'))).click()

                    sleep(5)

                    link="https://www.investing.com/"+asset
                    browser.get(link) #need to wait longer time
                    sleep(5)



#                    #check if ads exist
#                    try:
#                        check1=WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[3]/a[1]"]')))
#                        ask_chinese=True
#                    except:
#                        ask_chinese=False
#                        
#                    #close ask for chinese version pop up
#                    if ask_chinese==True:
#                        try:
#                            #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[1]/a'))).click()
#                            wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[3]/a[1]'))).click()
#                        except:
#                            pass
#                
#                    #check if adas exist
#                    try:
#                        check1=WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ab-intro"]/span/i')))
#                        black_fri=True
#                    except:
#                        black_fri=False
#                        

                    #us election adhot advertisement, black friday ads
#                    try:
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div[2]/main/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div[1]'))).click()
#                    except:
#                        pass  

#                    if asset=='rates-bonds/euro-bobl-historical-data':
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="widgetFieldDateRange"]'))).click()
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="startDate"]'))).clear()
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="startDate"]'))).send_keys(start_date)
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="endDate"]'))).clear()
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="endDate"]'))).send_keys(end_date)
#                        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="applyBtn"]'))).click()
#                        #wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="results_box"]')))
#                        #sleep(6)
#                        
#                        sleep(5)
#                        
#                        hoursTable = browser.find_elements_by_xpath('//*[@id="results_box"]')
#                        aa=hoursTable[0].text
#                        
#                        
#                        from io import StringIO
#                        #import datetime
#                        aa_replace_all=aa.replace(' ','@@@')
#                        #https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
#                        first_line=aa_replace_all.find('\n') #find first newline position Date Price Open High Low Vol. Change %\n
#                        last_line=aa_replace_all.rfind('\n')
#                        aa_replace_all=aa_replace_all[(first_line+1):(last_line)]#remove first row (open high low close)
#                        browser.quit()
#                        break

                    browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                    sleep(3)
                    try:
                        wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div[1]/div[2]'))).click()
                    except:
                        pass                        
                    
                    
                    
                    #download result box

                    hoursTable = browser.find_elements_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div[5]/div/div/div[3]/div/table')
                    aa=hoursTable[0].text
                    
                    
                    from io import StringIO
                    #import datetime
                    aa_replace_all=aa.replace(' ','@@@')
                    ff=aa_replace_all.find("Change@@@%")
                    aa_replace_all=aa_replace_all[ff+10:]
                    aa_replace_all=aa_replace_all[1:]
                    
                    import re
                    temp=re.findall(r"(\d+/\d+/\d+)@@@([0-9,.]+)@@@([0-9,.]+)@@@([0-9,.]+)@@@([0-9,.]+)@@@",aa_replace_all)
                    temp=pd.DataFrame(temp)
                    aa_replace_all=temp.copy()
                    
                    browser.quit()
                    break
                except:
                    eprint("Oops!",sys.exc_info()[0],"occured when extracting ",asset_name,'\n')
                    print("Oops!",sys.exc_info()[0],"occured when extracting ",asset_name,'\n')
                    try:
                        browser.quit()
                    except:
                        pass

            if len(aa_replace_all)>0:
                eprint(asset_name,' tried ',ii+1,' times extraction with success','\n')        
                print(asset_name,' tried ',ii+1,' times extraction with success','\n')  


#                if asset=='rates-bonds/euro-bobl-historical-data':
#                    aa_replace=StringIO(aa_replace_all) 
#                 
#                    df = pd.read_csv(aa_replace, index_col=0, header=None,sep='@@@',engine='python')  
#                    df['month']=df.index
#                    df.rename(columns={1:'day',2:'year',3:'Close',4:'Open',5:'High',6:'Low',7:'vol',8:'change_percent'},inplace=True)
#                    del df['vol'];del df['change_percent']
#                    df=df.astype(str)
#                    df['day']=df['day'].apply(lambda x:x.replace(',',''))                    
#                    df['Open']=df['Open'].apply(lambda x:x.replace(',',''))
#                    df['High']=df['High'].apply(lambda x:x.replace(',',''))
#                    df['Low']=df['Low'].apply(lambda x:x.replace(',',''))
#                    df['Close']=df['Close'].apply(lambda x:x.replace(',',''))
#                    def month_converter(month):
#                        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#                        return months.index(month) + 1
#                    df['month']=df['month'].apply(lambda x:month_converter(x))
#                 
#                    df['Date'] = pd.to_datetime(df[['year','month','day']]) #datetime object
#                    df_output=df[['Date','Open','High','Low','Close']].copy()
#                    df_output=df_output.reset_index(drop=True)
#                else:
                #aa_replace=StringIO(aa_replace_all) 
             
                #df = pd.read_csv(aa_replace, index_col=0, header=None,sep='@@@',engine='python')  
                #df=df.reset_index(drop=False)
                df=aa_replace_all.copy()
                df.columns=['Date','Close','Open','High','Low']
                #del df['vol'];del df['change_percent']
                try:
                    df['Open']=df['Open'].apply(lambda x:x.replace(',',''))
                    df['High']=df['High'].apply(lambda x:x.replace(',',''))
                    df['Low']=df['Low'].apply(lambda x:x.replace(',',''))
                    df['Close']=df['Close'].apply(lambda x:x.replace(',',''))
                except:
                    pass
                df['Date']=df['Date'].apply(lambda x:dt.strptime(x,"%m/%d/%Y"))
                df_output=df[['Date','Open','High','Low','Close']].copy()
                df_output=df_output.reset_index(drop=True)
            else:
                df_output=pd.DataFrame([])

            return df_output
        
        #remember, investing.com max show 20 years data
#        first_df=extract_from_investing(start_date='01/01/1990',end_date='12/31/2002',asset=data.symbol[i])                
#        time_temp='12/31/2002' if first_df.shape[0]==0 else max(first_df['Date']).strftime('%m/%d/%Y') #convert datetime to string, need to tell string format
#        print('finished first_df\n')
#        eprint('finished first_df\n')
#        
#        second_df=extract_from_investing(start_date=time_temp,end_date='12/31/2014',asset=data.symbol[i])                
#        time_temp='12/31/2014' if second_df.shape[0]==0 else max(second_df['Date']).strftime('%m/%d/%Y') #convert datetime to string, need to tell string format
#        print('finished second_df\n')
#        eprint('finished second_df\n')
                          
        third_df=extract_from_investing(start_date='12/31/2018',end_date='12/31/2040',asset=data.symbol[i])
        #third_df=df_output.copy()
        #third_df=extract_from_investing(asset=data.symbol[i])
        print('finished third_df\n')
        eprint('finished third_df\n')
        
        #final_output=first_df.append(second_df,ignore_index=True)
        #final_output=final_output.append(third_df,ignore_index=True)
        final_output=third_df.copy()
        
        #below if loop is out of above second for loop
        if final_output.shape[0]!=0:
            final_output2=final_output.drop_duplicates(subset='Date',keep='last')
            final_output2=final_output2.sort_values(by=['Date'],ascending=[True])
            final_output2=final_output2.reset_index(drop=True)
            
            #for futures, need to append to cum file
            cumulated_data = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')            
            final_output2=cumulated_data.append(final_output2)
            final_output2=final_output2.drop_duplicates(subset='Date',keep='last')
            final_output2['Open']=final_output2['Open'].astype(float)
            final_output2['High']=final_output2['High'].astype(float)
            final_output2['Low']=final_output2['Low'].astype(float)
            final_output2['Close']=final_output2['Close'].astype(float)
            final_output2=final_output2.reset_index(drop=True)
            
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            final_output2.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(storage_reference,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
            final_output2.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            eprint('Investing.com Finance Data Extraction ',asset_name,' ',count,' out of ',investingdotcom_source_total,'\n')
            print('Investing.com Finance Data Extraction ',asset_name,' ',count,' out of ',investingdotcom_source_total,'\n')
        else:
            eprint('Investing.com Finance Data Extraction ',asset_name,' not extracted/no data','\n')
            print('Investing.com Finance Data Extraction ',asset_name,' not extracted/no data','\n')
            






#this part is deal with 6 currency, which may not be timely from quandl at morning
#so download from euro central bank

from lxml import etree
import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict

#i=16
#url = 'https://w...content-available-to-author-only...h.com/investing/fund/OTPSX'
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='ECB')&(data.Type[i]=='currency'):
        output_df=pd.DataFrame([])
        for ii in range(0,20):
            try:
                request_link = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip?569f4e99b9b6e812e780f2dc232f1843'
                #url=request_link
                def fetch_multi_csv_zip_from_url(url, filenames=(), *args, **kwargs):
                    assert kwargs.get('compression') is None
                    req = urlopen(url,timeout=7)
                    zip_file = zipfile.ZipFile(BytesIO(req.read()))
                
                    if filenames:
                        names = zip_file.namelist()
                        for filename in filenames:
                            if filename not in names:
                                raise ValueError(
                                    'filename {} not in {}'.format(filename, names))
                    else:
                        filenames = zip_file.namelist()
                
                    return {name: pd.read_csv(zip_file.open(name), *args, **kwargs)
                            for name in filenames}
                    
                try:
                    from urllib.request import urlopen
                except ImportError:
                    from urllib2 import urlopen
                from io import BytesIO
                import zipfile
                import pandas as pd
                
                dfs = fetch_multi_csv_zip_from_url(request_link)
                output_df=dfs['eurofxref-hist.csv']
    
                if output_df.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i],'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i],'\n')

        no_of_trial=ii+1
        eprint(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')         
        print(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')          

        
        if output_df.shape[0]!=0:        
            output_df2=output_df[['Date',data.Name_use_python[i][-3:]]].copy()
            output_df2=output_df2.rename(columns={data.Name_use_python[i][-3:]:'Value'})
            
            output_df2['Date']=output_df2['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
            
            output_df2=output_df2.sort_values(by=['Date'],ascending=[True])
            output_df2=output_df2.reset_index(drop=True)
            
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            
            # Convert the dataframe to an XlsxWriter Excel object.
            output_df2.to_excel(writer, sheet_name='Sheet1')
            
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(storage_reference,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
            output_df2.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            
            
            eprint(data.Name_use_python[i],'from euro central bank downloded','\n')
            print(data.Name_use_python[i],'from euro central bank downloded','\n')
        else:
            eprint(data.Name_use_python[i],'no data from euro central bank','\n')
            print(data.Name_use_python[i],'no data from euro central bank','\n')       








































#merge with data_back_up_20180420, not include HSI, HSI made above
#i=2422   i=75   i=23
cumulated_data_folder='data_back_up_20210319'
cumulated_data_folder_path=os.path.join(target_dir,cumulated_data_folder)

total_extract_yes=data.loc[(data['Extract']=='Yes')&(data['Name_use_python']!='HSI')&(data['Name_use_python']!='hang_seng_oi'),:].shape[0]
count=0
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Name_use_python[i]!='HSI'):
        cumulated_data_path=os.path.join(cumulated_data_folder_path,data.Name_use_python[i]+'.xlsx')
        count=count+1
        if os.path.exists(cumulated_data_path):
            #print(i)
            cumulated_data = read_excel(cumulated_data_path,'Sheet1')
            cumulated_data=cumulated_data.sort_values(by='Date',ascending=True)
            cumulated_data=cumulated_data.reset_index(drop=True)
            cumulated_data_latest_date=cumulated_data.loc[cumulated_data.shape[0]-1,['Date']][0]
            #cumulated_data=cumulated_data.loc[cumulated_data['Date']<=cumulated_data_latest_date,:]
            
            latest_data_path=os.path.join(target_dir,data.Name_use_python[i]+'.xlsx')
            latest_data = read_excel(latest_data_path,'Sheet1')
            #find the latest date on backup file, and merge all date greater than latest date to it
            latest_data=latest_data.loc[latest_data['Date']>cumulated_data_latest_date,:]
    
            #merge together
            all_data=pd.concat([cumulated_data,latest_data],axis=0)
            all_data=all_data.reset_index(drop=True)
    
            #save file
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            all_data.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()

            eprint('Merge with '+cumulated_data_folder+' ',count,' out of ',total_extract_yes,'\n')
            print('Merge with '+cumulated_data_folder+' ',count,' out of ',total_extract_yes,'\n')
        









##quandl FHSI only start from 2017-07-16 so need to merge to
##FHSI_20051201to2020180413.xlsx
##,whcih is merge manually by fhsi_from_optionwalker_from20061228to20180413.xlsx #https://www.optionwalker.com/sharings
##and FHSI20051104-20131209 Daily_investigate.xlsx #long time ago from wilson
#from pandas import read_excel
#import pandas as pd
#import os
#import numpy as np
#fhsi_previous_path=os.path.join(target_dir,'data','FHSI_20051201to2020180413.xlsx')
#fhsi_previous = read_excel(fhsi_previous_path,'Sheet1')
#fhsi_previous=fhsi_previous.sort_values(by='Date',ascending=True)
#fhsi_previous=fhsi_previous.reset_index(drop=True)
#
#fhsi_latest_path=os.path.join(target_dir,'HSI.xlsx')
#fhsi_latest = read_excel(fhsi_latest_path,'Sheet1')
#
##if first time dowmload HSI in morning, 'Prev. Day Settlement Price' in columns
#if 'Prev. Day Settlement Price' in list(fhsi_latest.columns.values):
#    fhsi_latest=fhsi_latest.rename(columns={'Prev. Day Settlement Price':'Close'})
#    
##after first time dowmload HSI in morning,'Settle' in columns 
#if 'Settle' in list(fhsi_latest.columns.values):
#    fhsi_latest=fhsi_latest.rename(columns={'Settle':'Close'})
#
#
#fhsi_latest['Date2']=fhsi_latest['Date'].astype(str)
#fhsi_latest_use=fhsi_latest[['Date','Date2','Open','High','Low','Close']].copy()
#
#fhsi_latest_use=fhsi_latest_use.loc[fhsi_latest_use['Date']>'2018-04-01',:]
#del fhsi_latest_use['Date2']
#fhsi_latest_use=fhsi_latest_use.reset_index(drop=True)
#
#fhsi_new=pd.concat([fhsi_previous,fhsi_latest_use],axis=0)
#fhsi_new.drop_duplicates(subset='Date',inplace=True)
#fhsi_new=fhsi_new.reset_index(drop=True)
#
#fhsi_new=fhsi_new.rename(columns={'Close':'Settle'})
#
#output_path=os.path.join(target_dir,'HSI.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
## Convert the dataframe to an XlsxWriter Excel object.
#fhsi_new.to_excel(writer, sheet_name='Sheet1')
## Close the Pandas Excel writer and output the Excel file.
#writer.save()









#############################
########Production Mode######
#############################
#production mode will create a new row, which is new_date defined below
#so that factor value can be merged for predicting 
#in this new row, close is 101, open is 100, pnl is 1 only so less effect if this
#included in backtest mistakenly. note this this row just dummy and fake
            
production_mode=True






if production_mode==True:
    currentDay = dt.now().day
    currentMonth = dt.now().month
    currentYear = dt.now().year
    new_date=dt(currentYear,currentMonth,currentDay)
    hsi_old=read_excel('HSI'+'.xlsx','Sheet1')
    #in yahoo finance, say now is 6/4/2018 morning 8:30am
    #HSI already has row 6/4/2018 but value is fake, the same as previous day
    #so remove it and just assign 100 to it.
    hsi_old=hsi_old.loc[hsi_old['Date']!=new_date,:]
    hsi_old=hsi_old.append({'Date':new_date,'Open':100,'High':100,'Low':100,'Close':101}, ignore_index=True)
    hsi_old=hsi_old.reset_index(drop=True)
    writer = pd.ExcelWriter('HSI'+'.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    hsi_old.to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    writer.close()
    








#############################
########Merge Date###########
#############################
#this part is to create xxx_with_tidy.xlsx file inside is %change or absolute change for interest rate
#%reset -f
#暫時由呢度開始run read data, 上面係抽數, 抽完save as xlsx
import os
import numpy as np
os.chdir(r'C:\Users\daniellau\Dropbox\notebooks\index_analysis')

from pandas import read_excel
data = read_excel('index_table_v2_for_test.xlsx','Sheet1')
from datetime import datetime as dt
import datetime
import pandas as pd

import time



##read calendar
#calendar = read_excel(r'C:\Users\daniellau\Dropbox\notebooks\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
#calendar['Date2']=calendar['Date'].astype(str)
#calendar=calendar.loc[calendar['trading_date']==1,:]
#calendar=calendar.reset_index(drop=True)
#
#settlement = read_excel(r'C:\Users\daniellau\Dropbox\notebooks\index_analysis\daily_prediction_production\calendar.xlsx','settlement')
#settlement['settlement_day2']=settlement['settlement_day'].astype(str)





#i=274
#check whether date is distinct
#sometime in the morninng, in STI (singapore index), latest day will be the same as second last day with equal value
#may be yahoo not updated it, so remove duplicate in xxx_with_tidy.xlsx version
for i in range(0,len(data.symbol)):
    if data.Merge_tgh[i]=='Yes':
        vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
        vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
        vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
        unique_count=len(vars()[data.Name_use_python[i]]['Date2'].unique())
        date_count=vars()[data.Name_use_python[i]].shape[0]
        
        #find duplicated date
        check=vars()[data.Name_use_python[i]]['Date2'].value_counts()
        check_date=check[check>1].index.tolist()
        
        #store dupicated date row to output
        check2=vars()[data.Name_use_python[i]]['Date2'].isin(check_date)
        output=vars()[data.Name_use_python[i]][check2]
        if unique_count!=date_count:
            eprint('date in ',data.Name_use_python[i],' not distinct','\n')
            print('date in ',data.Name_use_python[i],' not distinct','\n')
            eprint(output)
            print(output)
        else:
            eprint('date in ',data.Name_use_python[i],' distinct','\n')
            print('date in ',data.Name_use_python[i],' distinct','\n')





#i=274
#i=2468#676
#read index price
merge_total=data.loc[(data['Merge_tgh']=='Yes'),:].shape[0]
count=0
for i in range(0,len(data.symbol)):
    if data.Merge_tgh[i]=='Yes':
        #vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
        #vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
        #vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
        #HSI_check=HSI
        print('Doing ',data.Name_use_python[i],'\n')
        if (data.Source[i]=='Yahoo')&(data.symbol[i]!='^HSI'):
            
            if data.Type[i][0:2]=='MF': #for mutual fund, open high low close all equal so need to assign open as close shift 1
                #remove row if open or close price isnan
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
                #HSI_check=HSI
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
                vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]].shift(1)
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].dropna(how='any')
            else:
                #remove row if open or close price isnan
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
                #HSI_check=HSI
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        
        #if HSI_index, also output volumn
        if (data.Source[i]=='Yahoo')&(data.symbol[i]=='^HSI'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i],'Volume':'Volume_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i],'Volume_'+data.Name_use_python[i]]]
        if (data.Source[i]=='Quandl') & (data.symbol[i]=='CHRIS/HKEX_HSI1'): #this is FHSI
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Settle)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]


        if (data.Source[i]=='hkex') & (data.symbol[i]=='hkex_symbol'): #this is FHSI from hkex
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi'): #this is hsi_oi from hkex
            
#            a_check=vars()[data.Name_use_python[i]].copy()
#            
#            #for 4 days before settlement day and include settlement day, try to remove these row
#            #because OI always drop, may not be indicative.
#            
#            all_date_oi=pd.DataFrame(a_check.loc[a_check['Date']<='2019-01-02','Date2'].copy())
#            date_after20190102=pd.DataFrame(calendar.loc[:,'Date2'].copy())
#            all_date_oi=all_date_oi.append(date_after20190102)
#
#            #find trading contract for each trading date
#            all_date_oi_list=all_date_oi['Date2'].values.tolist()
#            all_settlement_list=settlement['settlement_day2'].values
#            all_date_oi_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_oi_list]
#            all_date_oi['settlement_contract']=all_date_oi_found_settlement
#            all_date_oi=all_date_oi.reset_index(drop=True)
#            
#            
#            #indicate 5 days including trading date
#            x=all_date_oi.loc[all_date_oi['settlement_contract']=='2006-01-26',:]
#            def indicate1(x):
#                x['indicate']=0
#                x.iloc[-5:,-1]=1
#                output=pd.Series(x.iloc[:,-1],index=x.index)
#                return output
#            all_date_oi['indicate']=all_date_oi.groupby(['settlement_contract'],group_keys=False).apply(lambda x:indicate1(x))
#            
#            all_date_oi_remove=all_date_oi.loc[all_date_oi['indicate']==1,'Date2'].values.tolist()
#            
#            a_check['remove']=a_check['Date2'].apply(lambda x:'yes' if x in all_date_oi_remove else 'no')
#            a_check=a_check.loc[a_check['remove']=='no',:]
#            del a_check['remove']
#            
#            vars()[data.Name_use_python[i]]=a_check.copy()
            
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].OI)|np.isnan(vars()[data.Name_use_python[i]].OI_lag1)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'OI_lag1':'Open_'+data.Name_use_python[i],'OI':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi_volume'): #this is hsi_oi volume
            
            a_check=vars()[data.Name_use_python[i]].copy()
            #remove row if open or close price isnan
            
            vars()[data.Name_use_python[i]]['Volume_lag1']=vars()[data.Name_use_python[i]]['Volume'].shift(1)
            
            
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Volume_lag1)|np.isnan(vars()[data.Name_use_python[i]].Volume)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Volume_lag1':'Open_'+data.Name_use_python[i],'Volume':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
            


        
        if (data.Source[i]=='Quandl') & (data.symbol[i][0:5]=='CHRIS')&(data.Type[i]=='commodity'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Settle)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        if (data.Source[i]=='ECB') & (data.symbol[i][0:3]=='ECB'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]].Value),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Value'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Value']
            del vars()[data.Name_use_python[i]]['Date']
            del vars()[data.Name_use_python[i]]['Value']
        if (data.Source[i]=='Quandl') & (data.symbol[i]=='USTREASURY/REALLONGTERM'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)']),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)']
            del vars()[data.Name_use_python[i]]['Date']
            del vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)']
            
        if (data.Source[i]=='Quandl') & (data.symbol[i][0:20]=='USTREASURY/REALYIELD'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]][str(int(data.Year[i]))+' YR']),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+' YR'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+' YR']
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]].copy()

        if (data.Source[i]=='Quandl') & (data.symbol[i]=='MOFJ/INTEREST_RATE_JAPAN'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]][str(int(data.Year[i]))+'Y']),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+'Y'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+'Y']
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]].copy()
      
        if (data.Source[i]=='Quandl') & (data.Type[i]=='bond_futures'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Settle)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Open']#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Settle']
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]].copy()

        if (data.Source[i]=='Quandl') & (data.symbol[i]=='AAII/AAII_SENTIMENT'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Bearish)|np.isnan(vars()[data.Name_use_python[i]].Bullish)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Bearish':'Open_'+data.Name_use_python[i],'Bullish':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]


                
        if data.Source[i]=='analystz':
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        
        if data.Source[i]=='Custom':
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        if (data.Source[i]=='wsj')&(data.Type[i][0:2]=='MF'):
            #for mutual fund, open high low close all equal so need to assign open as close shift 1
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]].shift(1)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].dropna(how='any')        
        if (data.Source[i]=='wsj')&(data.Type[i][0:2]!='MF'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i],'Volume':'Volume_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i],'Volume_'+data.Name_use_python[i]]]
        
        if (data.Source[i]=='investing_com'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
            
            #for futures like brent oil and gold, if on monday morning perform extraction, it will include sunday night price,
            #as the market open at night
            #but investing.com will remove sunday later in historical data, so i also remove sunday price
            #using isoweekday, 7 is sunday
            key=vars()[data.Name_use_python[i]]['Date2'].apply(lambda x:dt.strptime(x,'%Y-%m-%d').isoweekday())!=7
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][key]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            
            
        #make % change column
        #for interst rate, sometimes it is zero (% change will be inf) and even if not zero, 
        #% change would be very big, so use absolute change
        if ((data.symbol[i]=='USTREASURY/REALLONGTERM')|(data.symbol[i][0:20]=='USTREASURY/REALYIELD')|(data.symbol[i]=='MOFJ/INTEREST_RATE_JAPAN')):
            vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]-vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]
        else:
            vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']=(vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]-vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]])/vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]
        
        #special made for AAII/AAII_SENTIMENT, if one of bull or bear >0.5, use bull-bear as factor
        if (data.Source[i]=='Quandl') & (data.symbol[i]=='AAII/AAII_SENTIMENT'):
            vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]>=0.5)|(vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]>=0.5),'indicator_greater05']=1
            vars()[data.Name_use_python[i]]['indicator_greater05']=vars()[data.Name_use_python[i]]['indicator_greater05'].fillna(0)
            vars()[data.Name_use_python[i]]['AAII_sentiment_Bull_minor_bear_change']=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]-vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]
            vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']=vars()[data.Name_use_python[i]]['AAII_sentiment_Bull_minor_bear_change']*vars()[data.Name_use_python[i]]['indicator_greater05']
            #check=vars()[data.Name_use_python[i]].copy()
        


        #if open price is zero, print out
        if(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0].shape[0]>0):
            eprint('open is zero')
            eprint(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0])
            print('open is zero')
            print(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0])
        
        #if %change>200% or change>2 (for interest rate), print out
        if ((data.symbol[i]=='USTREASURY/REALLONGTERM')|(data.symbol[i][0:20]=='USTREASURY/REALYIELD')):
            eprint(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>=2])
            print(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>=2])     
        
        
        
        #CHRIS_com_CME_HG1 in 2011-06-21, open price is 0, which is wrong, so delete these cases (7 rows)
        if (data.Name_use_python[i]=='CHRIS_com_CME_HG1'):
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0),:]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
        #0005, 2010-04-07 open price is wrong, so remove this row
        if (data.Name_use_python[i]=='0005_HK'):
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(vars()[data.Name_use_python[i]]['Date2']=='2010-04-07'),:]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            

            
        #create DateNum
        vars()[data.Name_use_python[i]]['Date3']=pd.to_datetime(vars()[data.Name_use_python[i]]['Date2'])#create a date with datetime format
        vars()[data.Name_use_python[i]]['DateNum'] = (vars()[data.Name_use_python[i]].Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
        vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
        del vars()[data.Name_use_python[i]]['Date3']
        
        #FCHI_check=FCHI.tail(100)
        #remove duplicate if date2 are the same, but keep the first record
        vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].drop_duplicates(subset='Date2', keep="first")
        



        #remove settlement day and one date after it for volume
        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi_volume'):   
#            calendar = read_excel(r'C:\Users\daniellau\Dropbox\notebooks\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
#            calendar['Date2']=calendar['Date'].astype(str)
#            calendar=calendar.loc[calendar['trading_date']==1,:]
#            calendar['Settlement_after_one']=calendar['Settlement_date'].shift(1)
#            remove_date=calendar.loc[calendar['Settlement_after_one']==1,'Date2'].values.tolist()
#            remove_date_df=pd.DataFrame({'Date2_remove':remove_date})
#            
#            a_check=vars()[data.Name_use_python[i]].copy()
#            vars()[data.Name_use_python[i]]=pd.merge(vars()[data.Name_use_python[i]],remove_date_df[['Date2_remove']].copy(),how='left',left_on=['Date2'],right_on=['Date2_remove'])            
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[pd.isnull(vars()[data.Name_use_python[i]]['Date2_remove']),:]
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
#            
#            del vars()[data.Name_use_python[i]]['Date2_remove']


            settlement_day = read_excel('daily_prediction_production/calendar.xlsx','settlement')
            settlement_day['Date2']=settlement_day['settlement_day'].astype(str)      
            settlement_day['settlement']=1
            
            tradeday_before20181224=read_excel('daily_prediction_production/calendar.xlsx','tradingdate_before20181227')
            calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar')
            calendar['Date2']=calendar['Date'].astype(str)
            calendar=calendar.loc[calendar['trading_date']==1,:]  
            
            all_trading_date=tradeday_before20181224.append(calendar[['Date2']])
            all_trading_date=all_trading_date.reset_index(drop=True)
            
            all_trading_date=pd.merge(all_trading_date,settlement_day[['Date2','settlement']].copy(),how='left',on=['Date2'])
            all_trading_date['settlement']=all_trading_date['settlement'].fillna(0)
            
            all_trading_date['s1']=all_trading_date['settlement'].shift(1)
            #all_trading_date['s2']=all_trading_date['settlement'].shift(-2)
            #all_trading_date['s3']=all_trading_date['settlement'].shift(-3)
            all_trading_date=all_trading_date.fillna(0)
            all_trading_date['one']=all_trading_date['settlement']+all_trading_date['s1']#+all_trading_date['s2']+all_trading_date['s3']
            
            
            vars()[data.Name_use_python[i]]=pd.merge(vars()[data.Name_use_python[i]],all_trading_date[['Date2','one']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])            
            
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['one']==0,:]
            #vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['one']==1,'hang_seng_oi_change']=0
            a_check=vars()[data.Name_use_python[i]].copy()

            
            
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)






        
        ###check abnormal "% change" (may be in one date before trading day, some asset not updated previous date's price
        #and return 0 in open price, so change is inf (e.g. CHRIS_bond_EUREX_FGBM1_20181227.xlsx)
        if (vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5),:].shape[0]>0):
            eprint('abnormal change >5 or <-5')
            eprint(vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5),:])
            print('abnormal change >5 or <-5')
            print(vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5),:])
            #remove abnormal change row
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~((vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5)),:]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)        

  
    
        writer = pd.ExcelWriter(data.Name_use_python[i]+'_with_tidy.xlsx', engine='xlsxwriter')
        vars()[data.Name_use_python[i]].to_excel(writer, sheet_name='Sheet1')
        writer.save()
        writer.close()
        count=count+1
        eprint('finished' ,count,'which is',' ',data.Name_use_python[i],' out of ',merge_total,'\n')
        print('finished' ,count,'which is',' ',data.Name_use_python[i],' out of ',merge_total,'\n') 
        




#logging.shutdown()






#create dependent variable Y
hsi_y=HSI.loc[:,['Date2','DateNum','Open_HSI','Close_HSI']]
hsi_y['Y_up']=hsi_y.apply(lambda row: (row.Close_HSI>=row.Open_HSI)*1,axis=1)
hsi_y['Y_down']=hsi_y.apply(lambda row: (row.Close_HSI<row.Open_HSI)*1,axis=1)

writer = pd.ExcelWriter('hsi_y.xlsx', engine='xlsxwriter')
hsi_y.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()









#############################
#######create factors########
#############################

import os
import datetime
import numpy as np
from numpy import inf
import time
import pandas as pd
from datetime import datetime as dt
os.chdir(r'C:\Users\daniellau\Dropbox\notebooks\index_analysis')
time_start=time.time()

from pandas import read_excel
data = read_excel('index_table_v2_for_test.xlsx','Sheet1')
hsi_y = read_excel('hsi_y.xlsx','Sheet1')

use_list=[data.Name_use_python[i] for i in range(0,len(data.symbol)) if data.Merge_tgh[i]=='Yes']
if 'HSI' in use_list:
    use_list.remove('HSI')

    

hsi_x=hsi_y.loc[:,['Date2','DateNum']]
hsi_x_store_closest=hsi_y.loc[:,['Date2','DateNum']] 
#i=53
#vars()[use_list[i]] = read_excel(use_list[i]+'_with_tidy.xlsx','Sheet1')
#appear=vars()[use_list[i]]
#one_date=9306
#target_data=appear
#this function is to read the closest date before that hsi trading date
#for example, if today is 2017-11-09, use assest %change in uk/eu market on 2017-11-08 
def find_closest_datenum(one_date,target_data):
    b=one_date-target_data['DateNum']
    min_diff=b[b>0].min()
    closest_datenum=one_date-min_diff
    return closest_datenum

#one_date=hsi_x['DateNum']
#target_data=vars()[use_list[53]]
def find_closest_datenum2(one_date,target_data):
    rep=target_data.shape[0]
    one_date=one_date.values #this is array
    one_date2=np.repeat(one_date,rep)
    target_data_np=np.tile(target_data['DateNum'].values,one_date.shape[0])
    b=one_date2-target_data_np

    ind=b>0
    one_date2=one_date2[ind]
    b=b[ind]
    
    db=pd.DataFrame({'one_date2':one_date2,'b':b})
    db_out=db.groupby(['one_date2'])['b'].min() #this is series
    
    if len(db_out)!=len(one_date):
        r=len(one_date)-len(db_out)
        zeroo=np.zeros(r);zeroo.fill(np.nan)
        db_out2=np.vstack((np.reshape(zeroo,(r,1)),db_out.values.reshape(len(db_out),1)))
        closest_datenum=one_date-db_out2.reshape(len(db_out2),)
    else:
        closest_datenum=one_date-db_out.values #values convert series to array
    
    return closest_datenum


#i='index_HK_XHKG_HSI_wsj'
#i='euro_bobl_investing'
count=0
for i in use_list:
    vars()[i] = read_excel(i+'_with_tidy.xlsx','Sheet1')
    appear=vars()[i]
    col_name=i+'_closest_datenum'
    #hsi_x[col_name]=hsi_x.apply(lambda row: find_closest_datenum(row['DateNum'],appear),axis=1)
    hsi_x[col_name] = find_closest_datenum2(hsi_x['DateNum'],appear)  
    
    
    hsi_x_store_closest[col_name+'_diff']=hsi_x['DateNum']-hsi_x[col_name]
    hsi_x_store_closest[col_name]=hsi_x[col_name].copy()
    
    hsi_x=pd.merge(left=hsi_x,right=appear[['DateNum',i+'_change']],how='left',left_on=col_name,right_on='DateNum')
    del hsi_x['DateNum_y']
    hsi_x=hsi_x.rename(columns={'DateNum_x':'DateNum'})
    
    # if not daily data, say monthly data, this data only use for one day, and other 0
    hsi_x[col_name+'first_factor_indicate']=hsi_x[col_name].shift(1)!=hsi_x[col_name]
    hsi_x[i+'_change']=hsi_x[i+'_change']*hsi_x[col_name+'first_factor_indicate']
    
    del hsi_x[col_name]
    del hsi_x[col_name+'first_factor_indicate']
    
    count=count+1
    print('finished change factor ',count,' out of ',len(use_list),'\n')
#hsi_x2=hsi_x.copy()
#sum(hsi_x2['PNC_closest_datenum']==hsi_x['PNC_closest_datenum'])
#if column A only has data starting from (say 2005-01-02) and hsi first day (say 1991-01-02), value within this period
#will be nan
hsi_x=hsi_x.fillna(0)
hsi_x_store_closest=hsi_x_store_closest.fillna(0)
hsi_x.isnull().any().any()


use_list_closest_diff=[x+'_closest_datenum_diff' for x in use_list]
use_list_closest_diff2=['Date2','DateNum']+use_list_closest_diff
hsi_x_store_closest_investigate=hsi_x_store_closest[use_list_closest_diff2].copy()

value_matrix=hsi_x_store_closest_investigate[use_list_closest_diff].as_matrix()
hsi_x_store_closest_investigate['1_counts']=(value_matrix==1).sum(axis=1)
hsi_x_store_closest_investigate['2_counts']=(value_matrix==2).sum(axis=1)
hsi_x_store_closest_investigate['3_counts']=(value_matrix==3).sum(axis=1)
hsi_x_store_closest_investigate['4_counts']=(value_matrix==4).sum(axis=1)
hsi_x_store_closest_investigate['5_counts']=(value_matrix==5).sum(axis=1)
hsi_x_store_closest_investigate['6_counts']=(value_matrix==6).sum(axis=1)
hsi_x_store_closest_investigate['6_greater_counts']=(value_matrix>6).sum(axis=1)

#save hsi_x_store_closest
temp_path=os.path.join(storage_reference,'daily_source_data_production','hsi_x_store_closest_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'_production.xlsx')
writer = pd.ExcelWriter(temp_path, engine='xlsxwriter')
hsi_x_store_closest_investigate.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


#find closest 20 day
hsi_x_store_closest_investigate_see=hsi_x_store_closest_investigate.tail(20).T
investigate_see_name=os.path.join(storage_reference,'daily_source_data_production','hsi_x_store_closest_transpose_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'_production.xlsx')
writer = pd.ExcelWriter(investigate_see_name, engine='xlsxwriter')
hsi_x_store_closest_investigate_see.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

#output to log file for last 20 rows
#logger.info(hsi_x_store_closest_investigate.tail(10).transpose())




data1=pd.DataFrame({'Datenum':[17363,17000],'nfp': [0,5]}) 
ema_custom_v2(data1,'Datenum','nfp',120)

hsi_x_temp=hsi_x.copy()  
#hsi_x_temp['Date3']=pd.to_datetime(hsi_x_temp['Date2'])#create a date with datetime format
#hsi_x_temp['DateNum'] = (hsi_x_temp.Date3-datetime.date(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#hsi_x_temp=hsi_x_temp.sort_values(by='DateNum',ascending=False)
#hsi_x_temp=hsi_x_temp.reset_index(drop=True)

#for hong kong stock, use ema up to yesterday as a forcast of today's %change
#
#i=2473
count=0
for i in range(0,len(data.symbol)):
    total=sum((data['UseEMA']=='Yes')&(data['Merge_tgh']=='Yes'))
    if (data.UseEMA[i]=='Yes')&(data.Merge_tgh[i]=='Yes'):
        vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'_with_tidy.xlsx','Sheet1')
        
        a_check=vars()[data.Name_use_python[i]].copy()
        
        appear=vars()[data.Name_use_python[i]].sort_values(by='DateNum',ascending=False).reset_index(drop=True)
        appear=appear[['Date2',data.Name_use_python[i]+'_change','DateNum']].copy()
        #in the first date, change is Nan, so need to remove this row, and now as it is sorted, so it is last row
        #appear=appear[0:appear.shape[0]-1]
        target_col=data.Name_use_python[i]+'_change'
        
        for ema_decay in [15,30]:
#            ema_decay=30#30
#            if data.Name_use_python[i]=='hang_seng_oi':
#                ema_decay=5
                
    
    
            count=count+1
            print('finished EMA ',count,' out of ',total,'\n')









hsi_y_x=pd.merge(left=hsi_y[['Date2','Y_up','Y_down']],right=hsi_x,how='left',on=['Date2'])
#hsi_y_x_check=pd.merge(left=hsi_y[['Date2','Y_up','Y_down']],right=hsi_x,how='left',on=['Date2'])
#hsi_y_x=hsi_y_x.loc[hsi_y_x['Date2']>='1991-01-04',:]
#hsi_y_x=hsi_y_x.dropna(how='any')
hsi_y_x=hsi_y_x[1:hsi_y_x.shape[0]]
hsi_y_x=hsi_y_x.reset_index(drop=True)

hsi_y_x.isnull().any().any()


time_end=time.time()
print('total time of creating factors is ',round((time_end-time_start)/60,4),' mins')

use_list_dataframe=pd.DataFrame({'factor_name':use_list})
#factor statistic/quality
colname='N225_change'
s=use_list_dataframe
def factor_stat(s):
    colname=s['factor_name']+'_change'
    
    #first inception date
    temp_array=np.array(hsi_x[colname],dtype=pd.Series).astype(np.float)
    r=0 if len(np.where(temp_array!=0)[0])==0 else min(np.where(temp_array!=0)[0])
    first_factor_date = hsi_x.loc[r,'Date2']
    
    #closeast date different, return max and min
    colname=s['factor_name']+'_closest_datenum'+'_diff'
    closest_date_max=hsi_x_store_closest[colname].max()
    closest_date_min=hsi_x_store_closest[colname][hsi_x_store_closest[colname]>0].min()
    
    return pd.Series({'first_factor_date':first_factor_date, 'closest_date_max': closest_date_max,'closest_date_min':closest_date_min})
    #return [first_factor_date,closest_date_min,closest_date_max]
use_list_dataframe = use_list_dataframe.merge(use_list_dataframe.apply(factor_stat, axis=1), left_index=True, right_index=True)
#use_list_dataframe[['factor_inception_date','closest_date_min','closest_date_max']]=use_list_dataframe.apply(factor_stat,axis=1)

#list(hsi_x.columns.values).index('AMT_change')






writer = pd.ExcelWriter('use_list_dataframe'+'.xlsx', engine='xlsxwriter')
use_list_dataframe.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()




























#create hsi oi 4 factors
oi_original= read_excel('hang_seng_oi'+'_with_tidy.xlsx','Sheet1')

oi_original=oi_original.sort_values(by='DateNum',ascending=False).reset_index(drop=True)
oi_original=pd.merge(oi_original,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
                      on=['Date2'],how='left')

oi_original['diff']=oi_original['Close_HSI']-oi_original['Open_HSI']

#latest method
oi_original.loc[(oi_original['diff']>=0),'hang_seng_oi_change_revised1']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised1']=oi_original['hang_seng_oi_change_revised1'].fillna(0)
oi_original.loc[(oi_original['diff']<0),'hang_seng_oi_change_revised2']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised2']=oi_original['hang_seng_oi_change_revised2'].fillna(0)

oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']>=0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']<0)),'hang_seng_oi_change_revised3']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised3']=oi_original['hang_seng_oi_change_revised3'].fillna(0)
oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']<0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']>=0)),'hang_seng_oi_change_revised4']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised4']=oi_original['hang_seng_oi_change_revised4'].fillna(0)



target_table=oi_original.copy()


for f_name in ['hang_seng_oi_change_revised1','hang_seng_oi_change_revised2',
               'hang_seng_oi_change_revised3','hang_seng_oi_change_revised4']:
    for ema_decay in [5]:
        #f_name='hang_seng_oi_change_revised2'
        appear=target_table[['Date2',f_name,'DateNum']].copy()
        target_col=f_name
        
        #ema_decay=2
            






#test hang_seng_oi and volume

oi_original= read_excel('hang_seng_oi'+'_with_tidy.xlsx','Sheet1')
oi_original['year']=oi_original['Date2'].apply(lambda x:int(x[0:4]))


oi_original=oi_original.sort_values(by='DateNum',ascending=False).reset_index(drop=True)
oi_original=pd.merge(oi_original,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
                      on=['Date2'],how='left')

oi_original['diff']=oi_original['Close_HSI']-oi_original['Open_HSI']






#volume
table_name='hang_seng_oi_volume_use_year_mean'
hsi_vol=hang_seng_oi_volume.copy()
hsi_vol['year']=hsi_vol['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)

hsi_vol=pd.merge(hsi_vol,vars()[table_name],how='left',left_on=['year'],right_on=['year_plus_one'])

hsi_vol.columns.values

asset_name='hang_seng_oi_volume'
hsi_vol.loc[hsi_vol[asset_name+'_change']>hsi_vol['mean_up'],asset_name+'_greatless_mean_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_up']
hsi_vol.loc[hsi_vol[asset_name+'_change']<hsi_vol['mean_down'],asset_name+'_greatless_mean_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_down']
hsi_vol[asset_name+'_greatless_mean_value_indicator']=hsi_vol[asset_name+'_greatless_mean_value_indicator'].fillna(0)

hsi_vol.loc[hsi_vol[asset_name+'_change']>hsi_vol['mean_up_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_up_sd1']
hsi_vol.loc[hsi_vol[asset_name+'_change']<hsi_vol['mean_down_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_down_sd1']
hsi_vol[asset_name+'_greatless_mean_sd1_value_indicator']=hsi_vol[asset_name+'_greatless_mean_sd1_value_indicator'].fillna(0)

hsi_vol.loc[hsi_vol[asset_name+'_change']>hsi_vol['mean_up_sd2'],asset_name+'_greatless_mean_sd2_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_up_sd2']
hsi_vol.loc[hsi_vol[asset_name+'_change']<hsi_vol['mean_down_sd2'],asset_name+'_greatless_mean_sd2_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_down_sd2']
hsi_vol[asset_name+'_greatless_mean_sd2_value_indicator']=hsi_vol[asset_name+'_greatless_mean_sd2_value_indicator'].fillna(0)



oi_original=pd.merge(oi_original,hsi_vol[['Date2','Open_hang_seng_oi_volume','Close_hang_seng_oi_volume','hang_seng_oi_volume_change',
                                          'hang_seng_oi_volume_greatless_mean_value_indicator','hang_seng_oi_volume_greatless_mean_sd1_value_indicator',
                                          'hang_seng_oi_volume_greatless_mean_sd2_value_indicator']].copy(),how='left',on=['Date2'])


#for settlement day and one day after it, hsi_vol has no values(removed the row), so in oi_original, it is nan, so remove it.
oi_original=oi_original.loc[~pd.isnull(oi_original['Close_hang_seng_oi_volume']),:]





oi_original['oi_over_volume']=(oi_original['Close_hang_seng_oi']-oi_original['Open_hang_seng_oi'])/oi_original['Close_hang_seng_oi_volume']






##latest method
oi_original.loc[(oi_original['diff']>=0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0),'hang_seng_oi_change_revised5']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised5']=oi_original['hang_seng_oi_change_revised5'].fillna(0)
oi_original.loc[(oi_original['diff']<0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0),'hang_seng_oi_change_revised6']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised6']=oi_original['hang_seng_oi_change_revised6'].fillna(0)

oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']>=0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']<0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0)),'hang_seng_oi_change_revised7']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised7']=oi_original['hang_seng_oi_change_revised7'].fillna(0)
oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']<0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']>=0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0)),'hang_seng_oi_change_revised8']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised8']=oi_original['hang_seng_oi_change_revised8'].fillna(0)







target_table=oi_original.copy()
    
    
for f_name in ['hang_seng_oi_change_revised5','hang_seng_oi_change_revised6',
               'hang_seng_oi_change_revised7','hang_seng_oi_change_revised8']:    
    for ema_decay in [5]:
        #f_name='hang_seng_oi_change_revised5'
        appear=target_table[['Date2',f_name,'DateNum']].copy()
        target_col=f_name
        









#probablic SAR



import pandas as pd

def psar(barsdata,d_name,o_name,h_name,l_name,c_name, iaf = 0.02, maxaf = 0.2):
    length = len(barsdata)
    dates = list(barsdata[d_name])
    open_price=list(barsdata[o_name])
    high = list(barsdata[h_name])
    low = list(barsdata[l_name])
    close = list(barsdata[c_name])
    psar = close[0:len(close)]
    psarbull = [None] * length
    psarbear = [None] * length
    bull = True
    af = iaf
    ep = low[0]
    hp = high[0]
    lp = low[0]
    
    for i in range(2,length):
        if bull:
            psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
        else:
            psar[i] = psar[i - 1] + af * (lp - psar[i - 1])
        
        reverse = False
        
        if bull:
            if low[i] < psar[i]:
                bull = False
                reverse = True
                psar[i] = hp
                lp = low[i]
                af = iaf
        else:
            if high[i] > psar[i]:
                bull = True
                reverse = True
                psar[i] = lp
                hp = high[i]
                af = iaf
    
        if not reverse:
            if bull:
                if high[i] > hp:
                    hp = high[i]
                    af = min(af + iaf, maxaf)
                if low[i - 1] < psar[i]:
                    psar[i] = low[i - 1]
                if low[i - 2] < psar[i]:
                    psar[i] = low[i - 2]
            else:
                if low[i] < lp:
                    lp = low[i]
                    af = min(af + iaf, maxaf)
                if high[i - 1] > psar[i]:
                    psar[i] = high[i - 1]
                if high[i - 2] > psar[i]:
                    psar[i] = high[i - 2]
                    
        if bull:
            psarbull[i] = psar[i]
        else:
            psarbear[i] = psar[i]

    return {"dates":dates, "open":open_price,"high":high, "low":low, "close":close, "psar":psar, "psarbear":psarbear, "psarbull":psarbull}





import sys
import os


HSI_sar=pd.read_excel('HSI_with_tidy.xlsx','Sheet1')



#date need to be ascending order
result = psar(HSI_sar,d_name='Date2',o_name='Open_HSI',h_name='High_HSI',l_name='Low_HSI',c_name='Close_HSI',iaf = 0.02, maxaf = 0.2)

out=pd.DataFrame({'Date2':result['dates'], "open":result['open'],"high":result['high'], "low":result['low'],'close':result['close'],'psar':result['psar'],'psarbear':result['psarbear'],'psarbull':result['psarbull']})
out['DateNum']=out['Date2'].apply(lambda x :(dt.strptime(x,"%Y-%m-%d")-dt(1970,1,1)).days)


out['psarbear_high_diff']=out['psarbear']-out['high']
out['psarbull_low_diff']=out['low']-out['psarbull']
out['Date3'] = [dt.strptime(x, '%Y-%m-%d') for x in out['Date2']]
#out=out[0:-1]


out['sar_up2']=out['psarbull_low_diff'].shift(1)
out['sar_down2']=out['psarbear_high_diff'].shift(1)
out['sar_up2']=out['sar_up2'].fillna(0)
out['sar_down2']=out['sar_down2'].fillna(0)



hsi_y_x=pd.merge(hsi_y_x,out[['Date2','sar_up2', 'sar_down2']],how='left',left_on=['Date2'],right_on=['Date2'])





#import pandas as pd
#hsi_y_x=pd.DataFrame({'dd':['rr']})
#
#np.__version__


import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_dataframe", hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x'+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

temp_path=os.path.join(storage_reference,'daily_source_data_production','hsi_y_x_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'_production.xlsx')
writer = pd.ExcelWriter(temp_path, engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()








#python send email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = "data success"
#The mail addresses and password
sender_address = 'daniel2019trading@gmail.com'
sender_pass = 'vhfrnlisxofeajsy'
receiver_address = 'daniel2019trading@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Data Extraction and Factors Creation Successful'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content))

#attachement
fp = open(os.path.join(target_dir,investigate_see_name), 'rb')
part = MIMEBase('application','vnd.ms-excel')
part.set_payload(fp.read())
fp.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=investigate_see_name)
message.attach(part)


#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')

















sys.stderr.close()
sys.stderr = sys.__stderr__












#logfile=pd.read_csv(stan_out_log)

#logfile='log\\stan_out_data_part_20190930_073049_production.log'
with open(stan_out_log) as f:
    data = f.readlines()

key_words=['error','Error','exception','Exception']

#check key work in log file line by line
output=[x for x in data if any(s in x for s in key_words)]
output="\n".join(output)

#python send email to check is there any exception/error in log file
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content = output
#The mail addresses and password
sender_address = 'daniel20ng@gmail.com'
sender_pass = 'vhy'
receiver_address = 'daniel20ing@gmail.com'
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Error/Exception in data extraction'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content))

#attachement
fp = open(os.path.join(target_dir,stan_out_log), 'rb')
part = MIMEBase('application',"octet-stream")           #send txt file as attachement
part.set_payload(fp.read())
fp.close()
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment', filename=stan_out_log)
message.attach(part)


#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')


index_price_v2_linux.py

#############################
########Download Data########
#############################



#%reset -f
import os
import numpy as np

import requests
import zipfile
import io

#os.chdir(r'C:\Users\jonahthonchan\Desktop\python\WinPython-64bit-3.6.2.0Qt5\ee\index_analysis')
target_dir_old='/home/jonahthonchan/Dropbox/ee/index_analysis'
target_dir='/home/jonahthonchan/my_storage/tradelog/index_analysis_cumulative'

use_hsi_future_price=True

os.chdir(target_dir)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


import pandas_datareader as pdr
from pandas import read_excel
data = read_excel(os.path.join(target_dir_old,'index_table_v2_for_test_backtest.xlsx'),'Sheet1')

chrome_driver_location='/home/jonahthonchan/Dropbox/ee/horse/chrome_driver/chromedriver_linux64/chromedriver84'


#python -m pip install pandas-datareader
#https://stackoverflow.com/questions/12433076/download-history-stock-prices-automatically-from-yahoo-finance-in-python
#import pandas_datareader as pdr
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep

from selenium import webdriver

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re



def change_permissions_recursive(temp_folder1, mode):
    for root, dirs, files in os.walk(temp_folder1, topdown=False):
        for dir in [os.path.join(root,d) for d in dirs]:
            os.chmod(dir, mode)
        for file in [os.path.join(root, f) for f in files]:
            os.chmod(file, mode)







#output stan out
import sys
import time
time_now_save=time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")
stan_out_log=os.path.join('log','stan_out_data_part_'+time_now_save+'_'+'.log')
sys.stderr = open(stan_out_log, 'w')






















#index_quote='0939.HK'
#index_quote='EWH'

#index_quote='FTSE'

#index_quote='%5EIXIC'
#start_date=dt(1991,1,1);end_date=dt(2030,12,31)
#def get_quote(index_quote,start_date,end_date):
#    i = 0
#    print('Doing ',index_quote)
#    while i < 4:
#        i += 1
#        print(i,'\n')
#        try:
#            # do stuff
#            out=pdr.get_data_yahoo(symbols=index_quote, start=start_date, end=end_date)
#
#            break
#        except:
#            continue
#    return out
##help(pdr.get_data_yahoo)
##tt=get_quote('0939.HK')
##temp=get_quote('2819.HK',datetime(1991,1,1),datetime(2030,12,31))
#
##out=pdr.get_data_yahoo(symbols='^HSI', start=datetime(1991,1,1), end=datetime(2030,12,31),interval='m')
#
#
#import os.path
#
##i=20
##download yahoo data and save to xlsx
#count=0
#yahoo_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='Yahoo'),:].shape[0]
#
#
#
#
#for i in range(0,len(data.symbol)):
#    if (data.Extract[i]=='Yes')&(data.Source[i]=='Yahoo'):
##        file_path=os.path.join(target_dir,data.Name_use_python[i]+'.xlsx')
##        if os.path.exists(file_path):
##            temp_old=read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
##            temp_old['Date2']=temp_old['Date'].dt.date
##            temp_old['Date2']=temp_old['Date2'].astype(str)
##            date_end=temp_old.Date2[temp_old.shape[0]-1]
##            date_end=datetime.strptime(date_end,'%Y-%m-%d')
#        
#        temp=get_quote(data.symbol[i],dt(1991,1,1),dt(2030,12,31))
#        # Create a Pandas Excel writer using XlsxWriter as the engine.
#        writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
#        
#        # Convert the dataframe to an XlsxWriter Excel object.
#        temp.to_excel(writer, sheet_name='Sheet1')
#        writer.save()
#        
#        #copy source as back up to daily_source_data_production
#        writer = pd.ExcelWriter(os.path.join('backtest_linux/database/Yahoo',data.Name_use_python[i]+'_'+time.strftime("%Y%m%d")+'.xlsx'), engine='xlsxwriter')
#        temp.to_excel(writer, sheet_name='Sheet1')
#        writer.save()
#        
#        count=count+1
#        print('Yahoo Finance Data Extraction ',count,' (',data.symbol[i],')',' out of ',yahoo_source_total,'\n')
#        eprint('Yahoo Finance Data Extraction ',count,' (',data.symbol[i],')',' out of ',yahoo_source_total,'\n')















#extract data from quandl
import quandl
quandl.ApiConfig.api_key = "F71H5iBEAKKaL1YK6yLz"
#CHRIS/HKEX_HSI1
#mydata = quandl.get("WIKI/IBM", start_date="2010-01-01", end_date="2023-06-04", collapse="daily", returns="pandas")
#mydata1 = quandl.get("NBSC/A190101_M", start_date="1991-01-01", end_date="2017-11-30", collapse="minute", returns="pandas")
#mydata2 = quandl.get("USTREASURY/REALYIELD", start_date="1991-01-01", end_date="2027-11-07", collapse="daily", returns="pandas")
#help(quandl.get)
#BCHARTS/{ANXHK}{USD}



#mydata = quandl.get("SHARADAR/SP500", start_date="2010-01-01", end_date="2023-06-04", returns="pandas")








def get_quote_quandl(index_quote):
    return quandl.get(index_quote, start_date="1991-01-01", end_date="2030-12-31", collapse="daily", returns="pandas")

#i=321 i=322#2472
#download data and save to xlsx
quandl_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='Quandl'),:].shape[0]
count=0
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='Quandl'):
        temp=pd.DataFrame([])
        for ii in range(0,20):
            try:
                temp=get_quote_quandl(data.symbol[i])
                
                if (data.symbol[i]=='USTREASURY/REALYIELD'):
                    url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2022/all?type=daily_treasury_real_yield_curve&field_tdr_date_value=2022&page&_format=csv'
                    webpage = urlopen(url)
                    datareader = csv.reader(io.TextIOWrapper(webpage))
                    us_yield = list(datareader)
                    
                    all_col_name=us_yield[0]
                    all_col_name_date=all_col_name.index('Date')
                    all_col_name_5=all_col_name.index('5 YR')
                    all_col_name_7=all_col_name.index('7 YR')
                    all_col_name_10=all_col_name.index('10 YR')
                    all_col_name_20=all_col_name.index('20 YR')
                    all_col_name_30=all_col_name.index('30 YR')
                    
                    us_yield_col1=[xx[all_col_name_date] for xx in us_yield[1:]]
                    us_yield_col2=[xx[all_col_name_5] for xx in us_yield[1:]]
                    us_yield_col3=[xx[all_col_name_7] for xx in us_yield[1:]]
                    us_yield_col4=[xx[all_col_name_10] for xx in us_yield[1:]]
                    us_yield_col5=[xx[all_col_name_20] for xx in us_yield[1:]]
                    us_yield_col6=[xx[all_col_name_30] for xx in us_yield[1:]]
                    
                    us_yield=pd.DataFrame({'Date':us_yield_col1,'5 YR':us_yield_col2,'7 YR':us_yield_col3,'10 YR':us_yield_col4,'20 YR':us_yield_col5,'30 YR':us_yield_col6})
                    us_yield['5 YR']=pd.to_numeric(us_yield['5 YR'], errors='coerce')
                    us_yield['7 YR']=pd.to_numeric(us_yield['7 YR'], errors='coerce')
                    us_yield['10 YR']=pd.to_numeric(us_yield['10 YR'], errors='coerce')
                    us_yield['20 YR']=pd.to_numeric(us_yield['20 YR'], errors='coerce')
                    us_yield['30 YR']=pd.to_numeric(us_yield['30 YR'], errors='coerce')
                    
                    
                    us_yield['Date']=us_yield['Date'].apply(lambda x: dt.strptime(x,'%m/%d/%Y'))
                    us_yield=us_yield.sort_values(by=['Date'],ascending=True)

                    temp=us_yield.reset_index(drop=True)
                    
                    
                if (data.symbol[i]=='USTREASURY/REALLONGTERM'):
                    url = 'https://home.treasury.gov/resource-center/data-chart-center/interest-rates/daily-treasury-rates.csv/2022/all?type=daily_treasury_real_long_term&field_tdr_date_value=2022&page&_format=csv'
                    webpage = urlopen(url)
                    datareader = csv.reader(io.TextIOWrapper(webpage))
                    us_yield = list(datareader)
                    
                    us_yield_col1=[xx[0] for xx in us_yield]
                    us_yield_col2=[xx[1] for xx in us_yield]
                    us_yield_col1=us_yield_col1[1:]
                    us_yield_col2=us_yield_col2[1:]
                    
                    us_yield=pd.DataFrame({'Date':us_yield_col1,'LT Real Average (>10Yrs)':us_yield_col2})
                    us_yield['LT Real Average (>10Yrs)']=pd.to_numeric(us_yield['LT Real Average (>10Yrs)'], errors='coerce')
                     
                    us_yield['Date']=us_yield['Date'].apply(lambda x: dt.strptime(x,'%m/%d/%Y'))
                    us_yield=us_yield.sort_values(by=['Date'],ascending=True)

                    temp=us_yield.reset_index(drop=True)


                if (data.symbol[i]=='AAII/AAII_SENTIMENT'):
                    if dt.today().strftime('%A')=='Friday':
                        count=count+1
                        for ii in range(0,2):
                            #clear_dir = r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\wsj_csv\temp\*"
                            download_dir = r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis"

                            etract_link='https://www.aaii.com/files/surveys/sentiment.xls'
                            
                            if os.path.exists(os.path.join(download_dir,'sentiment.xls')):
                                os.remove(os.path.join(download_dir,'sentiment.xls')) 
                            
                            try:
                                #download file to folder
                                import requests
                                from lxml.html import fromstring
                        
                    
                                def get_proxies():
                                    url = 'https://free-proxy-list.net/'
                                    response = requests.get(url)
                                    parser = fromstring(response.text)
                                    proxies = set()
                                    #i=parser.xpath('//tbody/tr')[0]
                                    for i in parser.xpath('//tbody/tr'):
                                        if (i.xpath('.//td[7][contains(text(),"yes")]')):
                                            #Grabbing IP and corresponding PORT
                                            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
                                            proxies.add(proxy)
                                    return proxies
                                
                                import requests
                                from itertools import cycle
                                import traceback
                                proxies = get_proxies()
                                proxy_pool = cycle(proxies)
                                url = 'https://httpbin.org/ip'
                                for iii in range(0,min(20,len(proxies))):
                                    #Get a proxy from the pool
                                    if not os.path.exists(os.path.join(download_dir,'sentiment.xls')):
                                        proxy_use = next(proxy_pool)
                                        print("Request #%d"%iii)
                                        chrome_options = webdriver.ChromeOptions()
                                        PROXY = proxy_use
                                        try:
                                            chrome_options.add_argument('--proxy-server=%s' % PROXY)
                                            preferences = {"download.default_directory": download_dir ,
                                                           "directory_upgrade": True,
                                                           "safebrowsing.enabled": True }
                                            chrome_options.add_experimental_option("prefs", preferences)
                                            
                                            driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\Users\jonahthonchan\Dropbox\ee\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')
                                            driver.set_page_load_timeout(30)
                                            driver.get(etract_link)
                                            
                                            
                                            count_time=0
                                            while (count_time<=30)&(not os.path.exists(os.path.join(download_dir,'sentiment.xls'))):
                                                time.sleep(2)
                                                count_time=count_time+2
                                                print('1213ting '+str(count_time)+' seconds')
                                            sleep(2)
                                            driver.close()
        
        
                                            #move incompete download
                                            import shutil
                                            for filename in os.listdir(download_dir):
                                                f = os.path.join(download_dir, filename)
                                                if 'crdownload' in f:
                                                    #print(f)
                                                    shutil.move(f,os.path.join(download_dir,'can_delete',filename))
                                        
                                      
                                        except:
                                            driver.close()
                                            eprint("Oops!",sys.exc_info()[0],"occured when extracting ",'AAII sentiment','\n')
                                            print("Oops!",sys.exc_info()[0],"occured when extracting ",'AAII_sentiment','\n')
                                        if os.path.exists(os.path.join(download_dir,'sentiment.xls')):
                                            break
                                    
    
    
                                #find the file name under temp and read it
                                filename_temp=os.path.join(download_dir,'sentiment.xls')
                                df=pd.read_excel(filename_temp,dtype=str, sheetname='SENTIMENT', skiprows =1)
                                
                                colname=['Date','Bullish','Neutral','Bearish',
                                         'Total','Bullish 8-Week Mov Avg','Bull-Bear Spread',
                                         'Bullish Average','Bullish Average + St. Dev','Bullish Average - St. Dev','S&P 500 Weekly High',
                                         'S&P 500 Weekly Low','S&P 500 Weekly Close']
                                df.columns=colname
                                df=df[185:]
                                df=df.reset_index(drop=True)
                                remove=df.loc[df['Date']=='Observations over life of survey'].index[0]
                                df=df[0:remove]
                                df=df.loc[~(df['Date']=='nan'),:]
                                
                                df=df.reset_index(drop=True)
                                
                                df['Date']=df['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d %H:%M:%S"))
                                
                                temp=df.copy()                            
                                #df=df_connect.copy()
                                #make sure downloaded a complete csv file
                                if (df.shape[0]!=0)&(filename_temp[-3:]=='xls'): break
                            except:
                                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')
                                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n') 
						
                if temp.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.symbol[i],'\n')

        no_of_trial=ii+1
        eprint(data.symbol[i],' tried ',no_of_trial,' times extraction with success','\n')
         
        
        
        if temp.shape[0]!=0:
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/Quandl',data.Name_use_python[i]+'.xlsx'), engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            temp.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            print('Quandl Finance Data Extraction ',data.symbol[i])
            
#            #copy source as back up to daily_source_data_production
#            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
#            temp.to_excel(writer, sheet_name='Sheet1')
#            writer.save()
            
            count=count+1
            eprint('Quandl Finance Data Extraction ',count,' out of ',quandl_source_total,'\n')
            print('Quandl Finance Data Extraction ',count,' out of ',quandl_source_total,'\n')
        else:
            eprint('Quandl Finance Data Extraction ',data.symbol[i],' not extracted','\n')
            print('Quandl Finance Data Extraction ',data.symbol[i],' not extracted','\n')


#temp=get_quote_quandl('CHRIS/HKEX_HSI1')
#writer = pd.ExcelWriter(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\fhsi_quandl.xlsx', engine='xlsxwriter')
## Convert the dataframe to an XlsxWriter Excel object.
#temp.to_excel(writer, sheet_name='Sheet1')
## Close the Pandas Excel writer and output the Excel file.
#writer.save()









from bs4 import BeautifulSoup
import urllib.request as urllib2
#from lxml import etree
#import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict
import glob
import shutil
#i=2416#24142418 2425  i=118 i=505  i=4   i=628  i=115 i=1652  i=1812   i=671  i=3454
#download WSJ data and save to xlsx
wsj_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='wsj'),:].shape[0]
count=0
#for i in range(1417,1920):
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='wsj'):
        symbol_name=data.symbol[i]
        df=pd.DataFrame([])
        output_bigfrontbox=pd.DataFrame([])        
        import requests
        import io
        
        count=count+1
        for ii in range(0,4):
            #clear_dir = r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\wsj_csv\temp\*"
            download_dir = os.path.join(target_dir,'backtest_linux/database/wsj/wsj_csv/temp')
            #remove this folder
            shutil.rmtree(download_dir)
            
            if not os.path.exists(download_dir):
                os.makedirs(download_dir)
            
            path_delete=os.path.join(download_dir,'HistoricalPrices.csv')
            
#            files = glob.glob(clear_dir)
#            for f in files:
#                os.remove(f)

            #symbol_name='HK/XHKG/0700'
            etract_link='https://www.wsj.com/market-data/quotes/'+symbol_name+'/historical-prices/download?MOD_VIEW=page&num_rows=100000&range_days=100000&startDate=01/01/1980&endDate=01/01/2100'
            try:
                if os.path.exists(path_delete):
                    os.remove(path_delete)                
                
                #download file to folder
                chrome_options = webdriver.ChromeOptions()
                preferences = {"download.default_directory": download_dir ,
                               "directory_upgrade": True,
                               "safebrowsing.enabled": True }
                chrome_options.add_experimental_option("prefs", preferences)
                chrome_options.add_argument('--no-sandbox')                           #in linux need to add this
                chrome_options.add_argument('--disable-dev-shm-usage')                #in linux need to add this
                chrome_options.add_argument('headless')

                
                
                #driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r'C:\Users\jonahthonchan\Dropbox\ee\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')
                driver = webdriver.Chrome(options=chrome_options,executable_path=chrome_driver_location)
                


                
                driver.get(etract_link)

                for iii in range(1,4):
                    sleep(1)
                    if os.path.exists(path_delete):
                        driver.close()
                        break

                #find the file name under temp and read it
                filename_temp=os.path.join(download_dir,'HistoricalPrices.csv')
                df=pd.read_csv(filename_temp)
                
                #df=df_connect.copy()
                #make sure downloaded a complete csv file
                if (df.shape[0]!=0)&(filename_temp[-3:]=='csv'): break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",symbol_name,'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",symbol_name,'\n')
    
        no_of_trial=ii+1
        eprint(symbol_name,' tried ',no_of_trial,' times extraction with success ',i,'\n')
        print(symbol_name,' tried ',no_of_trial,' times extraction with success ',i,'\n')
        
            
        if df.shape[0]!=0:
            #in wsj, there is a space before'Open'
            df.columns = df.columns.str.strip()
            
            df['Date']=df['Date'].apply(lambda x:dt.strptime(x,'%m/%d/%y'))#convert string (need to tell python string format) to datetime
            df=df.sort_values(by=['Date'],ascending=[True])
            df=df.reset_index(drop=True)
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/wsj',data.Name_use_python[i]+'.xlsx'), engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            df.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
#            #copy source as back up to daily_source_data_production
#            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
#            df.to_excel(writer, sheet_name='Sheet1')
#            writer.save()
#            eprint('WSJ Finance Data Extraction ',count,' out of ',wsj_source_total,'\n')
#            print('WSJ Finance Data Extraction ',count,' out of ',wsj_source_total,'\n')
        else:
            eprint('WSJ Finance Data Extraction ',symbol_name,' not extracted','\n')
            print('WSJ Finance Data Extraction ',symbol_name,' not extracted','\n')

        #find today price in front big box
        if (data.symbol[i][0:10]!='mutualfund'):
            for ii in range(0,2):
                etract_link='https://www.wsj.com/market-data/quotes/'+symbol_name+'/historical-prices'
                try:
    
                    #wsj is forbidden, need to use below.
                    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                           'Accept-Encoding': 'none',
                           'Accept-Language': 'en-US,en;q=0.8',
                           'Connection': 'keep-alive'}
                    
                    req = urllib2.Request(etract_link, headers=hdr)
                    
                    page = urllib2.urlopen(req,timeout=7)
                    soup = BeautifulSoup(page, "html.parser")
    
    
                    if (data.Type[i]=='index'):
                        div = soup.find('span', {'class':"timestamp_value"})
                        date_value=div.text.split(' ')[-1]
                        
                        div = soup.find('li', {'class':"crinfo_quote"})
                        div = div.find('span', {'id':"quote_val"})
                        close_value=float(div.text)
        
                        div = soup.find('ul', {'class':"cr_data_collection cr_charts_info"})
                        low_value=float(div.text.split('     ')[0].replace('1 Day Range','').split('-')[0].strip())
                        high_value=float(div.text.split('     ')[0].replace('1 Day Range','').split('-')[1].strip())
                        
                        div = soup.find('div', {'class':"cr_compare_data"})
                        div=div.find('ul', {'class':"cr_data_collection"})
                        open_value=float(div.text.split('   ')[0].split(' ')[-1])
                        
                        output_bigfrontbox=pd.DataFrame(OrderedDict({'Date':[date_value],' Open':[open_value],' High':[high_value],' Low':[low_value],' Close':[close_value]}))
                    
                    if ((data.Type[i]=='stock_basic_material')|
                        (data.Type[i]=='stock_consumer_good')|
                        (data.Type[i]=='stock_financial')|
                        (data.Type[i]=='stock_service')|
                        (data.Type[i]=='stock_technology')|
                        (data.Type[i]=='ETF')|
                        (data.Type[i]=='HSI_component')|
                        (data.Type[i]=='HHI_component')):
                        
                        div = soup.find('span', {'class':"timestamp_value"})
                        date_value=div.text.split(' ')[-1]
                        
                        div = soup.find('li', {'class':"crinfo_quote"})
                        div = div.find('span', {'id':"quote_val"})
                        close_value=float(div.text)
                        
                        div = soup.find('ul', {'class':"cr_data_collection cr_charts_info"})
                        div = div.find('span', {'id':"quote_volume"})
                        volume_value=float(div.text.replace(',',''))                
        
                        div = soup.find('ul', {'class':"cr_data_collection cr_charts_info"})
                        low_value=float(div.text.split('     ')[2].replace('1 Day Range','').split('-')[0].strip())
                        high_value=float(div.text.split('     ')[2].replace('1 Day Range','').split('-')[1].strip())
                        
                        div = soup.find('div', {'class':"cr_compare_data"})
                        div=div.find('ul', {'class':"cr_data_collection"})
                        open_value=float(div.text.split('   ')[0].split(' ')[-1])                
                    
                        #note that it is very fake, wsj historical data has ' ' in Open so it is ' Open'
                        output_bigfrontbox=pd.DataFrame(OrderedDict({'Date':[date_value],' Open':[open_value],' High':[high_value],' Low':[low_value],' Close':[close_value],' Volume':[volume_value]}))
                        
                    #df=df_connect.copy()
                    #make sure downloaded a complete csv file
                    if (output_bigfrontbox.shape[0]!=0): break
                except:
                    eprint("Oops!",sys.exc_info()[0],"occured when extracting wsj bigfrontbox",symbol_name,'\n')
                    print("Oops!",sys.exc_info()[0],"occured when extracting wsj bigfrontbox",symbol_name,'\n')
        
        if output_bigfrontbox.shape[0]!=0:
            if output_bigfrontbox.Date.values[-1] not in df.Date.values.tolist():
                df=df.append(output_bigfrontbox)
                output_msg='error '+symbol_name+' , wsj historical csv has no today data so appended bigfrontbox with Date '+output_bigfrontbox.Date.values[-1]+' Open '+str(output_bigfrontbox[' Open'].values[-1])+' Close '+str(output_bigfrontbox[' Close'].values[-1])
                print(output_msg)
                eprint(output_msg)
        
        
    #dji something no data in historical wsj, so use market watch price
    if (data.Extract[i]=='Yes')&(data.Name_use_python[i]=='index_DJIA_wsj')&(data.use_cnbc[i]=='Yes'):
        output_df=pd.DataFrame([])
        for ii in range(0,4):
            try:
             
                #url='https://www.cnbc.com/quotes/?symbol='+data.cnbc_symbol[i]
                url='https://www.cnbc.com/quotes/?symbol=.DJI'
                
                
                page = urllib2.urlopen(url,timeout=7)
                soup = BeautifulSoup(page, "html.parser")
                
                div = soup.find('div', {'class':"Summary-subsection"})
                div=div.find_all('li')
                open_price_value=float(div[0].text.replace('Open','').replace(',',''))
                high_price_value=float(div[1].text.replace('Day High','').replace(',',''))
                low_price_value=float(div[2].text.replace('Day Low','').replace(',',''))
                price_value=float(div[3].text.replace('Prev Close','').replace(',',''))
                
                
                
                url='https://apps.cnbc.com/view.asp?symbol=.DJI&uid=stocks/summary'
                page = urllib2.urlopen(url,timeout=7)
                soup = BeautifulSoup(page, "html.parser")

                
                div = soup.find('div', {'class':"fontSm"})
                
                d_temp=div.find_all('span')[0].text
                months_all = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                find_temp_m=[x for x in months_all if x in d_temp][0]
                year_all=range(2021,2200)
                find_temp_y=[str(x) for x in year_all if str(x) in d_temp][0]
                d_temp=d_temp[d_temp.find(find_temp_m):d_temp.find(find_temp_y)+4]
                
                date_raw=d_temp.replace(',','')                
              
                date_updated=date_raw  #string
                dt_new=dt.strptime(date_updated,'%b %d %Y') #string to dt
                date_updated=dt_new.strftime('%Y-%m-%d')  #dt to string
                        
                
                
                output_df=pd.DataFrame(OrderedDict({'Date':[date_updated],'Open':[open_price_value],'High':[high_price_value],'Low':[low_price_value],'Close':[price_value]}))
                print(data.Name_use_python[i].replace('_wsj',''),'\n')
                print(output_df,'\n')
                eprint(data.Name_use_python[i].replace('_wsj',''),'\n')
                eprint(output_df,'\n')
                if output_df.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')

        no_of_trial=ii+1
        eprint(data.Name_use_python[i].replace('_wsj',''),' with backup in cnbc tried ',no_of_trial,' times extraction with success','\n')         
        print(data.Name_use_python[i].replace('_wsj',''),' with backup in cnbc tried ',no_of_trial,' times extraction with success','\n')          

        
        if output_df.shape[0]!=0:        
            #save a back up of this market watch price
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/wsj',data.Name_use_python[i].replace('_wsj','')+'_from_cnbc.xlsx'), engine='xlsxwriter')
            output_df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
#            #copy source as back up to daily_source_data_production
#            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i].replace('_wsj','')+'_'+time_now_save+'_from_market_watch.xlsx'), engine='xlsxwriter')
#            output_df.to_excel(writer, sheet_name='Sheet1')
#            writer.save()
            
            vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
            #check2=vars()[data.Name_use_python[i]].copy()
            
            #date_updated='2019-05-23'
            #if the date in cnbc is already in wsj, then keep using wsj
            if sum(vars()[data.Name_use_python[i]]['Date2'].isin([date_updated]))>=1:
                print(data.Name_use_python[i]," wsj already have today data",'\n')
                eprint(data.Name_use_python[i]," wsj already have today data",'\n')
            else: #if not in wsj, append to wsj
                print(data.Name_use_python[i]," wsj don't have today data, now append prices from cnbc",'\n')
                eprint(data.Name_use_python[i]," wsj don't have today data, now append prices from cnbc",'\n')
                #copy last row and append it
                new_data = pd.DataFrame(vars()[data.Name_use_python[i]][-1:].values, columns=vars()[data.Name_use_python[i]].columns)
                vars()[data.Name_use_python[i]] = vars()[data.Name_use_python[i]].append(new_data)
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
                #replace last row value with market watch value
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date2']]=date_updated
                #check=vars()[data.Name_use_python[i]].copy()
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Open','High','Low','Close']]=[open_price_value,high_price_value,low_price_value,price_value]
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date']]=dt_new
            
            del vars()[data.Name_use_python[i]]['Date2']
            #check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].sort_values(by=['Date'],ascending=[True])
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/wsj',data.Name_use_python[i]+'.xlsx'), engine='xlsxwriter')
            
            # Convert the dataframe to an XlsxWriter Excel object.
            vars()[data.Name_use_python[i]].to_excel(writer, sheet_name='Sheet1')
            
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
        else:
            eprint(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')
            print(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')  
















#this part is deal with 6 mutual fund, which may not be timely from wsj at morning 8:30am
#so use market watch.com, https://www.marketwatch.com
#if the date in market watch is already in wsj, then replace the price in wsj with market watch price
#if not in wsj, append to it (copy last row and replicate in wsj and then revise date,open,high...)
from bs4 import BeautifulSoup
import urllib.request as urllib2
#from lxml import etree
#import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict

mutual_fund_list=['OTPSX_wsj','FBGKX_wsj','HJPNX_wsj','FJSCX_wsj','TBGVX_wsj']

#i=2462
#url = 'https://w...content-available-to-author-only...h.com/investing/fund/OTPSX'
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Name_use_python[i] in mutual_fund_list)&(data.use_cnbc[i]=='Yes'):
        output_df=pd.DataFrame([])
        for ii in range(0,20):
            try:
                #url = 'https://www.marketwatch.com/investing/fund/'+data.Name_use_python[i].replace('_wsj','')

                url='https://www.cnbc.com/quotes/?symbol='+data.Name_use_python[i].replace('_wsj','')

                page = urllib2.urlopen(url,timeout=7)
                soup = BeautifulSoup(page, "html.parser")
                #div = soup.find('div', {'id':"structured-data"})
                div = soup.find('span', {'class':"QuoteStrip-lastPrice"})
                price_value=div.text
                price_value=float(price_value)
                
                div = soup.find('div', {'class':"QuoteStrip-lastTradeTime"})
                date_raw=div.text.split(' ')[2]
                date_updated=date_raw  #string
                dt_new=dt.strptime(date_updated,'%m/%d/%y') #dt
                date_updated=dt_new.strftime('%Y-%m-%d')


#                #use market watch price
#                price_value=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]')[0].text_content() #[0] because under this xpath list only 1 element
#                price_value=float(price_value.replace(',',''))
#                 
#                #                      '//*[contains(concat( " ", @class, " " ), concat( " ", "value", " " ))]'
#                #/html/body/div[2]/div[2]/div[2]/div/div/div[2]/h3/span
#                
#                #format like this "Last Updated: Jan 3, 2019 4:08 p.m. HKST"
#                updated_time_raw=root.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "timestamp__time", " " ))]')[0].text_content()
#                result = re.search('Last Updated: (.*)', updated_time_raw).group(1)
#                result_split=result.split(",")
#                
#                year=int(result_split[1].strip()[0:4])
#                def month_converter(month):
#                    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#                    return months.index(month) + 1
#                month=month_converter(result_split[0].strip()[0:3])
#                day=[int(s) for s in result_split[0].split() if s.isdigit()][0]
#                dt_new = dt(year, month, day)
#                date_updated=dt_new.strftime('%Y-%m-%d')
                 
                output_df=pd.DataFrame(OrderedDict({'Date':[date_updated],'Close':[price_value]}))
                print(data.Name_use_python[i].replace('_wsj',''))
                print(output_df)
                eprint(data.Name_use_python[i].replace('_wsj',''))
                eprint(output_df)
                
                if output_df.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i].replace('_wsj',''),'\n')

        no_of_trial=ii+1
        eprint(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')         
        print(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')          

        
        if output_df.shape[0]!=0:        
            #save a back up of this cnbc price
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/wsj',data.Name_use_python[i].replace('_wsj','')+'_from_cnbc.xlsx'), engine='xlsxwriter')
            output_df.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
#            #copy source as back up to daily_source_data_production
#            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i].replace('_wsj','')+'_'+time_now_save+'_from_cnbc.xlsx'), engine='xlsxwriter')
#            output_df.to_excel(writer, sheet_name='Sheet1')
#            writer.save()
            
            vars()[data.Name_use_python[i]] = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
            #check2=vars()[data.Name_use_python[i]].copy()
            
            #date_updated='2018-12-31'
            #if the date in cnbc is already in wsj, then replace the price in wsj with cnbc price
            if sum(vars()[data.Name_use_python[i]]['Date2'].isin([date_updated]))>=1:
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Date2']==date_updated,['Open','High','Low','Close']]=price_value
            else: #if not in wsj, append to wsj
                #copy last row and append it
                new_data = pd.DataFrame(vars()[data.Name_use_python[i]][-1:].values, columns=vars()[data.Name_use_python[i]].columns)
                vars()[data.Name_use_python[i]] = vars()[data.Name_use_python[i]].append(new_data)
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
                #replace last row value with market watch value
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date2']]=date_updated
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Open','High','Low','Close']]=price_value
                vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]].index[-1],['Date']]=dt_new
            
            del vars()[data.Name_use_python[i]]['Date2']
            #check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].sort_values(by=['Date'],ascending=[True])
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/wsj',data.Name_use_python[i]+'.xlsx'), engine='xlsxwriter')
            
            # Convert the dataframe to an XlsxWriter Excel object.
            vars()[data.Name_use_python[i]].to_excel(writer, sheet_name='Sheet1')
            
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            eprint(data.Name_use_python[i].replace('_wsj',''),'from cnbc replaced wsj or merged to wsj','\n')
            print(data.Name_use_python[i].replace('_wsj',''),'from cnbc replaced wsj or merged to wsj','\n')
        else:
            eprint(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')
            print(data.Name_use_python[i].replace('_wsj',''),'no data from cnbc','\n')      








#download data from investing.com
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriver1213t
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import requests
import io
import sys
import pandas as pd




investingdotcom_source_total=data.loc[(data['Extract']=='Yes')&(data['Source']=='investing_com'),:].shape[0]
count=0
#i=2510;ii=0;i=2468  i=3115
#asset='commodities/brent-oil-historical-data'
for i in range(0,len(data.symbol)):
#for i in range(2468,2472):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='investing_com'):
        final_output=pd.DataFrame([])
        asset_name=data.Name_use_python[i]
        count=count+1
        

        def extract_from_investing(start_date,end_date,asset):
#                    start_date='11/25/2009';start_date='12/31/2002';end_date='11/25/1975'
#                    start_date='12/31/2014';end_date='11/25/2019';
#                    start_date='01/01/1990';end_date='12/31/2002'
#                    asset='rates-bonds/euro-bobl-historical-data';asset='commodities/brent-oil-historical-data'
#                    asset=data.symbol[i];start_date='12/31/2018';end_date='12/31/2040'
            df_output=pd.DataFrame([])
            for ii in range(0,2): #max try 20 times, if one time successful, it will quit this for loop
                #because pop up window may appear faster than clicking signin button, so error occure, so need to use try, except
                aa=''
                aa_replace_all=''

                try:
                    try:
                        #browser = webdriver.Chrome(executable_path=r'C:\Users\jonahthonchan\Dropbox\ee\horse\chrome_driver\chromedriver_win32\chromedriver79039.exe')
                        browser = webdriver.Chrome(executable_path=r'C:\Users\jonahthonchan\Dropbox\ee\horse\chrome_driver\chromedriver_win32\chromedriver_87.exe')

                    except:
                        browser = webdriver.Chrome(executable_path=r'C:\Users\jonahthonchan\Desktop\python\chromedriver770286510.exe')
                    #browser = webdriver.PhantomJS(r"C:\Users\jonahthonchan\Desktop\python\phantomjs.exe")
                    #because if running selenium in terminal/command prompt, will get this error (chrome will hang and 1213t so long)
                    #ERROR:latency_info.cc(144) Surface::TakeLatencyInfoFromFrame, LatencyInfo vector size 102 is too big.
                    #but run at console, no error
                    #so set this timeout at 10s, so if hang 10s, will appear timeout error
                    #then can go to exception handling(no need 1213t too long)
                    browser.set_page_load_timeout(80)

                    
                    link='https://www.investing.com/ad-free-subscription/?source=desktop&medium=header_button'
                    browser.get(link)
                    

                    #webdriver.ActionChains(browser).send_keys(Keys.ESCAPE).perform()
                    1213t = WebDriver1213t(browser, 30)
                    

                    1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="userAccount"]/div/a[1]'))).click()
                    #use email to login
                    1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginFormUser_email"]'))).send_keys('jonahthon.werwe1213@gmail.com')
                    1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="loginForm_password"]'))).send_keys('fdsf2334')
                    1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="signup"]/a'))).click()

                    sleep(5)

                    link="https://www.investing.com/"+asset
                    browser.get(link) #need to 1213t longer time
                    sleep(5)



#                    #check if ads exist
#                    try:
#                        check1=WebDriver1213t(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[3]/a[1]"]')))
#                        ask_chinese=True
#                    except:
#                        ask_chinese=False
#                        
#                    #close ask for chinese version pop up
#                    if ask_chinese==True:
#                        try:
#                            #1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[1]/a'))).click()
#                            1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="topAlertBarContainer"]/div/div[3]/a[1]'))).click()
#                        except:
#                            pass
#                
#                    #check if adas exist
#                    try:
#                        check1=WebDriver1213t(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="ab-intro"]/span/i')))
#                        black_fri=True
#                    except:
#                        black_fri=False
#                        
#                    #close black fri pop up
#                    if black_fri==True:
#                        #us election adhot advertisement, black friday ads
#                        try:
#                            1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ab-intro"]/span/i'))).click()
#                        except:
#                            pass  


#                    if asset=='rates-bonds/euro-bobl-historical-data':
#                        1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="widgetFieldDateRange"]'))).click()
#                        1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="startDate"]'))).clear()
#                        1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="startDate"]'))).send_keys(start_date)
#                        1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="endDate"]'))).clear()
#                        1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="endDate"]'))).send_keys(end_date)
#                        1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="applyBtn"]'))).click()
#                        #1213t.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="results_box"]')))
#                        #sleep(6)
#                        
#                        sleep(5)
#                        
#                        hoursTable = browser.find_elements_by_xpath('//*[@id="results_box"]')
#                        aa=hoursTable[0].text
#                        
#                        
#                        from io import StringIO
#                        #import datetime
#                        aa_replace_all=aa.replace(' ','@@@')
#                        #https://stackoverflow.com/questions/2294493/how-to-get-the-position-of-a-character-in-python
#                        first_line=aa_replace_all.find('\n') #find first newline position Date Price Open High Low Vol. Change %\n
#                        last_line=aa_replace_all.rfind('\n')
#                        aa_replace_all=aa_replace_all[(first_line+1):(last_line)]#remove first row (open high low close)
#                        browser.quit()
#                        break
#                    else:
                    browser.find_element_by_tag_name('html').send_keys(Keys.PAGE_DOWN)
                    sleep(3)
                    try:
                        1213t.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/main/div/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div[1]/div[2]'))).click()
                    except:
                        pass                        
                    
                    
                    
                    #download result box

                    hoursTable = browser.find_elements_by_xpath('/html/body/div[1]/div/div/div/div[2]/main/div/div[5]/div/div/div[3]/div/table')
                    aa=hoursTable[0].text
                    
                    
                    from io import StringIO
                    #import datetime
                    aa_replace_all=aa.replace(' ','@@@')
                    ff=aa_replace_all.find("Change@@@%")
                    aa_replace_all=aa_replace_all[ff+10:]
                    aa_replace_all=aa_replace_all[1:]
                    
                    import re
                    temp=re.findall(r"(\d+/\d+/\d+)@@@([0-9,.]+)@@@([0-9,.]+)@@@([0-9,.]+)@@@([0-9,.]+)@@@",aa_replace_all)
                    temp=pd.DataFrame(temp)
                    aa_replace_all=temp.copy()
                    
                    browser.quit()
                    break
                except:
                    eprint("Oops!",sys.exc_info()[0],"occured when extracting ",asset_name,'\n')
                    print("Oops!",sys.exc_info()[0],"occured when extracting ",asset_name,'\n')
                    try:
                        browser.quit()
                    except:
                        pass

            if len(aa_replace_all)>0:
                eprint(asset_name,' tried ',ii+1,' times extraction with success','\n')        
                print(asset_name,' tried ',ii+1,' times extraction with success','\n')  


#                if asset=='rates-bonds/euro-bobl-historical-data':
#                    aa_replace=StringIO(aa_replace_all) 
#                 
#                    df = pd.read_csv(aa_replace, index_col=0, header=None,sep='@@@',engine='python')  
#                    df['month']=df.index
#                    df.rename(columns={1:'day',2:'year',3:'Close',4:'Open',5:'High',6:'Low',7:'vol',8:'change_percent'},inplace=True)
#                    del df['vol'];del df['change_percent']
#                    df=df.astype(str)
#                    df['day']=df['day'].apply(lambda x:x.replace(',',''))                    
#                    df['Open']=df['Open'].apply(lambda x:x.replace(',',''))
#                    df['High']=df['High'].apply(lambda x:x.replace(',',''))
#                    df['Low']=df['Low'].apply(lambda x:x.replace(',',''))
#                    df['Close']=df['Close'].apply(lambda x:x.replace(',',''))
#                    def month_converter(month):
#                        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#                        return months.index(month) + 1
#                    df['month']=df['month'].apply(lambda x:month_converter(x))
#                 
#                    df['Date'] = pd.to_datetime(df[['year','month','day']]) #datetime object
#                    df_output=df[['Date','Open','High','Low','Close']].copy()
#                    df_output=df_output.reset_index(drop=True)
#                else:
                #aa_replace=StringIO(aa_replace_all) 
             
                #df = pd.read_csv(aa_replace, index_col=0, header=None,sep='@@@',engine='python')  
                #df=df.reset_index(drop=False)
                df=aa_replace_all.copy()
                df.columns=['Date','Close','Open','High','Low']
                #del df['vol'];del df['change_percent']
                try:
                    df['Open']=df['Open'].apply(lambda x:x.replace(',',''))
                    df['High']=df['High'].apply(lambda x:x.replace(',',''))
                    df['Low']=df['Low'].apply(lambda x:x.replace(',',''))
                    df['Close']=df['Close'].apply(lambda x:x.replace(',',''))
                except:
                    pass
                df['Date']=df['Date'].apply(lambda x:dt.strptime(x,"%m/%d/%Y"))
                df_output=df[['Date','Open','High','Low','Close']].copy()
                df_output=df_output.reset_index(drop=True)
            else:
                df_output=pd.DataFrame([])

            return df_output
        
        #remember, investing.com max show 20 years data
#        first_df=extract_from_investing(start_date='01/01/1990',end_date='12/31/2002',asset=data.symbol[i])                
#        time_temp='12/31/2002' if first_df.shape[0]==0 else max(first_df['Date']).strftime('%m/%d/%Y') #convert datetime to string, need to tell string format
#        print('finished first_df\n')
#        eprint('finished first_df\n')
#        
#        second_df=extract_from_investing(start_date=time_temp,end_date='12/31/2014',asset=data.symbol[i])                
#        time_temp='12/31/2014' if second_df.shape[0]==0 else max(second_df['Date']).strftime('%m/%d/%Y') #convert datetime to string, need to tell string format
#        print('finished second_df\n')
#        eprint('finished second_df\n')
                          
        third_df=extract_from_investing(start_date='12/31/2018',end_date='12/31/2040',asset=data.symbol[i])
        #third_df=df_output.copy()
        #third_df=extract_from_investing(asset=data.symbol[i])
        print('finished third_df\n')
        eprint('finished third_df\n')
        
        #final_output=first_df.append(second_df,ignore_index=True)
        #final_output=final_output.append(third_df,ignore_index=True)
        final_output=third_df.copy()
        
        #below if loop is out of above second for loop
        if final_output.shape[0]!=0:
            final_output2=final_output.drop_duplicates(subset='Date',keep='last')
            final_output2=final_output2.sort_values(by=['Date'],ascending=[True])
            final_output2=final_output2.reset_index(drop=True)
            
            #for futures, need to append to cum file
            cumulated_data = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')            
            final_output2=cumulated_data.append(final_output2)
            final_output2=final_output2.drop_duplicates(subset='Date',keep='last')
            final_output2['Open']=final_output2['Open'].astype(float)
            final_output2['High']=final_output2['High'].astype(float)
            final_output2['Low']=final_output2['Low'].astype(float)
            final_output2['Close']=final_output2['Close'].astype(float)
            final_output2=final_output2.reset_index(drop=True)
            
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            final_output2.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
            final_output2.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            eprint('Investing.com Finance Data Extraction ',asset_name,' ',count,' out of ',investingdotcom_source_total,'\n')
            print('Investing.com Finance Data Extraction ',asset_name,' ',count,' out of ',investingdotcom_source_total,'\n')
        else:
            eprint('Investing.com Finance Data Extraction ',asset_name,' not extracted/no data','\n')
            print('Investing.com Finance Data Extraction ',asset_name,' not extracted/no data','\n')
        
        #remember, investing.com max show 20 years data
#        first_df=extract_from_investing(start_date='01/01/1990',end_date='12/31/2002',asset=data.symbol[i])                
#        time_temp='12/31/2002' if first_df.shape[0]==0 else max(first_df['Date']).strftime('%m/%d/%Y') #convert datetime to string, need to tell string format
#        print('finished first_df\n')
#        eprint('finished first_df\n')
#        
#        second_df=extract_from_investing(start_date=time_temp,end_date='12/31/2014',asset=data.symbol[i])                
#        time_temp='12/31/2014' if second_df.shape[0]==0 else max(second_df['Date']).strftime('%m/%d/%Y') #convert datetime to string, need to tell string format
#        print('finished second_df\n')
#        eprint('finished second_df\n')
                          
        third_df=extract_from_investing(start_date='12/31/2018',end_date='12/31/2040',asset=data.symbol[i])
        #third_df=df_output.copy()
        #third_df=extract_from_investing(asset=data.symbol[i])
        print('finished third_df\n')
        eprint('finished third_df\n')
        
        #final_output=first_df.append(second_df,ignore_index=True)
        #final_output=final_output.append(third_df,ignore_index=True)
        final_output=third_df.copy()
        
        #below if loop is out of above second for loop
        if final_output.shape[0]!=0:
            final_output2=final_output.drop_duplicates(subset='Date',keep='last')
            final_output2=final_output2.sort_values(by=['Date'],ascending=[True])
            final_output2=final_output2.reset_index(drop=True)
            
            #for futures, need to append to cum file
            cumulated_data = read_excel(data.Name_use_python[i]+'.xlsx','Sheet1')            
            final_output2=cumulated_data.append(final_output2)
            final_output2=final_output2.drop_duplicates(subset='Date',keep='last')
            final_output2['Open']=final_output2['Open'].astype(float)
            final_output2['High']=final_output2['High'].astype(float)
            final_output2['Low']=final_output2['Low'].astype(float)
            final_output2['Close']=final_output2['Close'].astype(float)
            final_output2=final_output2.reset_index(drop=True)
            
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
            # Convert the dataframe to an XlsxWriter Excel object.
            final_output2.to_excel(writer, sheet_name='Sheet1')
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
            #copy source as back up to daily_source_data_production
            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
            final_output2.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            writer.close()
            eprint('Investing.com Finance Data Extraction ',asset_name,' ',count,' out of ',investingdotcom_source_total,'\n')
            print('Investing.com Finance Data Extraction ',asset_name,' ',count,' out of ',investingdotcom_source_total,'\n')
        else:
            eprint('Investing.com Finance Data Extraction ',asset_name,' not extracted/no data','\n')
            print('Investing.com Finance Data Extraction ',asset_name,' not extracted/no data','\n')
            
            
            









#this part is deal with 6 currency, which may not be timely from quandl at morning
#so download from euro central bank

#from lxml import etree
#import lxml.html as LH
import requests
import pandas as pd
import re
import datetime
from collections import OrderedDict

#i=293
#url = 'https://w...content-available-to-author-only...h.com/investing/fund/OTPSX'
for i in range(0,len(data.symbol)):
    if (data.Extract[i]=='Yes')&(data.Source[i]=='ECB')&(data.Type[i]=='currency'):
        output_df=pd.DataFrame([])
        for ii in range(0,20):
            try:
                request_link = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.zip?569f4e99b9b6e812e780f2dc232f1843'
                
                def fetch_multi_csv_zip_from_url(url, filenames=(), *args, **kwargs):
                    assert kwargs.get('compression') is None
                    req = urlopen(url,timeout=7)
                    zip_file = zipfile.ZipFile(BytesIO(req.read()))
                
                    if filenames:
                        names = zip_file.namelist()
                        for filename in filenames:
                            if filename not in names:
                                raise ValueError(
                                    'filename {} not in {}'.format(filename, names))
                    else:
                        filenames = zip_file.namelist()
                
                    return {name: pd.read_csv(zip_file.open(name), *args, **kwargs)
                            for name in filenames}
                    
                try:
                    from urllib.request import urlopen
                except ImportError:
                    from urllib2 import urlopen
                from io import BytesIO
                import zipfile
                import pandas as pd
                
                dfs = fetch_multi_csv_zip_from_url(request_link)
                output_df=dfs['eurofxref-hist.csv']
    
                if output_df.shape[0]!=0:break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i],'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting ",data.Name_use_python[i],'\n')

        no_of_trial=ii+1
        eprint(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')         
        print(data.Name_use_python[i].replace('_wsj',''),' tried ',no_of_trial,' times extraction with success','\n')          

        
        if output_df.shape[0]!=0:        
            output_df2=output_df[['Date',data.Name_use_python[i][-3:]]].copy()
            output_df2=output_df2.rename(columns={data.Name_use_python[i][-3:]:'Value'})
            
            output_df2['Date']=output_df2['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
            
            output_df2=output_df2.sort_values(by=['Date'],ascending=[True])
            output_df2=output_df2.reset_index(drop=True)
            
            writer = pd.ExcelWriter(os.path.join('backtest_linux/database/ECB',data.Name_use_python[i]+'.xlsx'), engine='xlsxwriter')
            
            # Convert the dataframe to an XlsxWriter Excel object.
            output_df2.to_excel(writer, sheet_name='Sheet1')
            
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            writer.close()
            
#            #copy source as back up to daily_source_data_production
#            writer = pd.ExcelWriter(os.path.join(target_dir,'daily_source_data_production',data.Name_use_python[i]+'_'+time_now_save+'.xlsx'), engine='xlsxwriter')
#            output_df2.to_excel(writer, sheet_name='Sheet1')
#            writer.save()
            
            
            eprint(data.Name_use_python[i],'from euro central bank downloded','\n')
            print(data.Name_use_python[i],'from euro central bank downloded','\n')
        else:
            eprint(data.Name_use_python[i],'no data from euro central bank','\n')
            print(data.Name_use_python[i],'no data from euro central bank','\n')       










##########################################
########extract fhsi from hkex############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np

from pyexcel.cookbook import merge_all_to_a_book
import glob


#this file accumulate record from hkex starting from 2019-01-02
fhsi_fixed_path=os.path.join(target_dir,'data','fhsi_20051202to_cum_with_OI.xlsx')
fhsi_fixed = read_excel(fhsi_fixed_path,'Sheet1')


today_day=time.strftime("%Y-%m-%d")
#today_day='2018-12-27'
#read trading calendar
calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)


settlement = read_excel('daily_prediction_production/calendar.xlsx','settlement')
settlement['settlement_day2']=settlement['settlement_day'].astype(str)

#find trading contract for each trading date
all_date_list=calendar['Date2'].values.tolist()
all_settlement_list=settlement['settlement_day2'].values
all_date_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_list]
calendar['settlement_contract']=all_date_found_settlement

#convert settlement_contract to string type, e.g. FEB 19
calendar['settlement_contract_another_format']=calendar['settlement_contract'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime('%b-%Y'))
calendar['settlement_contract_another_format']=calendar['settlement_contract_another_format'].apply(lambda x:x.split('-')[0].upper()+'-'+x.split('-')[1][-2:])



calendar=calendar.loc[(calendar['Date2']>='2019-01-02')&(calendar['Date2']<today_day),:]
all_date_original=calendar['Date2'].values.tolist()
all_date=[i[2:4]+i.split("-")[1]+i.split("-")[2] for i in all_date_original]






oi_path=os.path.join(target_dir,'data',"FHSI_HKEX","OI_from_HKEX")


j='200429'
for j in all_date:
    request_link="https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsif"+j+".zip"
    file_name="hsif"+j+".csv"
    file_name_xlsx="hsif"+j+".xlsx"
    file_path=os.path.join(oi_path,file_name)
    file_path_xlsx=os.path.join(oi_path,file_name_xlsx)
    output_df=pd.DataFrame([])
    #if the report is not in oi_path, then download
    if not os.path.exists(file_path):
        for ii in range(0,3):
            try:
                r = requests.get(request_link)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(oi_path)
                #sleep(0.5)            
                
                #convert to xlsx format because faile to read csv
                merge_all_to_a_book(glob.glob(file_path),file_path_xlsx)
                output_df=read_excel(file_path_xlsx)
                
                if output_df.shape[0]!=0:
                    print('downloaded ',j)
                    break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting hkex ",file_name,'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting hkex",file_name,'\n')







#if date in date_in_fhsi_fixed (from accumulated file) is not in calendar date (stored in all_date)
#then append hkex report to fhsi_fixed

date_in_fhsi_fixed=fhsi_fixed.Date2.values.tolist()

all_date_df=pd.DataFrame(all_date)
all_date_df['Date2']=all_date_original
all_date_df=all_date_df.rename(columns={0:'Date1'})
all_date_df['append']=all_date_df['Date2'].apply(lambda x:'no' if x in date_in_fhsi_fixed else 'yes')

all_date_append=all_date_df.loc[all_date_df['append']=='yes',:]
all_date_append=pd.merge(all_date_append,calendar[['Date2','settlement_contract_another_format']].copy(),
                         how='left',left_on=['Date2'],right_on=['Date2'])


#message_string='happy'
def send_an_email(message_string):
    #python send email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    mail_content = message_string
    #The mail addresses and password
    sender_address = 'random9522@gmail.com'
    sender_pass = '95229522'
    receiver_address = 'jonahthon.werwe1213@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'FHSI from HKEX'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()





#i=472
for i in range(0,all_date_append.shape[0]):
    date1=all_date_append['Date1'].values[i]
    date2=all_date_append['Date2'].values[i]
    
    datenum= (dt.strptime(date2,"%Y-%m-%d")-dt(1970,1,1)).days
    
    date_contract=all_date_append['settlement_contract_another_format'].values[i]
    file_name_xlsx="hsif"+date1+".xlsx"
    file_path_xlsx=os.path.join(oi_path,file_name_xlsx)
    
    if os.path.exists(file_path_xlsx):
        try:
            input_df=read_excel(file_path_xlsx)
            #remove first 5 columns
            cols = [1,2,3,4,5]
            input_df.drop(input_df.columns[cols],axis=1,inplace=True)
            
            input_df_As_column_name=input_df.loc[input_df['HANG SENG INDEX FUTURES DAILY MARKET REPORT (FINAL)']=='Contract Month',:].values.tolist()[0]
            input_df.columns=input_df_As_column_name
            
            OI=input_df.loc[input_df['Contract Month']==date_contract,'Open Interest'].values[0]
            OI_change=input_df.loc[input_df['Contract Month']==date_contract,'Change in OI'].values[0]
            OI_lag1=OI-OI_change
            
            #find next month contract
            find_number=input_df.loc[input_df['Contract Month']==date_contract,'Open Interest'].index.values[0]
            find_number_next_contract=find_number+1
            
            OI_next_contract=input_df['Open Interest'].values[find_number_next_contract:find_number_next_contract+1][0]
            if input_df['Change in OI'].values[find_number_next_contract:find_number_next_contract+1][0]=='-':
                OI_change_next_contract=0
            else:
                OI_change_next_contract=input_df['Change in OI'].values[find_number_next_contract:find_number_next_contract+1][0]
            OI_next_contract_lag1=OI_next_contract-OI_change_next_contract          
            
            openprice=input_df.loc[input_df['Contract Month']==date_contract,'*Open Price'].values[0]
            highprice=input_df.loc[input_df['Contract Month']==date_contract,'*Daily High'].values[0]    
            lowprice=input_df.loc[input_df['Contract Month']==date_contract,'*Daily Low'].values[0]    
            closeprice=input_df.loc[input_df['Contract Month']==date_contract,'Settlement Price'].values[0]
            vol=input_df.loc[input_df['Contract Month']==date_contract,'Volume'].values[0][0]  #use first volume
            
            #find next month volume
            vol_next_contract=input_df['Volume'].values[:,0][find_number_next_contract:find_number_next_contract+1][0]

            output_df=pd.DataFrame(OrderedDict({'Date2':[date2],'DateNum':[datenum],'Open':[openprice],'High':[highprice],'Low':[lowprice],
                                                'Close':[closeprice],'Volume':[vol],'Volume_next_contract':[vol_next_contract],'OI':[OI],'OI_lag1':[OI_lag1],'OI_next_contract':[OI_next_contract],'OI_next_contract_lag1':[OI_next_contract_lag1]}))
            
            output_df_string= "HKEX report "+ date2+' Open '+str(openprice)+' Close '+str(closeprice)+' OI '+str(OI)+' OI_lag1 '+str(OI_lag1)+' Volume '+str(vol)
            send_an_email(output_df_string)
            
            #check is numeric and sensible
            if ((type(OI)==int)&(type(OI_lag1)==int)&(type(openprice)==int)&
                (type(highprice)==int)&(type(lowprice)==int)&(type(closeprice)==int)&(type(vol)==int)):
            
                fhsi_fixed=fhsi_fixed.append(output_df)
                print("appended ",date2, " to fhsi_20051202to_cum_with_OI.xlsx successful")
            else:
                raise ValueError('one of the values may not be integer')
        except:
            eprint("Oops!",sys.exc_info()[0],sys.exc_info()[1]," problem occur when reading and extracting ",file_name_xlsx,'\n')
            print("Oops!",sys.exc_info()[0],sys.exc_info()[1]," problem occur when reading and extracting ",file_name_xlsx,'\n')
            
    else:
        print("error, file not fount ",file_name_xlsx)





#drop duplicate
fhsi_fixed=fhsi_fixed.drop_duplicates()
fhsi_fixed=fhsi_fixed.reset_index(drop=True)



#save to cumulative
#output fhsi_fixed
writer = pd.ExcelWriter(fhsi_fixed_path, engine='xlsxwriter')
fhsi_fixed.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


#need to change a bit format, because save to index_analsis
fhsi_fixed=fhsi_fixed.rename(columns={'Date2':'Date'})
fhsi_fixed['Date']=fhsi_fixed['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))

#also save to index_analsis
output_path=os.path.join('backtest_linux/database/hkex','HSI.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
fhsi_fixed[['Date','Open','High','Low','Close']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()

#also save to index_analsis
output_path=os.path.join('backtest_linux/database/hkex','hang_seng_oi.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
fhsi_fixed[['Date','OI','OI_lag1','OI_next_contract','OI_next_contract_lag1']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()

#also save to index_analsis as volume
output_path=os.path.join('backtest_linux/database/hkex','hang_seng_oi_volume.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
fhsi_fixed[['Date','OI','OI_lag1','Volume','Volume_next_contract']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()







##########################################
########extract hhi from hkex############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np

from pyexcel.cookbook import merge_all_to_a_book
import glob
from collections import OrderedDict


#this file accumulate record from hkex starting from 2019-01-02
hhi_fixed_path=os.path.join(target_dir,'data','hhi_20051103_to_cum.xlsx')
hhi_fixed = read_excel(hhi_fixed_path,'Sheet1')


today_day=time.strftime("%Y-%m-%d")
#today_day='2018-12-27'
#read trading calendar
calendar = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)


settlement = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','settlement')
settlement['settlement_day2']=settlement['settlement_day'].astype(str)

#find trading contract for each trading date
all_date_list=calendar['Date2'].values.tolist()
all_settlement_list=settlement['settlement_day2'].values
all_date_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_list]
calendar['settlement_contract']=all_date_found_settlement

#convert settlement_contract to string type, e.g. FEB 19
calendar['settlement_contract_another_format']=calendar['settlement_contract'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime('%b-%Y'))
calendar['settlement_contract_another_format']=calendar['settlement_contract_another_format'].apply(lambda x:x.split('-')[0].upper()+'-'+x.split('-')[1][-2:])



calendar=calendar.loc[(calendar['Date2']>='2019-01-02')&(calendar['Date2']<today_day),:]
all_date_original=calendar['Date2'].values.tolist()
all_date=[i[2:4]+i.split("-")[1]+i.split("-")[2] for i in all_date_original]






oi_path=os.path.join(target_dir,'data',"HHI_HKEX","OI_from_HKEX")


j='200429'
for j in all_date:
    request_link="https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hhif"+j+".zip"
    file_name="hhif"+j+".csv"
    file_name_xlsx="hhif"+j+".xlsx"
    file_path=os.path.join(oi_path,file_name)
    file_path_xlsx=os.path.join(oi_path,file_name_xlsx)
    output_df=pd.DataFrame([])
    #if the report is not in oi_path, then download
    if not os.path.exists(file_path):
        for ii in range(0,3):
            try:
                r = requests.get(request_link)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(oi_path)
                #sleep(0.5)            
                
                #convert to xlsx format because faile to read csv
                merge_all_to_a_book(glob.glob(file_path),file_path_xlsx)
                output_df=read_excel(file_path_xlsx)
                
                if output_df.shape[0]!=0:
                    print('downloaded ',j)
                    break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting hkex ",file_name,'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting hkex",file_name,'\n')







#if date in date_in_hhi_fixed (from accumulated file) is not in calendar date (stored in all_date)
#then append hkex report to hhi_fixed

date_in_hhi_fixed=hhi_fixed.Date2.values.tolist()

all_date_df=pd.DataFrame(all_date)
all_date_df['Date2']=all_date_original
all_date_df=all_date_df.rename(columns={0:'Date1'})
all_date_df['append']=all_date_df['Date2'].apply(lambda x:'no' if x in date_in_hhi_fixed else 'yes')

all_date_append=all_date_df.loc[all_date_df['append']=='yes',:]
all_date_append=pd.merge(all_date_append,calendar[['Date2','settlement_contract_another_format']].copy(),
                         how='left',left_on=['Date2'],right_on=['Date2'])


#message_string='happy'
def send_an_email(message_string):
    #python send email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    mail_content = message_string
    #The mail addresses and password
    sender_address = 'random9522@gmail.com'
    sender_pass = '95229522'
    receiver_address = 'jonahthon.werwe1213@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'HHI from HKEX'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()





#i=0
for i in range(0,all_date_append.shape[0]):
    date1=all_date_append['Date1'].values[i]
    date2=all_date_append['Date2'].values[i]
    
    datenum= (dt.strptime(date2,"%Y-%m-%d")-dt(1970,1,1)).days
    
    date_contract=all_date_append['settlement_contract_another_format'].values[i]
    file_name_xlsx="hhif"+date1+".xlsx"
    file_path_xlsx=os.path.join(oi_path,file_name_xlsx)
    
    if os.path.exists(file_path_xlsx):
        try:
            input_df=read_excel(file_path_xlsx)
            #remove first 5 columns
            cols = [1,2,3,4,5]
            input_df.drop(input_df.columns[cols],axis=1,inplace=True)
            
            input_df_As_column_name=input_df.loc[input_df['HANG SENG CHINA ENTERPRISES INDEX FUTURES DAILY MARKET REPORT (FINAL)']=='Contract Month',:].values.tolist()[0]
            input_df.columns=input_df_As_column_name
            
            OI=input_df.loc[input_df['Contract Month']==date_contract,'Open Interest'].values[0]
            OI_change=input_df.loc[input_df['Contract Month']==date_contract,'Change in OI'].values[0]
            OI_lag1=OI-OI_change
            
            openprice=input_df.loc[input_df['Contract Month']==date_contract,'*Open Price'].values[0]
            highprice=input_df.loc[input_df['Contract Month']==date_contract,'*Daily High'].values[0]    
            lowprice=input_df.loc[input_df['Contract Month']==date_contract,'*Daily Low'].values[0]    
            closeprice=input_df.loc[input_df['Contract Month']==date_contract,'Settlement Price'].values[0]
            vol=input_df.loc[input_df['Contract Month']==date_contract,'Volume'].values[0][0]  #use first volume

            output_df=pd.DataFrame(OrderedDict({'Date2':[date2],'DateNum':[datenum],'Open':[openprice],'High':[highprice],'Low':[lowprice],
                                                'Close':[closeprice],'Volume':[vol],'OI':[OI],'OI_lag1':[OI_lag1]}))
            
            output_df_string= "HKEX report "+ date2+' Open '+str(openprice)+' Close '+str(closeprice)+' OI '+str(OI)+' OI_lag1 '+str(OI_lag1)+' Volume '+str(vol)
            #send_an_email(output_df_string)
            
            #check is numeric and sensible
            if ((type(OI)==int)&(type(OI_lag1)==int)&(type(openprice)==int)&
                (type(highprice)==int)&(type(lowprice)==int)&(type(closeprice)==int)&(type(vol)==int)):
            
                hhi_fixed=hhi_fixed.append(output_df)
                print("appended ",date2, " to hhi_unknown_start_to_cum_with_OI.xlsx successful")
            else:
                raise ValueError('one of the values may not be integer')
        except:
            eprint("Oops!",sys.exc_info()[0],sys.exc_info()[1]," problem occur when reading and extracting ",file_name_xlsx,'\n')
            print("Oops!",sys.exc_info()[0],sys.exc_info()[1]," problem occur when reading and extracting ",file_name_xlsx,'\n')
            
    else:
        print("error, file not fount ",file_name_xlsx)





#drop duplicate
hhi_fixed=hhi_fixed.drop_duplicates()
hhi_fixed=hhi_fixed.reset_index(drop=True)



#save to cumulative
#output hhi_fixed
writer = pd.ExcelWriter(hhi_fixed_path, engine='xlsxwriter')
hhi_fixed.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


#need to change a bit format, because save to index_analsis
hhi_fixed=hhi_fixed.rename(columns={'Date2':'Date'})
hhi_fixed['Date']=hhi_fixed['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))

#also save to index_analsis
output_path=os.path.join(target_dir,'HHI.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
hhi_fixed[['Date','Open','High','Low','Close']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()


#also save to index_analsis
output_path=os.path.join(target_dir,'hhi_oi.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
hhi_fixed[['Date','OI','OI_lag1']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()












##########################################
########extract hsi option from hkex############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np

from pyexcel.cookbook import merge_all_to_a_book
import glob
from collections import OrderedDict




today_day=time.strftime("%Y-%m-%d")
#today_day='2018-12-27'
#read trading calendar
calendar = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)


settlement = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','settlement')
settlement['settlement_day2']=settlement['settlement_day'].astype(str)

#find trading contract for each trading date
all_date_list=calendar['Date2'].values.tolist()
all_settlement_list=settlement['settlement_day2'].values
all_date_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_list]
calendar['settlement_contract']=all_date_found_settlement

#convert settlement_contract to string type, e.g. FEB 19
calendar['settlement_contract_another_format']=calendar['settlement_contract'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime('%b-%Y'))
calendar['settlement_contract_another_format']=calendar['settlement_contract_another_format'].apply(lambda x:x.split('-')[0].upper()+'-'+x.split('-')[1][-2:])



calendar=calendar.loc[(calendar['Date2']>='2019-01-02')&(calendar['Date2']<today_day),:]
all_date_original=calendar['Date2'].values.tolist()
all_date=[i[2:4]+i.split("-")[1]+i.split("-")[2] for i in all_date_original]






oi_path=os.path.join(target_dir,'data',"HSIOption_HKEX","Daily_option_report")


j='200429'
for j in all_date:
    request_link="https://www.hkex.com.hk/eng/stat/dmstat/dayrpt/hsio"+j+".zip"
    file_name="hsio"+j+".csv"
    file_name_xlsx="hsio"+j+".xlsx"
    file_path=os.path.join(oi_path,file_name)
    file_path_xlsx=os.path.join(oi_path,file_name_xlsx)
    output_df=pd.DataFrame([])
    #if the report is not in oi_path, then download
    if not os.path.exists(file_path):
        for ii in range(0,3):
            try:
                r = requests.get(request_link)
                z = zipfile.ZipFile(io.BytesIO(r.content))
                z.extractall(oi_path)
                #sleep(0.5)            
                
                #convert to xlsx format because faile to read csv
                merge_all_to_a_book(glob.glob(file_path),file_path_xlsx)
                output_df=read_excel(file_path_xlsx)
                
                if output_df.shape[0]!=0:
                    print('downloaded ',j)
                    break
            except:
                eprint("Oops!",sys.exc_info()[0],"occured when extracting hkex ",file_name,'\n')
                print("Oops!",sys.exc_info()[0],"occured when extracting hkex",file_name,'\n')








#find option put call ratio

from pandas import read_excel
import pandas as pd
import os
import numpy as np

from pyexcel.cookbook import merge_all_to_a_book
import glob
from collections import OrderedDict




today_day=time.strftime("%Y-%m-%d")
#today_day='2018-12-27'
#read trading calendar
calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar')
calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)


settlement = read_excel('daily_prediction_production/calendar.xlsx','settlement')
settlement['settlement_day2']=settlement['settlement_day'].astype(str)

#find trading contract for each trading date
all_date_list=calendar['Date2'].values.tolist()
all_settlement_list=settlement['settlement_day2'].values
all_date_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_list]
calendar['settlement_contract']=all_date_found_settlement

#convert settlement_contract to string type, e.g. FEB 19
calendar['settlement_contract_another_format']=calendar['settlement_contract'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime('%b-%Y'))
calendar['settlement_contract_another_format']=calendar['settlement_contract_another_format'].apply(lambda x:x.split('-')[0].upper()+'-'+x.split('-')[1][-2:])



calendar=calendar.loc[(calendar['Date2']>='2019-01-02')&(calendar['Date2']<today_day),:]
all_date_original=calendar['Date2'].values.tolist()
all_date=[i[2:4]+i.split("-")[1]+i.split("-")[2] for i in all_date_original]






oi_path=os.path.join('data',"HSIOption_HKEX","Daily_option_report")


j='190102'
output_df=pd.DataFrame([])
for ind,j in enumerate(all_date):
    date2=calendar['Date2'].values[ind]
    datenum= (dt.strptime(date2,"%Y-%m-%d")-dt(1970,1,1)).days
    file_name_xlsx="hsio"+j+".xlsx"
    file_path_xlsx=os.path.join(oi_path,file_name_xlsx)
    if os.path.exists(file_path_xlsx):
        input_df=read_excel(file_path_xlsx)
        input_df_use=input_df.loc[input_df['Unnamed: 15']=='MONTH PUT/CALL RATIO',:]
        pc_ratio=input_df_use['Unnamed: 17'].values[0]
        
    
        output_df=output_df.append(pd.DataFrame(OrderedDict({'Date':[date2],'DateNum':[datenum],'pc_ratio':[pc_ratio]})))
    print(j)


#need to change a bit format, because save to index_analsis
output_df=output_df.rename(columns={'Date2':'Date'})
output_df['Date']=output_df['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))

#also save to index_analsis
output_path=os.path.join(target_dir,'pc_ratio.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
output_df[['Date','pc_ratio']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()



















##########################################
########extract n225############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen

from pyexcel.cookbook import merge_all_to_a_book
import glob


#read n225 from 2004-01-01
#n225_fixed_path=os.path.join(target_dir,'data','n225_futures','N225_futures_from_barchart.xlsx')
#n225_fixed = read_excel(n225_fixed_path,'Sheet1')
#n225_fixed=n225_fixed.rename(columns={'Last':'Close'})

n225_fixed_path=os.path.join(target_dir,'data','n225_futures','n225_futures_cum.xlsx')
n225_fixed = read_excel(n225_fixed_path,'Sheet1')


#drop duplicate
n225_fixed=n225_fixed.drop_duplicates()
n225_fixed=n225_fixed.reset_index(drop=True)


today_day=time.strftime("%Y-%m-%d")
#today_day='2018-12-27'
#read trading calendar
calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar_japan')

calendar['Date2']=calendar['Date'].astype(str)
calendar=calendar.loc[calendar['Date2']>='2021-01-01',:].copy()
calendar=calendar.loc[calendar['trading_date']==1,:]
calendar=calendar.reset_index(drop=True)


settlement = read_excel('daily_prediction_production/calendar.xlsx','settlement_japan')
settlement['settlement_day2']=settlement['settlement_day_two_day_before'].astype(str)

#find trading contract for each trading date
all_date_list=calendar['Date2'].values.tolist()
all_settlement_list=settlement['settlement_day2'].values
all_date_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_list]
calendar['settlement_contract']=all_date_found_settlement

#convert settlement_contract to string type, e.g. FEB 19
calendar['settlement_contract_another_format']=calendar['settlement_contract'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime('%b.%Y'))



calendar=calendar.loc[(calendar['Date2']==today_day),:]
target_day=calendar['Date2'].values.tolist()[-1]  #find out previous day
target_contractmonth=calendar['settlement_contract_another_format'].values.tolist()[-1] #find which contract










url = 'https://port.jpx.co.jp/jpx/template/quote.cgi?F=tmp/e_future_daytime'
html_page = urlopen(url,timeout=7)
soup = BeautifulSoup(html_page, "html.parser")
table = soup.find_all('div', {'class':'component-normal-table'})[0] # Grab the first table

months_all = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

r1=table.find_all('tr')[2]

r1_use=r1.find_all('td')
r1_use_text=[x.get_text() for x in r1_use]
r1_use_text

date1_year=int('20'+r1_use_text[1].split("'")[1].split('/')[0])
date1_contract=months_all[int(r1_use_text[1].split("'")[1].split('/')[1])-1]+'.'+str(date1_year)
date1_month=int(r1_use_text[2].replace('\r','').replace('\t','').split('/')[0])
date1_day=int(r1_use_text[2].replace('\r','').replace('\t','').split('/')[1])
open1=int(r1_use_text[3].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
high1=int(r1_use_text[4].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
low1=int(r1_use_text[5].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
close1=int(r1_use_text[6].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
vol1=int(r1_use_text[8].replace('\r','').replace('\t','').replace(',',''))
oi1=int(r1_use_text[15].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
oi1_month=int(r1_use_text[15].replace('\r','').replace('\t','').split('(')[1].split(')')[0].split('/')[0])
oi1_day=int(r1_use_text[15].replace('\r','').replace('\t','').split('(')[1].split(')')[0].split('/')[1])

df1=pd.DataFrame({'Date2':[dt(date1_year,date1_month,date1_day).strftime("%Y-%m-%d")],
                  'contractmonth':[date1_contract],
                  'Open':[open1],
                  'High':[high1],
                  'Low':[low1],
                  'Close':[close1],
                  'Volume':[vol1],
                  'OI':[oi1]})




r1=table.find_all('tr')[3]

r1_use=r1.find_all('td')
r1_use_text=[x.get_text() for x in r1_use]
r1_use_text=['nothing']+r1_use_text

date1_year=int('20'+r1_use_text[1].split("'")[1].split('/')[0])
date1_contract=months_all[int(r1_use_text[1].split("'")[1].split('/')[1])-1]+'.'+str(date1_year)
date1_month=int(r1_use_text[2].replace('\r','').replace('\t','').split('/')[0])
date1_day=int(r1_use_text[2].replace('\r','').replace('\t','').split('/')[1])
open1=int(r1_use_text[3].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
high1=int(r1_use_text[4].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
low1=int(r1_use_text[5].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
close1=int(r1_use_text[6].replace('\r','').replace('\t','').split('(')[0].replace(',',''))
vol1=int(r1_use_text[8].replace('\r','').replace('\t','').replace(',',''))
oi1=int(r1_use_text[15].replace('\r','').replace('\t','').split('(')[0].replace(',',''))

df2=pd.DataFrame({'Date2':[dt(date1_year,date1_month,date1_day).strftime("%Y-%m-%d")],
                  'contractmonth':[date1_contract],
                  'Open':[open1],
                  'High':[high1],
                  'Low':[low1],
                  'Close':[close1],
                  'Volume':[vol1],
                  'OI':[oi1]})


df1=df1.append(df2)
df1=df1.loc[(df1['contractmonth']==target_contractmonth)&(df1['Date2']==target_day),:].copy()


if (df1.shape[0]!=0)&(oi1_month==date1_month)&(oi1_day==date1_day):
    del df1['contractmonth']
    
    #append to cum
    n225_fixed=n225_fixed.append(df1)
    n225_fixed=n225_fixed.reset_index(drop=True)
    
    #drop duplicate
    n225_fixed=n225_fixed.drop_duplicates(subset=['Date2'], keep='last')
    n225_fixed=n225_fixed.reset_index(drop=True)

    output_df_string= "ose.jpx report "+ n225_fixed.Date2.values[-1]+' '+'open-'+str(n225_fixed.Open.values[-1])+' '+'close-'+str(n225_fixed.Close.values[-1])+' '+'vol-'+str(n225_fixed.Volume.values[-1])+' '+'OI-'+str(n225_fixed.OI.values[-1])


    #save to cumulative
    #output n225_fixed
    writer = pd.ExcelWriter(n225_fixed_path, engine='xlsxwriter')
    n225_fixed.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    writer.close()
    
    
    #need to change a bit format, because save to index_analsis
    n225_fixed=n225_fixed.rename(columns={'Date2':'Date'})
    n225_fixed['Date']=n225_fixed['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
    
    #also save to index_analsis
    output_path=os.path.join(target_dir,'n225.xlsx')
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    n225_fixed[['Date','Open','High','Low','Close','Volume','OI']].copy().to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    writer.close()
    
    #also save to index_analsis
    output_path=os.path.join(target_dir,'n225_oi.xlsx')
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    n225_fixed[['Date','Open','High','Low','Close','Volume','OI']].copy().to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    writer.close()
    
    #also save to index_analsis as volume
    output_path=os.path.join(target_dir,'n225_oi_volume.xlsx')
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    n225_fixed[['Date','Open','High','Low','Close','Volume','OI']].copy().to_excel(writer, sheet_name='Sheet1')
    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    writer.close()    
    
    
    
else:
    print('jpx website no ',target_day,' or OI date not match today')
    eprint('jpx website no ',target_day,' or OI date not match today')
    output_df_string='jpx website no ' +target_day



#message_string='happy'
def send_an_email(message_string):
    #python send email
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    mail_content = message_string
    #The mail addresses and password
    sender_address = 'random9522@gmail.com'
    sender_pass = '95229522'
    receiver_address = 'jonahthon.werwe1213@gmail.com'
    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'n225 from ose.jpx'   #The subject line
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content))

    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()


send_an_email(output_df_string)













##########################################
########extract n225 10 mins############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen

from pyexcel.cookbook import merge_all_to_a_book
import glob


#read n225 from 2004-01-01
#n225_fixed_path=os.path.join(target_dir,'data','n225_futures','N225_futures_from_barchart.xlsx')
#n225_fixed = read_excel(n225_fixed_path,'Sheet1')
#n225_fixed=n225_fixed.rename(columns={'Last':'Close'})

n225_fixed_path=os.path.join(target_dir,'data','n225_futures','n225_futures_10am_cum.xlsx')
n225_fixed = read_excel(n225_fixed_path,'Sheet1')


#drop duplicate
n225_fixed=n225_fixed.drop_duplicates()
n225_fixed=n225_fixed.reset_index(drop=True)


#need to change a bit format, because save to index_analsis
n225_fixed=n225_fixed.rename(columns={'Date2':'Date'})
n225_fixed['Date']=n225_fixed['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))

#also save to index_analsis
output_path=os.path.join('backtest_linux/database/jpx','n225_10am.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
n225_fixed[['Date','Open','High','Low','Close','Volume']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()






##########################################
########extract n225 0_to_15 mins############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen

from pyexcel.cookbook import merge_all_to_a_book
import glob


#read n225 from 2004-01-01
#n225_fixed_path=os.path.join(target_dir,'data','n225_futures','N225_futures_from_barchart.xlsx')
#n225_fixed = read_excel(n225_fixed_path,'Sheet1')
#n225_fixed=n225_fixed.rename(columns={'Last':'Close'})

n225_fixed_path=os.path.join(target_dir,'data','n225_futures','n225_futures_0_to_15_cum.xlsx')
n225_fixed = read_excel(n225_fixed_path,'Sheet1')


#drop duplicate
n225_fixed=n225_fixed.drop_duplicates()
n225_fixed=n225_fixed.reset_index(drop=True)


#need to change a bit format, because save to index_analsis
n225_fixed=n225_fixed.rename(columns={'Date2':'Date'})
n225_fixed['Date']=n225_fixed['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))

#also save to index_analsis
output_path=os.path.join('backtest_linux/database/jpx','n225_0_to_15.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
n225_fixed[['Date','Open','High','Low','Close','Volume']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()








##########################################
########extract n225 0_to_60 mins############
##########################################
from pandas import read_excel
import pandas as pd
import os
import numpy as np
from bs4 import BeautifulSoup
from urllib.request import urlopen

from pyexcel.cookbook import merge_all_to_a_book
import glob


#read n225 from 2004-01-01
#n225_fixed_path=os.path.join(target_dir,'data','n225_futures','N225_futures_from_barchart.xlsx')
#n225_fixed = read_excel(n225_fixed_path,'Sheet1')
#n225_fixed=n225_fixed.rename(columns={'Last':'Close'})

n225_fixed_path=os.path.join(target_dir,'data','n225_futures','n225_futures_0_to_60_cum.xlsx')
n225_fixed = read_excel(n225_fixed_path,'Sheet1')


#drop duplicate
n225_fixed=n225_fixed.drop_duplicates()
n225_fixed=n225_fixed.reset_index(drop=True)


#need to change a bit format, because save to index_analsis
n225_fixed=n225_fixed.rename(columns={'Date2':'Date'})
n225_fixed['Date']=n225_fixed['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))

#also save to index_analsis
output_path=os.path.join('backtest_linux/database/jpx','n225_0_to_60.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
n225_fixed[['Date','Open','High','Low','Close','Volume']].copy().to_excel(writer, sheet_name='Sheet1')
# Close the Pandas Excel writer and output the Excel file.
writer.save()
writer.close()









##merge with data_back_up_20180420, not include HSI, HSI made above
##i=2462
#cumulated_data_folder='data_back_up_20201218'
#cumulated_data_folder_path=os.path.join(target_dir,cumulated_data_folder)
#
#total_extract_yes=data.loc[(data['Extract']=='Yes')&(data['Name_use_python']!='HSI')&(data['Name_use_python']!='hang_seng_oi'),:].shape[0]
#count=0
#for i in range(0,len(data.symbol)):
#    if (data.Extract[i]=='Yes')&(data.Name_use_python[i]!='HSI'):
#        cumulated_data_path=os.path.join(cumulated_data_folder_path,data.Name_use_python[i]+'.xlsx')
#        count=count+1
#        if os.path.exists(cumulated_data_path):
#            cumulated_data = read_excel(cumulated_data_path,'Sheet1')
#            cumulated_data=cumulated_data.sort_values(by='Date',ascending=True)
#            cumulated_data=cumulated_data.reset_index(drop=True)
#            cumulated_data_latest_date=cumulated_data.loc[cumulated_data.shape[0]-1,['Date']][0]
#            #cumulated_data=cumulated_data.loc[cumulated_data['Date']<=cumulated_data_latest_date,:]
#            
#            latest_data_path=os.path.join(target_dir,data.Name_use_python[i]+'.xlsx')
#            latest_data = read_excel(latest_data_path,'Sheet1')
#            #find the latest date on backup file, and merge all date greater than latest date to it
#            latest_data=latest_data.loc[latest_data['Date']>cumulated_data_latest_date,:]
#    
#            #merge together
#            all_data=pd.concat([cumulated_data,latest_data],axis=0)
#            all_data=all_data.reset_index(drop=True)
#    
#            #save file
#            writer = pd.ExcelWriter(data.Name_use_python[i]+'.xlsx', engine='xlsxwriter')
#            all_data.to_excel(writer, sheet_name='Sheet1')
#            writer.save()
#            eprint('Merge with '+cumulated_data_folder+' ',count,' out of ',total_extract_yes,'\n')
#            print('Merge with '+cumulated_data_folder+' ',count,' out of ',total_extract_yes,'\n')
        







    









##inport HIBOR rate
##https://www.analystz.hk/indicators/hibor.php
#hibor_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hibor.txt"
#text_file = open(hibor_path, "r")
# 
#import ast
#with open(hibor_path, 'r') as f:
#    mylist = ast.literal_eval(f.read())
# 
#hibor = pd.DataFrame(mylist)
#
#hibor.isnull().values.any()
#hibor=hibor.rename(columns={'date':'Date','gab':'aggregated_balance','gmb':'monetary_base'})
#
#all_assets=list(hibor.columns.values)
#all_assets.remove('Date')
#
#i='g12M'
#for i in all_assets:
#    temp=hibor[['Date',i]]
#    temp=temp.rename(columns={i:'Close'})
#    temp['Open']=temp['Close'].shift(1)
#    #temp=temp.loc[~(np.isnan(temp['Open'])|np.isnan(temp['Close'])),:]
#    temp['Date']=temp['Date'].apply(lambda x:datetime.strptime(x, '%Y-%m-%d'))
#    writer = pd.ExcelWriter(i+'.xlsx', engine='xlsxwriter')
#    # Convert the dataframe to an XlsxWriter Excel object.
#    temp.to_excel(writer, sheet_name='Sheet1')
#    # Close the Pandas Excel writer and output the Excel file.
#    writer.save()















##quandl FHSI only start from 2017-07-16 so need to merge to
##FHSI_20051201to2020180413.xlsx
##,whcih is merge manually by fhsi_from_optionwalker_from20061228to20180413.xlsx #https://www.optionwalker.com/sharings
##and FHSI20051104-20131209 Daily_investigate.xlsx #long time ago from wilson
#from pandas import read_excel
#import pandas as pd
#import os
#import numpy as np
#fhsi_previous_path=os.path.join(target_dir,'data','FHSI_20051201to2020180413.xlsx')
#fhsi_previous = read_excel(fhsi_previous_path,'Sheet1')
#fhsi_previous=fhsi_previous.sort_values(by='Date',ascending=True)
#fhsi_previous=fhsi_previous.reset_index(drop=True)
#
#fhsi_latest_path=os.path.join(target_dir,'HSI.xlsx')
#fhsi_latest = read_excel(fhsi_latest_path,'Sheet1')
#
##if first time dowmload HSI in morning, 'Prev. Day Settlement Price' in columns
#if 'Prev. Day Settlement Price' in list(fhsi_latest.columns.values):
#    fhsi_latest=fhsi_latest.rename(columns={'Prev. Day Settlement Price':'Close'})
#    
##after first time dowmload HSI in morning,'Settle' in columns 
#if 'Settle' in list(fhsi_latest.columns.values):
#    fhsi_latest=fhsi_latest.rename(columns={'Settle':'Close'})
#
#
#fhsi_latest['Date2']=fhsi_latest['Date'].astype(str)
#fhsi_latest_use=fhsi_latest[['Date','Date2','Open','High','Low','Close']].copy()
#
#fhsi_latest_use=fhsi_latest_use.loc[fhsi_latest_use['Date']>'2018-04-01',:]
#del fhsi_latest_use['Date2']
#fhsi_latest_use=fhsi_latest_use.reset_index(drop=True)
#
#fhsi_new=pd.concat([fhsi_previous,fhsi_latest_use],axis=0)
#fhsi_new.drop_duplicates(subset='Date',inplace=True)
#fhsi_new=fhsi_new.reset_index(drop=True)
#
#fhsi_new=fhsi_new.rename(columns={'Close':'Settle'})
#
#output_path=os.path.join(target_dir,'HSI.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
## Convert the dataframe to an XlsxWriter Excel object.
#fhsi_new.to_excel(writer, sheet_name='Sheet1')
## Close the Pandas Excel writer and output the Excel file.
#writer.save()









#############################
########Production Mode######
#############################
#production mode will create a new row, which is new_date defined below
#so that factor value can be merged for predicting 
#in this new row, close is 101, open is 100, pnl is 1 only so less effect if this
#included in backtest mistakenly. note this this row just dummy and fake

#production_mode=False
#
#if production_mode==True:
#    currentDay = dt.now().day
#    currentMonth = dt.now().month
#    currentYear = dt.now().year
#    new_date=dt(currentYear,currentMonth,currentDay)
#    hsi_old=read_excel('HSI'+'.xlsx','Sheet1')
#    #in yahoo finance, say now is 6/4/2018 morning 8:30am
#    #HSI already has row 6/4/2018 but value is fake, the same as previous day
#    #so remove it and just assign 100 to it.
#    hsi_old=hsi_old.loc[hsi_old['Date']!=new_date,:]
#    hsi_old=hsi_old.append({'Date':new_date,'Open':100,'High':100,'Low':100,'Close':101}, ignore_index=True)
#    hsi_old=hsi_old.reset_index(drop=True)
#    writer = pd.ExcelWriter('HSI'+'.xlsx', engine='xlsxwriter')
#    # Convert the dataframe to an XlsxWriter Excel object.
#    hsi_old.to_excel(writer, sheet_name='Sheet1')
#    # Close the Pandas Excel writer and output the Excel file.
#    writer.save()



















##seperate data into morning and afternoon session
#folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
#
#fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")
#
##fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
#store = pd.HDFStore(fn)
#print(store)
#data_all_final= store.select('FHSI_minute')
# 
#store.close()
#
#
#data_all_final_check=data_all_final.head(10)
#data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
#data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})
#
#
#data_use=data.loc[data['Date2']=='2015-01-02',:]
#data_use=data.loc[data['Date2']=='2020-11-12',:]
#data_use=data_use.reset_index(drop=True)
#
#def split_morning_afternoon(data_use):
#    data_use2=data_use.copy()
#    data_use2['Date1_shift1']=data_use2['Date1'].shift(1)
#    data_use2['time_diff']=data_use2['Date1']-data_use2['Date1_shift1']
#    data_use2['time_diff_min']=data_use2['time_diff'].apply(lambda x:x.total_seconds()/60)
#
#    date_out=data_use2['Date2'].values[0]
#    print(date_out)
#
#    ind=data_use2['time_diff_min']>=60
#    ind=ind[ind==True]
#    ind_size=len(ind)
#    
#    
#    minute_threshold=1
#    
#    if ind_size!=0:
#        ind=ind.index[0]
#        
##        #below use threshold 1 min
##        #means morning start from 0915 to 1159, afternoon start from 1159 to last minute
##        data_use2_morning=data_use2.iloc[0:ind-minute_threshold]
##        data_use2_afternoon1=data_use2.iloc[ind-minute_threshold:ind]   
##        data_use2_afternoon2=data_use2.iloc[ind:-minute_threshold]  
##        data_use2_afternoon3=data_use2.iloc[-minute_threshold:]   
##        
##        open_morning=data_use2_morning['Open'].values[0]
##        high_morning=np.max(data_use2_morning['High'].values)
##        low_morning=np.min(data_use2_morning['Low'].values)
##        close_morning=data_use2_morning['Close'].values[-1]
##        
##        #open afternoon
##        data_use2_afternoon1=data_use2_afternoon1.head(minute_threshold)
##        data_use2_afternoon1['mean']=(data_use2_afternoon1['High']+data_use2_afternoon1['Low']+data_use2_afternoon1['Open']+data_use2_afternoon1['Close'])/4
##        open_afternoon=np.mean(data_use2_afternoon1['mean'].values)
##        
##        high_afternoon=np.max(data_use2_afternoon2['High'].values)
##        low_afternoon=np.min(data_use2_afternoon2['Low'].values)
##        
##        data_use2_afternoon3=data_use2_afternoon3.head(minute_threshold)
##        data_use2_afternoon3['mean']=(data_use2_afternoon3['High']+data_use2_afternoon3['Low']+data_use2_afternoon3['Open']+data_use2_afternoon3['Close'])/4
##        close_afternoon=np.mean(data_use2_afternoon3['mean'].values)
#        
#        #below use fix point
#        data_use2_morning=data_use2.iloc[0:ind-1]  
#        data_use2_afternoon1=data_use2.iloc[ind-1:]    
#        
#        open_morning=data_use2_morning['Open'].values[0]     
#        high_morning=np.max(data_use2_morning['High'].values)
#        low_morning=np.min(data_use2_morning['Low'].values)
#        close_morning=data_use2_morning['Open'].values[-1]    #use 1158 open
#        
#        open_afternoon=data_use2_afternoon1['Close'].values[0]   #use 1159 close
#        high_afternoon=np.max(data_use2_afternoon1['High'].values[1:])
#        low_afternoon=np.min(data_use2_afternoon1['Low'].values[1:])
#        close_afternoon=data_use2_afternoon1['Close'].values[-1]
#        
#    else:
#        open_morning=0
#        high_morning=0
#        low_morning=0
#        close_morning=0
#
#        open_afternoon=0
#        high_afternoon=0
#        low_afternoon=0
#        close_afternoon=0
#        
#    output=pd.DataFrame({'Date2':[date_out],
#                         'Open1':[open_morning],
#                         'High1':[high_morning],
#                         'Low1':[low_morning],
#                         'Close1':[close_morning],
#                         'Open2':[open_afternoon],
#                         'High2':[high_afternoon],
#                         'Low2':[low_afternoon],
#                         'Close2':[close_afternoon],
#                         'ind_size':[ind_size]})
#    
#    return output
#
#temp1=data.groupby("Date2").apply(lambda x:split_morning_afternoon(x.reset_index(drop=True)))
#temp1=temp1.loc[temp1['Close2']!=0,:]
#temp1['Open1']=temp1['Open1'].astype(int)
#temp1['High1']=temp1['High1'].astype(int)
#temp1['Low1']=temp1['Low1'].astype(int)
#temp1['Close1']=temp1['Close1'].astype(int)
#temp1['Open2']=temp1['Open2'].astype(int)
#temp1['High2']=temp1['High2'].astype(int)
#temp1['Low2']=temp1['Low2'].astype(int)
#temp1['Close2']=temp1['Close2'].astype(int)
#
#
#
#
#
#
##use morning as one of the factor
#temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
#temp1_morning=temp1_morning.rename(columns={'Open1':'Open_HSI','High1':'High_HSI',
#                                                            'Low1':'Low_HSI','Close1':'Close_HSI'})
#temp1_morning=temp1_morning.reset_index(drop=True)
#                        
##need to change a bit format to dt, because save to index_analsis
#temp1_morning['Date2']=temp1_morning['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI_morning.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_morning.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#
#
#
#
###use morning as Y
##temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
##temp1_morning=temp1_morning.rename(columns={'Date2':'Date','Open1':'Open','High1':'High',
##                                                           'Low1':'Low','Close1':'Close'})
##temp1_morning=temp1_morning.reset_index(drop=True)
##                        
###need to change a bit format to dt, because save to index_analsis
##temp1_morning['Date']=temp1_morning['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
##temp1_morning['DateNum']= (temp1_morning['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
##
###also save to index_analsis
##output_path=os.path.join(target_dir,'HSI.xlsx')
##writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
##temp1_morning.to_excel(writer, sheet_name='Sheet1')
##writer.save()
#
#
#
#
#
##use afternoon as Y
#temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
#temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
#                                                           'Low2':'Low','Close2':'Close'})                        
#temp1_afternoon=temp1_afternoon.reset_index(drop=True)      
#
#temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#
#temp1_afternoon.dtypes
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
#writer.save()









#enter_number_of_bar=10
#stop_number_of_bar=10
#exit_number_of_bar=10
#
#data_use=data.loc[data['Date2']=='2014-12-31',:]
#def find_min_6min(data_use):
#    data_use2=data_use.sort_values(by=['Date1'],ascending=False)
#    data_use2=data_use2.head(exit_number_of_bar)
#    #data_use2['mean']=(data_use2['High']+data_use2['Low'])/2
#    data_use2['mean']=(data_use2['High']+data_use2['Low']+data_use2['Open']+data_use2['Close'])/4
#    output=np.mean(data_use2['mean'].values)
#    return output
#
#new_column=data.groupby("Date2").apply(lambda x:find_min_6min(x))
#new_column=new_column.reset_index(drop=False)
#new_column=new_column.rename(columns={0:'close_adjusted_6min_mean'})
#
#
#
#data_use=data.loc[data['Date2']=='2014-12-31',:]
#def find_min_6min_adj_open(data_use):
#    data_use2=data_use.sort_values(by=['Date1'],ascending=True)
#    data_use2=data_use2.head(enter_number_of_bar)
#    #data_use2['mean']=(data_use2['High']+data_use2['Low'])/2
#    data_use2['mean']=(data_use2['High']+data_use2['Low']+data_use2['Open']+data_use2['Close'])/4
#    output=np.mean(data_use2['mean'].values)
#    #output=data_use2['Open']
#    return output
#
#new_column2=data.groupby("Date2").apply(lambda x:find_min_6min_adj_open(x))
#new_column2=new_column2.reset_index(drop=False)
#new_column2=new_column2.rename(columns={0:'open_adjusted_6min_mean'})
#
#new_column=pd.merge(new_column,new_column2,how='left',left_on=['Date2'],right_on=['Date2'])
#
#
#
#
#
##adjust HSI open close with 10 min open , 10 min close
#
#new_column['open_adjusted_6min_mean']=new_column['open_adjusted_6min_mean'].astype(int)
#new_column['close_adjusted_6min_mean']=new_column['close_adjusted_6min_mean'].astype(int)
#
#
#HSI= read_excel(r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\HSI.xlsx",'Sheet1')
#HSI['Date']=HSI['Date'].apply(lambda x:x.strftime("%Y-%m-%d")) # convert to string
#
##use default inner join
#HSI=pd.merge(HSI,new_column[['Date2','open_adjusted_6min_mean','close_adjusted_6min_mean']].copy(),left_on=['Date'],right_on=['Date2'])
#
#HSI['Open']=HSI['open_adjusted_6min_mean']
#HSI['Close']=HSI['close_adjusted_6min_mean']
#
#del HSI['open_adjusted_6min_mean']
#del HSI['close_adjusted_6min_mean']
#del HSI['Date2']
#
#
#
#HSI_check=HSI.copy()
#
#HSI.dtypes
#
#HSI.shape[0]
#
#sum(pd.isnull(HSI['Open']))
#
#
#
##need to change a bit format, because save to index_analsis
#HSI['Date']=HSI['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
## Convert the dataframe to an XlsxWriter Excel object.
#HSI[['Date','Open','High','Low','Close']].copy().to_excel(writer, sheet_name='Sheet1')
## Close the Pandas Excel writer and output the Excel file.
#writer.save()

















cot0_path=os.path.join(target_dir,'commitment_of_traders','Com95_06.xls')
cot0=pd.read_excel(cot0_path)

cot1_path=os.path.join(target_dir,'commitment_of_traders','Com07_14.xls')
cot1=pd.read_excel(cot1_path)

cot2_path=os.path.join(target_dir,'commitment_of_traders','Com15_16.xls')
cot2=pd.read_excel(cot2_path)

cot_use=cot0.append(cot1)
cot_use=cot_use.append(cot2)

cot_use.columns.values

cot_use['wd']=cot_use['Report_Date_as_MM_DD_YYYY'].apply(lambda x:x.isoweekday())
cot_use['wd'].unique()
cot_use['wd'].value_counts()
cot_use['date_increase']=5-cot_use['wd']

#remove wd=5 (don't know why release at friday)
cot_use=cot_use.loc[cot_use['wd']!=5,:]



def fun_convert1(x,y):
    return x+datetime.timedelta(days=y)
cot_use['Date1']=cot_use.apply(lambda a: fun_convert1(a.Report_Date_as_MM_DD_YYYY,a.date_increase),axis=1)

cot_use['Date_data']=cot_use['Report_Date_as_MM_DD_YYYY'].apply(lambda x:x.strftime('%Y-%m-%d'))

#date2 is the data release day
cot_use['Date2']=cot_use['Date1'].apply(lambda x:x.strftime('%Y-%m-%d'))
cot_use=cot_use.sort_values(by=['Date2'],ascending=True)


cot_use.columns.values

cot_use['product_market']=cot_use['Market_and_Exchange_Names']+'_'+cot_use['CFTC_Market_Code']+'_'+cot_use['CFTC_Contract_Market_Code']
cot_use_temp=cot_use.copy()

cot_use_temp=cot_use.copy()
a_check=pd.DataFrame(cot_use_temp['product_market'].unique())



U.S. TREASURY BONDS - CHICAGO BOARD OF TRADE_CBT_020601





b_check=cot_use.loc[(cot_use['product_market']=='1-MONTH LIBOR RATE - CHICAGO MERCANTILE EXCHANGE_CME')|(cot_use['product_market']=='1-MONTH LIBOR RATE - INTERNATIONAL MONETARY MARKET_CME')|(cot_use['product_market']=='1-MONTH LIBOR RATE - IMM 1-MONTH LIBOR_CME'),:]
b_check=cot_use.loc[(cot_use['product_market']=='GOLD - COMMODITY EXCHANGE INC._CMX '),:]
b_check=cot_use.loc[(cot_use['product_market']=='2-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE_CBT'),:]
b_check=cot_use.loc[(cot_use['CFTC_Contract_Market_Code']=='088691'),:]
b_check=cot_use.loc[(cot_use['CFTC_Contract_Market_Code']=='042601'),:]
b_check=cot_use.loc[(cot_use['CFTC_Contract_Market_Code']=='020601'),:]

2-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE_CBT
10-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE_CBT
5-YEAR U.S. TREASURY NOTES - CHICAGO BOARD OF TRADE_CBT







all_code=cot_use['CFTC_Contract_Market_Code'].unique().tolist()

k='042601'

pname=[]
var_use='Comm_Positions_Long_All'
for k in all_code:
    temp=cot_use.loc[cot_use['CFTC_Contract_Market_Code']==k,['Date_data','Date2','product_market',var_use]].copy()
    temp['Date']=temp['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
    temp=temp.reset_index(drop=True)



    if (temp.shape[0]>500)&(temp['Date2'].values[-1][0:4]=='2016'):
        pname_temp='cot_'+k+'_'+var_use
        pname.append(pname_temp)
        temp=temp.rename(columns={var_use:pname_temp})
        writer = pd.ExcelWriter(os.path.join('backtest_linux/database/cot',pname_temp+'.xlsx'), engine='xlsxwriter')
        
        # Convert the dataframe to an XlsxWriter Excel object.
        temp.to_excel(writer, sheet_name='Sheet1')
        
        # Close the Pandas Excel writer and output the Excel file.
        writer.save()
        writer.close()








































#############################
########Merge Data###########
#############################
#this part is to create xxx_with_tidy.xlsx file inside is %change or absolute change for interest rate
#%reset -f
#暫時由呢度開始run read data, 上面係抽數, 抽完save as xlsx
import os
import numpy as np
location='/home/jonahthonchan/Dropbox/ee/index_analysis'
os.chdir(location)

from pandas import read_excel
data = read_excel('index_table_v2_for_test_backtest.xlsx','Sheet1')
from datetime import datetime as dt
import datetime
import pandas as pd

import time
import sys




##read calendar
#calendar = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
#calendar['Date2']=calendar['Date'].astype(str)
#calendar=calendar.loc[calendar['trading_date']==1,:]
#calendar=calendar.reset_index(drop=True)
#
#settlement = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','settlement')
#settlement['settlement_day2']=settlement['settlement_day'].astype(str)









#i=274   i=2515    i=2518  i=3115  i=3122  i=3123  i=3124    i=3143   i=951   i=3452   i=628  i=115 i=553  i=315   i=3453  i=0  i=1436
#check whether date is distinct
#sometime in the morninng, in STI (singapore index), latest day will be the same as second last day with equal value
#may be yahoo not updated it, so remove duplicate in xxx_with_tidy.xlsx version
for i in range(0,len(data.symbol)):
#for i in range(1417,1920):
    if data.Merge_tgh[i]=='Yes':

        f_name=os.path.join(target_dir,'backtest_linux/database/'+data.Source[i]+'/'+data.Name_use_python[i]+'.xlsx')
        if os.path.exists(f_name):
            vars()[data.Name_use_python[i]] = read_excel(f_name,'Sheet1')
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
            vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
            unique_count=len(vars()[data.Name_use_python[i]]['Date2'].unique())
            date_count=vars()[data.Name_use_python[i]].shape[0]
            
            #find duplicated date
            check=vars()[data.Name_use_python[i]]['Date2'].value_counts()
            check_date=check[check>1].index.tolist()
            
            #store dupicated date row to output
            check2=vars()[data.Name_use_python[i]]['Date2'].isin(check_date)
            output=vars()[data.Name_use_python[i]][check2]
            if unique_count!=date_count:
                eprint('date in ',data.Name_use_python[i],' not distinct','\n')
                print('date in ',data.Name_use_python[i],' not distinct','\n')
                eprint(output)
                print(output)
            else:
                eprint('date in ',data.Name_use_python[i],' distinct','\n')
                print('date in ',data.Name_use_python[i],' distinct','\n')




#i=274
#i=2475   i=3173   i=628  i=115 i=553  i=315  i=0
#read index price
merge_total=data.loc[(data['Merge_tgh']=='Yes'),:].shape[0]
count=0
for i in range(0,len(data.symbol)):
#for i in range(1417,1920):
#for i in [628,115,1652,1812,671]:
    f_name=os.path.join(target_dir,'backtest_linux/database/'+data.Source[i]+'/'+data.Name_use_python[i]+'.xlsx')
    if (data.Merge_tgh[i]=='Yes')&(os.path.exists(f_name)):
        vars()[data.Name_use_python[i]] = read_excel(f_name,'Sheet1')
        vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date'].dt.date
        vars()[data.Name_use_python[i]]['Date2']=vars()[data.Name_use_python[i]]['Date2'].astype(str)
        #HSI_check=HSI
        print('Doing ',data.Name_use_python[i],'\n')
        if (data.Source[i]=='Yahoo')&(data.symbol[i]!='^HSI'):
            
            if data.Type[i][0:2]=='MF': #for mutual fund, open high low close all equal so need to assign open as close shift 1
                #remove row if open or close price isnan
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
                #HSI_check=HSI
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
                vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]].shift(1)
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].dropna(how='any')
            else:
                #remove row if open or close price isnan
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
                #HSI_check=HSI
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        
        #if HSI_index, also output volumn
        if (data.Source[i]=='Yahoo')&(data.symbol[i]=='^HSI'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i],'Volume':'Volume_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i],'Volume_'+data.Name_use_python[i]]]
        if (data.Source[i]=='Quandl') & (data.symbol[i]=='CHRIS/HKEX_HSI1'): #this is FHSI
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Settle)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        if (data.Source[i]=='hkex') & (data.symbol[i]=='hkex_symbol'): #this is FHSI from hkex
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        if (data.Source[i]=='hkex') & (data.symbol[i]=='hhif'): #this is hhi from hkex
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        if (data.Source[i]=='hkex')&(data.Type[i]=='pc_ratio'):
            #remove row if open or close price isnan
            #a_check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]][data.Name_use_python[i]]),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][data.Name_use_python[i]].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][data.Name_use_python[i]]

            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]),:]


        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi'): #this is hsi_oi from hkex
            
#            a_check=vars()[data.Name_use_python[i]].copy()
#            
#            #for 4 days before settlement day and include settlement day, try to remove these row
#            #because OI always drop, may not be indicative.
#            
#            all_date_oi=pd.DataFrame(a_check.loc[a_check['Date']<='2019-01-02','Date2'].copy())
#            date_after20190102=pd.DataFrame(calendar.loc[:,'Date2'].copy())
#            all_date_oi=all_date_oi.append(date_after20190102)
#
#            #find trading contract for each trading date
#            all_date_oi_list=all_date_oi['Date2'].values.tolist()
#            all_settlement_list=settlement['settlement_day2'].values
#            all_date_oi_found_settlement=[all_settlement_list[all_settlement_list>=i][0] for i in all_date_oi_list]
#            all_date_oi['settlement_contract']=all_date_oi_found_settlement
#            all_date_oi=all_date_oi.reset_index(drop=True)
#            
#            
#            #indicate 5 days including trading date
#            x=all_date_oi.loc[all_date_oi['settlement_contract']=='2006-01-26',:]
#            def indicate1(x):
#                x['indicate']=0
#                x.iloc[-2:,-1]=1
#                output=pd.Series(x.iloc[:,-1],index=x.index)
#                return output
#            all_date_oi['indicate']=all_date_oi.groupby(['settlement_contract'],group_keys=False).apply(lambda x:indicate1(x))
#            
#            all_date_oi_remove=all_date_oi.loc[all_date_oi['indicate']==1,'Date2'].values.tolist()
#            
#            a_check['remove']=a_check['Date2'].apply(lambda x:'yes' if x in all_date_oi_remove else 'no')
#            a_check=a_check.loc[a_check['remove']=='no',:]
#            del a_check['remove']
#            
#            vars()[data.Name_use_python[i]]=a_check.copy()
            
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].OI)|np.isnan(vars()[data.Name_use_python[i]].OI_lag1)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'OI_lag1':'Open_'+data.Name_use_python[i],'OI':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

#            #remove row if open or close price isnan
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].OI)|np.isnan(vars()[data.Name_use_python[i]].OI_lag1)),:].reset_index(drop=True)
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'OI_lag1':'Open_'+data.Name_use_python[i],'OI':'Close_'+data.Name_use_python[i]})
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i],'OI_next_contract','OI_next_contract_lag1']]




        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi_volume'): #this is hsi_oi volume
            
            a_check=vars()[data.Name_use_python[i]].copy()
            #remove row if open or close price isnan
            
#            vars()[data.Name_use_python[i]]['Volume_lag1']=vars()[data.Name_use_python[i]]['Volume'].shift(1)
#            vars()[data.Name_use_python[i]]['Volume_next_contract_lag1']=vars()[data.Name_use_python[i]]['Volume_next_contract'].shift(1)
#            
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Volume_lag1)|np.isnan(vars()[data.Name_use_python[i]].Volume)),:].reset_index(drop=True)
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Volume_lag1':'Open_'+data.Name_use_python[i],'Volume':'Close_'+data.Name_use_python[i]})
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i],'Volume_next_contract','Volume_next_contract_lag1']]


            vars()[data.Name_use_python[i]]['Volume_lag1']=vars()[data.Name_use_python[i]]['Volume'].shift(1)
            
            
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Volume_lag1)|np.isnan(vars()[data.Name_use_python[i]].Volume)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Volume_lag1':'Open_'+data.Name_use_python[i],'Volume':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
            
        if (data.Source[i]=='jpx') & ((data.symbol[i]=='n225_oi_volume')|(data.symbol[i]=='n225_oi')): #this is hsi_oi volume
            
            a_check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]['Volume_lag1']=vars()[data.Name_use_python[i]]['Volume'].shift(1)
            
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Volume_lag1)|np.isnan(vars()[data.Name_use_python[i]].Volume)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Volume_lag1':'Open_'+data.Name_use_python[i],'Volume':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

        
        if (data.Source[i]=='Quandl') & (data.symbol[i][0:5]=='CHRIS')&(data.Type[i]=='commodity'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Settle)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        if (data.Source[i]=='ECB') & (data.symbol[i][0:3]=='ECB'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]].Value),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Value'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Value']
            del vars()[data.Name_use_python[i]]['Date']
            del vars()[data.Name_use_python[i]]['Value']
        if (data.Source[i]=='Quandl') & (data.symbol[i]=='USTREASURY/REALLONGTERM'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)']),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)']
            del vars()[data.Name_use_python[i]]['Date']
            del vars()[data.Name_use_python[i]]['LT Real Average (>10Yrs)']
            
        if (data.Source[i]=='Quandl') & (data.symbol[i][0:20]=='USTREASURY/REALYIELD'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]][str(int(data.Year[i]))+' YR']),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+' YR'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+' YR']
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]].copy()

        if (data.Source[i]=='Quandl') & (data.symbol[i]=='MOFJ/INTEREST_RATE_JAPAN'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]][str(int(data.Year[i]))+'Y']),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+'Y'].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][str(int(data.Year[i]))+'Y']
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]].copy()
      
        if (data.Source[i]=='Quandl') & (data.Type[i]=='bond_futures'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Settle)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Open']#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Settle']
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]].copy()

        if (data.Source[i]=='Quandl') & (data.symbol[i]=='AAII/AAII_SENTIMENT'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Bearish)|np.isnan(vars()[data.Name_use_python[i]].Bullish)),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Bearish':'Open_'+data.Name_use_python[i],'Bullish':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

                
        if data.Source[i]=='analystz':
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        
        if data.Source[i]=='Custom':
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
        
        
        if (data.Source[i]=='wsj')&(data.Type[i][0:2]=='MF'):
            #for mutual fund, open high low close all equal so need to assign open as close shift 1
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]].shift(1)
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].dropna(how='any')        
        if (data.Source[i]=='wsj')&(data.Type[i][0:2]!='MF'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i],'Volume':'Volume_'+data.Name_use_python[i]})
            if 'Volume_'+data.Name_use_python[i] not in vars()[data.Name_use_python[i]].columns.values:
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]
            else:
                vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i],'Volume_'+data.Name_use_python[i]]]
        
        if (data.Source[i]=='investing_com'):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

            #for futures like brent oil and gold, if on monday morning perform extraction, it will include sunday night price,
            #as the market open at night
            #but investing.com will remove sunday later in historical data, so i also remove sunday price
            #using isoweekday, 7 is sunday
            key=vars()[data.Name_use_python[i]]['Date2'].apply(lambda x:dt.strptime(x,'%Y-%m-%d').isoweekday())!=7
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]][key]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)


        if (data.Source[i]=='jpx')&((data.Type[i]=='n225')|(data.Type[i]=='n225_10am')|(data.Type[i]=='n225_0_to_15')|(data.Type[i]=='n225_0_to_60')):
            #remove row if open or close price isnan
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(np.isnan(vars()[data.Name_use_python[i]].Open)|np.isnan(vars()[data.Name_use_python[i]].Close)),:].reset_index(drop=True)
            #HSI_check=HSI
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Close':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[:,['Date2','Open_'+data.Name_use_python[i],'High_'+data.Name_use_python[i],'Low_'+data.Name_use_python[i],'Close_'+data.Name_use_python[i]]]

            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)



        if (data.Source[i]=='cot')&(data.Type[i]=='Comm_Positions_Long_All'):
            #remove row if open or close price isnan
            #a_check=vars()[data.Name_use_python[i]].copy()
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]][data.Name_use_python[i]]),:].reset_index(drop=True)
            vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][data.Name_use_python[i]].shift(1)#=vars()[data.Name_use_python[i]].rename(columns={'Open':'Open_'+data.Name_use_python[i],'High':'High_'+data.Name_use_python[i],'Low':'Low_'+data.Name_use_python[i],'Settle':'Close_'+data.Name_use_python[i]})
            vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]=vars()[data.Name_use_python[i]][data.Name_use_python[i]]

            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~np.isnan(vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]),:]



                
        
        #make % change column
        #for interst rate, sometimes it is zero(% change will be inf) and even if not zero, 
        #% change would be very big, so use absolute change
        if ((data.symbol[i]=='USTREASURY/REALLONGTERM')|(data.symbol[i][0:20]=='USTREASURY/REALYIELD')|(data.symbol[i]=='MOFJ/INTEREST_RATE_JAPAN')):
            vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]-vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]
        else:
            vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']=(vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]-vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]])/vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]
        
        #special made for AAII/AAII_SENTIMENT, if one of bull or bear >0.5, use bull-bear as factor
        if (data.Source[i]=='Quandl') & (data.symbol[i]=='AAII/AAII_SENTIMENT'):
            vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]>=0.5)|(vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]>=0.5),'indicator_greater05']=1
            vars()[data.Name_use_python[i]]['indicator_greater05']=vars()[data.Name_use_python[i]]['indicator_greater05'].fillna(0)
            vars()[data.Name_use_python[i]]['AAII_sentiment_Bull_minor_bear_change']=vars()[data.Name_use_python[i]]['Close_'+data.Name_use_python[i]]-vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]
            vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']=vars()[data.Name_use_python[i]]['AAII_sentiment_Bull_minor_bear_change']*vars()[data.Name_use_python[i]]['indicator_greater05']
            #check=vars()[data.Name_use_python[i]].copy()        


        #if open price is zero, print out
        if(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0].shape[0]>0):
            eprint('open is zero')
            eprint(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0])
            print('open is zero')
            print(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0])
        
        #if %change>200% or change>2 (for interest rate), print out
        if ((data.symbol[i]=='USTREASURY/REALLONGTERM')|(data.symbol[i][0:20]=='USTREASURY/REALYIELD')):
            eprint(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>=2])    
            print(vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>=2])      
        
        
        #CHRIS_com_CME_HG1 in 2011-06-21, open price is 0, which is wrong, so delete these cases (7 rows)
        if (data.Name_use_python[i]=='CHRIS_com_CME_HG1'):
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(vars()[data.Name_use_python[i]]['Open_'+data.Name_use_python[i]]==0),:]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
        #0005, 2010-04-07 open price is wrong, so remove this row
        if (data.Name_use_python[i]=='0005_HK'):
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~(vars()[data.Name_use_python[i]]['Date2']=='2010-04-07'),:]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
            
        
        
        
        
        
        
        
            
        #create DateNum
        vars()[data.Name_use_python[i]]['Date3']=pd.to_datetime(vars()[data.Name_use_python[i]]['Date2'])#create a date with datetime format
        vars()[data.Name_use_python[i]]['DateNum'] = (vars()[data.Name_use_python[i]].Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
        vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
        del vars()[data.Name_use_python[i]]['Date3']
        
        #FCHI_check=FCHI.tail(100)
        #remove duplicate if date2 are the same, but keep the first record
        vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].drop_duplicates(subset='Date2', keep="first")
        










#        #remove one date after settlement in hang_Seng_oi_tidy
#        #because before 2019/01/01, historically no settlement date OI value of next month contract
#        #so in the next date of settlemet day, OI_lag 1 has no value.
#        #although hkex OI report has this value, but to be consistent, remove these dates.
#        
#        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi'):   
#            settlement_day = read_excel('daily_prediction_production/calendar.xlsx','settlement')
#            settlement_day['Date2']=settlement_day['settlement_day'].astype(str)      
#            settlement_day['settlement']=1
#            
#            tradeday_before20181224=read_excel('daily_prediction_production/calendar.xlsx','tradingdate_before20181227')
#            calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar')
#            calendar['Date2']=calendar['Date'].astype(str)
#            calendar=calendar.loc[calendar['trading_date']==1,:]  
#            
#            all_trading_date=tradeday_before20181224.append(calendar[['Date2']])
#            all_trading_date=all_trading_date.reset_index(drop=True)
#            
#            all_trading_date=pd.merge(all_trading_date,settlement_day[['Date2','settlement']].copy(),how='left',on=['Date2'])
#            all_trading_date['settlement']=all_trading_date['settlement'].fillna(0)
#            
#            all_trading_date['s1']=all_trading_date['settlement'].shift(-1)
#            all_trading_date['s2']=all_trading_date['settlement'].shift(-2)
#            all_trading_date['s3']=all_trading_date['settlement'].shift(-3)
#            all_trading_date=all_trading_date.fillna(0)
#            all_trading_date['one']=all_trading_date['settlement']+all_trading_date['s1']+all_trading_date['s2']+all_trading_date['s3']
#            
#            
#            vars()[data.Name_use_python[i]]=pd.merge(vars()[data.Name_use_python[i]],all_trading_date[['Date2','settlement','s1','s2','s3','one']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])            
#            
#            
#            vars()[data.Name_use_python[i]]['OI_next_contract_change']=(vars()[data.Name_use_python[i]]['OI_next_contract']-vars()[data.Name_use_python[i]]['OI_next_contract_lag1'])/vars()[data.Name_use_python[i]]['OI_next_contract_lag1']
#            
#            
#            a_check=vars()[data.Name_use_python[i]].copy()
#            
#            #before 2019-01-01, remove settlement day and one day after settlemnet
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~((vars()[data.Name_use_python[i]]['one']==1)&(vars()[data.Name_use_python[i]]['Date2']<='2018-12-31')),:]
#            
#            #for settlement date, use next month contract change
#            vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]]['settlement']==1),'hang_seng_oi_volume_change']=(vars()[data.Name_use_python[i]]['Volume_next_contract']-vars()[data.Name_use_python[i]]['Volume_next_contract_lag1'])/vars()[data.Name_use_python[i]]['Volume_next_contract_lag1']
#
#            #for one day after settlement date, use current month change
#            vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]]['s1']==1),'hang_seng_oi_volume_change']=(vars()[data.Name_use_python[i]]['Close_hang_seng_oi_volume']-vars()[data.Name_use_python[i]]['Volume_next_contract_lag1'])/vars()[data.Name_use_python[i]]['Volume_next_contract_lag1']
#            
#            
#            vars()[data.Name_use_python[i]].dtypes
#            
#            
#            #vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['one']==1,'hang_seng_oi_change']=0
#            a_check=vars()[data.Name_use_python[i]].copy()
#
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)








        #remove settlement day and one date after it for volume
        if (data.Source[i]=='hkex') & (data.symbol[i]=='hsi_oi_volume'):   
#            calendar = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\daily_prediction_production\calendar.xlsx','calendar')
#            calendar['Date2']=calendar['Date'].astype(str)
#            calendar=calendar.loc[calendar['trading_date']==1,:]
#            calendar['Settlement_after_one']=calendar['Settlement_date'].shift(1)
#            remove_date=calendar.loc[calendar['Settlement_after_one']==1,'Date2'].values.tolist()
#            remove_date_df=pd.DataFrame({'Date2_remove':remove_date})
#            
#            a_check=vars()[data.Name_use_python[i]].copy()
#            vars()[data.Name_use_python[i]]=pd.merge(vars()[data.Name_use_python[i]],remove_date_df[['Date2_remove']].copy(),how='left',left_on=['Date2'],right_on=['Date2_remove'])            
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[pd.isnull(vars()[data.Name_use_python[i]]['Date2_remove']),:]
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)
#            
#            del vars()[data.Name_use_python[i]]['Date2_remove']


            settlement_day = read_excel('daily_prediction_production/calendar.xlsx','settlement')
            settlement_day['Date2']=settlement_day['settlement_day'].astype(str)      
            settlement_day['settlement']=1
            
            tradeday_before20181224=read_excel('daily_prediction_production/calendar.xlsx','tradingdate_before20181227')
            calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar')
            calendar['Date2']=calendar['Date'].astype(str)
            calendar=calendar.loc[calendar['trading_date']==1,:]  
            
            all_trading_date=tradeday_before20181224.append(calendar[['Date2']])
            all_trading_date=all_trading_date.reset_index(drop=True)
            
            all_trading_date=pd.merge(all_trading_date,settlement_day[['Date2','settlement']].copy(),how='left',on=['Date2'])
            all_trading_date['settlement']=all_trading_date['settlement'].fillna(0)
            
            all_trading_date['s1']=all_trading_date['settlement'].shift(1)
            #all_trading_date['s2']=all_trading_date['settlement'].shift(-2)
            #all_trading_date['s3']=all_trading_date['settlement'].shift(-3)
            all_trading_date=all_trading_date.fillna(0)
            all_trading_date['one']=all_trading_date['settlement']+all_trading_date['s1']#+all_trading_date['s2']+all_trading_date['s3']
            
            


#            vars()[data.Name_use_python[i]]=pd.merge(vars()[data.Name_use_python[i]],all_trading_date[['Date2','settlement','s1','one']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])            
#            
#            a_check=vars()[data.Name_use_python[i]].copy()
#            
#            #before 2019-01-01, remove settlement day and one day after settlemnet
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~((vars()[data.Name_use_python[i]]['one']==1)&(vars()[data.Name_use_python[i]]['Date2']<='2018-12-31')),:]
#
#            #after 2019-01-01, remove settlement day
#            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~((vars()[data.Name_use_python[i]]['settlement']==1)&(vars()[data.Name_use_python[i]]['Date2']>'2018-12-31')),:]
#                        
#
#            #for one day after settlement date, use current month change
#            vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]]['s1']==1),'hang_seng_oi_volume_change']=(vars()[data.Name_use_python[i]]['Close_hang_seng_oi_volume']-vars()[data.Name_use_python[i]]['Volume_next_contract_lag1'])/vars()[data.Name_use_python[i]]['Volume_next_contract_lag1']
#            
#            
#            vars()[data.Name_use_python[i]].dtypes
#            
#            
#            #vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['one']==1,'hang_seng_oi_change']=0
#            a_check=vars()[data.Name_use_python[i]].copy()


            
            vars()[data.Name_use_python[i]]=pd.merge(vars()[data.Name_use_python[i]],all_trading_date[['Date2','one']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])            
            
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['one']==0,:]
            #vars()[data.Name_use_python[i]].loc[vars()[data.Name_use_python[i]]['one']==1,'hang_seng_oi_change']=0
            a_check=vars()[data.Name_use_python[i]].copy()



            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)





        
        ###check abnormal "% change" (may be in one date before trading day, some asset not updated previous date's price
        #and return 0 in open price, so change is inf (e.g. CHRIS_bond_EUREX_FGBM1_20181227.xlsx)
        if (vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5),:].shape[0]>0):
            eprint('abnormal change >5 or <-5')
            eprint(vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5),:])
            print('abnormal change >5 or <-5')
            print(vars()[data.Name_use_python[i]].loc[(vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5),:])
            #remove abnormal change row
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].loc[~((vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']>5) | (vars()[data.Name_use_python[i]][data.Name_use_python[i]+'_change']<-5)),:]
            vars()[data.Name_use_python[i]]=vars()[data.Name_use_python[i]].reset_index(drop=True)   



        
        if data.Name_use_python[i]=='HSI':
            output_path=location
        else:
            output_path=os.path.join(target_dir,'backtest_linux/database/tidy')
            #output_path='backtest_linux/database/tidy'
        
        writer = pd.ExcelWriter(os.path.join(output_path,data.Name_use_python[i]+'_with_tidy.xlsx'), engine='xlsxwriter')
        vars()[data.Name_use_python[i]].to_excel(writer, sheet_name='Sheet1')
        writer.save()
        writer.close()
        count=count+1
        eprint('finished' ,count,'which is',' ',data.Name_use_python[i],' out of ',merge_total,'\n')
        print('finished' ,count,'which is',' ',data.Name_use_python[i],' out of ',merge_total,'\n')        







#change_permissions_recursive('/home/jonahthonchan/Dropbox/ee/index_analysis/backtest_linux', 0o777)



















##hsi OI
#
#data_oi = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\data\fhsi_from_optionwalker_from20061228to20180413.xlsx','Sheet1')
#
#data_oi['Gross O.I._lag1']=data_oi['Gross O.I.'].shift(-1)
#data_oi['hang_seng_oi_change']=(data_oi['Gross O.I.']-data_oi['Gross O.I._lag1'])/data_oi['Gross O.I.']
#data_oi.loc[data_oi['hang_seng_oi_change']>0.3,'hang_seng_oi_change']=0
#
#
#data_oi['Date2']=data_oi['Date'].dt.date
#data_oi['Date2']=data_oi['Date2'].astype(str)
#
#
#C:\Users\jonahthonchan\Dropbox\ee\index_analysis
#
##create DateNum
#data_oi['Date3']=pd.to_datetime(data_oi['Date2'])#create a date with datetime format
#data_oi['DateNum'] = (data_oi.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#data_oi=data_oi.reset_index(drop=True)
#del data_oi['Date3']
#
#data_oi=data_oi[['Date2','DateNum','hang_seng_oi_change']].copy()
#data_oi['hang_seng_oi_change']=data_oi['hang_seng_oi_change'].fillna(0)
#data_oi=data_oi.reset_index(drop=True)
#data_oi=data_oi.sort_values(by=['Date2'],ascending=[True])
#
#writer = pd.ExcelWriter(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hang_seng_oi_with_tidy.xlsx', engine='xlsxwriter')
#data_oi.to_excel(writer, sheet_name='Sheet1')
#writer.save()














































            
















#create dependent variable Y
hsi_y=HSI.loc[:,['Date2','DateNum','Open_HSI','Close_HSI']].copy()
hsi_y['Y_up']=hsi_y.apply(lambda row: (row.Close_HSI>=row.Open_HSI)*1,axis=1)
hsi_y['Y_down']=hsi_y.apply(lambda row: (row.Close_HSI<row.Open_HSI)*1,axis=1)

writer = pd.ExcelWriter('backtest_linux/database/hkex/hsi_y.xlsx', engine='xlsxwriter')
hsi_y.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()




#create dependent variable Y for n225
n225_y=n225.loc[:,['Date2','DateNum','Open_n225','Close_n225']].copy()
n225_y['Y_up']=n225_y.apply(lambda row: (row.Close_n225>=row.Open_n225)*1,axis=1)
n225_y['Y_down']=n225_y.apply(lambda row: (row.Close_n225<row.Open_n225)*1,axis=1)

writer = pd.ExcelWriter('backtest_linux/database/jpx/n225_y.xlsx', engine='xlsxwriter')
n225_y.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



#create dependent variable Y for n225_10am
n225_10am_y=n225_10am.loc[:,['Date2','DateNum','Open_n225_10am','Close_n225_10am']].copy()
n225_10am_y['Y_up']=n225_10am_y.apply(lambda row: (row.Close_n225_10am>=row.Open_n225_10am)*1,axis=1)
n225_10am_y['Y_down']=n225_10am_y.apply(lambda row: (row.Close_n225_10am<row.Open_n225_10am)*1,axis=1)

writer = pd.ExcelWriter('backtest_linux/database/jpx/n225_10am_y.xlsx', engine='xlsxwriter')
n225_10am_y.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


#create dependent variable Y for n225_0_to_15
n225_0_to_15_y=n225_0_to_15.loc[:,['Date2','DateNum','Open_n225_0_to_15','Close_n225_0_to_15']].copy()
n225_0_to_15_y['Y_up']=n225_0_to_15_y.apply(lambda row: (row.Close_n225_0_to_15>=row.Open_n225_0_to_15)*1,axis=1)
n225_0_to_15_y['Y_down']=n225_0_to_15_y.apply(lambda row: (row.Close_n225_0_to_15<row.Open_n225_0_to_15)*1,axis=1)

writer = pd.ExcelWriter('backtest_linux/database/jpx/n225_0_to_15_y.xlsx', engine='xlsxwriter')
n225_0_to_15_y.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



#create dependent variable Y for n225_0_to_60
n225_0_to_60_y=n225_0_to_60.loc[:,['Date2','DateNum','Open_n225_0_to_60','Close_n225_0_to_60']].copy()
n225_0_to_60_y['Y_up']=n225_0_to_60_y.apply(lambda row: (row.Close_n225_0_to_60>=row.Open_n225_0_to_60)*1,axis=1)
n225_0_to_60_y['Y_down']=n225_0_to_60_y.apply(lambda row: (row.Close_n225_0_to_60<row.Open_n225_0_to_60)*1,axis=1)

writer = pd.ExcelWriter('backtest_linux/database/jpx/n225_0_to_60_y.xlsx', engine='xlsxwriter')
n225_0_to_60_y.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()









##############################
#####pre analysis in data#####
##############################
#check correlation
import os
import numpy as np
os.chdir('/home/jonahthonchan/Dropbox/ee/index_analysis')
from pandas import read_excel
data = read_excel('index_table_v2_for_test_backtest.xlsx','Sheet1')


use_list=[data.Name_use_python[i] for i in range(0,len(data.symbol)) if data.Merge_tgh[i]=='Yes']

from pandas import read_excel
HSI_data_all = read_excel('hsi_y_x.xlsx','Sheet1')
HSI_data_all=HSI_data_all.loc[HSI_data_all['Date2']<='2010-10-31',:]
HSI_data_all.shape
hsi_y = read_excel('hsi_y.xlsx','Sheet1')

use_list_corr=[x+'_change' for x in use_list]
use_list_corr.insert(0,'Y_up')
if 'HSI_change' in use_list_corr:
    use_list_corr.remove('HSI_change')

use_list_corr.remove('SOLEBDX_investing_change')
use_list_corr.remove('pc_ratio_change')
 

cor_table=HSI_data_all[use_list_corr].corr()
cor_table=cor_table.sort_values(by='Y_up',ascending=False)
cor_table['index']=cor_table.index


#a_check=hsi_y_x[['Date2','MICDX_change']].copy()


create factor txt file
import os
base_folder=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
base_file='factor_test_2019_1_ema_v2.txt'
factor_path=os.path.join(base_folder,base_file)

import ast
with open(factor_path, 'r') as f:
    use_factor_list2 = ast.literal_eval(f.read())


from pandas import read_excel
factor_high_corr = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\factor\factor_high_corr_.xlsx','japan_mega_cap')

factor_high_corr_list=factor_high_corr['factor'].values.tolist()

#j='TWCCX_change'
all_name=[]
for j in factor_high_corr_list:
    target=j
    use_factor_list3=use_factor_list2+[target]
    out=''
    for i in use_factor_list3:
        out=out+"'"+i+"',"
    out="["+out[0:(len(out)-1)]+"]"
    name=base_file.replace('.txt','')+'_'+target+'.txt'
    all_name.append(name)
    target_file=os.path.join(base_folder,name)
    textfile = open(target_file, 'w')
    textfile.write(out)
    textfile.close()

all_name_replicate=[]
for k in all_name:
    for j in range(0,8):
        all_name_replicate.append(k)

out=pd.DataFrame({'factor_txt':np.asarray(all_name_replicate)})

temp_path=os.path.join(base_folder,'factor_txt_name_japan_mega_cap.xlsx')

writer = pd.ExcelWriter(temp_path, engine='xlsxwriter')
out.to_excel(writer, sheet_name='factor')








#add factor one by one to base factor
import pandas as pd
import os
base_folder=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
base_file='factor_test_2019_1_ema_v2.txt'#'factor_test_2019_1_ema_v2.txt'
factor_path=os.path.join(base_folder,base_file)

import ast
with open(factor_path, 'r') as f:
    use_factor_list2 = ast.literal_eval(f.read())

factors_add=['volumn4ne30po1_change','volumn4ne15po1_change','volumn5po1ne1po10_change','volumn5ne30ne1po10_change','volumn5ne120ne1po10_change',
             'volumn4ne30po1_greatless_mean_value_indicator','volumn4ne15po1_greatless_mean_value_indicator','volumn5po1ne1po10_greatless_mean_value_indicator','volumn5ne30ne1po10_greatless_mean_value_indicator','volumn5ne120ne1po10_greatless_mean_value_indicator',
             'volumn4ne30po1_greatless_mean_sd2_value_indicator','volumn4ne15po1_greatless_mean_sd2_value_indicator','volumn5po1ne1po10_greatless_mean_sd2_value_indicator','volumn5ne30ne1po10_greatless_mean_sd2_value_indicator','volumn5ne120ne1po10_greatless_mean_sd2_value_indicator']

factors_add=['AAII_sentiment_change_greatless_indicate_change','AAII_sentiment_change_greatless_change','AAII_sentiment_Bull_great_bear_change_change',
                    'AAII_sentiment_Bullish_greater05_change_change','AAII_sentiment_Bullish_greater0333_change_change','AAII_sentiment_Bullish_greater04_change_change',
                    'bear_bull_max_indicator_change','bear_bull_max_value_change','AAII_sentiment_Bull_minor_bear_change_change',
                    'AAII_sentiment_Bull_minor_bear_with_atleastone_greater0333_change_change','AAII_sentiment_Bull_minor_bear_with_atleastone_greater04_change_change',
                    'AAII_sentiment_Bull_minor_bear_with_atleastone_greater05_change_change']

j='volcountne15po10po6_change'
all_name=[]
for j in factors_add:
    target=j
    use_factor_list3=use_factor_list2+[target]
    out=''
    for i in use_factor_list3:
        out=out+"'"+i+"',"
    out="["+out[0:(len(out)-1)]+"]"
    
    name=base_file.replace('.txt','')+'_'+target+'.txt'
    target_file=os.path.join(base_folder,'factor',name)
    textfile = open(target_file, 'w')
    textfile.write(out)
    textfile.close()

#create replication of name
name_pd=pd.DataFrame([])
for j in factors_add:
    target=j
    name=base_file.replace('.txt','')+'_'+target+'.txt'
    temp=pd.DataFrame([name])
    for i in range(0,3):
        name_pd=name_pd.append(temp)


        
        
        
        
#create factor.txt

import pandas as pd
import os
base_folder='/home/jonahthonchan/Dropbox/ee/index_analysis'
base_file='factor/factor_test_2019_1_ema_v2_AAII_sentiment_oi_revised5678_decay5.txt'#'factor_test_2019_1_ema_v2.txt'
factor_path=os.path.join(base_folder,base_file)

import ast
with open(factor_path, 'r') as f:
    use_factor_list2 = ast.literal_eval(f.read())




import os
import numpy as np
os.chdir('/home/jonahthonchan/Dropbox/ee/index_analysis')
from pandas import read_excel
data = read_excel('index_table_v2_for_test_backtest.xlsx','Sheet1')


f2=data['Name_use_python'].values[3177:]



#j=['MCDFX_change', 'MICDX_change']
n1=0
checklist=pd.DataFrame([])
for j in f2:
    target=j
    use_factor_list3=use_factor_list2+[target+'_change']
    out=''
    for i in use_factor_list3:
        out=out+"'"+i+"',"
    out="["+out[0:(len(out)-1)]+"]"
    
    n1=n1+1
    
    name='factor'+str(n1)+'.txt'
    target_file=os.path.join(base_folder,'factor',name)
    textfile = open(target_file, 'w')
    textfile.write(out)
    textfile.close()
    
    j_str='-'.join(j)
    
    checklist=checklist.append(pd.DataFrame({'factor':[j_str],'filename':[name]}))        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#check correlation by factor.txt
#import os
#import numpy as np
#os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
#from pandas import read_excel
#data = read_excel('index_table_v2_for_test_backtest.xlsx','Sheet1')
#
#base_folder=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
#base_file='factor_base_47_interact_comm2_with_HSI_index_v2_83188_MF_japan_stock_1_high_corr_HJPNX_OTPSX_FBGKX_change_TBGVX_change_XBI_DHFCX.txt'
#factor_path=os.path.join(base_folder,base_file)
#
#import ast
#with open(factor_path, 'r') as f:
#    use_list_corr = ast.literal_eval(f.read())
#
#from pandas import read_excel
#HSI_data_all = read_excel('hsi_y_x.xlsx','Sheet1')
#HSI_data_all=HSI_data_all.loc[HSI_data_all['Date2']<='2010-10-31',:]
#HSI_data_all.shape
#hsi_y = read_excel('hsi_y.xlsx','Sheet1')
#
#
#use_list_corr.insert(0,'Y_up')
#if 'HSI_change' in use_list_corr:
#    use_list_corr.remove('HSI_change')
#
#cor_table=HSI_data_all[use_list_corr].corr()
#cor_table=cor_table.sort_values(by='Y_up',ascending=False)
#cor_table['index']=cor_table.index
#
#cor_positive=cor_table.loc[cor_table['Y_up']>0,'index'].values.tolist()
#cor_positive.remove('Y_up')
#cor_positive.append('Date2')
#
#all_name=[]
#out=''
#for i in cor_positive:
#    out=out+"'"+i+"',"
#out="["+out[0:(len(out)-1)]+"]"
#name='factor_split_8.txt'
#all_name.append(name)
#target_file=os.path.join(base_folder,name)
#textfile = open(target_file, 'w')
#textfile.write(out)
#textfile.close()
#
#
#cor_negative=cor_table.loc[cor_table['Y_up']<0,'index'].values.tolist()
#cor_negative.append('Date2')
#
#all_name=[]
#out=''
#for i in cor_negative:
#    out=out+"'"+i+"',"
#out="["+out[0:(len(out)-1)]+"]"
#name='factor_split_9.txt'
#all_name.append(name)
#target_file=os.path.join(base_folder,name)
#textfile = open(target_file, 'w')
#textfile.write(out)
#textfile.close()




#make special volumn factor 
#read FHSI_minute_20051201to20190326.hdf5
import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
from pandas import read_excel

folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")
#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()

data_all_final_check=data_all_final.head(10)



data_fhsi_minute=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data_fhsi_minute=data_fhsi_minute.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})
data_fhsi_minute=data_fhsi_minute.reset_index(drop=True)


#analyse volumn in last n minute, if price increase, volumn change is +ve, vice verser.
start_row=-31 #(-31 and -1 is last 30 mins)
end_row=-1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2013-10-07',:].reset_index(drop=True)
def analyse_volumn(x,start_row,end_row):
    x['cum_vol']=x['TotalVolume'].cumsum()
    if end_row>=0:
        data_use=x[(start_row):(end_row)].copy()
    else:
        data_use=x[(start_row):(x.shape[0]+1+end_row)].copy()

    data_use=data_use.reset_index(drop=True)
    size=data_use.shape[0]

    vol_change=(data_use['cum_vol'].values[size-1]-data_use['cum_vol'].values[0])/data_use['cum_vol'].values[0] if data_use['cum_vol'].values[0]!=0 else 0
    price_change=1 if ((data_use['Close'].values[size-1]-data_use['Close'].values[0])>=0) else -1
    vol_change=vol_change*price_change
    
    date_target=data_use['Date2'].values[0]
    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days
    return pd.Series([date_target,vol_change,datenum])
 


data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-6,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'FHSIVol4_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('FHSIVol4_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#find 10 largest volumns
start_row=-60
end_row=-1
see_how_many=10 #(sort by volumn then find out how many largest to be considered)
cut_off=8 #if 8 out of see_how_many is +ve then output 1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2013-10-07',:].reset_index(drop=True)

start_row=-10
end_row=-1
see_how_many=1
cut_off=1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2019-03-26',:].reset_index(drop=True)


def analyse_volumn(x,start_row,end_row,see_how_many,cutoff):
    x['cum_vol']=x['TotalVolume'].cumsum()
    x['price_change']=x['Close']-x['Open']
    if end_row>=0:
        data_use=x[(start_row):(end_row)].copy()
    else:
        data_use=x[(start_row):(x.shape[0]+1+end_row)].copy()

    date_target=data_use['Date2'].values[0]
    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days        
    data_use=data_use.sort_values(by=['TotalVolume'],ascending=[False])[0:see_how_many]
    data_use=data_use.reset_index(drop=True)
    count_price_up=sum(data_use.price_change.values>0)
    count_price_down=sum(data_use.price_change.values<0)
    
    output=0
    if count_price_up>=cut_off: output=1 
    if count_price_down>=cut_off: output=-1 
    
    return pd.Series([date_target,output,datenum])




data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-15,-1,10,6))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne15po10po6_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne15po10po6_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-15,-1,10,8))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne15po10po8_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne15po10po8_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-15,-1,10,9))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne15po10po9_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne15po10po9_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-30,-1,10,7))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne30po10po7_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne30po10po7_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-30,-1,10,9))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne30po10po9_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne30po10po9_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-10,-1,8,7))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne10po8po7_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne10po8po7_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-1,-1,1,1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne1po1po1_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne1po1po1_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-10,-1,1,1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne10po1po1_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne10po1po1_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn(x.reset_index(drop=True),-30,-1,1,1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:'volcountne30po1po1_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)

os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
writer = pd.ExcelWriter('volcountne30po1po1_with_tidy.xlsx', engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()






#find the max volumn in last n minute, use max vol/price change as factor
start_row=-31 #(-31 and -1 is last 30 mins)
end_row=-1
 
start_row=-10
end_row=-1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2019-03-21',:].reset_index(drop=True)
 
 
def analyse_volumn2(x,start_row,end_row):
    x['cum_vol']=x['TotalVolume'].cumsum()
    x['price_change']=x['Close']-x['Open']
    if end_row>=0:
        data_use=x[(start_row):(end_row)].copy()
    else:
        data_use=x[(start_row):(x.shape[0]+1+end_row)].copy()
 
    data_use=data_use.reset_index(drop=True)
    date_target=data_use['Date2'].values[0]
    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days        
 
    output=0
    max_vol=max(data_use['TotalVolume'])
    if data_use.loc[data_use['TotalVolume']==max_vol,:].shape[0]==1:
        price_change=data_use.loc[data_use['TotalVolume']==max_vol,'price_change'].values[0]
        if price_change!=0:
            output=max_vol/price_change
 
    return pd.Series([date_target,output,datenum])
 
factor_name='volmaxne10po1'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn2(x.reset_index(drop=True),-10,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
factor_name='volmaxne5po1'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn2(x.reset_index(drop=True),-5,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
factor_name='volmaxne15po1'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn2(x.reset_index(drop=True),-15,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
factor_name='volmaxne30po1'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn2(x.reset_index(drop=True),-30,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
 

 
 
 
 
 
 
#if >cutoff, use mean price as factor value
start_row=-60
end_row=-1
see_how_many=10 #(sort by volumn then find out how many largest to be considered)
cut_off=8 #if 8 out of see_how_many is +ve then output 1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2013-10-07',:].reset_index(drop=True)
 
start_row=-1
end_row=-1
see_how_many=1
cut_off=1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2008-01-23',:].reset_index(drop=True)
 
 
def analyse_volumn3(x,start_row,end_row,see_how_many,cutoff):
    x['cum_vol']=x['TotalVolume'].cumsum()
    x['price_change']=x['Close']-x['Open']
    if end_row>=0:
        data_use=x[(start_row):(end_row)].copy()
    else:
        data_use=x[(start_row):(x.shape[0]+1+end_row)].copy()
 
    date_target=data_use['Date2'].values[0]
    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days        
    data_use=data_use.sort_values(by=['TotalVolume'],ascending=[False])[0:see_how_many]
    data_use=data_use.reset_index(drop=True)
    count_price_up=sum(data_use.price_change.values>0)
    count_price_down=sum(data_use.price_change.values<0)
    
    mean_up=0
    mean_down=0
    if len(data_use.price_change.values)>0:
        mean_up=data_use.price_change.values[data_use.price_change.values>0].mean()
        mean_down=data_use.price_change.values[data_use.price_change.values<0].mean()
 
    output=0
    if count_price_up>=cut_off: output=mean_up 
    if count_price_down>=cut_off: output=mean_down 
 
    return pd.Series([date_target,output,datenum])
 
factor_name='meanpricene20po10po7'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-20,-1,10,7))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
factor_name='meanpricene10po10po7'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-10,-1,10,7))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


factor_name='meanpricene1po1po1'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-1,-1,1,1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
factor_name='meanpricene10po8po7'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-10,-1,8,7))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
factor_name='meanpricene15po10po6'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-15,-1,10,6))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

factor_name='meanpricene15po10po9'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-15,-1,10,9))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
factor_name='meanpricene30po10po9'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn3(x.reset_index(drop=True),-30,-1,10,9))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name+'_change',2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



'volmaxne10po1','volmaxne5po1','volmaxne15po1','volmaxne30po1','meanpricene20po10po7','meanpricene10po10po7','meanpricene1po1po1','meanpricene10po8po7','meanpricene15po10po6','meanpricene15po10po9','meanpricene30po10po9'




#in last n minutes, find  vol/price change and find mean of positive vol/price change, mean of negative vol/price change, and substract
start_row=-31 #(-31 and -1 is last 30 mins)
end_row=-1
 
start_row=-30
end_row=-1
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2017-08-30',:].reset_index(drop=True)
 
 
def analyse_volumn4(x,start_row,end_row):
    x['cum_vol']=x['TotalVolume'].cumsum()
    x['price_change']=x['Close']-x['Open']
    x['vol/pricechange']=x['TotalVolume']/x['price_change']
    x.loc[x['price_change']==0,'vol/pricechange']=0
    if end_row>=0:
        data_use=x[(start_row):(end_row)].copy()
    else:
        data_use=x[(start_row):(x.shape[0]+1+end_row)].copy()
 
    data_use=data_use.reset_index(drop=True)
    date_target=data_use['Date2'].values[0]
    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days        
 
    use=data_use['vol/pricechange'].values
 
 
    if sum(data_use['TotalVolume'])!=0:
        use_positive= np.array([0])if len(use[data_use['vol/pricechange'].values>0])==0 else use[data_use['vol/pricechange'].values>0]
        use_negative= np.array([0])if len(use[data_use['vol/pricechange'].values<0])==0 else use[data_use['vol/pricechange'].values<0]
        output=use_positive.mean()+use_negative.mean()
    else:
        output=0
 
    return pd.Series([date_target,output,datenum])
 
factor_name='volumn4ne30po1_change'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn4(x.reset_index(drop=True),-30,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name,2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

factor_name='volumn4ne15po1_change'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn4(x.reset_index(drop=True),-15,-1))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name,2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
 
 
 

 
 
 
 
#in last n minutes, find 10 largest volumn, then  find mean of positive price change, mean of negative price change, and substract
start_row=-31 #(-31 and -1 is last 30 mins)
end_row=-1
 
start_row=1
end_row=-1
see_how_many=10
x=data_fhsi_minute.loc[data_fhsi_minute['Date2']=='2005-12-01',:].reset_index(drop=True)
 

def analyse_volumn5(x,start_row,end_row,see_how_many):
    x['cum_vol']=x['TotalVolume'].cumsum()
    x['price_change']=x['Close']-x['Open']
    x['vol/pricechange']=x['TotalVolume']/x['price_change']
    x.loc[x['price_change']==0,'vol/pricechange']=0
    if end_row>=0:
        data_use=x[(start_row):(end_row)].copy()
    else:
        data_use=x[(start_row):(x.shape[0]+1+end_row)].copy()
 
    data_use=data_use.reset_index(drop=True)
    date_target=data_use['Date2'].values[0]
    datenum=(dt.strptime(date_target,"%Y-%m-%d")-dt(1970,1,1)).days        
 
    data_use=data_use.sort_values(by=['TotalVolume'],ascending=[False])[0:see_how_many]
    data_use=data_use.reset_index(drop=True) 
 
    use=data_use['price_change'].values
 
    if sum(data_use['TotalVolume'])!=0:
        use_positive= np.array([0])if len(use[data_use['price_change'].values>0])==0 else use[data_use['price_change'].values>0]
        use_negative= np.array([0])if len(use[data_use['price_change'].values<0])==0 else use[data_use['price_change'].values<0]
        output=use_positive.mean()+use_negative.mean()
    else:
        output=0
 
    return pd.Series([date_target,output,datenum])
 
factor_name='volumn5po1ne1po10_change'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn5(x.reset_index(drop=True),1,-1,10))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name,2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
 
factor_name='volumn5ne30ne1po10_change'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn5(x.reset_index(drop=True),-30,-1,10))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name,2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()
 
factor_name='volumn5ne120ne1po10_change'
data_fhsi_minute_extracted=data_fhsi_minute.groupby('Date2').apply(lambda x:analyse_volumn5(x.reset_index(drop=True),-120,-1,10))
data_fhsi_minute_extracted=data_fhsi_minute_extracted.rename(columns={0:'Date2',1:factor_name,2:'DateNum'}) 
data_fhsi_minute_extracted=data_fhsi_minute_extracted.reset_index(drop=True)
writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
data_fhsi_minute_extracted.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


#'volumn4ne30po1_change','volumn4ne15po1_change','volumn5po1ne1po10_change','volumn5ne30ne1po10_change','volumn5ne120ne1po10_change'









import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
from pandas import read_excel

folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis"
#make AAII_AAII_SENTIMENT factor
AAII_AAII_SENTIMENT_temp = read_excel(os.path.join(folder_path,'AAII_AAII_SENTIMENT'+'.xlsx'),'Sheet1')
AAII_AAII_SENTIMENT_temp['Date2']=AAII_AAII_SENTIMENT_temp['Date'].dt.date
AAII_AAII_SENTIMENT_temp['Date2']=AAII_AAII_SENTIMENT_temp['Date2'].astype(str)

AAII_AAII_SENTIMENT_temp=AAII_AAII_SENTIMENT_temp.loc[~pd.isnull(AAII_AAII_SENTIMENT_temp['Bullish']),:]
AAII_AAII_SENTIMENT_temp=AAII_AAII_SENTIMENT_temp.reset_index(drop=True)

AAII_AAII_SENTIMENT_temp['Bullish_lag1']=AAII_AAII_SENTIMENT_temp['Bullish'].shift(1)
AAII_AAII_SENTIMENT_temp['Bearish_lag1']=AAII_AAII_SENTIMENT_temp['Bearish'].shift(1)



#create bullish and bearish % change
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change']=(AAII_AAII_SENTIMENT_temp['Bullish']-AAII_AAII_SENTIMENT_temp['Bullish_lag1'])/AAII_AAII_SENTIMENT_temp['Bullish_lag1']
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change']=(AAII_AAII_SENTIMENT_temp['Bearish']-AAII_AAII_SENTIMENT_temp['Bearish_lag1'])/AAII_AAII_SENTIMENT_temp['Bearish_lag1']

#ifif bullish>bullish lag1 and bear<bear lag1,1 otherwise -1
AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change']>=0)&(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change']<=0),'AAII_sentiment_change_greatless_indicate']=1
AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change']<=0)&(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change']>=0),'AAII_sentiment_change_greatless_indicate']=-1
AAII_AAII_SENTIMENT_temp['AAII_sentiment_change_greatless_indicate']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_change_greatless_indicate'].fillna(0)

#ifif bullish>bullish lag1 and bear<bear lag1,1 otherwise -1 (but not use indicator, use sum of their absolute)
AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change']>=0)&(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change']<=0),'AAII_sentiment_change_greatless']=abs(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change'])+abs(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change'])
AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change']<=0)&(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change']>=0),'AAII_sentiment_change_greatless']=-1*(abs(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_change'])+abs(AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bearish_change']))
AAII_AAII_SENTIMENT_temp['AAII_sentiment_change_greatless']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_change_greatless'].fillna(0)





#if bull > bear then 1, if not then -1
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_great_bear_change']=1*(AAII_AAII_SENTIMENT_temp['Bullish']>AAII_AAII_SENTIMENT_temp['Bearish'])
AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_great_bear_change']==0,'AAII_sentiment_Bull_great_bear_change']=-1
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_great_bear_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_great_bear_change'].fillna(0)





#if bull>0.5 then 1, if bear>0.5 then -1
AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['Bullish']>0.5,'AAII_sentiment_Bullish_greater05_change']=1
AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['Bearish']>0.5,'AAII_sentiment_Bullish_greater05_change']=-1
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_greater05_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_greater05_change'].fillna(0)

AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['Bullish']>0.333,'AAII_sentiment_Bullish_greater0333_change']=1
AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['Bearish']>0.333,'AAII_sentiment_Bullish_greater0333_change']=-1
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_greater0333_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_greater0333_change'].fillna(0)

AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['Bullish']>0.4,'AAII_sentiment_Bullish_greater04_change']=1
AAII_AAII_SENTIMENT_temp.loc[AAII_AAII_SENTIMENT_temp['Bearish']>0.4,'AAII_sentiment_Bullish_greater04_change']=-1
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_greater04_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bullish_greater04_change'].fillna(0)







#bear_bull_max_indicator bear_bull_max_value
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_change']=AAII_AAII_SENTIMENT_temp['Bullish']-AAII_AAII_SENTIMENT_temp['Bearish']

AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['Bullish']>AAII_AAII_SENTIMENT_temp['Bearish'])&(AAII_AAII_SENTIMENT_temp['Bullish']>AAII_AAII_SENTIMENT_temp['Neutral']),'bull_max_indicator']=1
AAII_AAII_SENTIMENT_temp['bull_max_indicator']=AAII_AAII_SENTIMENT_temp['bull_max_indicator'].fillna(0)
AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['Bearish']>AAII_AAII_SENTIMENT_temp['Bullish'])&(AAII_AAII_SENTIMENT_temp['Bearish']>AAII_AAII_SENTIMENT_temp['Neutral']),'bear_max_indicator']=-1
AAII_AAII_SENTIMENT_temp['bear_max_indicator']=AAII_AAII_SENTIMENT_temp['bear_max_indicator'].fillna(0)
AAII_AAII_SENTIMENT_temp['bear_bull_max_indicator']=AAII_AAII_SENTIMENT_temp['bull_max_indicator']+AAII_AAII_SENTIMENT_temp['bear_max_indicator']

AAII_AAII_SENTIMENT_temp['bull_max_value']=AAII_AAII_SENTIMENT_temp['bull_max_indicator']*AAII_AAII_SENTIMENT_temp['Bullish']
AAII_AAII_SENTIMENT_temp['bear_max_value']=AAII_AAII_SENTIMENT_temp['bear_max_indicator']*AAII_AAII_SENTIMENT_temp['Bearish']
AAII_AAII_SENTIMENT_temp['bear_bull_max_value']=AAII_AAII_SENTIMENT_temp['bull_max_value']+AAII_AAII_SENTIMENT_temp['bear_max_value']






#if either greater 0.333, output AAII_sentiment_Bull_minor_bear_change
AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['Bullish']>=0.333)|(AAII_AAII_SENTIMENT_temp['Bearish']>=0.333),'indicator_greater0333']=1
AAII_AAII_SENTIMENT_temp['indicator_greater0333']=AAII_AAII_SENTIMENT_temp['indicator_greater0333'].fillna(0)
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_with_atleastone_greater0333_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_change']*AAII_AAII_SENTIMENT_temp['indicator_greater0333']

AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['Bullish']>=0.4)|(AAII_AAII_SENTIMENT_temp['Bearish']>=0.4),'indicator_greater04']=1
AAII_AAII_SENTIMENT_temp['indicator_greater04']=AAII_AAII_SENTIMENT_temp['indicator_greater04'].fillna(0)
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_with_atleastone_greater04_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_change']*AAII_AAII_SENTIMENT_temp['indicator_greater04']

AAII_AAII_SENTIMENT_temp.loc[(AAII_AAII_SENTIMENT_temp['Bullish']>=0.5)|(AAII_AAII_SENTIMENT_temp['Bearish']>=0.5),'indicator_greater05']=1
AAII_AAII_SENTIMENT_temp['indicator_greater05']=AAII_AAII_SENTIMENT_temp['indicator_greater05'].fillna(0)
AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_with_atleastone_greater05_change']=AAII_AAII_SENTIMENT_temp['AAII_sentiment_Bull_minor_bear_change']*AAII_AAII_SENTIMENT_temp['indicator_greater05']






date_target=AAII_AAII_SENTIMENT_temp['Date2']
AAII_AAII_SENTIMENT_temp['DateNum'] = AAII_AAII_SENTIMENT_temp['Date2'].apply(lambda x:(dt.strptime(x,"%Y-%m-%d")-dt(1970,1,1)).days)



factor_name_list=['AAII_sentiment_change_greatless_indicate','AAII_sentiment_change_greatless','AAII_sentiment_Bull_great_bear_change',
                    'AAII_sentiment_Bullish_greater05_change','AAII_sentiment_Bullish_greater0333_change','AAII_sentiment_Bullish_greater04_change',
                    'bear_bull_max_indicator','bear_bull_max_value','AAII_sentiment_Bull_minor_bear_change',
                    'AAII_sentiment_Bull_minor_bear_with_atleastone_greater0333_change','AAII_sentiment_Bull_minor_bear_with_atleastone_greater04_change',
                    'AAII_sentiment_Bull_minor_bear_with_atleastone_greater05_change']
for i in factor_name_list:
    factor_name=i
    output=AAII_AAII_SENTIMENT_temp[['Date2',factor_name,'DateNum']].copy()
    factor_name2=factor_name+'_change'
    output=output.rename(columns={factor_name:factor_name2})
    
    writer = pd.ExcelWriter(os.path.join(folder_path,factor_name+'_with_tidy.xlsx'), engine='xlsxwriter')
    output.to_excel(writer, sheet_name='Sheet1')
    writer.save()
    writer.close()




























#############################
#######create factors########
#############################

import os
import datetime
import numpy as np
from numpy import inf
import time
import pandas as pd
from datetime import datetime as dt
#os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
os.chdir('/home/jonahthonchan/Dropbox/ee/index_analysis')


#hsi_y_path='backtest_linux/database/hkex/hsi_y.xlsx'
#tidy_path='backtest_linux/database/tidy'


hsi_y_path='hsi_y.xlsx'
tidy_path=''


#hsi_y_path='backtest_linux/database/jpx/n225_y.xlsx'
#tidy_path='backtest_linux/database/tidy'

#hsi_y_path='backtest_linux/database/jpx/n225_0_to_60_y.xlsx'
#tidy_path='backtest_linux/database/tidy'












time_start=time.time()

from pandas import read_excel
data = read_excel('index_table_v2_for_test_backtest.xlsx','Sheet1')
hsi_y = read_excel(hsi_y_path,'Sheet1')

if 'Open_n225_0_to_60' in list(hsi_y.columns.values):
    hsi_y=hsi_y.rename(columns={'Open_n225_0_to_60':'Open_HSI','Close_n225_0_to_60':'Close_HSI'})


use_list=[data.Name_use_python[i] for i in range(0,len(data.symbol)) if data.Merge_tgh[i]=='Yes']

#factor_name_list=['AAII_sentiment_change_greatless_indicate','AAII_sentiment_change_greatless','AAII_sentiment_Bull_great_bear_change',
#                    'AAII_sentiment_Bullish_greater05_change','AAII_sentiment_Bullish_greater0333_change','AAII_sentiment_Bullish_greater04_change',
#                    'bear_bull_max_indicator','bear_bull_max_value','AAII_sentiment_Bull_minor_bear_change',
#                    'AAII_sentiment_Bull_minor_bear_with_atleastone_greater0333_change','AAII_sentiment_Bull_minor_bear_with_atleastone_greater04_change',
#                    'AAII_sentiment_Bull_minor_bear_with_atleastone_greater05_change']

use_list=use_list#+factor_name_list

#use_list.append('FHSIVol4')
#use_list=use_list+['volumn4ne30po1','volumn4ne15po1','volumn5po1ne1po10','volumn5ne30ne1po10','volumn5ne120ne1po10']




if 'HSI' in use_list:
    use_list.remove('HSI')
#use_list.index('ECB_cur_EURHUF')
#use_list2=list(set(use_list))
#create price change function
#x=HSI_data_all
#index_name='XAX'
#def price_change(x,index_name):
#    change=(x['Close_'+index_name]-x['Open_'+index_name])/x['Open_'+index_name]
#    change[change == inf]=0 #for some date, like CHRIS_com_CME_HG1 in 2011-06-22, open price is 0, so change=inf
#    change[change == -inf]=0
#    change[np.isnan(change)]=0 # if 0/0, return na
#    return change 
    

hsi_x=hsi_y.loc[:,['Date2','DateNum']]
hsi_x_store_closest=hsi_y.loc[:,['Date2','DateNum']] 
#i=3
#vars()[use_list[i]] = read_excel(use_list[i]+'_with_tidy.xlsx','Sheet1')
#appear=vars()[use_list[i]]
#one_date=9306
#target_data=appear
#this function is to read the closest date before that hsi trading date
#for example, if today is 2017-11-09, use assest %change in uk/eu market on 2017-11-08 
def find_closest_datenum(one_date,target_data):
    b=one_date-target_data['DateNum']
    min_diff=b[b>0].min()
    closest_datenum=one_date-min_diff
    return closest_datenum

#one_date=hsi_x['DateNum']
#target_data=appear
def find_closest_datenum2(one_date,target_data):
    rep=target_data.shape[0]
    one_date=one_date.values #this is array
    one_date2=np.repeat(one_date,rep)
    target_data_np=np.tile(target_data['DateNum'].values,one_date.shape[0])
    b=one_date2-target_data_np

    ind=b>0
    one_date2=one_date2[ind]
    b=b[ind]
    
    db=pd.DataFrame({'one_date2':one_date2,'b':b})
    db_out=db.groupby(['one_date2'])['b'].min() #this is series
    
    if len(db_out)!=len(one_date):
        r=len(one_date)-len(db_out)
        zeroo=np.zeros(r);zeroo.fill(np.nan)
        db_out2=np.vstack((np.reshape(zeroo,(r,1)),db_out.values.reshape(len(db_out),1)))
        closest_datenum=one_date-db_out2.reshape(len(db_out2),)
    else:
        closest_datenum=one_date-db_out.values #values convert series to array
    
    return closest_datenum


#i='AAII_AAII_SENTIMENT'
count=0
for i in use_list:
    
    vars()[i] = read_excel(os.path.join(tidy_path,i+'_with_tidy.xlsx'),'Sheet1')
    appear=vars()[i]
    col_name=i+'_closest_datenum'
    #hsi_x[col_name]=hsi_x.apply(lambda row: find_closest_datenum(row['DateNum'],appear),axis=1)
    hsi_x[col_name] = find_closest_datenum2(hsi_x['DateNum'],appear)  
    
    
    hsi_x_store_closest[col_name+'_diff']=hsi_x['DateNum']-hsi_x[col_name]
    hsi_x_store_closest[col_name]=hsi_x[col_name].copy()
    
    hsi_x=pd.merge(left=hsi_x,right=appear[['DateNum',i+'_change']],how='left',left_on=col_name,right_on='DateNum')
    del hsi_x['DateNum_y']
    hsi_x=hsi_x.rename(columns={'DateNum_x':'DateNum'})
    
    # if not daily data, say monthly data, this data only use for one day, and other 0
    hsi_x[col_name+'first_factor_indicate']=hsi_x[col_name].shift(1)!=hsi_x[col_name]
    hsi_x[i+'_change']=hsi_x[i+'_change']*hsi_x[col_name+'first_factor_indicate']
    
    del hsi_x[col_name]
    del hsi_x[col_name+'first_factor_indicate']
    
    count=count+1
    print('finished change factor ',count,' out of ',len(use_list),'\n')
#hsi_x2=hsi_x.copy()
#sum(hsi_x2['PNC_closest_datenum']==hsi_x['PNC_closest_datenum'])
#if column A only has data starting from (say 2005-01-02) and hsi first day (say 1991-01-02), value within this period
#will be nan
hsi_x=hsi_x.fillna(0)
hsi_x_store_closest=hsi_x_store_closest.fillna(0)
hsi_x.isnull().any().any()















use_list_closest_diff=[x+'_closest_datenum_diff' for x in use_list]
use_list_closest_diff2=['Date2','DateNum']+use_list_closest_diff
hsi_x_store_closest_investigate=hsi_x_store_closest[use_list_closest_diff2].copy()

value_matrix=hsi_x_store_closest_investigate[use_list_closest_diff].values
hsi_x_store_closest_investigate['1_counts']=(value_matrix==1).sum(axis=1)
hsi_x_store_closest_investigate['2_counts']=(value_matrix==2).sum(axis=1)
hsi_x_store_closest_investigate['3_counts']=(value_matrix==3).sum(axis=1)
hsi_x_store_closest_investigate['4_counts']=(value_matrix==4).sum(axis=1)
hsi_x_store_closest_investigate['5_counts']=(value_matrix==5).sum(axis=1)
hsi_x_store_closest_investigate['6_counts']=(value_matrix==6).sum(axis=1)
hsi_x_store_closest_investigate['6_greater_counts']=(value_matrix>6).sum(axis=1)

#save hsi_x_store_closest
writer = pd.ExcelWriter('hsi_x_store_closest'+'.xlsx', engine='xlsxwriter')
hsi_x_store_closest_investigate.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


#find closest 20 day
hsi_x_store_closest_investigate_see=hsi_x_store_closest_investigate.tail(20).T
investigate_see_name='./daily_source_data_production/hsi_x_store_closest_transpose_'+time.strftime("%Y%m%d")+'_'+time.strftime("%H%M%S")+'_production.xlsx'
writer = pd.ExcelWriter(investigate_see_name, engine='xlsxwriter')
hsi_x_store_closest_investigate_see.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

#output to log file for last 20 rows
#logger.info(hsi_x_store_closest_investigate.tail(20))

#def price_direct(x,index_name):
#    return x['Close_'+index_name]
#
#direct_price=HSI_data_all.loc[:,['Date2']]
#for i in use_list:
#    direct_price[i+'_Close_direct']=price_direct(HSI_data_all,i).shift(1)
#    
#hsi_x=pd.merge(left=hsi_x,right=direct_price,how='left',on=['Date2'])
#hsi_x=hsi_x[1:hsi_x.shape[0]]
#hsi_x=hsi_x.reset_index(drop=True)    
#
#hsi_x.isnull().any().any()

#
#price_change_factor=HSI_data_all.loc[:,['Date2']]
#i='ECB_cur_EURBGN'
#for i in use_list:
#    price_change_factor[i+'_change']=price_change(HSI_data_all,i)
#    
#price_change_factor2=price_change_factor.copy()
#for i in use_list:
#    a=i+'_change'
#    price_change_factor2[a]=price_change_factor2[a].shift(1)
#
#
#hsi_x=pd.merge(left=hsi_x,right=price_change_factor2,how='left',on=['Date2'])
#
#hsi_x.isnull().any().any()

#define ema function
#data=appear;datenum_field='DateNum';target_field=target_col;decay=30
#data=data1;datenum_field='Datenum';target_field='nfp';decay=5


#data=HSI_source.copy()
#datenum_field='DateNum'
#target_field='smaBuy_original'
#decay=5


#datenum is in decending order
def ema_custom_v2(data,datenum_field,target_field,decay):
    datenum_vector=np.array(data[datenum_field],dtype=pd.Series).astype(np.float)#convert dataframe column to array
    target_vector=np.array(data[target_field],dtype=pd.Series).astype(np.float)
    
    m=len(target_vector)
    r=0 if len(np.where(target_vector!=0)[0])==0 else max(np.where(target_vector!=0)[0])
    datenum_vector=datenum_vector[:r+1]
    target_vector=target_vector[:r+1]
    
    n=len(datenum_vector)        
    temp=np.tile(datenum_vector,n) #make replication
    matrix_fill_h=np.reshape(temp,(n,n))
    matrix_fill_v=matrix_fill_h.T
    diff=matrix_fill_v-matrix_fill_h
    ind=diff<0 #filter out negative value
    diff[ind]=0
    diff=diff[0:diff.shape[0]-1,1:diff.shape[0]]*-1.0
    matrix_fill=diff
    
    up_tri_all1=np.triu(np.ones((n-1,n-1),dtype=np.int),0)
    matrix_fill_use=np.multiply(np.exp(matrix_fill/decay),up_tri_all1)
    
    matrix_fill_use_div_rowsum=matrix_fill_use/np.sum(matrix_fill_use,axis=1,keepdims=True)
    x=np.reshape(target_vector[1:len(target_vector)],(len(target_vector)-1,1))#exclude first elemnt of target vector
    #output=np.vstack((np.dot(matrix_fill_use_div_rowsum,x),np.array([0.0])))#append 0 to last row
    output=np.vstack((np.dot(matrix_fill_use_div_rowsum,x),np.reshape(np.zeros(m-r),(m-r,1))))#append 0 to last row
    name='EMA_'+target_field
    data[name]=output
    return data

data1=pd.DataFrame({'Datenum':[17010,17000,16990],'nfp': [0,5,8]}) 
ema_custom_v2(data1,'Datenum','nfp',5)

#array([[0.13533528, 0.01831564],
#       [0.        , 0.13533528]])
#    
#array([[0.88079708, 0.11920292],
#       [0.        , 1.        ]])
#    
#data1=pd.DataFrame({'Datenum':[17001,17000,16990],'nfp': [0,5,8]}) 
#ema_custom_v2(data1,'Datenum','nfp',120)
#
#array([[0.13533528, 0.01831564],
#       [0.        , 0.13533528]])    
    



hsi_x_temp=hsi_x.copy()  
#hsi_x_temp['Date3']=pd.to_datetime(hsi_x_temp['Date2'])#create a date with datetime format
#hsi_x_temp['DateNum'] = (hsi_x_temp.Date3-datetime.date(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#hsi_x_temp=hsi_x_temp.sort_values(by='DateNum',ascending=False)
#hsi_x_temp=hsi_x_temp.reset_index(drop=True)

#for hong kong stock, use ema up to yesterday as a forcast of today's %change
#
#i=2473 i=274
count=0
for i in range(0,len(data.symbol)):
    total=sum((data['UseEMA']=='Yes')&(data['Merge_tgh']=='Yes'))
    if (data.UseEMA[i]=='Yes')&(data.Merge_tgh[i]=='Yes'):
        for ema_decay in [15,30]:
            vars()[data.Name_use_python[i]] = read_excel(os.path.join(tidy_path,data.Name_use_python[i]+'_with_tidy.xlsx'),'Sheet1')
            
            a_check=vars()[data.Name_use_python[i]].copy()
            
            appear=vars()[data.Name_use_python[i]].sort_values(by='DateNum',ascending=False).reset_index(drop=True)
            appear=appear[['Date2',data.Name_use_python[i]+'_change','DateNum']].copy()
            #in the first date, change is Nan, so need to remove this row, and now as it is sorted, so it is last row
            #appear=appear[0:appear.shape[0]-1]
            target_col=data.Name_use_python[i]+'_change'
            
#            ema_decay=30#30
#            if data.Name_use_python[i]=='hang_seng_oi':
#                ema_decay=5
                
                
    #        #approach 3
    #        #merge hsi_x date with asset date and fill na with zero
    #        #NA means the date is in HSI but not in asset
    #        hsi_x_temp=hsi_x.copy()  
    #        
    #        first_date_of_hsi=hsi_x_temp.head(1)['Date2'].values[0]
    #        last_date_of_hsi=hsi_x_temp.tail(1)['Date2'].values[0]
    #        #using outer merge make more sense
    #        hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']].copy(),
    #                            right=appear[['Date2',data.Name_use_python[i]+'_change']].copy(),
    #                            how='outer',on=['Date2'])     
    #        hsi_x_temp=hsi_x_temp.loc[(hsi_x_temp['Date2']>=first_date_of_hsi)&(hsi_x_temp['Date2']<=last_date_of_hsi),:].copy()
    #        
    #        hsi_x_temp.sort_values(by='Date2',ascending=False,inplace=True)
    #        hsi_x_temp['DateNum2']=hsi_x_temp['Date2'].apply(lambda x:(dt.strptime(x,"%Y-%m-%d")-dt(1970,1,1)).days)
    #        
    #        hsi_x_temp[target_col]=hsi_x_temp[target_col].fillna(0)
    #
    #        hsi_x_temp=ema_custom_v2(hsi_x_temp,'DateNum2',target_col,ema_decay)
    #        hsi_x_temp['EMA_'+target_col+'_v3']=hsi_x_temp['EMA_'+target_col].copy()
    #
    #        hsi_x=pd.merge(left=hsi_x,right=hsi_x_temp[['Date2','EMA_'+target_col+'_v3']],how='left',on=['Date2'])         
     
                
                
                
                
            #approach 1
            #merge hsi_x date with asset date and fill na with zero
            #NA means the date is in HSI but not in asset
            hsi_x_temp=hsi_x.copy()  
            hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']],right=appear[['Date2',data.Name_use_python[i]+'_change']],how='left',on=['Date2'])        
            hsi_x_temp=hsi_x_temp.fillna(0)
            
            hsi_x_temp.sort_values(by='Date2',ascending=False,inplace=True)
            target_col=data.Name_use_python[i]+'_change'
            hsi_x_temp=ema_custom_v2(hsi_x_temp,'DateNum',target_col,ema_decay)
            name_old='EMA_'+target_col
            name_new='EMA_'+target_col+'_v1_'+str(ema_decay)
            hsi_x_temp=hsi_x_temp.rename(columns={name_old:name_new})
            
            hsi_x=pd.merge(left=hsi_x,right=hsi_x_temp[['Date2',name_new]],how='left',on=['Date2'])     
            
            
            
            
            
    #        #appraoch2
    #        #for each date with NA value in hsi_x
    #        #append to asset and perform ema and output the value
    #        hsi_x_temp=hsi_x.copy()  
    #        hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']],right=appear[['Date2',data.Name_use_python[i]+'_change']],how='left',on=['Date2'])        
    #        hsi_x_temp_Date_with_na=hsi_x_temp.loc[pd.isnull(hsi_x_temp[data.Name_use_python[i]+'_change']),'Date2'].values.tolist()
    #        
    #        #j='2020-04-24'
    #        #j='2020-04-29'
    #        df_store_na_date=pd.DataFrame([])
    #        if len(hsi_x_temp_Date_with_na)!=0: #for hk stock, date same as HSI, so no NA
    #            for j in hsi_x_temp_Date_with_na:
    #                appear_temp=appear.loc[appear['Date2']<j,:]
    #                last_date=dt.strptime(j,'%Y-%m-%d')
    #                add_datenum= (last_date-dt(1970,1,1)).days
    #                add=pd.DataFrame([[j,0,add_datenum]],columns=list(appear_temp.columns.values))
    #                appear_temp=pd.concat([add,appear_temp])
    #                appear_temp=appear_temp.reset_index(drop=True)
    #        
    #                appear_temp=ema_custom_v2(appear_temp,'DateNum',target_col,ema_decay)
    #                factor_value=appear_temp['EMA_'+target_col][0]
    #                add=pd.DataFrame([[j,factor_value]],columns=['Date2','EMA_'+target_col])
    #                df_store_na_date=pd.concat([df_store_na_date,add])
    #        else:
    #            df_store_na_date=pd.DataFrame(columns=['Date2','EMA_'+target_col])
    #        
    #        #find the ema for those date appear on both hsi_x and asset
    #        appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
    #        hsi_x_temp=hsi_x.copy()
    #        hsi_x_temp=pd.merge(hsi_x_temp[['Date2','DateNum']],appear[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
    #        hsi_x_temp=pd.merge(hsi_x_temp,df_store_na_date[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
    #        hsi_x_temp=hsi_x_temp.fillna(0)
    #        hsi_x_temp['EMA_'+target_col+'_v2']=hsi_x_temp['EMA_'+target_col+'_x']+hsi_x_temp['EMA_'+target_col+'_y']
    #
    #        hsi_x=pd.merge(hsi_x,hsi_x_temp[['Date2','EMA_'+target_col+'_v2']],how='left',left_on=['Date2'],right_on=['Date2'])
    #
    
    
    
    
            #appraoch2 equivalent (faster)
            #for each date with NA value in hsi_x
            #append to asset and perform ema and output the value
            hsi_x_temp=hsi_x.copy()  
            hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']],right=appear[['Date2',data.Name_use_python[i]+'_change']],how='left',on=['Date2'])        
            hsi_x_temp_Date_with_na=pd.DataFrame(hsi_x_temp.loc[pd.isnull(hsi_x_temp[data.Name_use_python[i]+'_change']),'Date2'].copy())
            
            if len(hsi_x_temp_Date_with_na)!=0: #for hk stock, date same as HSI, so no NA
                #find out latest date in hsi_y_x
                #if say today is trading date, asset won't have this date, so need to append to "appear"
                latest_date_hsi=max(hsi_x_temp_Date_with_na['Date2'])
                last_date=dt.strptime(latest_date_hsi,'%Y-%m-%d')
                add_datenum= (last_date-dt(1970,1,1)).days
                
                if latest_date_hsi>max(appear['Date2']):
                    add_df=pd.DataFrame({'Date2':[latest_date_hsi],target_col:[np.nan],'DateNum':add_datenum})
                    appear=add_df.append(appear)
                appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
                
                #
                hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na.loc[hsi_x_temp_Date_with_na['Date2']<max(appear['Date2']),:].copy()
        
                
                date_in_asset=appear['Date2'].values
                
                #say, if 2018-09-09 is not in appear, and 2018-09-10 is the closest date in appear greatest then it
                #the ema of 2018-09-09 will be the same as 2018-09-10
                hsi_x_temp_Date_with_na_work['latest_date']=hsi_x_temp_Date_with_na_work['Date2'].apply(lambda x:date_in_asset[x<date_in_asset][-1])
                hsi_x_temp_Date_with_na_work=pd.merge(hsi_x_temp_Date_with_na_work,
                                                      appear[['Date2','EMA_'+target_col]].copy(),how='left',
                                                      left_on=['latest_date'],
                                                      right_on=['Date2'])
                del hsi_x_temp_Date_with_na_work['Date2_y']
                hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na_work.rename(columns={'Date2_x':'Date2'})
            else:
                appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
                hsi_x_temp_Date_with_na_work=pd.DataFrame(columns=['Date2','latest_date','EMA_'+target_col])
            
            hsi_x_temp=pd.merge(hsi_x_temp[['Date2','DateNum']],appear[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
            hsi_x_temp=pd.merge(hsi_x_temp,hsi_x_temp_Date_with_na_work[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
            hsi_x_temp=hsi_x_temp.fillna(0)
            hsi_x_temp['EMA_'+target_col+'_v2_'+str(ema_decay)]=hsi_x_temp['EMA_'+target_col+'_x']+hsi_x_temp['EMA_'+target_col+'_y']
    
            hsi_x=pd.merge(hsi_x,hsi_x_temp[['Date2','EMA_'+target_col+'_v2_'+str(ema_decay)]],how='left',left_on=['Date2'],right_on=['Date2'])
    
    
            count=count+1
            print('finished EMA ',count,' out of ',total,'\n')

#hsi_x.isnull().any().any()

##for some day, e.g.2001-03-14, hsi has data but 0002, 0386... no data, 
##so nan appear in EMA after merging
#hsi_x=hsi_x.fillna(0)




a_check=list(hsi_x.columns.values)
len(a_check)


a_check=set(list(hsi_x.columns.values))
len(a_check)


#dynamic normalization or centralize or standardard(between -1 and 1)

##non ema factor
#non_ema_factor=[data.Name_use_python[i]+'_change' for i in range(0,len(data.symbol)) if (data.Merge_tgh[i]=='Yes')&(data.UseEMA[i]!='Yes')]
#if 'HSI_change' in non_ema_factor:
#    non_ema_factor.remove('HSI_change')
##ema factor
#ema_factor=['EMA_'+data.Name_use_python[i]+'_change' for i in range(0,len(data.symbol)) if (data.Merge_tgh[i]=='Yes')&(data.UseEMA[i]=='Yes')]
##merge together
#use_factor_list=non_ema_factor+ema_factor
#
#data_target=hsi_x.copy()
#i='ECB_cur_EURAUD_change'
#def normal_central_stand(data_target,mode,use_factor_list):
#    if mode=='normalization':
#        for i in use_factor_list:
#            temp_array=np.array(data_target[i],dtype=pd.Series).astype(np.float)
#            m=len(temp_array)
#            r=0 if len(np.where(temp_array!=0)[0])==0 else min(np.where(temp_array!=0)[0])
#            
#            temp_array2=temp_array[r:m]
#            temp_array2_mean=pd.Series(temp_array2).expanding().mean().values #find cumulated mean
#            #temp_array2_std=pd.expanding_std(pd.Series(temp_array2), min_periods=1,freq=None,ddof=0)
#            temp_array2_std=pd.Series(temp_array2).expanding(min_periods=1).std(ddof=0).values
#
#            temp_array2_normal=np.divide((temp_array2[1:len(temp_array2)]-temp_array2_mean[1:len(temp_array2)]),temp_array2_std[1:len(temp_array2)])
#            temp_array2_normal_output=np.vstack((np.reshape(np.zeros(r+1),(r+1,1)),np.reshape(temp_array2_normal,(len(temp_array2_normal),1))))
#            new_name=i+'_normal'
#            data_target[new_name]=temp_array2_normal_output
#    if mode=='standardization':
#        for i in use_factor_list:
#            temp_array=np.array(data_target[i],dtype=pd.Series).astype(np.float)
#            m=len(temp_array)
#            r=0 if len(np.where(temp_array!=0)[0])==0 else min(np.where(temp_array!=0)[0])
#            
#            temp_array2=temp_array[r:m]
#            temp_array2_min=np.minimum.accumulate(temp_array2) #find cumulated min
#            temp_array2_max=np.maximum.accumulate(temp_array2) #find cumulated max
#
#            temp_array2_standard=np.divide((temp_array2[1:len(temp_array2)]-temp_array2_min[1:len(temp_array2_min)]),(temp_array2_max[1:len(temp_array2_max)]-temp_array2_min[1:len(temp_array2_min)]))
#            temp_array2_standard_output=np.vstack((np.reshape(np.zeros(r+1),(r+1,1)),np.reshape(temp_array2_standard,(len(temp_array2_standard),1))))
#            new_name=i+'_standard'
#            data_target[new_name]=temp_array2_standard_output
#    if mode=='centralize':
#        for i in use_factor_list:
#            temp_array=np.array(data_target[i],dtype=pd.Series).astype(np.float)
#            m=len(temp_array)
#            r=0 if len(np.where(temp_array!=0)[0])==0 else min(np.where(temp_array!=0)[0])
#            
#            temp_array2=temp_array[r:m]
#            temp_array2_mean=pd.Series(temp_array2).expanding().mean().values #find cumulated mean
#
#            temp_array2_central=temp_array2-temp_array2_mean
#            temp_array2_central_output=np.vstack((np.reshape(np.zeros(r),(r,1)),np.reshape(temp_array2_central,(len(temp_array2_central),1))))
#            new_name=i+'_central'
#            data_target[new_name]=temp_array2_central_output
#    return data_target
#data_target.loc[3141,:]

#use_factor_list.remove('Date2')
#hsi_x=normal_central_stand(data_target=hsi_x,mode='normalization',use_factor_list=use_factor_list)
#hsi_x=normal_central_stand(data_target=hsi_x,mode='standardization',use_factor_list=use_factor_list)
#hsi_x=normal_central_stand(data_target=hsi_x,mode='centralize',use_factor_list=use_factor_list)






hsi_y_x=pd.merge(left=hsi_y[['Date2','Y_up','Y_down']],right=hsi_x,how='left',on=['Date2'])
#hsi_y_x_check=pd.merge(left=hsi_y[['Date2','Y_up','Y_down']],right=hsi_x,how='left',on=['Date2'])
#hsi_y_x=hsi_y_x.loc[hsi_y_x['Date2']>='1991-01-04',:]
#hsi_y_x=hsi_y_x.dropna(how='any')
hsi_y_x=hsi_y_x[1:hsi_y_x.shape[0]]
hsi_y_x=hsi_y_x.reset_index(drop=True)

hsi_y_x.isnull().any().any()


time_end=time.time()
print('total time of creating factors is ',round((time_end-time_start)/60,4),' mins')

use_list_dataframe=pd.DataFrame({'factor_name':use_list})
#factor statistic/quality
colname='N225_change'
s=use_list_dataframe
def factor_stat(s):
    colname=s['factor_name']+'_change'
    
    #first inception date
    temp_array=np.array(hsi_x[colname],dtype=pd.Series).astype(np.float)
    r=0 if len(np.where(temp_array!=0)[0])==0 else min(np.where(temp_array!=0)[0])
    first_factor_date = hsi_x.loc[r,'Date2']
    
    #closeast date different, return max and min
    colname=s['factor_name']+'_closest_datenum'+'_diff'
    closest_date_max=hsi_x_store_closest[colname].max()
    closest_date_min=hsi_x_store_closest[colname][hsi_x_store_closest[colname]>0].min()
    
    return pd.Series({'first_factor_date':first_factor_date, 'closest_date_max': closest_date_max,'closest_date_min':closest_date_min})
    #return [first_factor_date,closest_date_min,closest_date_max]
use_list_dataframe = use_list_dataframe.merge(use_list_dataframe.apply(factor_stat, axis=1), left_index=True, right_index=True)
#use_list_dataframe[['factor_inception_date','closest_date_min','closest_date_max']]=use_list_dataframe.apply(factor_stat,axis=1)

#list(hsi_x.columns.values).index('AMT_change')













#add common use field to hsi_y_x

hsi_y_x['month']=hsi_y_x['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').month)
hsi_y_x.loc[(hsi_y_x['month']>=1)&(hsi_y_x['month']<=3),'quarter1']=1
hsi_y_x.loc[(hsi_y_x['month']>=4)&(hsi_y_x['month']<=6),'quarter2']=2
hsi_y_x.loc[(hsi_y_x['month']>=7)&(hsi_y_x['month']<=9),'quarter3']=3
hsi_y_x.loc[(hsi_y_x['month']>=10)&(hsi_y_x['month']<=12),'quarter4']=4
hsi_y_x['year']=hsi_y_x['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)


hsi_y_x['quarter1']=hsi_y_x['quarter1'].fillna(0)
hsi_y_x['quarter2']=hsi_y_x['quarter2'].fillna(0)
hsi_y_x['quarter3']=hsi_y_x['quarter3'].fillna(0)
hsi_y_x['quarter4']=hsi_y_x['quarter4'].fillna(0)

for ii in range(1,13):
    hsi_y_x.loc[(hsi_y_x['month']==ii),'month'+str(ii)]=1
    hsi_y_x['month'+str(ii)]=hsi_y_x['month'+str(ii)].fillna(0)



#create interaction factors
interact_list=[]
for i in range(0,len(data.symbol)):
    if (data.create_interaction[i]=='Yes'):
        if data.UseEMA[i]=='Yes':
            interact_list.append('EMA_'+data['Name_use_python'][i]+'_change')
        else:
            interact_list.append(data['Name_use_python'][i]+'_change')
#i=0
#j=1
for i in range(0,len(interact_list)-1):
    for j in range(i+1,len(interact_list)):
        hsi_y_x[interact_list[i]+'_interact_'+interact_list[j]]=hsi_y_x[interact_list[i]]*hsi_y_x[interact_list[j]]


#create quarterly factors
#i=14


#for i in range(0,len(data.symbol)):
#    if (data.create_quarter[i]=='Yes')&(data.Name_use_python[i]!='HSI'):
#        if data.UseEMA[i]=='Yes':
#            hsi_y_x.loc[(hsi_y_x['month']>=1)&(hsi_y_x['month']<=3),'EMA_'+data['Name_use_python'][i]+'_q1'+'_change']=hsi_y_x['EMA_'+data['Name_use_python'][i]+'_change']
#            hsi_y_x.loc[(hsi_y_x['month']>=4)&(hsi_y_x['month']<=6),'EMA_'+data['Name_use_python'][i]+'_q2'+'_change']=hsi_y_x['EMA_'+data['Name_use_python'][i]+'_change']
#            hsi_y_x.loc[(hsi_y_x['month']>=7)&(hsi_y_x['month']<=9),'EMA_'+data['Name_use_python'][i]+'_q3'+'_change']=hsi_y_x['EMA_'+data['Name_use_python'][i]+'_change']
#            hsi_y_x.loc[(hsi_y_x['month']>=10)&(hsi_y_x['month']<=12),'EMA_'+data['Name_use_python'][i]+'_q4'+'_change']=hsi_y_x['EMA_'+data['Name_use_python'][i]+'_change']
#
#        else:
#            hsi_y_x.loc[(hsi_y_x['month']>=1)&(hsi_y_x['month']<=3),data['Name_use_python'][i]+'_q1'+'_change']=hsi_y_x[data['Name_use_python'][i]+'_change']
#            hsi_y_x.loc[(hsi_y_x['month']>=4)&(hsi_y_x['month']<=6),data['Name_use_python'][i]+'_q2'+'_change']=hsi_y_x[data['Name_use_python'][i]+'_change']
#            hsi_y_x.loc[(hsi_y_x['month']>=7)&(hsi_y_x['month']<=9),data['Name_use_python'][i]+'_q3'+'_change']=hsi_y_x[data['Name_use_python'][i]+'_change']
#            hsi_y_x.loc[(hsi_y_x['month']>=10)&(hsi_y_x['month']<=12),data['Name_use_python'][i]+'_q4'+'_change']=hsi_y_x[data['Name_use_python'][i]+'_change']

hsi_y_x=hsi_y_x.fillna(0)
hsi_y_x2=hsi_y_x.copy()
#hsi_y_x=hsi_y_x2.copy()

#create oil >0 and gold>0 factor
#hsi_y_x.loc[(hsi_y_x['GDAXI_change']>0)&(hsi_y_x['FTSE_change']>0)&(hsi_y_x['IXIC_change']>0)&(hsi_y_x['DJI_change']>0)&(hsi_y_x['GSPC_change']>0),'many1_great0_indicator']=1
#hsi_y_x.loc[~((hsi_y_x['GDAXI_change']>0)&(hsi_y_x['FTSE_change']>0)&(hsi_y_x['IXIC_change']>0)&(hsi_y_x['DJI_change']>0)&(hsi_y_x['GSPC_change']>0)),'many1_great0_indicator']=0
#
#hsi_y_x.loc[(hsi_y_x['GDAXI_change']<0)&(hsi_y_x['FTSE_change']<0)&(hsi_y_x['IXIC_change']<0)&(hsi_y_x['DJI_change']<0)&(hsi_y_x['GSPC_change']<0),'many1_less0_indicator']=1
#hsi_y_x.loc[~((hsi_y_x['GDAXI_change']<0)&(hsi_y_x['FTSE_change']<0)&(hsi_y_x['IXIC_change']<0)&(hsi_y_x['DJI_change']<0)&(hsi_y_x['GSPC_change']<0)),'many1_less0_indicator']=0
#
#hsi_y_x.loc[(hsi_y_x['GDAXI_change']>0)&(hsi_y_x['FTSE_change']>0)&(hsi_y_x['IXIC_change']>0)&(hsi_y_x['DJI_change']>0)&(hsi_y_x['GSPC_change']>0),'many1_group_indicator']=1
#hsi_y_x.loc[(hsi_y_x['GDAXI_change']<0)&(hsi_y_x['FTSE_change']<0)&(hsi_y_x['IXIC_change']<0)&(hsi_y_x['DJI_change']<0)&(hsi_y_x['GSPC_change']<0),'many1_group_indicator']=-1
#hsi_y_x['many1_group_indicator']=hsi_y_x['many1_group_indicator'].fillna(0)




#create factor if greater than average change
hsi_y_temp=hsi_y.copy()
hsi_y_temp['year']=hsi_y_temp['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)
hsi_y_temp['change']=hsi_y_temp['Close_HSI']-hsi_y_temp['Open_HSI']
#DJI_use=DJI.copy()
#DJI_use['year']=DJI_use['Date2'].apply(lambda x: datetime.strptime(x,'%Y-%m-%d').year)









#if use this, only use last year mean, may varies a lot
#def find_mean(x,asset_name):
#    mean_up=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].mean()
#    mean_down=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].mean()
#    sd_up=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].std(ddof=0)
#    sd_down=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].std(ddof=0)
#
#    mean_up_sd1=mean_up+sd_up
#    mean_up_sd2=mean_up+sd_up*2
#    mean_down_sd1=mean_down-sd_down
#    mean_down_sd2=mean_down-sd_down*2
#    return pd.Series([mean_up,mean_up_sd1,mean_up_sd2,mean_down,mean_down_sd1,mean_down_sd2])


#use cumulative mean
#x=HSSCX_use.loc[HSSCX_use['year']==2021,:]
#asset_name='HSSCX'
#xd=vars()[asset_name+'_use'].copy()
def find_mean(x,asset_name,xd):
    y_now=x.year.values[0]
    n=0
    x=xd.loc[(xd['year']<=y_now)&(xd['year']>=y_now-n),:].copy()
    
    mean_up=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].mean()
    mean_down=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].mean()
    sd_up=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].std(ddof=0)
    sd_down=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].std(ddof=0)

    mean_up_sd1=mean_up+sd_up
    mean_up_sd2=mean_up+sd_up*2
    mean_down_sd1=mean_down-sd_down
    mean_down_sd2=mean_down-sd_down*2
    return pd.Series([mean_up,mean_up_sd1,mean_up_sd2,mean_down,mean_down_sd1,mean_down_sd2])


#x=HSSCX_use.loc[HSSCX_use['year']==2021,:]
#asset_name='HSSCX'
#xd=vars()[asset_name+'_use'].copy()
#def find_mean(x,asset_name,xd):
#    y_now=x.year.values[0]
#    x=xd.loc[xd['year']<=y_now,:].copy()
#    
#    up_data=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].values
#    down_data=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].values
#    
#    mean_up=np.nanpercentile(up_data,50)
#    mean_down=np.nanpercentile(down_data,50)
#
#    mean_up_sd1=np.nanpercentile(up_data,75)
#    mean_up_sd2=np.nanpercentile(up_data,95)
#    mean_down_sd1=np.nanpercentile(down_data,25)
#    mean_down_sd2=np.nanpercentile(down_data,5)
#    return pd.Series([mean_up,mean_up_sd1,mean_up_sd2,mean_down,mean_down_sd1,mean_down_sd2])



#x=DJI_use.loc[DJI_use['year']==1993,:]
#asset_name='DJI'
#y=DJI_use.copy()
#def find_mean(y,x,asset_name):
#    year_use=x.head(1)['year'].values[0]
#    x=y.loc[y['year']<=year_use,:].copy().reset_index(drop=True)
#    mean_up=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].mean()
#    mean_down=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].mean()
#    sd_up=x.loc[x[asset_name+'_change']>0,:][asset_name+'_change'].std(ddof=0)
#    sd_down=x.loc[x[asset_name+'_change']<0,:][asset_name+'_change'].std(ddof=0)
#
#    mean_up_sd1=mean_up+sd_up
#    mean_up_sd2=mean_up+sd_up*2
#    mean_down_sd1=mean_down-sd_down
#    mean_down_sd2=mean_down-sd_down*2
#    return pd.Series([mean_up,mean_up_sd1,mean_up_sd2,mean_down,mean_down_sd1,mean_down_sd2,sd_up,sd_down])


#DJI_use_year_mean=DJI_use.groupby(['year']).apply(lambda x:find_mean(x.reset_index(drop=True),'DJI'))
#DJI_use_year_mean=DJI_use_year_mean.rename(columns={0:'mean_up',1:'mean_up_sd1',2:'mean_up_sd2',3:'mean_down',4:'mean_down_sd1',5:'mean_down_sd2'})
#DJI_use_year_mean.reset_index(0,inplace=True)
#DJI_use_year_mean['year_plus_one']=DJI_use_year_mean['year']+1

#asset_name='DJI'
#mean_asset_list=['GSPC','DJI','IXIC','NYA','FTSE','GDAXI','FCHI','N225','HSI_index','00001.SS','AORD','MXX','EWH','CHRIS_com_CME_GC1','CHRIS_com_CME_O1','CHRIS_com_ICE_B1','ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD']
mean_asset_list=['GSPC','DJI','HSI_index','IXIC','NYA','VIX','FTSE','GDAXI','FCHI','AORD','MXX','CHRIS_com_CME_GC1','CHRIS_com_CME_O1','EWH',
                 'CHRIS_com_ICE_B1','ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD',
                 'USTREASURY_REALLONGTERM','USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10','USTREASURY_REALYIELD_20',
                 'HDB','UBS','BBVA','DB','CM','CAJ','PHG','MSFT','T','AMX','MCK','CVX','BHP','RIO','PBR_A','CHRIS_bond_EUREX_FGBM1']
                 #'EMA_N225','EMA_HSI_index','EMA_00001.SS','EMA_1398_HK','EMA_0001_HK','EMA_0016_HK','EMA_0002_HK']
#mean_asset_list=['DJI']
                 
use_list
mean_asset_list=['GSPC','DJI','IXIC','NYA','VIX','FTSE',
                 'GDAXI','FCHI','AORD','MXX','CHRIS_com_CME_GC1',
                 'CHRIS_com_CME_O1','CHRIS_com_ICE_B1','ECB_cur_EURPHP','ECB_cur_EURRUB',
                 'ECB_cur_EURSGD','ECB_cur_EURUSD','USTREASURY_REALLONGTERM',
                 'USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10',
                 'USTREASURY_REALYIELD_20','UBS','BBVA','DB','CM','CAJ',
                 'PHG','T','AMX','MCK','CVX','BHP','RIO','PBR_A',
                 'CHRIS_bond_EUREX_FGBM1','HDB','ECB_cur_EURCNY','ECB_cur_EURHKD',
                 'MSFT','EWH',
                 '83188.HK','FJSCX','HJPNX','OTPSX',
                 'FBGKX','TBGVX','XBI','DHFCX']  
                
mean_asset_list=['ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD',
                 'USTREASURY_REALLONGTERM','USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10',
                 'USTREASURY_REALYIELD_20','index_SPX_wsj','index_DJIA_wsj','index_COMP_wsj','index_NYA_wsj','index_VIX_wsj',
                 'index_UK_NULL_UKX_wsj','index_DX_XETR_DAX_wsj','index_FR_XPAR_PX1_wsj','index_JP_XTKS_NIK_wsj','index_HK_XHKG_HSI_wsj',
                 'index_CN_SHCOMP_wsj','index_AU_XASX_XAO_wsj','index_MX_XMEX_IPC_wsj','etf_HK_XHKG_3188_wsj','etf_EWH_wsj',
                 'etf_XBI_wsj','HK_XHKG_1398_wsj','HK_XHKG_0001_wsj','HK_16_wsj','HK_XHKG_0002_wsj','HDB_wsj','UBS_wsj',
                 'BBVA_wsj','DB_wsj','CM_wsj','CAJ_wsj','PHG_wsj','MSFT_wsj','T_wsj','AMX_wsj','MCK_wsj','CVX_wsj','BHP_wsj',
                 'RIO_wsj','PBRA_wsj','OTPSX_wsj','FBGKX_wsj','HJPNX_wsj','FJSCX_wsj','TBGVX_wsj','DHFCX_wsj','brent_oil_investing',
                 'euro_bobl_investing','gold_futures_investing','oats_futures_investing']
        
        
        
        
mean_asset_list=['GSPC','DJI','IXIC','NYA','FTSE','GDAXI','FCHI','N225','HSI_index','00001.SS','AORD','MXX']
                 
                 
    
mean_asset_list=['index_DJIA_wsj','brent_oil_investing','euro_bobl_investing',
                 'gold_futures_investing','oats_futures_investing','hang_seng_oi','hang_seng_oi_volume']

#mean_asset_list=['FAS','PSK','VGIT']

                 #'index_CN_SHCOMP_wsj','etf_HK_XHKG_3188_wsj','etf_EWH_wsj']#,'0700_HK','0005_HK','1299_HK']
                 #'EMA_N225','EMA_HSI_index','EMA_00001.SS','EMA_1398_HK','EMA_0001_HK','EMA_0016_HK','EMA_0002_HK']

#asset_name='MGFIX'
#asset_name='index_DJIA_wsj'
#asset_name='brent_oil_investing'
#asset_name='euro_bobl_investing'
#asset_name='gold_futures_investing'
#asset_name='oats_futures_investing'
#hsi_y_x_2=hsi_y_x.copy()  
#hsi_y_x=hsi_y_x_2.copy()
for asset_name in mean_asset_list:
    vars()[asset_name+'_use']=vars()[asset_name].copy()
    vars()[asset_name+'_use']['year']=vars()[asset_name+'_use']['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)
    #DJI_use
    table_name=asset_name+'_use_year_mean'
    table_use=vars()[asset_name+'_use'].copy()
    #vars()[table_name]=vars()[asset_name+'_use'].groupby(['year']).apply(lambda x:find_mean(x.reset_index(drop=True),asset_name))
    vars()[table_name]=vars()[asset_name+'_use'].groupby(['year']).apply(lambda x:find_mean(x.reset_index(drop=True),asset_name,table_use))
    #vars()[table_name]=vars()[table_name].rename(columns={0:'mean_up',1:'mean_up_sd1',2:'mean_up_sd2',3:'mean_down',4:'mean_down_sd1',5:'mean_down_sd2',6:'sd_up',7:'sd_down'})
    vars()[table_name]=vars()[table_name].rename(columns={0:'mean_up',1:'mean_up_sd1',2:'mean_up_sd2',3:'mean_down',4:'mean_down_sd1',5:'mean_down_sd2'})    
    vars()[table_name].reset_index(0,inplace=True)
    vars()[table_name]['year_plus_one']=vars()[table_name]['year']+1
    
    
    a_check=vars()[table_name].copy()
    
    hsi_y_x_use=hsi_y_x[['Date2','year',asset_name+'_change']].copy()
    hsi_y_x_use=pd.merge(hsi_y_x_use,vars()[table_name],how='left',left_on=['year'],right_on=['year_plus_one'])
    
#    #also merge mean value to asset_name
#    if asset_name=='hang_seng_oi':
#        vars()[asset_name+'_use']=pd.merge(vars()[asset_name+'_use'],vars()[table_name],how='left',left_on=['year'],right_on=['year_plus_one'])
#        vars()[asset_name+'_use'].loc[vars()[asset_name+'_use'][asset_name+'_change']>=0,asset_name+'_fair_value']=vars()[asset_name+'_use'][asset_name+'_change']-vars()[asset_name+'_use']['mean_up']
#        vars()[asset_name+'_use'].loc[vars()[asset_name+'_use'][asset_name+'_change']<0,asset_name+'_fair_value']=vars()[asset_name+'_use'][asset_name+'_change']-vars()[asset_name+'_use']['mean_down']
#
#    a_check=vars()[asset_name+'_use'].copy()
#    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>0,'normal_up']=(hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up'])/hsi_y_x_use['sd_up']
#    hsi_y_x_use['normal_up']=hsi_y_x_use['normal_up'].fillna(0)
#    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<0,'normal_down']=(hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down'])/hsi_y_x_use['sd_down']
#    hsi_y_x_use['normal_down']=hsi_y_x_use['normal_down'].fillna(0)
#    
#    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>hsi_y_x_use['mean_up'],asset_name+'_greatless_mean_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up']
#    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<hsi_y_x_use['mean_down'],asset_name+'_greatless_mean_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down']
#    hsi_y_x_use[asset_name+'_greatless_mean_value_indicator']=hsi_y_x_use[asset_name+'_greatless_mean_value_indicator'].fillna(0)
#    
#    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>hsi_y_x_use['mean_up_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up_sd1']
#    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<hsi_y_x_use['mean_down_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down_sd1']
#    hsi_y_x_use[asset_name+'_greatless_mean_sd1_value_indicator']=hsi_y_x_use[asset_name+'_greatless_mean_sd1_value_indicator'].fillna(0)
#    
#    hsi_y_x_use.loc[hsi_y_x_use['normal_up']>0.84,asset_name+'_greatless_mean_sd2_value_indicator']=hsi_y_x_use['normal_up']
#    hsi_y_x_use.loc[hsi_y_x_use['normal_down']<-0.84,asset_name+'_greatless_mean_sd2_value_indicator']=hsi_y_x_use['normal_down']
#    hsi_y_x_use[asset_name+'_greatless_mean_sd2_value_indicator']=hsi_y_x_use[asset_name+'_greatless_mean_sd2_value_indicator'].fillna(0)
#    
   

    

    #hsi_y_x_use['hang_seng_oi_fair_value']
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>=0,asset_name+'_fair_value']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up']
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<0,asset_name+'_fair_value']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down']
        
    
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>hsi_y_x_use['mean_up'],asset_name+'_greatless_mean_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up']
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<hsi_y_x_use['mean_down'],asset_name+'_greatless_mean_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down']
    hsi_y_x_use[asset_name+'_greatless_mean_value_indicator']=hsi_y_x_use[asset_name+'_greatless_mean_value_indicator'].fillna(0)
    
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>hsi_y_x_use['mean_up_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up_sd1']
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<hsi_y_x_use['mean_down_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down_sd1']
    hsi_y_x_use[asset_name+'_greatless_mean_sd1_value_indicator']=hsi_y_x_use[asset_name+'_greatless_mean_sd1_value_indicator'].fillna(0)
    
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']>hsi_y_x_use['mean_up_sd2'],asset_name+'_greatless_mean_sd2_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_up_sd2']
    hsi_y_x_use.loc[hsi_y_x_use[asset_name+'_change']<hsi_y_x_use['mean_down_sd2'],asset_name+'_greatless_mean_sd2_value_indicator']=hsi_y_x_use[asset_name+'_change']-hsi_y_x_use['mean_down_sd2']
    hsi_y_x_use[asset_name+'_greatless_mean_sd2_value_indicator']=hsi_y_x_use[asset_name+'_greatless_mean_sd2_value_indicator'].fillna(0)
    
    hsi_y_x=pd.merge(hsi_y_x,hsi_y_x_use[['Date2',asset_name+'_fair_value',asset_name+'_greatless_mean_value_indicator',asset_name+'_greatless_mean_sd1_value_indicator',asset_name+'_greatless_mean_sd2_value_indicator']],how='left',left_on=['Date2'],right_on=['Date2'])
    
    hsi_y_x[asset_name+'_change_lag2']=hsi_y_x[asset_name+'_change'].shift(1)
    hsi_y_x[asset_name+'_change_lag3']=hsi_y_x[asset_name+'_change'].shift(2)
    hsi_y_x=hsi_y_x.fillna(0)
    
    
    

    
    
    

#aa=list(hsi_y_x.columns.values)
# mixture of ADR and Hong Kong
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_1398_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['IDCBY_wsj_greatless_mean_value_indicator']>0),'1398_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_1398_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['IDCBY_wsj_greatless_mean_value_indicator']<0),'1398_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_0001_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['CKHUY_wsj_greatless_mean_value_indicator']>0),'0001_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_0001_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['CKHUY_wsj_greatless_mean_value_indicator']<0),'0001_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_16_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['SUHJY_wsj_greatless_mean_value_indicator']>0),'16_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_16_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['SUHJY_wsj_greatless_mean_value_indicator']<0),'16_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_0002_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['CLPHY_wsj_greatless_mean_value_indicator']>0),'0002_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_0002_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['CLPHY_wsj_greatless_mean_value_indicator']<0),'0002_both_greater']=-1
#
#
#
#
#
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_0005_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['HSBC_wsj_greatless_mean_value_indicator']>0),'0005_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_0005_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['HSBC_wsj_greatless_mean_value_indicator']<0),'0005_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_1299_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['AAGIY_wsj_greatless_mean_value_indicator']>0),'1299_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_1299_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['AAGIY_wsj_greatless_mean_value_indicator']<0),'1299_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_939_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['CICHY_wsj_greatless_mean_value_indicator']>0),'939_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_939_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['CICHY_wsj_greatless_mean_value_indicator']<0),'939_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_700_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['HSNGY_wsj_greatless_mean_value_indicator']>0),'700_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_700_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['HSNGY_wsj_greatless_mean_value_indicator']<0),'700_both_greater']=-1
#
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_941_wsj_greatless_mean_value_indicator']>0)&(hsi_y_x['CHL_wsj_greatless_mean_value_indicator']>0),'941_both_greater']=1
#hsi_y_x.loc[(hsi_y_x['HK_XHKG_941_wsj_greatless_mean_value_indicator']<0)&(hsi_y_x['CHL_wsj_greatless_mean_value_indicator']<0),'941_both_greater']=-1
#
#
#hsi_y_x.loc[(hsi_y_x['1299_both_greater']==1)&(hsi_y_x['0005_both_greater']==1),'5_1299_939_greater']=1
#hsi_y_x.loc[(hsi_y_x['1299_both_greater']==-1)&(hsi_y_x['0005_both_greater']==-1),'5_1299_939_greater']=-1


#hsi_y_x=hsi_y_x.fillna(0)


#create indicator if 4 or 6 out of 7 main hsi component is positive or negative

#hsi_y_x_temp=hsi_y_x[['0700_HK_change','0005_HK_change',
#                      '0939_HK_change','1299_HK_change','0941_HK_change','1398_HK_change','2318_HK_change']].copy()
#hsi_y_x_temp=hsi_y_x[['0700_HK_change','0005_HK_change','1299_HK_change']].copy()
#hsi_y_x_temp=hsi_y_x[['0700_HK_greatless_mean_value_indicator',
#                      '0005_HK_greatless_mean_value_indicator',
#                      '1299_HK_greatless_mean_value_indicator']].copy()
##list(hsi_y_x.columns.values)
#
#hsi_y_x_temp_matrix=hsi_y_x_temp.as_matrix()
#temp_greater_zero=(hsi_y_x_temp_matrix>0).sum(axis=1)
#temp_less_zero=(hsi_y_x_temp_matrix<0).sum(axis=1)
#temp_up=(temp_greater_zero>=3)*1
#temp_down=(temp_less_zero>=3)*1
#hsi_y_x_temp['temp_up']=temp_up
#hsi_y_x_temp['temp_down']=temp_down
#
#hsi_y_x['temp_up_down']=temp_up-temp_down



#
#DJI_use_year_mean=DJI_use.groupby(['year']).apply(lambda x:find_mean(DJI_use,x.reset_index(drop=True),'DJI'))
#DJI_use_year_mean=DJI_use_year_mean.rename(columns={0:'mean_up',1:'mean_up_sd1',2:'mean_up_sd2',3:'mean_down',4:'mean_down_sd1',5:'mean_down_sd2'})
#DJI_use_year_mean.reset_index(0,inplace=True)
#DJI_use_year_mean['year_plus_one']=DJI_use_year_mean['year']+1



factor_indicator=['index_DJIA_wsj','brent_oil_investing','euro_bobl_investing',
                 'gold_futures_investing','oats_futures_investing','hang_seng_oi','hang_seng_oi_volume']


#factor_indicator=['FAS','PSK','VGIT']


                  #'FHSIVol4']
                  #'index_CN_SHCOMP_wsj','etf_HK_XHKG_3188_wsj','etf_EWH_wsj']#,'0700_HK','0005_HK','1299_HK']

#create indicator factor
for i in factor_indicator:
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd2_value_indicator']>0,i+'_greatless_mean_sd2_value_indicator_10']=1
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd2_value_indicator']<0,i+'_greatless_mean_sd2_value_indicator_10']=-1
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd2_value_indicator']==0,i+'_greatless_mean_sd2_value_indicator_10']=0

for i in factor_indicator:
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_value_indicator']>0,i+'_greatless_mean_value_indicator_10']=1
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_value_indicator']<0,i+'_greatless_mean_value_indicator_10']=-1
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_value_indicator']==0,i+'_greatless_mean_value_indicator_10']=0

for i in factor_indicator:
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd1_value_indicator']>0,i+'_greatless_mean_sd1_value_indicator_10']=1
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd1_value_indicator']<0,i+'_greatless_mean_sd1_value_indicator_10']=-1
    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd1_value_indicator']==0,i+'_greatless_mean_sd1_value_indicator_10']=0
#for i in factor_indicator:
#    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd1_value_indicator']>0,i+'_greatless_mean_sd1_value_indicator_10']=1
#    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd1_value_indicator']<0,i+'_greatless_mean_sd1_value_indicator_10']=-1
#    hsi_y_x.loc[hsi_y_x[i+'_greatless_mean_sd1_value_indicator']==0,i+'_greatless_mean_sd1_value_indicator_10']=0
    
hsi_y_x['brent_oil_gold_future_interact_indicator']=hsi_y_x['brent_oil_investing_greatless_mean_value_indicator_10']*hsi_y_x['gold_futures_investing_greatless_mean_value_indicator_10']












##difference between hsi and fhsi
#hsi_y_x_temp=hsi_y_x[['Date2','DateNum']].copy()
#
#hsi_y_x_temp=pd.merge(hsi_y_x_temp,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
#                      on=['Date2'],how='left')
#
#
#hsi_y_x_temp['Close_HSI_lag1']=hsi_y_x_temp['Close_HSI'].shift(1)
#hsi_y_x_temp['Close_HSI_lag1']=hsi_y_x_temp['Close_HSI_lag1'].fillna(0)
#
#hsi_y_x_temp=pd.merge(hsi_y_x_temp,index_HK_XHKG_HSI_wsj[['Date2','Close_index_HK_XHKG_HSI_wsj']].copy(),
#                      on=['Date2'],how='left')
#
#hsi_y_x_temp['Close_index_HK_XHKG_HSI_wsj_lag1']=hsi_y_x_temp['Close_index_HK_XHKG_HSI_wsj'].shift(1)
#hsi_y_x_temp['Close_index_HK_XHKG_HSI_wsj_lag1']=hsi_y_x_temp['Close_index_HK_XHKG_HSI_wsj_lag1'].fillna(0)
#
#hsi_y_x_temp['fhsi_minor_hsi']=hsi_y_x_temp['Close_HSI_lag1']-hsi_y_x_temp['Close_index_HK_XHKG_HSI_wsj_lag1']
#
#hsi_y_x_temp.loc[hsi_y_x_temp['fhsi_minor_hsi']>=0,'fhsi_minor_hsi_indicate']=1
#hsi_y_x_temp.loc[hsi_y_x_temp['fhsi_minor_hsi']<0,'fhsi_minor_hsi_indicate']=-1
#
#
#
#hsi_y_x=pd.merge(hsi_y_x,hsi_y_x_temp[['Date2','fhsi_minor_hsi','fhsi_minor_hsi_indicate']],how='left',left_on=['Date2'],right_on=['Date2'])







##random factor
#dim=hsi_y_x.shape[0]
#for i in range(2,201,2):
#    print(i)
#    s=np.random.normal(0,1,dim)
#    var1='random'+str(i)
#    var2='random'+str(i-1)
#    hsi_y_x[var1]=s
#    hsi_y_x[var2]=s*-1




##add percentile break down
#
#f1=['index_SPX_wsj_change',
#'ITOT_change',
#'VMBS_change',
#'VOO_change',
#'SCHG_change',
#'SCHX_change',
#'ECB_cur_EURCNY_change',
#'ECB_cur_EURSGD_change',
#'CWB_change',
#'HK_XHKG_1299_wsj_change',
#'IWF_change',
#'IWP_change',
#'EMA_index_DJIA_wsj_change_v2_15',
#'IVW_change',
#'RSP_change',
#'ILF_change',
#'index_NYA_wsj_change',
#'HK_1088_wsj_change',
#'SCHV_change',
#'copper_futures_investing_change',
#'VTV_change',
#'VTI_change',
#'ECB_cur_EURMYR_change']
#
##hsi_y_x.year
##df=hsi_y_x.copy()
##p1=25
##p2=50
##p3=75
##target_var='index_SPX_wsj_change'
##year_var='year'
#
#def percentile_breakdown(df,p1,p2,p3,target_var,year_var):
#    target_variable=target_var
#    distinct_year=df[year_var].unique()
#    distinct_year=[i for i in distinct_year if i >=2007]
#    #yy=2010
#    percentile_cum=pd.DataFrame([])
#    for yy in distinct_year:
#        data_use=df.loc[df[year_var]<yy,target_variable].values
#        first_percentile_capture=np.nanpercentile(data_use,25)
#        second_percentile_capture=np.nanpercentile(data_use,50)
#        third_percentile_capture=np.nanpercentile(data_use,75)
#        t1='first_percentile_'+target_variable
#        t2='second_percentile_'+target_variable
#        t3='third_percentile_'+target_variable
#        percentile_cum=percentile_cum.append(pd.DataFrame({year_var:[yy],
#                                                           t1:[first_percentile_capture],
#                                                           t2:[second_percentile_capture],
#                                                           t3:[third_percentile_capture]}))
#    
#    
#    df=pd.merge(df,percentile_cum,how='left',on=[year_var])
#    a_check=df.tail(1000)
#    
#    new_var=target_variable+'_percentile'
#    df.loc[(df[target_variable]<=df[t1])|(df[target_variable]>=df[t3]),new_var]=df[target_variable]
#    df.loc[(df[target_variable]>df[t1])&(df[target_variable]<df[t3]),new_var+'_middle']=df[target_variable]
#    df[new_var]=df[new_var].fillna(0)
#    df[new_var+'_middle']=df[new_var+'_middle'].fillna(0)
#    #df.dtypes
#    return df
#
##k='index_SPX_wsj_change'
#for k in f1:
#    hsi_y_x=percentile_breakdown(hsi_y_x,25,50,75,k,'year')
#
#
#
#aa=''
#for k in f1:
#    aa=aa+"'"+k+"'"+","+"'"+k+'_percentile'+"'"+","+"'"+k+'_percentile_middle'+"'"+","













hsi_y_x_temp2=hsi_y_x.copy()





import sys
sys.exit('stop here')













hsi_y_x=hsi_y_x_temp2.copy()



#test hang_seng_oi

oi_original= read_excel(os.path.join(tidy_path,'hang_seng_oi'+'_with_tidy.xlsx'),'Sheet1')
oi_original['year']=oi_original['Date2'].apply(lambda x:int(x[0:4]))


oi_original=oi_original.sort_values(by='DateNum',ascending=False).reset_index(drop=True)
oi_original=pd.merge(oi_original,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
                      on=['Date2'],how='left')

oi_original['diff']=oi_original['Close_HSI']-oi_original['Open_HSI']




#latest method
oi_original.loc[(oi_original['diff']>=0),'hang_seng_oi_change_revised1']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised1']=oi_original['hang_seng_oi_change_revised1'].fillna(0)
oi_original.loc[(oi_original['diff']<0),'hang_seng_oi_change_revised2']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised2']=oi_original['hang_seng_oi_change_revised2'].fillna(0)

oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']>=0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']<0)),'hang_seng_oi_change_revised3']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised3']=oi_original['hang_seng_oi_change_revised3'].fillna(0)
oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']<0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']>=0)),'hang_seng_oi_change_revised4']=oi_original['hang_seng_oi_change']
oi_original['hang_seng_oi_change_revised4']=oi_original['hang_seng_oi_change_revised4'].fillna(0)












target_table=oi_original.copy()












#for f_name in ['hang_seng_oi_change_revised1','hang_seng_oi_change_revised2',
#               'hang_seng_oi_change_revised3','hang_seng_oi_change_revised4']:

    
    
    
    
for f_name in ['hang_seng_oi_change_revised1','hang_seng_oi_change_revised2',
               'hang_seng_oi_change_revised3','hang_seng_oi_change_revised4']:
#               'hang_seng_oi_fair_value_revised1','hang_seng_oi_fair_value_revised2',
#               
#for f_name in ['hang_seng_oi_fair_value_revised3','hang_seng_oi_fair_value_revised4']:
    for ema_decay in [1,2,3,5,10,15]:
        #f_name='hang_seng_oi_change_revised1'
        appear=target_table[['Date2',f_name,'DateNum']].copy()
        target_col=f_name
        
        #ema_decay=5
            
        #appraoch2 equivalent (faster)
        #for each date with NA value in hsi_x
        #append to asset and perform ema and output the value
        hsi_x_temp=hsi_x.copy()  
        hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']],right=appear[['Date2',f_name]],how='left',on=['Date2'])        
        hsi_x_temp_Date_with_na=pd.DataFrame(hsi_x_temp.loc[pd.isnull(hsi_x_temp[f_name]),'Date2'].copy())
        
        if len(hsi_x_temp_Date_with_na)!=0: #for hk stock, date same as HSI, so no NA
            #find out latest date in hsi_y_x
            #if say today is trading date, asset won't have this date, so need to append to "appear"
            latest_date_hsi=max(hsi_x_temp_Date_with_na['Date2'])
            last_date=dt.strptime(latest_date_hsi,'%Y-%m-%d')
            add_datenum= (last_date-dt(1970,1,1)).days
            
            if latest_date_hsi>max(appear['Date2']):
                add_df=pd.DataFrame({'Date2':[latest_date_hsi],target_col:[np.nan],'DateNum':add_datenum})
                appear=add_df.append(appear)
            appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
            hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na.loc[hsi_x_temp_Date_with_na['Date2']<max(appear['Date2']),:].copy()
            date_in_asset=appear['Date2'].values
            
            #say, if 2018-09-09 is not in appear, and 2018-09-10 is the closest date in appear greatest then it
            #the ema of 2018-09-09 will be the same as 2018-09-10
            hsi_x_temp_Date_with_na_work['latest_date']=hsi_x_temp_Date_with_na_work['Date2'].apply(lambda x:date_in_asset[x<date_in_asset][-1])
            hsi_x_temp_Date_with_na_work=pd.merge(hsi_x_temp_Date_with_na_work,
                                                  appear[['Date2','EMA_'+target_col]].copy(),how='left',
                                                  left_on=['latest_date'],
                                                  right_on=['Date2'])
            del hsi_x_temp_Date_with_na_work['Date2_y']
            hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na_work.rename(columns={'Date2_x':'Date2'})
        else:
            appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
            hsi_x_temp_Date_with_na_work=pd.DataFrame(columns=['Date2','latest_date','EMA_'+target_col])
        
        hsi_x_temp=pd.merge(hsi_x_temp[['Date2','DateNum']],appear[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
        hsi_x_temp=pd.merge(hsi_x_temp,hsi_x_temp_Date_with_na_work[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
        hsi_x_temp=hsi_x_temp.fillna(0)
        hsi_x_temp['EMA_'+target_col+'_v2'+'_'+str(ema_decay)]=hsi_x_temp['EMA_'+target_col+'_x']+hsi_x_temp['EMA_'+target_col+'_y']
        
        hsi_y_x=pd.merge(hsi_y_x,hsi_x_temp[['Date2','EMA_'+target_col+'_v2'+'_'+str(ema_decay)]],how='left',left_on=['Date2'],right_on=['Date2'])


hsi_y_x.columns.values











#test hang_seng_oi and volume

oi_original= read_excel(os.path.join(tidy_path,'hang_seng_oi'+'_with_tidy.xlsx'),'Sheet1')
oi_original['year']=oi_original['Date2'].apply(lambda x:int(x[0:4]))


oi_original=oi_original.sort_values(by='DateNum',ascending=False).reset_index(drop=True)
oi_original=pd.merge(oi_original,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
                      on=['Date2'],how='left')

oi_original['diff']=oi_original['Close_HSI']-oi_original['Open_HSI']






#volume
table_name='hang_seng_oi_volume_use_year_mean'
hsi_vol=hang_seng_oi_volume.copy()
hsi_vol['year']=hsi_vol['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)

hsi_vol=pd.merge(hsi_vol,vars()[table_name],how='left',left_on=['year'],right_on=['year_plus_one'])

hsi_vol.columns.values

asset_name='hang_seng_oi_volume'
hsi_vol.loc[hsi_vol[asset_name+'_change']>hsi_vol['mean_up'],asset_name+'_greatless_mean_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_up']
hsi_vol.loc[hsi_vol[asset_name+'_change']<hsi_vol['mean_down'],asset_name+'_greatless_mean_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_down']
hsi_vol[asset_name+'_greatless_mean_value_indicator']=hsi_vol[asset_name+'_greatless_mean_value_indicator'].fillna(0)

hsi_vol.loc[hsi_vol[asset_name+'_change']>hsi_vol['mean_up_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_up_sd1']
hsi_vol.loc[hsi_vol[asset_name+'_change']<hsi_vol['mean_down_sd1'],asset_name+'_greatless_mean_sd1_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_down_sd1']
hsi_vol[asset_name+'_greatless_mean_sd1_value_indicator']=hsi_vol[asset_name+'_greatless_mean_sd1_value_indicator'].fillna(0)

hsi_vol.loc[hsi_vol[asset_name+'_change']>hsi_vol['mean_up_sd2'],asset_name+'_greatless_mean_sd2_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_up_sd2']
hsi_vol.loc[hsi_vol[asset_name+'_change']<hsi_vol['mean_down_sd2'],asset_name+'_greatless_mean_sd2_value_indicator']=hsi_vol[asset_name+'_change']-hsi_vol['mean_down_sd2']
hsi_vol[asset_name+'_greatless_mean_sd2_value_indicator']=hsi_vol[asset_name+'_greatless_mean_sd2_value_indicator'].fillna(0)



oi_original=pd.merge(oi_original,hsi_vol[['Date2','Open_hang_seng_oi_volume','Close_hang_seng_oi_volume','hang_seng_oi_volume_change',
                                          'hang_seng_oi_volume_greatless_mean_value_indicator','hang_seng_oi_volume_greatless_mean_sd1_value_indicator',
                                          'hang_seng_oi_volume_greatless_mean_sd2_value_indicator']].copy(),how='left',on=['Date2'])


#for settlement day and one day after it, hsi_vol has no values(removed the row), so in oi_original, it is nan, so remove it.
oi_original=oi_original.loc[~pd.isnull(oi_original['Close_hang_seng_oi_volume']),:]





oi_original['oi_over_volume']=(oi_original['Close_hang_seng_oi']-oi_original['Open_hang_seng_oi'])/oi_original['Close_hang_seng_oi_volume']






##latest method
oi_original.loc[(oi_original['diff']>=0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0),'hang_seng_oi_change_revised5']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised5']=oi_original['hang_seng_oi_change_revised5'].fillna(0)
oi_original.loc[(oi_original['diff']<0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0),'hang_seng_oi_change_revised6']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised6']=oi_original['hang_seng_oi_change_revised6'].fillna(0)

oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']>=0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']<0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0)),'hang_seng_oi_change_revised7']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised7']=oi_original['hang_seng_oi_change_revised7'].fillna(0)
oi_original.loc[((oi_original['diff']>=0)&(oi_original['hang_seng_oi_change']<0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0))|((oi_original['diff']<0)&(oi_original['hang_seng_oi_change']>=0)&(oi_original['hang_seng_oi_volume_greatless_mean_sd2_value_indicator']>0)),'hang_seng_oi_change_revised8']=oi_original['oi_over_volume']
oi_original['hang_seng_oi_change_revised8']=oi_original['hang_seng_oi_change_revised8'].fillna(0)







target_table=oi_original.copy()

f_name='hang_seng_oi_change_revised5'
for f_name in ['hang_seng_oi_change_revised5','hang_seng_oi_change_revised6',
               'hang_seng_oi_change_revised7','hang_seng_oi_change_revised8']:    
    for ema_decay in [1,2,3,5,10,15,20,25,30]:
        #f_name='hang_seng_oi_change_revised5'
        appear=target_table[['Date2',f_name,'DateNum']].copy()
        target_col=f_name
        
        #ema_decay=2
            
        #appraoch2 equivalent (faster)
        #for each date with NA value in hsi_x
        #append to asset and perform ema and output the value
        hsi_x_temp=hsi_x.copy()  
        hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']],right=appear[['Date2',f_name]],how='left',on=['Date2'])        
        hsi_x_temp_Date_with_na=pd.DataFrame(hsi_x_temp.loc[pd.isnull(hsi_x_temp[f_name]),'Date2'].copy())
        
        if len(hsi_x_temp_Date_with_na)!=0: #for hk stock, date same as HSI, so no NA
            #find out latest date in hsi_y_x
            #if say today is trading date, asset won't have this date, so need to append to "appear"
            latest_date_hsi=max(hsi_x_temp_Date_with_na['Date2'])
            last_date=dt.strptime(latest_date_hsi,'%Y-%m-%d')
            add_datenum= (last_date-dt(1970,1,1)).days
            
            if latest_date_hsi>max(appear['Date2']):
                add_df=pd.DataFrame({'Date2':[latest_date_hsi],target_col:[np.nan],'DateNum':add_datenum})
                appear=add_df.append(appear)
            appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
            hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na.loc[hsi_x_temp_Date_with_na['Date2']<max(appear['Date2']),:].copy()
            date_in_asset=appear['Date2'].values
            
            #say, if 2018-09-09 is not in appear, and 2018-09-10 is the closest date in appear greatest then it
            #the ema of 2018-09-09 will be the same as 2018-09-10
            hsi_x_temp_Date_with_na_work['latest_date']=hsi_x_temp_Date_with_na_work['Date2'].apply(lambda x:date_in_asset[x<date_in_asset][-1])
            hsi_x_temp_Date_with_na_work=pd.merge(hsi_x_temp_Date_with_na_work,
                                                  appear[['Date2','EMA_'+target_col]].copy(),how='left',
                                                  left_on=['latest_date'],
                                                  right_on=['Date2'])
            del hsi_x_temp_Date_with_na_work['Date2_y']
            hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na_work.rename(columns={'Date2_x':'Date2'})
        else:
            appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
            hsi_x_temp_Date_with_na_work=pd.DataFrame(columns=['Date2','latest_date','EMA_'+target_col])
        
        hsi_x_temp=pd.merge(hsi_x_temp[['Date2','DateNum']],appear[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
        hsi_x_temp=pd.merge(hsi_x_temp,hsi_x_temp_Date_with_na_work[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
        hsi_x_temp=hsi_x_temp.fillna(0)
        hsi_x_temp['EMA_'+target_col+'_v2'+'_'+str(ema_decay)]=hsi_x_temp['EMA_'+target_col+'_x']+hsi_x_temp['EMA_'+target_col+'_y']
        
        hsi_y_x=pd.merge(hsi_y_x,hsi_x_temp[['Date2','EMA_'+target_col+'_v2'+'_'+str(ema_decay)]],how='left',left_on=['Date2'],right_on=['Date2'])


hsi_y_x.columns.values














##use high water low water
#settlement_day = read_excel('daily_prediction_production/calendar.xlsx','settlement')
#settlement_day['Date2']=settlement_day['settlement_day'].astype(str)      
#settlement_day['settlement']=1
#
#tradeday_before20181224=read_excel('daily_prediction_production/calendar.xlsx','tradingdate_before20181227')
#calendar = read_excel('daily_prediction_production/calendar.xlsx','calendar')
#calendar['Date2']=calendar['Date'].astype(str)
#calendar=calendar.loc[calendar['trading_date']==1,:]  
#
#all_trading_date=tradeday_before20181224.append(calendar[['Date2']])
#all_trading_date=all_trading_date.reset_index(drop=True)
#
#all_trading_date=pd.merge(all_trading_date,settlement_day[['Date2','settlement']].copy(),how='left',on=['Date2'])
#all_trading_date['settlement']=all_trading_date['settlement'].fillna(0)
#
#all_trading_date['s1']=all_trading_date['settlement'].shift(-1)
#
#all_trading_date=pd.merge(all_trading_date,index_HK_XHKG_HSI_wsj[['Date2','Close_index_HK_XHKG_HSI_wsj']].copy(),how='left',on=['Date2'])
#
#
#all_trading_date=pd.merge(all_trading_date,hsi_y[['Date2','Close_HSI']].copy(),how='left',on=['Date2'])
#
#
#all_trading_date.loc[(all_trading_date['Close_HSI']>=all_trading_date['Close_index_HK_XHKG_HSI_wsj'])&(all_trading_date['settlement']==1),'water_settlement_impact_indicator']=1
#all_trading_date.loc[(all_trading_date['Close_HSI']<all_trading_date['Close_index_HK_XHKG_HSI_wsj'])&(all_trading_date['settlement']==1),'water_settlement_impact_indicator']=-1
#all_trading_date=all_trading_date.fillna(0)
#
#all_trading_date.loc[(all_trading_date['Close_HSI']>=all_trading_date['Close_index_HK_XHKG_HSI_wsj'])&(all_trading_date['settlement']==1),'water_settlement_impact_value']=all_trading_date['Close_HSI']-all_trading_date['Close_index_HK_XHKG_HSI_wsj']
#all_trading_date.loc[(all_trading_date['Close_HSI']<all_trading_date['Close_index_HK_XHKG_HSI_wsj'])&(all_trading_date['settlement']==1),'water_settlement_impact_value']=all_trading_date['Close_HSI']-all_trading_date['Close_index_HK_XHKG_HSI_wsj']
#all_trading_date=all_trading_date.fillna(0)
#
#
#water_df=pd.merge(hsi_y_x[['Date2','DateNum']].copy(),all_trading_date[['Date2','water_settlement_impact_indicator','water_settlement_impact_value']].copy(),how='left',on=['Date2'])
#water_df=water_df.sort_values(by=['Date2'],ascending=False)
#
#target_table=water_df.copy()
#
#
#    
#    
#for f_name in ['water_settlement_impact_indicator','water_settlement_impact_value']:    
#
#    for ema_decay in [1,2,3,5,10,15,20,25,30]:
#        #f_name='hang_seng_oi_change_revised5'
#        appear=target_table[['Date2',f_name,'DateNum']].copy()
#        target_col=f_name
#        
#        #ema_decay=2
#            
#        #appraoch2 equivalent (faster)
#        #for each date with NA value in hsi_x
#        #append to asset and perform ema and output the value
#        hsi_x_temp=hsi_x.copy()  
#        hsi_x_temp=pd.merge(left=hsi_x_temp[['Date2','DateNum']],right=appear[['Date2',f_name]],how='left',on=['Date2'])        
#        hsi_x_temp_Date_with_na=pd.DataFrame(hsi_x_temp.loc[pd.isnull(hsi_x_temp[f_name]),'Date2'].copy())
#        
#        if len(hsi_x_temp_Date_with_na)!=0: #for hk stock, date same as HSI, so no NA
#            #find out latest date in hsi_y_x
#            #if say today is trading date, asset won't have this date, so need to append to "appear"
#            latest_date_hsi=max(hsi_x_temp_Date_with_na['Date2'])
#            last_date=dt.strptime(latest_date_hsi,'%Y-%m-%d')
#            add_datenum= (last_date-dt(1970,1,1)).days
#            
#            if latest_date_hsi>max(appear['Date2']):
#                add_df=pd.DataFrame({'Date2':[latest_date_hsi],target_col:[np.nan],'DateNum':add_datenum})
#                appear=add_df.append(appear)
#            appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
#            hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na.loc[hsi_x_temp_Date_with_na['Date2']<max(appear['Date2']),:].copy()
#            date_in_asset=appear['Date2'].values
#            
#            #say, if 2018-09-09 is not in appear, and 2018-09-10 is the closest date in appear greatest then it
#            #the ema of 2018-09-09 will be the same as 2018-09-10
#            hsi_x_temp_Date_with_na_work['latest_date']=hsi_x_temp_Date_with_na_work['Date2'].apply(lambda x:date_in_asset[x<date_in_asset][-1])
#            hsi_x_temp_Date_with_na_work=pd.merge(hsi_x_temp_Date_with_na_work,
#                                                  appear[['Date2','EMA_'+target_col]].copy(),how='left',
#                                                  left_on=['latest_date'],
#                                                  right_on=['Date2'])
#            del hsi_x_temp_Date_with_na_work['Date2_y']
#            hsi_x_temp_Date_with_na_work=hsi_x_temp_Date_with_na_work.rename(columns={'Date2_x':'Date2'})
#        else:
#            appear=ema_custom_v2(appear,'DateNum',target_col,ema_decay)
#            hsi_x_temp_Date_with_na_work=pd.DataFrame(columns=['Date2','latest_date','EMA_'+target_col])
#        
#        hsi_x_temp=pd.merge(hsi_x_temp[['Date2','DateNum']],appear[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
#        hsi_x_temp=pd.merge(hsi_x_temp,hsi_x_temp_Date_with_na_work[['Date2','EMA_'+target_col]],how='left',left_on=['Date2'],right_on=['Date2'])
#        hsi_x_temp=hsi_x_temp.fillna(0)
#        hsi_x_temp['EMA_'+target_col+'_v2'+'_'+str(ema_decay)]=hsi_x_temp['EMA_'+target_col+'_x']+hsi_x_temp['EMA_'+target_col+'_y']
#        
#        hsi_y_x=pd.merge(hsi_y_x,hsi_x_temp[['Date2','EMA_'+target_col+'_v2'+'_'+str(ema_decay)]],how='left',left_on=['Date2'],right_on=['Date2'])
#
#
#a_check=hsi_y_x[['Date2','EMA_water_settlement_impact_indicator_v2_5']].copy()








#test thousand impact

hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()
hsi_y_temp['Close_HSI_shift1']=hsi_y_temp['Close_HSI'].shift(1)
hsi_y_temp['Close_HSI_shift1']=hsi_y_temp['Close_HSI_shift1'].fillna(0)
hsi_y_temp['3digit']=hsi_y_temp['Close_HSI_shift1'].apply(lambda x: int(str(round(x))[-3:]))
hsi_y_temp['3digit_1000']=1000-hsi_y_temp['3digit']
hsi_y_temp.loc[hsi_y_temp['3digit_1000']>500,'3digit_1000_lower']=hsi_y_temp['3digit']
hsi_y_temp.loc[hsi_y_temp['3digit_1000']<=500,'3digit_1000_upper']=hsi_y_temp['3digit_1000']
hsi_y_temp=hsi_y_temp.fillna(0)




hsi_y_temp['3digit_useopen']=hsi_y_temp['Open_HSI'].apply(lambda x: int(str(round(x))[-3:]))
hsi_y_temp['3digit_1000_useopen']=1000-hsi_y_temp['3digit_useopen']
hsi_y_temp.loc[hsi_y_temp['3digit_1000_useopen']>500,'3digit_1000_lower_useopen']=hsi_y_temp['3digit_useopen']
hsi_y_temp.loc[hsi_y_temp['3digit_1000_useopen']<=500,'3digit_1000_upper_useopen']=hsi_y_temp['3digit_1000_useopen']
hsi_y_temp=hsi_y_temp.fillna(0)




hsi_y_x=pd.merge(hsi_y_x,hsi_y_temp[['Date2','3digit_1000_lower','3digit_1000_upper','3digit_1000_lower_useopen','3digit_1000_upper_useopen']],how='left',left_on=['Date2'],right_on=['Date2'])




#round(21450.4)
#round(21650,-3)
#round(21500,-3)
#round(21499,-3)







#testpc_ratio
pc_ratio= read_excel(os.path.join(tidy_path,'pc_ratio'+'_with_tidy.xlsx'),'Sheet1')
pc_ratio['pc_ratio_lag1']=pc_ratio['pc_ratio'].shift(1)


pc_ratio=pd.merge(pc_ratio,oi_original[['Date2','diff']].copy(),how='left',on=['Date2'])
pc_ratio['diff_lag1']=pc_ratio['diff'].shift(1)

pc_ratio.loc[(pc_ratio['diff_lag1']>=0)&(pc_ratio['pc_ratio_lag1']<1),'pc_ratio_up']=pc_ratio['pc_ratio_lag1']
pc_ratio.loc[(pc_ratio['diff_lag1']<0)&(pc_ratio['pc_ratio_lag1']>=1),'pc_ratio_down']=pc_ratio['pc_ratio_lag1']


hsi_y_x=pd.merge(hsi_y_x,pc_ratio[['Date2','pc_ratio_up','pc_ratio_down']].copy(),how='left',on=['Date2'])
hsi_y_x=hsi_y_x.fillna(0)












#test break open impact

hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()


hsi_y_temp['Close_HSI_lag1']=hsi_y_temp['Close_HSI'].shift(1)

hsi_y_temp['break_open']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])
hsi_y_temp['break_open']=hsi_y_temp['break_open'].fillna(0)

hsi_y_temp['break_open_percent']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])/hsi_y_temp['Close_HSI_lag1']
hsi_y_temp['break_open_percent']=hsi_y_temp['break_open_percent'].fillna(0)

hsi_y_x=pd.merge(hsi_y_x,hsi_y_temp[['Date2','break_open','break_open_percent']],how='left',left_on=['Date2'],right_on=['Date2'])


#del hsi_y_x['break_open']
#del hsi_y_x['hsi_morning_change']





















#hsi morning change factor
hsi_morning=pd.read_excel('HSI_morning.xlsx','Sheet1')
hsi_morning['Date2']=hsi_morning['Date2'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_morning_change']=(hsi_morning['Close_HSI']-hsi_morning['Open_HSI'])/hsi_morning['Open_HSI']
hsi_morning['hsi_morning_change_indicator']=(hsi_morning['hsi_morning_change']>=0)*1

hsi_y_x=pd.merge(hsi_y_x,hsi_morning[['Date2','hsi_morning_change','hsi_morning_change_indicator']],how='left',left_on=['Date2'],right_on=['Date2'])








#full day prediction
full_day=pd.read_csv('./mis/all_prediction.csv')
temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()
from pandas import read_excel
in_sample_fitting=pd.read_excel('./mis/30013_test_2005_to_2010_insample_model2021.xlsx','daily_detail_summary')
in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()





in_sample_fitting=in_sample_fitting.append(temp)

hsi_y_x=pd.merge(hsi_y_x,in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

hsi_y_x=hsi_y_x.rename(columns={'Y_up_predict':'full_prediction_indicate',
                                'up_prediction_prob':'full_prediction_prob'})


hsi_y_x_temp2=hsi_y_x.copy()



































































hsi_y_x=hsi_y_x_temp2.copy()


#probablic SAR


import numpy as np
import talib
from talib import abstract
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt

def psar(barsdata,d_name,o_name,h_name,l_name,c_name, iaf = 0.02, maxaf = 0.2):
    length = len(barsdata)
    dates = list(barsdata[d_name])
    open_price=list(barsdata[o_name])
    high = list(barsdata[h_name])
    low = list(barsdata[l_name])
    close = list(barsdata[c_name])
    psar = close[0:len(close)]
    psarbull = [None] * length
    psarbear = [None] * length
    bull = True
    af = iaf
    ep = low[0]
    hp = high[0]
    lp = low[0]
    
    for i in range(2,length):
        if bull:
            psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
        else:
            psar[i] = psar[i - 1] + af * (lp - psar[i - 1])
        
        reverse = False
        
        if bull:
            if low[i] < psar[i]:
                bull = False
                reverse = True
                psar[i] = hp
                lp = low[i]
                af = iaf
        else:
            if high[i] > psar[i]:
                bull = True
                reverse = True
                psar[i] = lp
                hp = high[i]
                af = iaf
    
        if not reverse:
            if bull:
                if high[i] > hp:
                    hp = high[i]
                    af = min(af + iaf, maxaf)
                if low[i - 1] < psar[i]:
                    psar[i] = low[i - 1]
                if low[i - 2] < psar[i]:
                    psar[i] = low[i - 2]
            else:
                if low[i] < lp:
                    lp = low[i]
                    af = min(af + iaf, maxaf)
                if high[i - 1] > psar[i]:
                    psar[i] = high[i - 1]
                if high[i - 2] > psar[i]:
                    psar[i] = high[i - 2]
                    
        if bull:
            psarbull[i] = psar[i]
        else:
            psarbear[i] = psar[i]

    return {"dates":dates, "open":open_price,"high":high, "low":low, "close":close, "psar":psar, "psarbear":psarbear, "psarbull":psarbull}



import sys
import os


HSI_sar=pd.read_excel('HSI_with_tidy.xlsx','Sheet1')
#date need to be ascending order
result = psar(HSI_sar,d_name='Date2',o_name='Open_HSI',h_name='High_HSI',l_name='Low_HSI',c_name='Close_HSI',iaf = 0.02, maxaf = 0.2)

out=pd.DataFrame({'Date2':result['dates'], "open":result['open'],"high":result['high'], "low":result['low'],'close':result['close'],'psar':result['psar'],'psarbear':result['psarbear'],'psarbull':result['psarbull']})
out['DateNum']=out['Date2'].apply(lambda x :(dt.strptime(x,"%Y-%m-%d")-dt(1970,1,1)).days)


out['psarbear_high_diff']=out['psarbear']-out['high']
out['psarbull_low_diff']=out['low']-out['psarbull']
out['Date3'] = [dt.strptime(x, '%Y-%m-%d') for x in out['Date2']]
#out=out[0:-1]


out['sar_up2']=out['psarbull_low_diff'].shift(1)
out['sar_down2']=out['psarbear_high_diff'].shift(1)
out['sar_up2']=out['sar_up2'].fillna(0)
out['sar_down2']=out['sar_down2'].fillna(0)



hsi_y_x=pd.merge(hsi_y_x,out[['Date2','sar_up2', 'sar_down2']],how='left',left_on=['Date2'],right_on=['Date2'])


out_name='hsi_y_x'
#out_name='hsi_y_x_n225_0_to_60'

import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore(out_name+'.hdf5', "w", complib=str("zlib"), complevel=5)
store.put(out_name+'_dataframe',hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()








#try price - ema 10 factor
HSI_source_temp=pd.read_excel('HSI_with_tidy.xlsx','Sheet1')
HSI_source_temp['Date2']=HSI_source_temp['Date2'].astype(str)
HSI_source_temp=HSI_source_temp.rename(columns={"Close_HSI":'close'})
HSI_source_temp['ema_10']=abstract.EMA(HSI_source_temp,10)
HSI_source_temp['price_ema10']=100*(HSI_source_temp['close']-HSI_source_temp['ema_10'])/HSI_source_temp['ema_10']


HSI_source_temp['f1']=100*(1/(1+np.exp(-1*HSI_source_temp['price_ema10'])))
HSI_source_temp['f1']=HSI_source_temp['f1'].shift(1)


HSI_source_temp.loc[(HSI_source_temp['f1']>=90),'f1_v2']=-1
HSI_source_temp.loc[(HSI_source_temp['f1']<=10),'f1_v2']=1


HSI_source_temp['f1_v2']=HSI_source_temp['f1_v2'].fillna(0)

hsi_y_x=pd.merge(hsi_y_x,HSI_source_temp[['Date2','f1','f1_v2']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

out_name='hsi_y_x'
import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore(out_name+'.hdf5', "w", complib=str("zlib"), complevel=5)
store.put(out_name+'_dataframe',hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()















#data=HSI_source.copy()
#datenum_field='DateNum'
#target_field='smaBuy_original'
#decay=5
    
#datenum is in decending order
def ema_custom_v2(data,datenum_field,target_field,decay):
    datenum_vector=np.array(data[datenum_field],dtype=pd.Series).astype(np.float)#convert dataframe column to array
    target_vector=np.array(data[target_field],dtype=pd.Series).astype(np.float)
    
    m=len(target_vector)
    r=0 if len(np.where(target_vector!=0)[0])==0 else max(np.where(target_vector!=0)[0])
    datenum_vector=datenum_vector[:r+1]
    target_vector=target_vector[:r+1]
    
    n=len(datenum_vector)        
    temp=np.tile(datenum_vector,n) #make replication
    matrix_fill_h=np.reshape(temp,(n,n))
    matrix_fill_v=matrix_fill_h.T
    diff=matrix_fill_v-matrix_fill_h
    ind=diff<0 #filter out negative value
    diff[ind]=0
    diff=diff[0:diff.shape[0]-1,1:diff.shape[0]]*-1.0
    matrix_fill=diff
    
    up_tri_all1=np.triu(np.ones((n-1,n-1),dtype=np.int),0)
    matrix_fill_use=np.multiply(np.exp(matrix_fill/decay),up_tri_all1)
    
    matrix_fill_use_div_rowsum=matrix_fill_use/np.sum(matrix_fill_use,axis=1,keepdims=True)
    x=np.reshape(target_vector[1:len(target_vector)],(len(target_vector)-1,1))#exclude first elemnt of target vector
    #output=np.vstack((np.dot(matrix_fill_use_div_rowsum,x),np.array([0.0])))#append 0 to last row
    output=np.vstack((np.dot(matrix_fill_use_div_rowsum,x),np.reshape(np.zeros(m-r),(m-r,1))))#append 0 to last row
    name='EMA_'+target_field
    data[name]=output
    return data

data1=pd.DataFrame({'Datenum':[17010,17000,16990],'nfp': [0,5,8]}) 
ema_custom_v2(data1,'Datenum','nfp',5)











import sys
import os


#import numpy as np
#np.__version__
#import talib
#import pandas as pd
#os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')





#for hsi only
selection_target='fhsi'
HSI_source=pd.read_excel('HSI_with_tidy.xlsx','Sheet1')
HSIvolume_source=pd.read_excel('hang_seng_oi_volume.xlsx','Sheet1')
HSIvolume_source['Date2']=HSIvolume_source['Date'].dt.date
HSIvolume_source['Date2']=HSIvolume_source['Date2'].astype(str)
HSI_source=pd.merge(HSI_source,HSIvolume_source[['Date2','Volume']].copy(),how='left',on=['Date2'])
HSI_source=HSI_source[0:-1].copy()
HSI_source=HSI_source.rename(columns={'Open_HSI':'open','High_HSI':'high','Low_HSI':'low','Close_HSI':'close','Volume':'volume'})


#For US stock
selection_target='BAC'
selection_target='WFC'
selection_target='AAPL'
selection_target='BP'
selection_target='MSFT'
selection_target='CSCO'
selection_target='INTC'
selection_target='BMY'
selection_target='C'
selection_target='CVX'
selection_target='VZ'
selection_target='F'
selection_target='SLB'

selection_target='LVS'

selection_target='NVDA'

selection_target='M'
selection_target='AMD'
selection_target='PLTR'
selection_target='VALE'
selection_target='WISH'
selection_target='NIO'
selection_target='PFE'
selection_target='CLF'



HSI_source=pd.read_excel(os.path.join('backtest_linux/database/tidy',selection_target+'_with_tidy.xlsx'),'Sheet1')
t1='Open_'+selection_target
t2='High_'+selection_target
t3='Low_'+selection_target
t4='Close_'+selection_target
t5='Volume_'+selection_target
t6=selection_target+'_change'
HSI_source=HSI_source.rename(columns={t1:'open',t2:'high',t3:'low',t4:'close',t5:'volume',t6:'HSI_change'})

HSI_source=HSI_source.loc[HSI_source['Date2']>='2005-01-01',['Date2','open','high','low','close','volume','HSI_change','DateNum']].copy()









#future_period=5
#change_at_least=0.02
#
##find max close in the future 5 day, not include today
#HSI_source['period_maxclose']=HSI_source.close.rolling(future_period).max().shift(-future_period)
#HSI_source['period_minclose']=HSI_source.close.rolling(future_period).min().shift(-future_period)
#
##remove both null
#HSI_source=HSI_source.loc[(~pd.isnull(HSI_source['period_minclose']))&(~pd.isnull(HSI_source['period_maxclose'])),:].copy()
#
#HSI_source['period_maxclose_change']=(HSI_source['period_maxclose']-HSI_source['open'])/HSI_source['open']
#HSI_source['period_minclose_change']=(HSI_source['period_minclose']-HSI_source['open'])/HSI_source['open']
#
#HSI_source.loc[(HSI_source['period_maxclose_change']>change_at_least)|(HSI_source['period_minclose_change']>change_at_least),'Y_up_cum']=1
#HSI_source.loc[(HSI_source['period_maxclose_change']<-change_at_least)|(HSI_source['period_minclose_change']<-change_at_least),'Y_down_cum']=1
#
#
#HSI_source['temp1']=(abs(HSI_source['period_maxclose_change'])>abs(HSI_source['period_minclose_change']))*1
#HSI_source['temp2']=np.where(HSI_source['temp1']==1,np.sign(HSI_source['period_maxclose_change']),np.sign(HSI_source['period_minclose_change']))
#
##both larger than change_at_least
#sum((HSI_source['Y_up_cum']==1)&(HSI_source['Y_down_cum']==1))/HSI_source.shape[0]
##both smaller than change_at_least
#sum(pd.isnull(HSI_source['Y_up_cum'])&pd.isnull(HSI_source['Y_down_cum']))/HSI_source.shape[0]
#
#
##for those both less than/larger than change_at_least, follow the sign of abs max of 'period_maxclose_change' and 'period_miuclose_change'
#HSI_source.loc[(HSI_source['Y_up_cum']==1)&(HSI_source['Y_down_cum']==1)&(HSI_source['temp2']==1),'Y_up_cum2']=1
#HSI_source.loc[(HSI_source['Y_up_cum']==1)&(HSI_source['Y_down_cum']==1)&(HSI_source['temp2']==-1),'Y_down_cum2']=1
#HSI_source.loc[pd.isnull(HSI_source['Y_up_cum'])&pd.isnull(HSI_source['Y_down_cum'])&(HSI_source['temp2']==1),'Y_up_cum2']=1
#HSI_source.loc[pd.isnull(HSI_source['Y_up_cum'])&pd.isnull(HSI_source['Y_down_cum'])&(HSI_source['temp2']==-1),'Y_down_cum2']=1
#
#
#both_equal=((HSI_source['Y_up_cum']==1)&(HSI_source['Y_down_cum']==1))|(pd.isnull(HSI_source['Y_up_cum'])&pd.isnull(HSI_source['Y_down_cum']))
#
#HSI_source.loc[both_equal,'Y_up_cum_final']=HSI_source['Y_up_cum2']
#HSI_source.loc[~both_equal,'Y_up_cum_final']=HSI_source['Y_up_cum']
#
#HSI_source.loc[both_equal,'Y_down_cum_final']=HSI_source['Y_down_cum2']
#HSI_source.loc[~both_equal,'Y_down_cum_final']=HSI_source['Y_down_cum']
#
#del HSI_source['Y_up_cum'];del HSI_source['Y_down_cum']
#del HSI_source['Y_up_cum2'];del HSI_source['Y_down_cum2']
#del HSI_source['temp1'];del HSI_source['temp2']
#
#HSI_source=HSI_source.fillna(0)


#or use normal response
HSI_source['Y_up_cum_final']=HSI_source.apply(lambda row: (row.close>=row.open)*1,axis=1)
HSI_source['Y_down_cum_final']=HSI_source.apply(lambda row: (row.close<row.open)*1,axis=1)
















#date need to be ascending order
result = psar(HSI_source,d_name='Date2',o_name='open',h_name='high',l_name='low',c_name='close',iaf = 0.02, maxaf = 0.2) #iaf 0.02

out=pd.DataFrame({'Date2':result['dates'], "open":result['open'],"high":result['high'], "low":result['low'],'close':result['close'],'psar':result['psar'],'psarbear':result['psarbear'],'psarbull':result['psarbull']})
out['DateNum']=out['Date2'].apply(lambda x :(dt.strptime(x,"%Y-%m-%d")-dt(1970,1,1)).days)


out['psarbear_high_diff']=out['psarbear']-out['high']
out['psarbull_low_diff']=out['low']-out['psarbull']
out['Date3'] = [dt.strptime(x, '%Y-%m-%d') for x in out['Date2']]
#out=out[0:-1]


plt.plot(out['Date3'], out['close'])
plt.plot(out['Date3'], out['psarbull'])
plt.plot(out['Date3'], out['psarbear'])
plt.grid()
plt.show()




out['sar_up']=out['psarbull'].shift(1)
out['sar_down']=out['psarbear'].shift(1)
out.loc[~(pd.isnull(out['sar_up'])),'sar_up_indicator']=1
out.loc[~(pd.isnull(out['sar_down'])),'sar_down_indicator']=1
out['sar_up_indicator']=out['sar_up_indicator'].fillna(0)
out['sar_down_indicator']=out['sar_down_indicator'].fillna(0)
out['sar_indicator']=out['sar_up_indicator']-out['sar_down_indicator']

out['sar_up']=out['sar_up'].fillna(0)
out['sar_down']=out['sar_down'].fillna(0)
out['sar_value_indicator']=out['sar_up']-out['sar_down']



out['sar_up2']=out['psarbull_low_diff'].shift(1)
out['sar_down2']=out['psarbear_high_diff'].shift(1)
out['sar_up2']=out['sar_up2'].fillna(0)
out['sar_down2']=out['sar_down2'].fillna(0)
out['sar_value2_indicator']=out['sar_up2']-out['sar_down2']

#out.loc[out['sar_up2']<=1000,'sar_up2']=0
#out.loc[out['sar_down2']<=1000,'sar_down2']=0





HSI_source=pd.merge(HSI_source,out[['Date2','sar_up','sar_down',
                                'sar_up_indicator', 'sar_down_indicator',
                                'sar_indicator',
                                'sar_value_indicator',
                                'sar_up2', 'sar_down2',
                                'sar_value2_indicator']],how='left',left_on=['Date2'],right_on=['Date2'])


#hsi_y_x_temp2=hsi_y_x.copy()









#hsi_y_x=hsi_y_x_temp2.copy()


import numpy as np
import pandas as pd
import talib
from talib import abstract
#date need to be arranged in ascending order using ta-lib




# Calculate parabolic sar
HSI_source['SAR'] = abstract.SAR(HSI_source,acceleration=0.02, maximum=0.2)
HSI_source['SAREXT'] = abstract.SAREXT(HSI_source)



# Plot Parabolic SAR with close price
HSI_source[['close', 'SAR']][:500].plot(figsize=(10,5))
plt.grid()
plt.show()




#sar use percentile
HSI_source.loc[HSI_source['SAR']>=HSI_source['high'],'sar_talib_down2']=HSI_source['SAR']-HSI_source['high']
HSI_source.loc[HSI_source['SAR']<=HSI_source['low'],'sar_talib_up2']=HSI_source['low']-HSI_source['SAR']

HSI_source['sar_talib_down2_shift1']=HSI_source['sar_talib_down2'].shift(1)
HSI_source['sar_talib_down2_shift1']=HSI_source['sar_talib_down2_shift1'].fillna(0)
HSI_source['sar_talib_up2_shift1']=HSI_source['sar_talib_up2'].shift(1)
HSI_source['sar_talib_up2_shift1']=HSI_source['sar_talib_up2_shift1'].fillna(0)

HSI_source['year_cohord']=HSI_source['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)
HSI_source['sar_talib_modified']=HSI_source['sar_talib_up2_shift1']-HSI_source['sar_talib_down2_shift1']

HSI_source['sar_talib_modified_original']=HSI_source['sar_talib_modified'].copy()


target_variable='sar_talib_modified_original'


distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
a_check=HSI_source.tail(1000)

new_var=target_variable+'_percentile'
HSI_source.loc[(HSI_source[target_variable]<=HSI_source[t1])|(HSI_source[target_variable]>=HSI_source[t3]),new_var]=HSI_source[target_variable]
HSI_source.loc[HSI_source[target_variable]<=HSI_source[t1],new_var+'lower']=HSI_source[target_variable]*-1
HSI_source.loc[HSI_source[target_variable]>=HSI_source[t3],new_var+'upper']=HSI_source[target_variable]
HSI_source[new_var+'lower']=HSI_source[new_var+'lower'].fillna(0)
HSI_source[new_var+'upper']=HSI_source[new_var+'upper'].fillna(0)

HSI_source[new_var]=HSI_source[new_var].fillna(0)
















#muli 
vector_arith_multi=abstract.MULT(HSI_source)
HSI_source['vector_arith_multi']=vector_arith_multi
HSI_source['vector_arith_multi_shift1']=HSI_source['vector_arith_multi'].shift(1)


help(abstract.MULT)


#linear
linint=abstract.LINEARREG_INTERCEPT(HSI_source)
HSI_source['linint']=linint
HSI_source['linint_shift1']=HSI_source['linint'].shift(1)
HSI_source['linint_change']=(HSI_source['linint']-HSI_source['linint_shift1'])/HSI_source['linint_shift1']
HSI_source['linint_shift1_change']=HSI_source['linint_change'].shift(1)



#ad  Chaikin A/D Line
ad=abstract.AD(HSI_source)
HSI_source['ad']=ad
HSI_source['ad_shift1']=HSI_source['ad'].shift(1)
HSI_source['ad_change']=(HSI_source['ad']-HSI_source['ad_shift1'])/HSI_source['ad_shift1']
HSI_source['ad_change_shift1']=HSI_source['ad_change'].shift(1)

HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['ad_change']<0),'ad1']=HSI_source['ad_change']
HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['ad_change']>=0),'ad2']=HSI_source['ad_change']
HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['ad_change']>=0),'ad3']=HSI_source['ad_change']
HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['ad_change']<0),'ad4']=HSI_source['ad_change']



HSI_source['ad1_shift1']=HSI_source['ad1'].shift(1)
HSI_source['ad2_shift1']=HSI_source['ad2'].shift(1)
HSI_source['ad3_shift1']=HSI_source['ad3'].shift(1)
HSI_source['ad4_shift1']=HSI_source['ad4'].shift(1)
HSI_source=HSI_source.fillna(0)













#OBV  On-Balance Volume  https://www.fmlabs.com/reference/default.htm?url=OBV.htm
obv=abstract.OBV(HSI_source)
HSI_source['obv']=obv
HSI_source['obv_shift1']=HSI_source['obv'].shift(1)
HSI_source['obv_change']=(HSI_source['obv']-HSI_source['obv_shift1'])


HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['obv_change']<0),'obv1']=HSI_source['obv_change']
HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['obv_change']>=0),'obv2']=HSI_source['obv_change']
HSI_source.loc[(HSI_source['HSI_change']>=0)&(HSI_source['obv_change']>=0),'obv3']=HSI_source['obv_change']
HSI_source.loc[(HSI_source['HSI_change']<0)&(HSI_source['obv_change']<0),'obv4']=HSI_source['obv_change']


HSI_source['obv1_shift1']=HSI_source['obv1'].shift(1)
HSI_source['obv2_shift1']=HSI_source['obv2'].shift(1)
HSI_source['obv3_shift1']=HSI_source['obv3'].shift(1)
HSI_source['obv4_shift1']=HSI_source['obv4'].shift(1)
HSI_source=HSI_source.fillna(0)







#money flow 14
moneyflow=abstract.MFI(HSI_source,14)
HSI_source['moneyflow']=moneyflow
HSI_source['moneyflow_shift1']=HSI_source['moneyflow'].shift(1)
HSI_source.loc[(HSI_source['moneyflow_shift1']<=20),'moneyflow_up']=HSI_source['moneyflow_shift1']
HSI_source['moneyflow_up']=HSI_source['moneyflow_up'].fillna(0)

HSI_source.loc[(HSI_source['moneyflow_shift1']>=80),'moneyflow_down']=HSI_source['moneyflow_shift1']
HSI_source['moneyflow_down']=HSI_source['moneyflow_down'].fillna(0)








#william 14
william=abstract.WILLR(HSI_source,14)
HSI_source['william']=william*-1
HSI_source['william_shift1']=HSI_source['william'].shift(1)
HSI_source.loc[(HSI_source['william_shift1']<=20),'william_up']=HSI_source['william_shift1']
HSI_source['william_up']=HSI_source['william_up'].fillna(0)

HSI_source.loc[(HSI_source['william_shift1']>=80),'william_down']=HSI_source['william_shift1']
HSI_source['william_down']=HSI_source['william_down'].fillna(0)






#UltimateOscillator 14

UltimateOscillator=abstract.ULTOSC(HSI_source, timeperiod1=7, timeperiod2=14, timeperiod3=28)
HSI_source['UltimateOscillator']=UltimateOscillator
HSI_source['UltimateOscillator_shift1']=HSI_source['UltimateOscillator'].shift(1)
HSI_source.loc[(HSI_source['UltimateOscillator_shift1']<=30),'UltimateOscillator_up']=HSI_source['UltimateOscillator_shift1']
HSI_source['UltimateOscillator_up']=HSI_source['UltimateOscillator_up'].fillna(0)

HSI_source.loc[(HSI_source['UltimateOscillator_shift1']>=70),'UltimateOscillator_down']=HSI_source['UltimateOscillator_shift1']
HSI_source['UltimateOscillator_down']=HSI_source['UltimateOscillator_down'].fillna(0)







#true range

truerange_plus=abstract.PLUS_DM(HSI_source,timeperiod=14)
truerange_minus=abstract.MINUS_DM(HSI_source,timeperiod=14)
HSI_source['truerange_plus']=truerange_plus
HSI_source['truerange_minus']=truerange_minus

HSI_source['truerange_plus_shift1']=HSI_source['truerange_plus'].shift(1)
HSI_source['truerange_minus_shift1']=HSI_source['truerange_minus'].shift(1)

HSI_source['truerange']=HSI_source['truerange_plus_shift1']-HSI_source['truerange_minus_shift1']


HSI_source.loc[(HSI_source['truerange']>=0),'truerange_up']=HSI_source['truerange']
HSI_source['truerange_up']=HSI_source['truerange_up'].fillna(0)

HSI_source.loc[(HSI_source['truerange']<0),'truerange_down']=HSI_source['truerange']
HSI_source['truerange_down']=HSI_source['truerange_down'].fillna(0)
HSI_source['truerange_down']=HSI_source['truerange_down']*-1











#DX
directmove=abstract.DX(HSI_source,14)
HSI_source['directmove']=directmove
HSI_source['directmove_shift1']=HSI_source['directmove'].shift(1)
HSI_source.loc[(HSI_source['directmove_shift1']>=50),'directmove_up']=HSI_source['directmove_shift1']
HSI_source['directmove_up']=HSI_source['directmove_up'].fillna(0)

HSI_source.loc[(HSI_source['directmove_shift1']<=2),'directmove_down']=HSI_source['directmove_shift1']
HSI_source['directmove_down']=HSI_source['directmove_down'].fillna(0)













#bop
balancepower=abstract.BOP(HSI_source,14)
HSI_source['balancepower']=balancepower
HSI_source['balancepower_shift1']=HSI_source['balancepower'].shift(1)
HSI_source.loc[(HSI_source['balancepower_shift1']>=0),'balancepower_up']=HSI_source['balancepower_shift1']
HSI_source['balancepower_up']=HSI_source['balancepower_up'].fillna(0)

HSI_source.loc[(HSI_source['balancepower_shift1']<0),'balancepower_down']=HSI_source['balancepower_shift1']
HSI_source['balancepower_down']=HSI_source['balancepower_down'].fillna(0)







#aroon OSC  (up-down)
aroon=abstract.AROONOSC(HSI_source,14)
HSI_source['aroon']=aroon
HSI_source['aroon_shift1']=HSI_source['aroon'].shift(1)
HSI_source.loc[(HSI_source['aroon_shift1']>=0),'aroon_up']=HSI_source['aroon_shift1']
HSI_source['aroon_up']=HSI_source['aroon_up'].fillna(0)

HSI_source.loc[(HSI_source['aroon_shift1']<0),'aroon_down']=HSI_source['aroon_shift1']
HSI_source['aroon_down']=HSI_source['aroon_down'].fillna(0)

HSI_source.loc[(HSI_source['aroon_shift1']>=70),'aroon_up_70']=HSI_source['aroon_shift1']
HSI_source['aroon_up_70']=HSI_source['aroon_up_70'].fillna(0)
HSI_source.loc[(HSI_source['aroon_shift1']<=-70),'aroon_down_70']=HSI_source['aroon_shift1']
HSI_source['aroon_down_70']=HSI_source['aroon_down_70'].fillna(0)




target_variable='aroon_shift1'
distinct_year=HSI_source['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=HSI_source.loc[HSI_source['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


HSI_source=pd.merge(HSI_source,percentile_cum,how='left',on=['year_cohord'])
a_check=HSI_source.tail(1000)

new_var=target_variable+'_percentile'
HSI_source.loc[(HSI_source[target_variable]<=HSI_source[t1])|(HSI_source[target_variable]>=HSI_source[t3]),new_var]=HSI_source[target_variable]
HSI_source.loc[HSI_source[target_variable]<=HSI_source[t1],new_var+'lower']=HSI_source[target_variable]*-1
HSI_source.loc[HSI_source[target_variable]>=HSI_source[t3],new_var+'upper']=HSI_source[target_variable]
HSI_source[new_var+'lower']=HSI_source[new_var+'lower'].fillna(0)
HSI_source[new_var+'upper']=HSI_source[new_var+'upper'].fillna(0)

HSI_source[new_var]=HSI_source[new_var].fillna(0)










#short ema over long ema
shortSMA=abstract.SMA(HSI_source,7)
longSMA=abstract.SMA(HSI_source,200)
HSI_source['shortSMA'] = shortSMA
HSI_source['longSMA'] =longSMA
HSI_source['smaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
HSI_source['smaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))

HSI_source['smaSell']=HSI_source['smaSell']*1
HSI_source['smaBuy']=HSI_source['smaBuy']*1

HSI_source['smaSell_original']=HSI_source['smaSell'].shift(-1)
HSI_source['smaBuy_original']=HSI_source['smaBuy'].shift(-1)

HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
HSI_source=ema_custom_v2(HSI_source,'DateNum','smaSell_original',5)
HSI_source=ema_custom_v2(HSI_source,'DateNum','smaBuy_original',5)
HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)



#short ema over long ema
shortSMA=abstract.SMA(HSI_source,3)
longSMA=abstract.SMA(HSI_source,10)
HSI_source['shortSMA'] = shortSMA
HSI_source['longSMA'] =longSMA
HSI_source['smaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
HSI_source['smaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))

HSI_source['smaSell']=HSI_source['smaSell']*1
HSI_source['smaBuy']=HSI_source['smaBuy']*1

HSI_source['smaSell_original2']=HSI_source['smaSell'].shift(-1)
HSI_source['smaBuy_original2']=HSI_source['smaBuy'].shift(-1)

HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
HSI_source=ema_custom_v2(HSI_source,'DateNum','smaSell_original2',5)
HSI_source=ema_custom_v2(HSI_source,'DateNum','smaBuy_original2',5)
HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)



#CDL3OUTSIDE - Three Outside Up/Down
pattern1 = abstract.CDL3OUTSIDE(HSI_source)
HSI_source['pattern1']=pattern1
HSI_source['pattern1']=HSI_source['pattern1'].shift(1)
HSI_source.loc[(HSI_source['pattern1']>0),'pattern1_positive']=HSI_source['pattern1']
HSI_source['pattern1_positive']=HSI_source['pattern1_positive'].fillna(0)

HSI_source.loc[(HSI_source['pattern1']<0),'pattern1_negative']=HSI_source['pattern1']
HSI_source['pattern1_negative']=HSI_source['pattern1_negative'].fillna(0)



#cci
cci = abstract.CCI(HSI_source)
HSI_source['cci']=cci
HSI_source['cci']=HSI_source['cci'].shift(1)
HSI_source.loc[(HSI_source['cci']>100),'cci_down']=HSI_source['cci']
HSI_source.loc[(HSI_source['cci']<-100),'cci_up']=HSI_source['cci']*-1
HSI_source=HSI_source.fillna(0)







#CMO - Chande Momentum Oscillator
t_var='cmo'
vars()[t_var] = abstract.CMO(HSI_source, timeperiod=14)
HSI_source[t_var]=vars()[t_var]
HSI_source[t_var]=HSI_source[t_var].shift(1)
HSI_source.loc[(HSI_source[t_var]>0),t_var+'_up']=HSI_source[t_var]
HSI_source.loc[(HSI_source[t_var]<0),t_var+'_down']=HSI_source[t_var]*-1
HSI_source=HSI_source.fillna(0)



#MOM - Momentum
t_var='mom'
vars()[t_var] = abstract.MOM(HSI_source, timeperiod=10)
HSI_source[t_var]=vars()[t_var]
HSI_source[t_var]=HSI_source[t_var].shift(1)
HSI_source=HSI_source.fillna(0)



#PPO - Percentage Price Oscillator
t_var='ppo'
vars()[t_var] = abstract.PPO(HSI_source,fastperiod=12, slowperiod=26, matype=0)
HSI_source[t_var]=vars()[t_var]
HSI_source[t_var]=HSI_source[t_var].shift(1)
HSI_source.loc[(HSI_source[t_var]>0),t_var+'_up']=HSI_source[t_var]
HSI_source.loc[(HSI_source[t_var]<0),t_var+'_down']=HSI_source[t_var]*-1
HSI_source=HSI_source.fillna(0)


#BBANDS - Bollinger Bands
bb = abstract.BBANDS(HSI_source, timeperiod=5, nbdevup=2.0, nbdevdn=2.0, matype=0)
HSI_source['bb_down']=(bb['upperband']-HSI_source.close).shift(1)
HSI_source['bb_up']=(HSI_source.close-bb['lowerband']).shift(1)


#https://phemex.com/academy/what-is-mesa-adaptive-moving-average#:~:text=The%20MESA%20Adaptive%20Moving%20Average,value%20and%20signals%20market%20trends.
#MAMA - MESA Adaptive Moving Average
#If the MAMA crosses the FAMA line from below and moves higher, the market tends to be bullish, 
#and traders frequently consider this as a buy signal. On the other hand, when the MAMA line crosses
# the FAMA from above and shifts underneath, the market is considered to be undergoing a bearish trend
#, which is generally a strong signal for investors to enter short positions.
mama = abstract.MAMA(HSI_source, fastlimit=0.5, slowlimit=0.5)
shortSMA= mama.mama
longSMA=mama.fama
HSI_source['mamaSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
HSI_source['mamaBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))

HSI_source['mamaSell']=HSI_source['mamaSell']*1
HSI_source['mamaBuy']=HSI_source['mamaBuy']*1

HSI_source['mamaSell_original']=HSI_source['mamaSell'].shift(-1)
HSI_source['mamaBuy_original']=HSI_source['mamaBuy'].shift(-1)

HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
HSI_source=ema_custom_v2(HSI_source,'DateNum','mamaSell_original',5)
HSI_source=ema_custom_v2(HSI_source,'DateNum','mamaBuy_original',5)
HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)




#APO - Absolute Price Oscillator
t_var='apo'
vars()[t_var] = abstract.APO(HSI_source, fastperiod=12, slowperiod=26, matype=0)
HSI_source[t_var]=vars()[t_var]
HSI_source[t_var]=HSI_source[t_var].shift(1)
HSI_source.loc[(HSI_source[t_var]>0),t_var+'_up']=HSI_source[t_var]
HSI_source.loc[(HSI_source[t_var]<0),t_var+'_down']=HSI_source[t_var]*-1
HSI_source=HSI_source.fillna(0)


#rsi
t_var='rsi'
vars()[t_var] = abstract.RSI(HSI_source, timeperiod=14)
HSI_source[t_var]=vars()[t_var]
HSI_source[t_var]=HSI_source[t_var].shift(1)
HSI_source.loc[(HSI_source[t_var]>70),t_var+'_up']=HSI_source[t_var]
HSI_source.loc[(HSI_source[t_var]<30),t_var+'_down']=HSI_source[t_var]
HSI_source=HSI_source.fillna(0)



#Stochastic Oscillator
#%D values over 75 indicate an overbought condition; values under 25 indicate an oversold condition. 
#When the Fast %D crosses above the Slow %D, it is a buy signal; when it crosses below, it is a sell signal.
stock_o = abstract.STOCH(HSI_source, fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
slowk=stock_o.slowk
slowd=stock_o.slowd

t_var='slowd'
HSI_source[t_var]=slowd
HSI_source[t_var]=HSI_source[t_var].shift(1)
HSI_source.loc[(HSI_source[t_var]>75),t_var+'_down']=HSI_source[t_var]
HSI_source.loc[(HSI_source[t_var]<25),t_var+'_up']=HSI_source[t_var]
HSI_source=HSI_source.fillna(0)

shortSMA= slowd
longSMA=slowk
HSI_source['stock_oSell'] = ((shortSMA.shift(1) <= longSMA.shift(1)) & (shortSMA.shift(2) >= longSMA.shift(2)))
HSI_source['stock_oBuy'] = ((shortSMA.shift(1) >= longSMA.shift(1)) & (shortSMA.shift(2) <= longSMA.shift(2)))

HSI_source['stock_oSell']=HSI_source['stock_oSell']*1
HSI_source['stock_oBuy']=HSI_source['stock_oBuy']*1

HSI_source['stock_oSell_original']=HSI_source['stock_oSell'].shift(-1)
HSI_source['stock_oBuy_original']=HSI_source['stock_oBuy'].shift(-1)

HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=False)
HSI_source=ema_custom_v2(HSI_source,'DateNum','stock_oSell_original',5)
HSI_source=ema_custom_v2(HSI_source,'DateNum','stock_oBuy_original',5)
HSI_source=HSI_source.sort_values(by=['DateNum'],ascending=True)







sys.exit('stop here')







var_temp=['sar_up_indicator','sar_down_indicator',
'sar_value_indicator',
'sar_up2', 'sar_down2',
'sar_value2_indicator',
'sar_talib_modified_original_percentilelower','sar_talib_modified_original_percentileupper',
'sar_talib_modified_original_percentile',
'ad_change_shift1',
'ad3_shift1','ad4_shift1',
'ad1_shift1','ad2_shift1',
'obv3_shift1','obv4_shift1',   #on balance volume
'moneyflow_up','moneyflow_down',
'william_up','william_down',
'UltimateOscillator_up','UltimateOscillator_down',
'truerange_up','truerange_down',
'directmove_up','directmove_down',
'balancepower_up','balancepower_down',
'aroon_shift1',
'aroon_up','aroon_down',
'aroon_up_70','aroon_down_70',
'aroon_shift1_percentilelower','aroon_shift1_percentileupper',
'smaBuy','smaSell',
'EMA_smaSell_original','EMA_smaBuy_original',
'EMA_smaSell_original2','EMA_smaBuy_original2',
'pattern1_positive','pattern1_negative',
'cci_up','cci_down',
'cmo_up','cmo_down',
'mom',
'ppo_up','ppo_down',
'bb_up','bb_down',
'mamaSell','mamaBuy',
'EMA_mamaSell_original','EMA_mamaBuy_original',
'apo',
'rsi_up','rsi_down',
'slowd_down','slowd_up',
'stock_oSell','stock_oBuy',
'EMA_stock_oBuy_original','EMA_stock_oSell_original']


needed_var=['Date2']+var_temp
hsi_y_x=pd.merge(hsi_y_x,HSI_source[needed_var],how='left',left_on=['Date2'],right_on=['Date2'])
hsi_y_x=hsi_y_x.fillna(0)












var_temp=[['sar_up_indicator','sar_down_indicator'],
['sar_value_indicator'],
['sar_up2', 'sar_down2'],
['sar_value2_indicator'],
['sar_talib_modified_original_percentilelower','sar_talib_modified_original_percentileupper'],
['sar_talib_modified_original_percentile'],
['ad_change_shift1'],
['ad3_shift1','ad4_shift1'],
['ad1_shift1','ad2_shift1'],
['obv3_shift1','obv4_shift1'],   #on balance volume
['moneyflow_up','moneyflow_down'],
['william_up','william_down'],
['UltimateOscillator_up','UltimateOscillator_down'],
['truerange_up','truerange_down'],
['directmove_up','directmove_down'],
['balancepower_up','balancepower_down'],
['aroon_shift1'],
['aroon_up','aroon_down'],
['aroon_up_70','aroon_down_70'],
['aroon_shift1_percentilelower','aroon_shift1_percentileupper'],
['smaBuy','smaSell'],
['EMA_smaSell_original','EMA_smaBuy_original'],
['EMA_smaSell_original2','EMA_smaBuy_original2'],
['pattern1_positive','pattern1_negative'],
['cci_up','cci_down'],
['cmo_up','cmo_down'],
['mom'],
['ppo_up','ppo_down'],
['bb_up','bb_down'],
['mamaSell','mamaBuy'],
['EMA_mamaSell_original','EMA_mamaBuy_original'],
['apo'],
['rsi_up','rsi_down'],
['slowd_down','slowd_up'],
['stock_oSell','stock_oBuy'],
['EMA_stock_oBuy_original','EMA_stock_oSell_original']]

checklist=pd.DataFrame([])
n1=0
for ii in var_temp:  
    f2=['Date2']+ii
    #j=['MCDFX_change', 'MICDX_change']
    base_folder='/home/jonahthonchan/Dropbox/ee/index_analysis'
    
    
    
    use_factor_list3=f2.copy()
    out=''
    for i in use_factor_list3:
        out=out+"'"+i+"',"
    out="["+out[0:(len(out)-1)]+"]"
    
    
    n1=n1+1
    name='factor'+str(n1)+'.txt'
    target_file=os.path.join('factor',name)
    textfile = open(target_file, 'w')
    textfile.write(out)
    textfile.close()
    
    checklist=checklist.append(pd.DataFrame({'new_factor':[ii],'factor':[out],'filename':[name]}))

#a_check=hsi_y_x[['sar_up_indicator','sar_down_indicator','sar_value_indicator','sar_up2', 'sar_down2','sar_value2_indicator']].copy()




from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
HSI_source_select=HSI_source.loc[HSI_source['Date2']<='2010-12-31',:].copy()

all_f=var_temp

HSI_source_select['Y_selection']=HSI_source_select.Y_up_cum_final-HSI_source_select.Y_down_cum_final
# create a base classifier used to evaluate a subset of attributes
model = LogisticRegression(max_iter=3000)

# create the RFE model and select 3 attributes
rfe = RFE(model, 1)
use_factor_list_nodate=all_f.copy()
rfe = rfe.fit(HSI_source_select.loc[:,all_f], HSI_source_select.Y_selection)
# summarize the selection of the attributes
print(rfe.support_)
out=rfe.ranking_
out=out.tolist()


output=pd.DataFrame({'use_factor':all_f,'rank':out})

output=output.sort_values(by=['rank'],ascending=[True])
output=output.reset_index(drop=True)




checklist=pd.DataFrame([])
n1=0
for ii in range(2,35):  
    f_use=output.use_factor.values.tolist()[0:ii].copy()
    f2=['Date2']+f_use
    #j=['MCDFX_change', 'MICDX_change']
    base_folder='/home/jonahthonchan/Dropbox/ee/index_analysis'
    
    
    
    use_factor_list3=f2.copy()
    out=''
    for i in use_factor_list3:
        out=out+"'"+i+"',"
    out="["+out[0:(len(out)-1)]+"]"
    
    
    n1=n1+1
    name='factor'+str(n1)+'.txt'
    target_file=os.path.join(base_folder,'factor',name)
    textfile = open(target_file, 'w')
    textfile.write(out)
    textfile.close()
    
    checklist=checklist.append(pd.DataFrame({'new_factor':[ii],'factor':[out],'filename':[name]}))









































#random factor
dim=hsi_y_x.shape[0]
s=np.random.normal(0,1,dim)
hsi_y_x['random1']=s
hsi_y_x['random2']=s*-1

hsi_y_x['constant_factor']=1

writer = pd.ExcelWriter('use_list_dataframe'+'.xlsx', engine='xlsxwriter')
use_list_dataframe.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_dataframe", hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x'+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()








#random factor
dim=HSI_source.shape[0]
s=np.random.normal(0,1,dim)
HSI_source['random1']=s
HSI_source['random2']=s*-1

s=np.random.normal(0,1,dim)
HSI_source['random3']=s
HSI_source['random4']=s*-1

s=np.random.normal(0,1,dim)
HSI_source['random5']=s
HSI_source['random6']=s*-1

s=np.random.normal(0,1,dim)
HSI_source['random7']=s
HSI_source['random8']=s*-1


HSI_source['constant_factor']=1

#save HSI_source as hsi_y_x
out_name='hsi_y_x'+'_'+selection_target

import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore(out_name+'.hdf5', "w", complib=str("zlib"), complevel=5)
store.put(out_name+'_dataframe',HSI_source, data_columns=HSI_source.columns)
store.close()

writer = pd.ExcelWriter(out_name+'.xlsx', engine='xlsxwriter')
HSI_source.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()











sys.exit('stop here')












sys.stderr.close()
sys.stderr = sys.__stderr__


a_check=list(hsi_y_x.columns.values)
len(a_check)

a_check=set(list(hsi_y_x.columns.values))
len(a_check)























































#random forest
hsi_y_x_for_random_forest=pd.merge(hsi_y_x,hsi_y[['Date2','Open_HSI','Close_HSI']],how='left',left_on='Date2',right_on='Date2')
hsi_y_x_for_random_forest['Y_hsi_change']=hsi_y_x_for_random_forest['Close_HSI']-hsi_y_x_for_random_forest['Open_HSI']

from sklearn.ensemble import RandomForestRegressor

year_random_forest=[i for i in hsi_y_x_for_random_forest.year.unique() if i >=2007]

#asset_name+'_greatless_mean_value_indicator',asset_name+'_greatless_mean_sd1_value_indicator',asset_name+'_greatless_mean_sd2_value_indicator'

#create used fields
used_fields=[]
mean_asset_list=['GSPC','DJI','IXIC','NYA','FTSE','GDAXI','FCHI','N225','HSI_index','00001.SS','AORD','MXX','EWH',
                 'CHRIS_com_CME_GC1','CHRIS_com_CME_O1','CHRIS_com_ICE_B1','ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD'
                 'USTREASURY_REALLONGTERM','USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10','USTREASURY_REALYIELD_20',
                 'HDB','UBS','BBVA','DB','CM','CAJ','PHG','MSFT','T','AMX','MCK','CVX','BHP','RIO','PBR_A','CHRIS_bond_EUREX_FGBM1',
                 '83188.HK','FJSCX','HJPNX','OTPSX','FBGKX','TBGVX','XBI','DHFCX']

mean_asset_list=['GSPC','DJI','IXIC','NYA','FTSE','GDAXI','FCHI','N225','HSI_index','00001.SS','AORD','MXX']

#'Date2','GSPC_change','DJI_change','IXIC_change','NYA_change','VIX_change','FTSE_change',
#                     'GDAXI_change','FCHI_change','AORD_change','MXX_change','EMA_N225_change','EMA_00001.SS_change',
#                     'EMA_1398_HK_change','EMA_0016_HK_change','EMA_0002_HK_change','CHRIS_com_CME_GC1_change',
#                     'CHRIS_com_CME_O1_change','CHRIS_com_ICE_B1_change','ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
#                     'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','USTREASURY_REALLONGTERM_change',
#                     'USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
#                     'USTREASURY_REALYIELD_20_change','UBS_change','BBVA_change','DB_change','CM_change','CAJ_change',
#                     'PHG_change','T_change','AMX_change','MCK_change','CVX_change','BHP_change','RIO_change','PBR_A_change',
#                     'CHRIS_bond_EUREX_FGBM1_change','HDB_change','EMA_0001_HK_change','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change',
#                     'MSFT_change','CHRIS_com_CME_GC1_change_interact_CHRIS_com_ICE_B1_change','EMA_HSI_index_change','EWH_change',
#                     'DJI_greatless_mean_sd2_value_indicator','83188.HK_change','FJSCX_change','HJPNX_change','OTPSX_change',
#                     'FBGKX_change','TBGVX_change','XBI_change','DHFCX_change'

for i in mean_asset_list:
#    used_fields.append(i+'_greatless_mean_value_indicator')
#    used_fields.append(i+'_greatless_mean_sd1_value_indicator')
#    used_fields.append(i+'_greatless_mean_sd2_value_indicator')
#    used_fields.append(i+'_change_lag2')
#    used_fields.append(i+'_change_lag3')
    used_fields.append(i+'_change')


from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import RandomForestClassifier
# import machine learning algorithms
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
#i=2011
RF_factor=np.array([])
for i in year_random_forest:
    #i=2011
    hsi_y_x_for_random_forest['year']=hsi_y_x_for_random_forest['year'].astype(int)
    x_train=hsi_y_x_for_random_forest.loc[hsi_y_x_for_random_forest['year']<i,used_fields].copy()
    y_train=hsi_y_x_for_random_forest.loc[hsi_y_x_for_random_forest['year']<i,'Y_hsi_change'].copy()
    #y_train=hsi_y_x_for_random_forest.loc[hsi_y_x_for_random_forest['year']<i,'EWH_change'].copy() #Y_up Y_hsi_change

    x_test=hsi_y_x_for_random_forest.loc[hsi_y_x_for_random_forest['year']==i,used_fields].copy()
    y_test=hsi_y_x_for_random_forest.loc[hsi_y_x_for_random_forest['year']==i,'Y_hsi_change'].copy()
    #y_test=hsi_y_x_for_random_forest.loc[hsi_y_x_for_random_forest['year']==i,'EWH_change'].copy()
    
    #If None, then max_features=n_features. (for each tree it consider all features so only row is randomly chosen)
    #max_depth, If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples.
    #regressor = RandomForestClassifier(bootstrap=True,criterion='entropy',max_depth=None,max_features=None,n_estimators=1000, random_state=None,n_jobs=8) 
    regressor = RandomForestRegressor(bootstrap=True,n_estimators=1000,max_features=None,max_depth=None, random_state=None,n_jobs=8)  
    #regressor = GradientBoostingClassifier(n_estimators=1000, learning_rate = 0.01, max_features=None, max_depth = None, random_state = 0)
    #regressor = GradientBoostingRegressor(n_estimators=1000, learning_rate = learning_rate, max_features=None, max_depth = None, random_state = 0)
    
    regressor.fit(x_train, y_train)  
    y_pred = regressor.predict(x_test)
    y_pred=np.reshape(y_pred,(np.shape(y_pred)[0],1))
    if i==2007:
        RF_factor=y_pred
        RF_factor=np.reshape(RF_factor,(np.shape(RF_factor)[0],1))
        RF_factor=np.vstack((np.zeros((y_train.shape[0],1)),RF_factor))
    else:
        RF_factor=np.vstack((RF_factor,y_pred))
        
    from sklearn import metrics
    print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    #Returns the mean accuracy on the given test data and labels.
    
    #accuracy if categorical
#    accuracy_score(y_test,np.reshape(y_pred,(y_pred.shape[0],)))
#    print(regressor.score(x_train,y_train))
#    print(regressor.score(x_test,y_test))
    
    #accuracy if regressor
    test_check=y_test>=0 ;
#    test_check=test_check.values
#    test_check.shape
    prediction_check=y_pred>=0
    prediction_check=np.reshape(prediction_check,(prediction_check.shape[0],))

    correct=((test_check==True)&(prediction_check==True))|((test_check==False)&(prediction_check==False))
    accuracy=sum(correct)/correct.shape[0];print(accuracy)
    #print(regressor.feature_importances_)




import pandas as pd
feature_importances = pd.DataFrame(regressor.feature_importances_,index = x_train.columns,columns=['importance']).sort_values('importance',ascending=False)    
feature_importances['index']=feature_importances.index
#AORD_change_lag3,CHRIS_bond_EUREX_FGBM1_change_lag2,ECB_cur_EURPHP_change_lag2,CHRIS_com_CME_O1_change_lag3
#AORD_greatless_mean_value_indicator,ECB_cur_EURRUB_greatless_mean_value_indicator




learning_rates = [0.001,0.01,0.05, 0.1, 0.25, 0.5, 0.75, 1]
for learning_rate in learning_rates:
    #learning_rates=2
    regressor = GradientBoostingRegressor(n_estimators=1000, learning_rate = learning_rate, max_features=None, max_depth = None, random_state = 0)
    regressor.fit(x_train, y_train)
    print("Learning rate: ", learning_rate)
    print(regressor.score(x_train,y_train))
    print(regressor.score(x_test,y_test))















statistic_table=pd.DataFrame(columns=['mse_train','mse_test','accuracy_train','accuracy_test','max_depth'])    

for i in range(0,10):
    max_depth=i+1
    regressor = RandomForestClassifier(bootstrap=True,criterion='entropy',max_depth=i+1,max_features=None,n_estimators=1000, random_state=None,n_jobs=8)
    #regressor = RandomForestClassifier(bootstrap=True,criterion='entropy',min_samples_leaf=i,max_depth=None,max_features=None,n_estimators=1000, random_state=None,n_jobs=8)
    #regressor = RandomForestRegressor(bootstrap=True,n_estimators=1000,max_depth=i+1,max_features=None, random_state=None,n_jobs=8)  
    regressor.fit(x_train, y_train)
    y_pred_test = regressor.predict(x_test)
    y_pred_train = regressor.predict(x_train)
    
    mse_train=metrics.mean_absolute_error(y_train, y_pred_train)
    mse_test=metrics.mean_absolute_error(y_test,y_pred_test)
    accuracy_train=regressor.score(x_train,y_train)
    accuracy_test=regressor.score(x_test,y_test)
    
    first=pd.DataFrame({'mse_train':mse_train,'mse_test':mse_test,'accuracy_train':accuracy_train,'accuracy_test':accuracy_test,'max_depth':max_depth},index=[0])
    statistic_table=statistic_table.append(first)
    print("finished ",i)



from pylab import *
plt.figure(figsize=(13,3), dpi=80, facecolor='w', edgecolor='k')
plt.subplot(1,3,1)
#plt.plot(statistic_table_train['run'],statistic_table_train['accuracy_train'], linestyle='--', color='b')
plt.plot(statistic_table['max_depth'],statistic_table['mse_train'],'*', color='r')
plt.plot(statistic_table['max_depth'],statistic_table['mse_test'],'*', color='b')
plt.legend(loc='best')
plt.xlabel('max_depth')
plt.ylabel('mse')
plt.title('mse')

plt.subplot(1,3,2)
plt.plot(statistic_table['max_depth'],statistic_table['accuracy_train'],'*', color='r')
plt.plot(statistic_table['max_depth'],statistic_table['accuracy_test'],'*', color='b')
plt.legend(loc='best')
plt.xlabel('max_depth')
plt.ylabel('accuracy')
plt.title('accuracy')


    
hsi_y_x['RF_factor']=RF_factor





#hsi_y_x_check=hsi_y_x['FHSIVol4_change']



hsi_y_x=read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hsi_y_x.xlsx',"Sheet1")
#hsi_y = read_excel('hsi_y.xlsx','Sheet1')
#os.chdir(r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis")










#decision tree
#Decision Tree for Regression

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
hsi_y_x_for_decisiontree=pd.merge(hsi_y_x,hsi_y[['Date2','Open_HSI','Close_HSI']],how='left',left_on='Date2',right_on='Date2')
hsi_y_x_for_decisiontree['Y_hsi_change']=hsi_y_x_for_decisiontree['Close_HSI']-hsi_y_x_for_decisiontree['Open_HSI']


year_decisiontree=[i for i in hsi_y_x_for_decisiontree.year.unique() if i >=2007]

#create used fields
used_fields=[]
mean_asset_list=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change']

mean_asset_list=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_NYA_wsj_change','index_VIX_wsj_change','index_UK_NULL_UKX_wsj_change',
                     'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2',
                     'EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_16_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','gold_futures_investing_greatless_mean_sd2_value_indicator_10',
                     'oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                     'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','USTREASURY_REALLONGTERM_change',
                     'USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                     'USTREASURY_REALYIELD_20_change','UBS_wsj_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                     'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change',
                     'euro_bobl_investing_greatless_mean_sd2_value_indicator_10','HDB_wsj_change','EMA_HK_XHKG_0001_wsj_change_v2','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change',
                     'MSFT_wsj_change','brent_oil_gold_future_interact_indicator','EMA_index_HK_XHKG_HSI_wsj_change_v2','etf_EWH_wsj_change',
                     'index_DJIA_wsj_greatless_mean_sd2_value_indicator','etf_HK_XHKG_3188_wsj_change','FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change',
                     'FBGKX_wsj_change','TBGVX_wsj_change','etf_XBI_wsj_change','DHFCX_wsj_change','AAII_AAII_SENTIMENT_change']


mean_asset_list_currency=['ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                          'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change']

mean_asset_list_index=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_NYA_wsj_change','index_VIX_wsj_change','index_UK_NULL_UKX_wsj_change',
                       'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2']

mean_asset_list_interest=['USTREASURY_REALLONGTERM_change','USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                          'USTREASURY_REALYIELD_20_change']

mean_asset_list_american=['UBS_wsj_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                          'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change','HDB_wsj_change','MSFT_wsj_change']


mean_asset_list_fund=['FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change','FBGKX_wsj_change','TBGVX_wsj_change','DHFCX_wsj_change']

mean_asset_list=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_NYA_wsj_change','index_VIX_wsj_change','index_UK_NULL_UKX_wsj_change',
                     'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2',
                     'EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_16_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','gold_futures_investing_greatless_mean_sd2_value_indicator_10',
                     'oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                     'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','USTREASURY_REALLONGTERM_change',
                     'USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                     'USTREASURY_REALYIELD_20_change','UBS_wsj_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                     'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change',
                     'euro_bobl_investing_greatless_mean_sd2_value_indicator_10','HDB_wsj_change','EMA_HK_XHKG_0001_wsj_change_v2','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change',
                     'MSFT_wsj_change','brent_oil_gold_future_interact_indicator','EMA_index_HK_XHKG_HSI_wsj_change_v2','etf_EWH_wsj_change',
                     'index_DJIA_wsj_greatless_mean_sd2_value_indicator','etf_HK_XHKG_3188_wsj_change','FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change',
                     'FBGKX_wsj_change','TBGVX_wsj_change','etf_XBI_wsj_change','DHFCX_wsj_change']#,'FHSIVol4_greatless_mean_sd2_value_indicator']



mean_asset_list_etf=['etf_EWH_wsj_change','etf_HK_XHKG_3188_wsj_change','etf_XBI_wsj_change','EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','EMA_HK_XHKG_0001_wsj_change_v2','EMA_HK_16_wsj_change_v2']

mean_asset_list_futures=['gold_futures_investing_greatless_mean_sd2_value_indicator_10','oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','euro_bobl_investing_greatless_mean_sd2_value_indicator_10','brent_oil_gold_future_interact_indicator']

mean_asset_list=['ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD',
                 'USTREASURY_REALLONGTERM','USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10',
                 'USTREASURY_REALYIELD_20','index_SPX_wsj','index_DJIA_wsj','index_COMP_wsj','index_NYA_wsj','index_VIX_wsj',
                 'index_UK_NULL_UKX_wsj','index_DX_XETR_DAX_wsj','index_FR_XPAR_PX1_wsj','index_JP_XTKS_NIK_wsj','index_HK_XHKG_HSI_wsj',
                 'index_CN_SHCOMP_wsj','index_AU_XASX_XAO_wsj','index_MX_XMEX_IPC_wsj','etf_HK_XHKG_3188_wsj','etf_EWH_wsj',
                 'etf_XBI_wsj','HK_XHKG_1398_wsj','HK_XHKG_0001_wsj','HK_16_wsj','HK_XHKG_0002_wsj','HDB_wsj','UBS_wsj',
                 'BBVA_wsj','DB_wsj','CM_wsj','CAJ_wsj','PHG_wsj','MSFT_wsj','T_wsj','AMX_wsj','MCK_wsj','CVX_wsj','BHP_wsj',
                 'RIO_wsj','PBRA_wsj','OTPSX_wsj','FBGKX_wsj','HJPNX_wsj','FJSCX_wsj','TBGVX_wsj','DHFCX_wsj','brent_oil_investing',
                 'euro_bobl_investing','gold_futures_investing','oats_futures_investing']
mean_asset_list=[i+"_greatless_mean_sd2_value_indicator" for i in mean_asset_list]
    
used_fields=mean_asset_list

#for i in mean_asset_list:
#    used_fields.append(i+'_change')
    
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeRegressor,DecisionTreeClassifier  
import numpy as np

def dt_run(used_fields,replic):
    #i=2011
    #replic=2
    #j=0
    DT_factor_cum=np.array([])
    for j in range(0,replic):
        DT_factor=np.array([])
        for i in year_decisiontree:
            #i=2007
            hsi_y_x_for_decisiontree['year']=hsi_y_x_for_decisiontree['year'].astype(int)
            x_train=hsi_y_x_for_decisiontree.loc[hsi_y_x_for_decisiontree['year']<i,used_fields].copy()
            y_train=hsi_y_x_for_decisiontree.loc[hsi_y_x_for_decisiontree['year']<i,'Y_hsi_change'].copy() #Y_up Y_hsi_change
        
            x_test=hsi_y_x_for_decisiontree.loc[hsi_y_x_for_decisiontree['year']==i,used_fields].copy()
            y_test=hsi_y_x_for_decisiontree.loc[hsi_y_x_for_decisiontree['year']==i,'Y_hsi_change'].copy() #Y_up Y_hsi_change
            
            regressor =DecisionTreeRegressor()  
            regressor.fit(x_train, y_train)  
            y_pred = regressor.predict(x_test)
            y_pred=np.reshape(y_pred,(np.shape(y_pred)[0],1))
            y_pred
            if i==2007:
                DT_factor=y_pred
                DT_factor=np.reshape(DT_factor,(np.shape(DT_factor)[0],1))
                DT_factor=np.vstack((np.zeros((y_train.shape[0],1)),DT_factor))
            else:
                DT_factor=np.vstack((DT_factor,y_pred))
                
            from sklearn import metrics
            #accuracy if regressor
            test_check=y_test>=0 ;
            prediction_check=y_pred>=0
            prediction_check=np.reshape(prediction_check,(prediction_check.shape[0],))
        
            correct=((test_check==True)&(prediction_check==True))|((test_check==False)&(prediction_check==False))
            accuracy=sum(correct)/correct.shape[0];print(accuracy)
            #print(regressor.feature_importances_)
        
            print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
            print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
            print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred))) 
        if j==0:
            DT_factor_cum=np.zeros(shape=DT_factor.shape)
        DT_factor_cum=DT_factor_cum+DT_factor
        
    DT_factor_cum=DT_factor_cum/replic
    return DT_factor_cum




hsi_y_x['DT_factor_classifier']=DT_factor

hsi_y_x['hsi_prediction']=dt_run(mean_asset_list,5)

hsi_y_x['DT_factor_index_regressor']=dt_run(mean_asset_list_index,10)
hsi_y_x['DT_factor_interestrate_regressor']=dt_run(mean_asset_list_interest,10)
hsi_y_x['DT_factor_currency_regressor']=dt_run(mean_asset_list_currency,10)
hsi_y_x['DT_factor_americanstock_regressor']=dt_run(mean_asset_list_american,10)
hsi_y_x['DT_factor_fund_regressor']=dt_run(mean_asset_list_fund,10)
hsi_y_x['DT_factor_etf_hkstock_regressor']=dt_run(mean_asset_list_etf,10)
hsi_y_x['DT_factor_future_regressor']=dt_run(mean_asset_list_futures,10)
hsi_y_x['DT_factor']=dt_run(mean_asset_list,10)

hsi_y_x['DT_factor_FHSIVol4']=dt_run(mean_asset_list,10)

used_fields=[i+"_greatless_mean_sd2_value_indicator" for i in mean_asset_list]
hsi_y_x['DT_factor_all_greatless_sd2']=dt_run(used_fields,10)

used_fields=[i+"_greatless_mean_sd1_value_indicator" for i in mean_asset_list]
hsi_y_x['DT_factor_all_greatless_sd1']=dt_run(used_fields,10)

used_fields=[i+"_greatless_mean_value_indicator" for i in mean_asset_list]
hsi_y_x['DT_factor_all_greatless']=dt_run(used_fields,10)


writer = pd.ExcelWriter('use_list_dataframe'+'.xlsx', engine='xlsxwriter')
use_list_dataframe.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_dataframe", hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x'+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

























#k-mean
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score


hsi_y_x_for_kmean=pd.merge(hsi_y_x,hsi_y[['Date2','Open_HSI','Close_HSI']],how='left',left_on='Date2',right_on='Date2')
hsi_y_x_for_kmean['Y_hsi_change']=hsi_y_x_for_kmean['Close_HSI']-hsi_y_x_for_kmean['Open_HSI']


from sklearn.ensemble import RandomForestRegressor


year_kmean=[i for i in hsi_y_x_for_kmean.year.unique() if i >=2007]

mean_asset_list=['GSPC','DJI','IXIC','NYA','VIX','FTSE','GDAXI','FCHI','AORD','MXX','CHRIS_com_CME_GC1','CHRIS_com_CME_O1','EWH',
                 'CHRIS_com_ICE_B1','ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD',
                 'USTREASURY_REALLONGTERM','USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10','USTREASURY_REALYIELD_20',
                 'HDB','UBS','BBVA','DB','CM','CAJ','PHG','MSFT','T','AMX','MCK','CVX','BHP','RIO','PBR_A','CHRIS_bond_EUREX_FGBM1']


mean_asset_list=['GSPC','DJI','IXIC','NYA','VIX','FTSE','GDAXI','FCHI','AORD','MXX']
mean_asset_list=['EWH']#HSI_index']#,'FTSE','N225','EWH','CHRIS_com_CME_GC1','CHRIS_com_ICE_B1']
        
        
used_fields=[] 
for i in mean_asset_list:
#    used_fields.append(i+'_greatless_mean_value_indicator')
#    used_fields.append(i+'_greatless_mean_sd1_value_indicator')
#    used_fields.append(i+'_greatless_mean_sd2_value_indicator')
#    used_fields.append(i+'_change_lag2')
#    used_fields.append(i+'_change_lag3')
    used_fields.append(i+'_change')




## Number of clusters
#kmeans = KMeans(n_clusters=3)
## Fitting the input data
#kmeans = kmeans.fit(X)
## Getting the cluster labels
#labels = kmeans.predict(X)
## Centroid values
#centroids = kmeans.cluster_centers_



kmean_factor=np.array([])
for j in year_kmean:
    #j=2013
    hsi_y_x_for_kmean['year']=hsi_y_x_for_kmean['year'].astype(int)
    x_train=hsi_y_x_for_kmean.loc[hsi_y_x_for_kmean['year']<j,used_fields].copy()
    y_train=hsi_y_x_for_kmean.loc[hsi_y_x_for_kmean['year']<j,'Y_up'].copy() #Y_up Y_hsi_change

    x_test=hsi_y_x_for_kmean.loc[hsi_y_x_for_kmean['year']==j,used_fields].copy()
    x_test=x_test.reset_index(drop=True)
    y_test=hsi_y_x_for_kmean.loc[hsi_y_x_for_kmean['year']==j,'Y_up'].copy()
    
    no_of_replication=1 #used for avergae the centroid  #cannot use this because centroid are not same position for each run
    number_of_cluster=4
    centroids=np.zeros((number_of_cluster,x_train.shape[1]))
    for k in range(0,no_of_replication):
#        all_centroid_within_Data=False
#        
#        data_max=x_train.as_matrix().max(axis=0)
#        data_min=x_train.as_matrix().min(axis=0)
#        
#        while all_centroid_within_Data==False:
#            # Number of clusters
#            kmeans = KMeans(n_clusters=number_of_cluster)
#            # Fitting the input data
#            kmeans = kmeans.fit(x_train)
#            # Getting the cluster labels (for which group)
#            # labels = kmeans.predict(x_train)
#            center_final=kmeans.cluster_centers_
#            center_final_great_max=center_final>data_max
#            center_final_less_min=center_final<data_min
#            if (center_final_great_max.sum()+center_final_less_min.sum())==0:
#                all_centroid_within_Data=True

        # Number of clusters
        kmeans = KMeans(n_clusters=number_of_cluster,init='random',n_init=500,n_jobs=8,max_iter=30000,algorithm='auto')
        # Fitting the input data
        kmeans = kmeans.fit(x_train)
        # Getting the cluster labels (for which group)
        # labels = kmeans.predict(x_train)
        center_final=kmeans.cluster_centers_
        centroids = center_final+centroids
        #print("finished ",k," replication")
    centroids=centroids/no_of_replication
    
    #x=x_train.loc[0,:]
    def find_label(x):
        x=x.as_matrix()
        minor=(x-centroids)**2
        minor=np.sum(minor,axis=1)
        answer=np.argmin(minor)
        return answer
        
    labels=x_train.apply(lambda x:find_label(x.reset_index(drop=True)),axis=1)
    
    
    labels = np.reshape(labels.values,(len(labels),1))
    #merge with y
    y_reshape=np.reshape(y_train.as_matrix(),(len(y_train.as_matrix()),1))
    labels_with_y=np.hstack((labels,y_reshape))
    
    #if labels don't have any centroid group, only find out those group with any data in training x_train
    all_group=np.unique(labels).tolist()
    all_group
    centroids=centroids[np.unique(labels),:]
    # Centroid values
    
    centroids_group=dict()
    for i in all_group:
        #i=2
        subset_i=labels_with_y[labels_with_y[:,0]==i]
        percent_0=sum(subset_i[:,1]==0)/subset_i.shape[0]
        percent_1=1-percent_0
        decision=1*(percent_1>=percent_0)
        centroids_group.update({'Group_'+str(i):decision})
    

    #x=x_test.loc[26,:]
    def find_class(x):
        x=x.as_matrix()
        minor=(x-centroids)**2
        minor=np.sum(minor,axis=1)
        answer=np.argmin(minor)
        output=centroids_group['Group_'+str(all_group[answer])]
        return output
        
    y_pred=x_test.apply(lambda x:find_class(x.reset_index(drop=True)),axis=1)
    y_pred=y_pred.values
    y_pred=np.reshape(y_pred,(np.shape(y_pred)[0],1))

    if j==2007:
        kmean_factor=y_pred
        kmean_factor=np.reshape(kmean_factor,(np.shape(kmean_factor)[0],1))
        kmean_factor=np.vstack((np.zeros((y_train.shape[0],1)),kmean_factor))
    else:
        kmean_factor=np.vstack((kmean_factor,y_pred))
        
    from sklearn import metrics
    #print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
    #Returns the mean accuracy on the given test data and labels.
    
    #accuracy if categorical
    print('year',j,'accuracy is ',accuracy_score(y_test,np.reshape(y_pred,(y_pred.shape[0],))))

    
    
    
    
hsi_y_x['kmean_factor']=kmean_factor
















#GBM

import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
hsi_y_x_for_GBM=pd.merge(hsi_y_x,hsi_y[['Date2','Open_HSI','Close_HSI']],how='left',left_on='Date2',right_on='Date2')
hsi_y_x_for_GBM['Y_hsi_change']=hsi_y_x_for_GBM['Close_HSI']-hsi_y_x_for_GBM['Open_HSI']


year_GBM=[i for i in hsi_y_x_for_GBM.year.unique() if i >=2008]

#create used fields
used_fields=[]
mean_asset_list=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change']

mean_asset_list=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_NYA_wsj_change','index_VIX_wsj_change','index_UK_NULL_UKX_wsj_change',
                     'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2',
                     'EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_16_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','gold_futures_investing_greatless_mean_sd2_value_indicator_10',
                     'oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                     'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','USTREASURY_REALLONGTERM_change',
                     'USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                     'USTREASURY_REALYIELD_20_change','UBS_wsj_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                     'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change',
                     'euro_bobl_investing_greatless_mean_sd2_value_indicator_10','HDB_wsj_change','EMA_HK_XHKG_0001_wsj_change_v2','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change',
                     'MSFT_wsj_change','brent_oil_gold_future_interact_indicator','EMA_index_HK_XHKG_HSI_wsj_change_v2','etf_EWH_wsj_change',
                     'index_DJIA_wsj_greatless_mean_sd2_value_indicator','etf_HK_XHKG_3188_wsj_change','FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change',
                     'FBGKX_wsj_change','TBGVX_wsj_change','etf_XBI_wsj_change','DHFCX_wsj_change','FHSIVol4_greatless_mean_sd2_value_indicator']


mean_asset_list_currency=['ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                          'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change']

mean_asset_list_index=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_NYA_wsj_change','index_VIX_wsj_change','index_UK_NULL_UKX_wsj_change',
                       'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2']

mean_asset_list_interest=['USTREASURY_REALLONGTERM_change','USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                          'USTREASURY_REALYIELD_20_change']

mean_asset_list_american=['UBS_wsj_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                          'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change','HDB_wsj_change','MSFT_wsj_change']


mean_asset_list_fund=['FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change','FBGKX_wsj_change','TBGVX_wsj_change','DHFCX_wsj_change']

mean_asset_list=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_NYA_wsj_change','index_VIX_wsj_change','index_UK_NULL_UKX_wsj_change',
                     'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2',
                     'EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_16_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','gold_futures_investing_greatless_mean_sd2_value_indicator_10',
                     'oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                     'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','USTREASURY_REALLONGTERM_change',
                     'USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                     'USTREASURY_REALYIELD_20_change','UBS_wsj_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                     'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change',
                     'euro_bobl_investing_greatless_mean_sd2_value_indicator_10','HDB_wsj_change','EMA_HK_XHKG_0001_wsj_change_v2','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change',
                     'MSFT_wsj_change','brent_oil_gold_future_interact_indicator','EMA_index_HK_XHKG_HSI_wsj_change_v2','etf_EWH_wsj_change',
                     'index_DJIA_wsj_greatless_mean_sd2_value_indicator','etf_HK_XHKG_3188_wsj_change','FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change',
                     'FBGKX_wsj_change','TBGVX_wsj_change','etf_XBI_wsj_change','DHFCX_wsj_change','AAII_AAII_SENTIMENT_change']#,'FHSIVol4_greatless_mean_sd2_value_indicator']



mean_asset_list_etf=['etf_EWH_wsj_change','etf_HK_XHKG_3188_wsj_change','etf_XBI_wsj_change','EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','EMA_HK_XHKG_0001_wsj_change_v2','EMA_HK_16_wsj_change_v2']

mean_asset_list_futures=['gold_futures_investing_greatless_mean_sd2_value_indicator_10','oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','euro_bobl_investing_greatless_mean_sd2_value_indicator_10','brent_oil_gold_future_interact_indicator']

mean_asset_list=['ECB_cur_EURCNY','ECB_cur_EURHKD','ECB_cur_EURPHP','ECB_cur_EURRUB','ECB_cur_EURSGD','ECB_cur_EURUSD',
                 'USTREASURY_REALLONGTERM','USTREASURY_REALYIELD_5','USTREASURY_REALYIELD_7','USTREASURY_REALYIELD_10',
                 'USTREASURY_REALYIELD_20','index_SPX_wsj','index_DJIA_wsj','index_COMP_wsj','index_NYA_wsj','index_VIX_wsj',
                 'index_UK_NULL_UKX_wsj','index_DX_XETR_DAX_wsj','index_FR_XPAR_PX1_wsj','index_JP_XTKS_NIK_wsj','index_HK_XHKG_HSI_wsj',
                 'index_CN_SHCOMP_wsj','index_AU_XASX_XAO_wsj','index_MX_XMEX_IPC_wsj','etf_HK_XHKG_3188_wsj','etf_EWH_wsj',
                 'etf_XBI_wsj','HK_XHKG_1398_wsj','HK_XHKG_0001_wsj','HK_16_wsj','HK_XHKG_0002_wsj','HDB_wsj','UBS_wsj',
                 'BBVA_wsj','DB_wsj','CM_wsj','CAJ_wsj','PHG_wsj','MSFT_wsj','T_wsj','AMX_wsj','MCK_wsj','CVX_wsj','BHP_wsj',
                 'RIO_wsj','PBRA_wsj','OTPSX_wsj','FBGKX_wsj','HJPNX_wsj','FJSCX_wsj','TBGVX_wsj','DHFCX_wsj','brent_oil_investing',
                 'euro_bobl_investing','gold_futures_investing','oats_futures_investing']
mean_asset_list=[i+"_greatless_mean_sd2_value_indicator" for i in mean_asset_list]
    
used_fields=mean_asset_list

#for i in mean_asset_list:
#    used_fields.append(i+'_change')
    
#GBM
#https://github.com/h2oai/h2o-3/blob/master/h2o-docs/src/product/tutorials/gbm/gbmTuning.ipynb
import sys
sys.path.append(r'C:\Users\jonahthonchan\Desktop\python\GBM\dist\h2o-3.24.0.3')
sys.path.append(r'C:\Users\jonahthonchan\Desktop\python\tabulate\dist\tabulate-0.8.3')
sys.path.append(r'C:\Users\jonahthonchan\Desktop\python\future\dist\future-0.17.1\src')
#sys.path.append(r'C:\Users\jonahthonchan\Desktop\python\six\dist\six-1.12.0')

import h2o
import numpy as np
import math
from h2o.estimators.gbm import H2OGradientBoostingEstimator
from h2o.grid.grid_search import H2OGridSearch

replic=1
def GBM_run(used_fields,replic):
    #i=2011
    #replic=2
    #j=0
    GBM_factor_cum=np.array([])
    for j in range(0,replic):
        GBM_factor=np.array([])
        for i in year_GBM:
            #i=2008
            h2o.cluster().shutdown()
            h2o.init(nthreads=-1, strict_version_check=True)
            use_response='Y_up'
            hsi_y_x_for_GBM['year']=hsi_y_x_for_GBM['year'].astype(int)
            x_train=hsi_y_x_for_GBM.loc[hsi_y_x_for_GBM['year']<(i-1),used_fields].copy()
            y_train=hsi_y_x_for_GBM.loc[hsi_y_x_for_GBM['year']<(i-1),use_response].copy() #Y_up Y_hsi_change
            x_train[use_response]=y_train

            x_valid=hsi_y_x_for_GBM.loc[hsi_y_x_for_GBM['year']==(i-1),used_fields].copy()
            y_valid=hsi_y_x_for_GBM.loc[hsi_y_x_for_GBM['year']==(i-1),use_response].copy() #Y_up Y_hsi_change
            x_valid[use_response]=y_valid
           
            x_test=hsi_y_x_for_GBM.loc[hsi_y_x_for_GBM['year']==i,used_fields].copy()
            y_test=hsi_y_x_for_GBM.loc[hsi_y_x_for_GBM['year']==i,use_response].copy() #Y_up Y_hsi_change
            x_test[use_response]=y_test
            

            
            ## pick a response for the supervised problem
            response = use_response
            
            train= h2o.H2OFrame(x_train)
            train[response] = train[response].asfactor()  
            predictors = train.columns[:-1]

            valid=h2o.H2OFrame(x_valid)
            valid[response] = valid[response].asfactor() 
            
            test=h2o.H2OFrame(x_test)
            test[response] = test[response].asfactor()  
            
            #We only provide the required parameters, everything else is default
            #h2o.init(nthreads=-1, strict_version_check=True)
            
#            gbm = H2OGradientBoostingEstimator()
#            gbm.train(x=predictors, y=response, training_frame=train)
#            ## Show a detailed model summary
#            print (gbm)
#            y_pred = gbm.predict(test).as_data_frame()['predict']
#            y_pred=np.reshape(y_pred,(np.shape(y_pred)[0],1))
            
            
            # create hyperameter and search criteria lists (ranges are inclusive..exclusive))
            hyper_params_tune = {'max_depth' : list(range(5,16,7)),
                            #'sample_rate': [x/100. for x in range(20,101)],
                            #'col_sample_rate' : [x/100. for x in range(20,101)],
                            #'col_sample_rate_per_tree': [x/100. for x in range(20,101)],
                            #'col_sample_rate_change_per_level': [x/100. for x in range(90,111)],
                            #'min_rows': [2**x for x in range(0,int(math.log(train.nrow,2)-1)+1)],
                            #'nbins': [2**x for x in range(4,11)],
                            #'nbins_cats': [2**x for x in range(4,13)],
                            #'min_split_improvement': [0,1e-8,1e-6,1e-4],
                            #'histogram_type': ["UniformAdaptive","QuantilesGlobal","RoundRobin"]
                            }
            search_criteria_tune = {'strategy': "RandomDiscrete",
                               #'max_runtime_secs': 3600,  ## limit the runtime to 60 minutes
                               #'max_models': 100,  ## build no more than 100 models
                                   'seed' : 1234,
                                   'stopping_rounds' : 5,
                                   'stopping_metric' : "AUC",
                                   'stopping_tolerance': 1e-3
                                   }
            #In [15]:
            gbm_final_grid = H2OGradientBoostingEstimator(distribution='bernoulli',
                                ## more trees is better if the learning rate is small enough 
                                ## here, use "more than enough" trees - we have early stopping
                                ntrees=100,
                                ## smaller learning rate is better
                                ## since we have learning_rate_annealing, we can afford to start with a 
                                #bigger learning rate
                                learn_rate=0.05,
                                ## learning rate annealing: learning_rate shrinks by 1% after every tree 
                                ## (use 1.00 to disable, but then lower the learning_rate)
                                learn_rate_annealing = 0.99,
                                ## score every 10 trees to make early stopping reproducible 
                                #(it depends on the scoring interval)
                                score_tree_interval = 10,
                                ## fix a random number generator seed for reproducibility
                                seed = 1234,
                                ## early stopping once the validation AUC doesn't improve by at least 0.01% for 
                                #5 consecutive scoring events
                                stopping_rounds = 5,
                                stopping_metric = "AUC",
                                stopping_tolerance = 1e-4)
             

            
            
            
            
            
            
            
            
            
            #Build grid search with previously made GBM and hyper parameters
            final_grid = H2OGridSearch(gbm_final_grid, hyper_params = hyper_params_tune,
                                                grid_id = 'final_grid',
                                                search_criteria = search_criteria_tune)
            #Train grid search
            final_grid.train(x=predictors, 
                       y=response,
                       ## early stopping based on timeout (no model should take more than 1 hour - modify as needed)
                       max_runtime_secs = 100, 
                       training_frame = train,
                       validation_frame = valid)
            
            print (final_grid)
            
            
            
            ## Sort the grid models by AUC
            sorted_final_grid = final_grid.get_grid(sort_by='auc',decreasing=True)
            
            print (sorted_final_grid)
            
            
            
            
            
            #Let's see how well the best model of the grid search 
            #(as judged by validation set AUC) does on the held out test set:
            
            
            #Get the best model from the list (the model name listed at the top of the table)
            best_model = h2o.get_model(sorted_final_grid.sorted_metric_table()['model_ids'][0])
            performance_best_model = best_model.model_performance(test)
            print (performance_best_model.auc())
            
            
            #We can inspect the winning model's parameters:
            
            
            params_list = []
            for key, value in best_model.params.items():
                params_list.append(str(key)+" = "+str(value['actual']))
            params_list
            
            
            
            #Keeping the same "best" model, we can make test set predictions as follows:
            
            #In [23]:
            preds = best_model.predict(test).as_data_frame()
            
            
            best_model.model_performance(valid)

            y_pred = np.array(best_model.predict(test).as_data_frame()['predict'])
            y_pred.size()
            y_pred=np.reshape(y_pred,(np.shape(y_pred)[0],1))        
            
            if i==2008:
                GBM_factor=y_pred
                GBM_factor=np.reshape(GBM_factor,(np.shape(GBM_factor)[0],1))
                GBM_factor=np.vstack((np.zeros((y_train.shape[0],1)),GBM_factor))
            else:
                GBM_factor=np.vstack((GBM_factor,y_pred))
                
            from sklearn import metrics
            #accuracy if regressor
            test_check=y_test>=0 ;
            prediction_check=y_pred>=0
            prediction_check=np.reshape(prediction_check,(prediction_check.shape[0],))
        
            correct=((test_check==True)&(prediction_check==True))|((test_check==False)&(prediction_check==False))
            accuracy=sum(correct)/correct.shape[0]
            print(accuracy)
            #print(regressor.feature_importances_)
        
            print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))  
            print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))  
            print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
            
        if j==0:
            GBM_factor_cum=np.zeros(shape=GBM_factor.shape)
        GBM_factor_cum=GBM_factor_cum+GBM_factor
        
    GBM_factor_cum=GBM_factor_cum/replic
    return GBM_factor_cum





#hsi_y_x['DT_factor_index_regressor']=dt_run(mean_asset_list_index,10)
#hsi_y_x['DT_factor_interestrate_regressor']=dt_run(mean_asset_list_interest,10)
#hsi_y_x['DT_factor_currency_regressor']=dt_run(mean_asset_list_currency,10)
#hsi_y_x['DT_factor_americanstock_regressor']=dt_run(mean_asset_list_american,10)
#hsi_y_x['DT_factor_fund_regressor']=dt_run(mean_asset_list_fund,10)
#hsi_y_x['DT_factor_etf_hkstock_regressor']=dt_run(mean_asset_list_etf,10)
#hsi_y_x['DT_factor_future_regressor']=dt_run(mean_asset_list_futures,10)
#hsi_y_x['DT_factor']=dt_run(mean_asset_list,10)
#
#hsi_y_x['DT_factor_FHSIVol4']=dt_run(mean_asset_list,10)
#
#used_fields=[i+"_greatless_mean_sd2_value_indicator" for i in mean_asset_list]
#hsi_y_x['DT_factor_all_greatless_sd2']=dt_run(used_fields,10)
#
#used_fields=[i+"_greatless_mean_sd1_value_indicator" for i in mean_asset_list]
#hsi_y_x['DT_factor_all_greatless_sd1']=dt_run(used_fields,10)
#
#used_fields=[i+"_greatless_mean_value_indicator" for i in mean_asset_list]
#hsi_y_x['DT_factor_all_greatless']=dt_run(used_fields,10)


hsi_y_x['GBM_factor']=GBM_run(mean_asset_list,1)



writer = pd.ExcelWriter('use_list_dataframe'+'.xlsx', engine='xlsxwriter')
use_list_dataframe.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_dataframe", hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x'+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()




























#great less count factor
factor_use=['GSPC_change','DJI_change','IXIC_change', 'NYA_change', 'VIX_change',
             'FTSE_change', 'GDAXI_change', 'FCHI_change', 'AORD_change', 'MXX_change',
             'EMA_N225_change', 'EMA_00001.SS_change', 'EMA_1398_HK_change', 'EMA_0016_HK_change',
             'EMA_0002_HK_change','EMA_HSI_index_change'
             'CHRIS_com_CME_GC1_change', 'CHRIS_com_CME_O1_change', 'CHRIS_com_ICE_B1_change',
             'ECB_cur_EURPHP_change', 'ECB_cur_EURRUB_change', 'ECB_cur_EURSGD_change',
             'ECB_cur_EURUSD_change', 'USTREASURY_REALLONGTERM_change',
             'USTREASURY_REALYIELD_5_change', 'USTREASURY_REALYIELD_7_change', 'USTREASURY_REALYIELD_10_change',
             'USTREASURY_REALYIELD_20_change',
             'UBS_change', 'BBVA_change', 'DB_change', 'CM_change', 'CAJ_change', 'PHG_change',
             'T_change', 'AMX_change',
             'MCK_change', 'CVX_change', 'BHP_change', 'RIO_change', 'PBR_A_change',
             'CHRIS_bond_EUREX_FGBM1_change',
             'HDB_change', 'EMA_0001_HK_change', 'ECB_cur_EURCNY_change', 'ECB_cur_EURHKD_change', 'MSFT_change',
             'CHRIS_com_CME_GC1_change_interact_CHRIS_com_ICE_B1_change','EWH_change',]

factor_use=['CHRIS_com_CME_GC1_change', 'AORD_change', 'PBR_A_change',
               'CHRIS_com_CME_O1_change', 'AMX_change',
               'CHRIS_bond_EUREX_FGBM1_change', 'CAJ_change', 'RIO_change',
               'HDB_change', 'DB_change', 'ECB_cur_EURUSD_change',
               'ECB_cur_EURHKD_change', 'ECB_cur_EURCNY_change', 'BBVA_change',
               'MXX_change', 'IXIC_change', 'ECB_cur_EURSGD_change',
               'ECB_cur_EURPHP_change']

#factor_use=[i.replace('_change','')+'_greatless_mean_value_indicator' for i in factor_use]

factor_use_down=['BHP_change', 'EWH_change',
                   'CHRIS_com_ICE_B1_change', 'FCHI_change', 'VIX_change', 'UBS_change',
                   'PHG_change', 'CVX_change', 'ECB_cur_EURRUB_change',
                   'USTREASURY_REALYIELD_5_change',
                   'GDAXI_change', 'NYA_change', 'FTSE_change',
                   'MSFT_change', 'GSPC_change', 'CM_change',
                   'USTREASURY_REALYIELD_10_change', 'DJI_change',
                   'MCK_change',
                   'T_change']

#factor_use_down=[i.replace('_change','')+'_greatless_mean_value_indicator' for i in factor_use_down]


hsi_y_x_use_down=hsi_y_x[factor_use_down].copy().as_matrix()*(-1)

hsi_y_x_use=hsi_y_x[factor_use].copy().as_matrix()
hsi_y_x_use=np.hstack((hsi_y_x_use,hsi_y_x_use_down))

count_greater_zero=(hsi_y_x_use>0).sum(axis=1)
count_less_zero=(hsi_y_x_use<0).sum(axis=1)
count_non_zero=np.count_nonzero(hsi_y_x_use,axis=1)
count_greater_zero_percent=count_greater_zero/count_non_zero
count_less_zero_percent=count_less_zero/count_non_zero

del hsi_y_x['count_factor']
hsi_y_x['count_factor2']=count_greater_zero_percent-count_less_zero_percent
hsi_y_x.loc[abs(hsi_y_x['count_factor2'])>0.3,'count_factor']=hsi_y_x['count_factor2']
hsi_y_x=hsi_y_x.fillna(0)

#create RSI
def rsi(x,parameter):
    x['change']=x['Close_HSI_index']-x['Open_HSI_index']
    x.loc[x['change']>=0,'gain']=x['change'];x.loc[x['change']<0,'gain']=0
    x.loc[x['change']<0,'loss']=-1*x['change'];x.loc[x['change']>=0,'loss']=0
    x['ave_gain']=x.gain.rolling(window=parameter).mean()
    x['ave_loss']=x.loss.rolling(window=parameter).mean()
    x['RS']=x['ave_gain']/x['ave_loss']
    x.loc[x['RS']==0,'RSI']=100;x.loc[x['RS']>0,'RSI']=100-100/(1+x['RS'])
    x=x.fillna(0)
    x['RSI_shift1']=x['RSI'].shift(1)
    x['RSI_shift1']=x['RSI_shift1'].fillna(0)
    x['RSI_shift2']=x['RSI'].shift(2)
    x['RSI_shift2']=x['RSI_shift2'].fillna(0)
    x['RSI_change']=x['RSI_shift1']-x['RSI_shift2']
    return x#pd.Series((x['RSI_change'].values,x['RSI_shift1'].values))
 
HSI_index_new=rsi(HSI_index,14)
 
HSI_index_new=HSI_index_new.rename(columns={'RSI_shift1':'RSI_shift1_change'})
hsi_y_x=pd.merge(hsi_y_x,HSI_index_new[['Date2','RSI_shift1_change','RSI_change']],how='left',left_on=['Date2'],right_on=['Date2'])

#fill nan by last record because 2012-03-19 no value in HSI_index_new
hsi_y_x=hsi_y_x.fillna(method='ffill')


#moving average indicators
hsi_index_for_ma=HSI_index.copy()
hsi_index_for_ma=hsi_index_for_ma.sort_values(by=['Date2'],ascending=[False])
hsi_index_for_ma=ema_custom_v2(hsi_index_for_ma,'DateNum','Close_HSI_index',10)
hsi_index_for_ma['EMA_Close_HSI_index_10']=hsi_index_for_ma['EMA_Close_HSI_index']
hsi_index_for_ma=ema_custom_v2(hsi_index_for_ma,'DateNum','Close_HSI_index',50)
hsi_index_for_ma['EMA_Close_HSI_index_50']=hsi_index_for_ma['EMA_Close_HSI_index']
hsi_index_for_ma['10_50_diff']=abs(hsi_index_for_ma['EMA_Close_HSI_index_10']-hsi_index_for_ma['EMA_Close_HSI_index_50'])
hsi_index_for_ma.loc[hsi_index_for_ma['EMA_Close_HSI_index_10']>=hsi_index_for_ma['EMA_Close_HSI_index_50'],'10_50_ema']=hsi_index_for_ma['10_50_diff']
hsi_index_for_ma.loc[hsi_index_for_ma['EMA_Close_HSI_index_10']<hsi_index_for_ma['EMA_Close_HSI_index_50'],'10_50_ema']=-1*hsi_index_for_ma['10_50_diff']

hsi_y_x=pd.merge(hsi_y_x,hsi_index_for_ma[['Date2','10_50_ema']],how='left',left_on=['Date2'],right_on=['Date2'])


hsi_y_x=hsi_y_x.fillna(0)


#create price volumn indicator
#x=HSI_index.copy()
def price_volume(x):
    x['change']=x['Close_HSI_index']-x['Open_HSI_index']
    x.loc[x['change']>=0,'gain']=x['change'];x.loc[x['change']<0,'gain']=0
    x.loc[x['change']<0,'loss']=-1*x['change'];x.loc[x['change']>=0,'loss']=0
    
    x['Volume_HSI_index_shift1']=x['Volume_HSI_index'].shift(1)
    x['volume_change']=x['Volume_HSI_index']-x['Volume_HSI_index_shift1']

    x.loc[(x['change']>0)&(x['volume_change']>0),'price_up_vol_up']=1
    x['price_up_vol_up']=x['price_up_vol_up'].fillna(0)
    x.loc[(x['change']>0)&(x['volume_change']<0),'price_up_vol_down']=1
    x['price_up_vol_down']=x['price_up_vol_down'].fillna(0)
    x.loc[(x['change']<0)&(x['volume_change']>0),'price_down_vol_up']=1
    x['price_down_vol_up']=x['price_down_vol_up'].fillna(0)
    x.loc[(x['change']<0)&(x['volume_change']<0),'price_down_vol_down']=1
    x['price_down_vol_down']=x['price_down_vol_down'].fillna(0)
    
    x['price_up_vol_up_shift1']=x['price_up_vol_up'].shift(1)
    x['price_up_vol_down_shift1']=x['price_up_vol_down'].shift(1)
    x['price_down_vol_up_shift1']=x['price_down_vol_up'].shift(1)
    x['price_down_vol_down_shift1']=x['price_down_vol_down'].shift(1)
    x=x.fillna(0)
    x['upup_downdown']=x['price_up_vol_up_shift1']-x['price_down_vol_down_shift1']
    x['updown_downup']=x['price_up_vol_down_shift1']+x['price_down_vol_up_shift1']

    return x#pd.Series((x['RSI_change'].values,x['RSI_shift1'].values))
 
HSI_index_new=price_volume(HSI_index)
 
hsi_y_x=pd.merge(hsi_y_x,HSI_index_new[['Date2','price_up_vol_up_shift1','price_up_vol_down_shift1','price_down_vol_up_shift1','price_down_vol_down_shift1','upup_downdown','updown_downup']],how='left',left_on=['Date2'],right_on=['Date2'])

#fill nan by last record because 2012-03-19 no value in HSI_index_new
hsi_y_x=hsi_y_x.fillna(method='ffill')
#
#hsi_y_x['EWH_change_same']=hsi_y_x['EWH_change']
#hsi_y_x['GSPC_change_same']=hsi_y_x['GSPC_change']
#hsi_y_x['DJI_change_same']=hsi_y_x['DJI_change']

#hsi_y_x=hsi_y_x2.copy()
#ARIMA model
#https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
hsi_y_x_for_time_series=pd.merge(hsi_y_x,hsi_y[['Date2','Open_HSI','Close_HSI']],how='left',left_on='Date2',right_on='Date2')
hsi_y_x_for_time_series['Y_hsi_change']=hsi_y_x_for_time_series['Close_HSI']-hsi_y_x_for_time_series['Open_HSI']

hsi_y_x_for_time_series_use2=hsi_y_x_for_time_series[['Date2','Y_hsi_change']].copy()
hsi_y_x_for_time_series_use2['Y_hsi_change']=hsi_y_x_for_time_series_use2['Y_hsi_change'].astype(float)

test_year=2009
train_end=str(test_year-1)+'-12-31'
test_start=str(test_year)+'-01-01'
test_end='2018'+'-12-31'

hsi_y_x_for_time_series_use_train=hsi_y_x_for_time_series_use2.loc[hsi_y_x_for_time_series_use2['Date2']<=train_end,:]
hsi_y_x_for_time_series_use_train=hsi_y_x_for_time_series_use_train.reset_index(drop=True)

hsi_y_x_for_time_series_use_test=hsi_y_x_for_time_series_use2.loc[(hsi_y_x_for_time_series_use2['Date2']>=test_start)&(hsi_y_x_for_time_series_use2['Date2']<=test_end),:]
hsi_y_x_for_time_series_use_test=hsi_y_x_for_time_series_use_test.reset_index(drop=True)

from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
from pandas.plotting import autocorrelation_plot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score

series=hsi_y_x_for_time_series_use_train['Y_hsi_change']
series.index=hsi_y_x_for_time_series_use_train['Date2']
series.dtypes


print(series.head())
series.plot()
pyplot.show()

autocorrelation_plot(series)
pyplot.show()





# fit model
model = ARIMA(series, order=(1,0,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())



# plot residual errors
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
pyplot.show()
residuals.plot(kind='kde')
pyplot.show()
print(residuals.describe())


#rolling forecast

train=hsi_y_x_for_time_series_use_train['Y_hsi_change'].copy()
test=hsi_y_x_for_time_series_use_test['Y_hsi_change'].copy()

history = [x for x in train]
predictions = []
for t in range(len(test)):
    model = ARIMA(history, order=(2,0,0)) #1,2,0
    model_fit = model.fit(disp=0)
    output = model_fit.forecast()
    yhat = output[0][0] # first is forecast, second is sd of forecast, 3,4 is CI of forecast
    predictions.append(yhat)  #append forecast ro prediction
    obs = test[t]
    history.append(obs) #append one by one in test to history
    print('predicted=%f, expected=%f' % (yhat, obs))
    print('doing ',t, ' out of ',range(len(test)))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

test_check=test>=0
prediction_check=pd.Series(predictions)>=0
accuracy_score(test_check, prediction_check)

correct=((test_check==True)&(prediction_check==True))|((test_check==False)&(prediction_check==False))
accuracy=sum(correct)/correct.shape[0];print(accuracy)
test_plain=abs(test)
pnl=sum(test_plain[correct])-sum(test_plain[~correct]);print(pnl)


# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
pyplot.show()


#append to hsi_y_x


prediction_Array=np.reshape(pd.Series(predictions).values,(pd.Series(predictions).values.shape[0],1))
zero_array=np.reshape(np.zeros(train.shape[0]),(train.shape[0],1))
append_to_hsi_y_x=np.vstack((zero_array,prediction_Array))

hsi_y_x['hsi_ARIMA']=append_to_hsi_y_x











#HMM
#os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis')
#hsi_y_x=read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hsi_y_x.xlsx',"Sheet1")
#hsi_y = read_excel('hsi_y.xlsx','Sheet1')

hsi_y_x_for_hmm=pd.merge(hsi_y_x,hsi_y[['Date2','Open_HSI','Close_HSI']],how='left',left_on='Date2',right_on='Date2')
hsi_y_x_for_hmm['Y_hsi_change']=hsi_y_x_for_hmm['Close_HSI']-hsi_y_x_for_hmm['Open_HSI']



all_hmm_factor=['index_SPX_wsj_change','index_DJIA_wsj_change','index_COMP_wsj_change','index_UK_NULL_UKX_wsj_change',
                     'index_DX_XETR_DAX_wsj_change','index_FR_XPAR_PX1_wsj_change','index_AU_XASX_XAO_wsj_change','index_MX_XMEX_IPC_wsj_change',
                     'ECB_cur_EURPHP_change','ECB_cur_EURRUB_change',
                     'ECB_cur_EURSGD_change','ECB_cur_EURUSD_change','USTREASURY_REALLONGTERM_change',
                     'USTREASURY_REALYIELD_5_change','USTREASURY_REALYIELD_7_change','USTREASURY_REALYIELD_10_change',
                     'USTREASURY_REALYIELD_20_change','BBVA_wsj_change','DB_wsj_change','CM_wsj_change','CAJ_wsj_change',
                     'PHG_wsj_change','T_wsj_change','AMX_wsj_change','MCK_wsj_change','CVX_wsj_change','BHP_wsj_change','RIO_wsj_change','PBRA_wsj_change',
                     'HDB_wsj_change','EMA_HK_XHKG_0001_wsj_change_v2','ECB_cur_EURCNY_change','ECB_cur_EURHKD_change',
                     'MSFT_wsj_change','EMA_index_HK_XHKG_HSI_wsj_change_v2','etf_EWH_wsj_change',
                     'FJSCX_wsj_change','HJPNX_wsj_change','OTPSX_wsj_change',
                     'TBGVX_wsj_change','DHFCX_wsj_change']  

non_hmm_factor=['AAII_AAII_SENTIMENT_change','EMA_index_JP_XTKS_NIK_wsj_change_v2','EMA_index_CN_SHCOMP_wsj_change_v2','index_NYA_wsj_change',
                'etf_HK_XHKG_3188_wsj_change','etf_XBI_wsj_change','UBS_wsj_change','FBGKX_wsj_change','index_VIX_wsj_change',
                'EMA_HK_XHKG_1398_wsj_change_v2','EMA_HK_16_wsj_change_v2','EMA_HK_XHKG_0002_wsj_change_v2','gold_futures_investing_greatless_mean_sd2_value_indicator_10',
                'oats_futures_investing_greatless_mean_sd2_value_indicator_10','brent_oil_investing_greatless_mean_sd2_value_indicator_10','euro_bobl_investing_greatless_mean_sd2_value_indicator_10',
                'brent_oil_gold_future_interact_indicator','index_DJIA_wsj_greatless_mean_sd2_value_indicator']


all_hmm_factor=['AMX_wsj_change']

all_hmm_factor_split=[]
kk='AMX_wsj_change'
import sys
for kk in all_hmm_factor:
    factor_use=kk
    used_fields=['Date2','year',factor_use]
    
    r_hmm_path=r"C:\Users\jonahthonchan\Desktop\R\r_work\hmm"
    
    year_hmm=[i for i in hsi_y_x_for_hmm.year.unique() if i >=2007]
    year_hmm=[i for i in year_hmm if i>=2011 ]
    #i=2011
    
    hmm_grouping=np.array([])
    
    for i in year_hmm:
        #i=2011
        hsi_y_x_for_hmm['year']=hsi_y_x_for_hmm['year'].astype(int)
        train_xy=hsi_y_x_for_hmm.loc[hsi_y_x_for_hmm['year']<i,used_fields].copy()
    
        test_xy=hsi_y_x_for_hmm.loc[hsi_y_x_for_hmm['year']==i,used_fields].copy()
    
    
        train_name="train_xy_for_hmm"+factor_use+'_'+str(i)+'.csv'
        file_name_hmm_csv=os.path.join(r_hmm_path,train_name)
        train_xy.to_csv(file_name_hmm_csv,sep=',', encoding='utf-8')
    
        test_name="test_xy_for_hmm"+factor_use+'_'+str(i)+'.csv'
        file_name_hmm_csv=os.path.join(r_hmm_path,test_name)
        test_xy.to_csv(file_name_hmm_csv,sep=',', encoding='utf-8')
    
        #run R hmm
        import subprocess
        command = r"C:\Program Files\R\R-3.6.3\bin\Rscript"
        arg = '--vanilla'
        path2script = r"C:\Users\jonahthonchan\Desktop\R\r_work\viterbi_use.R"
        
        #if also use a sink in R script to output stdout and stderr, this log only output error, not stdour
        #if comment out sink in R, this log will also output stdout and stderr 
        rllog_name=os.path.join(r'C:\Users\jonahthonchan\Desktop\R\r_work\hmm',factor_use+'_'+str(i)+'_stdout_err.txt')
        with open(rllog_name,'wb') as fileobj:
            subprocess.call([command, arg, path2script,factor_use,str(i)],
                             stdout=fileobj, stderr=subprocess.STDOUT, shell=False)    
        
        fileobj.close()


        
        
        
        #read train and test prediction
        train_name="train_xy_"+factor_use+'_'+str(i)+'_hmm_output.csv'
        file_name_hmm_csv=os.path.join(r_hmm_path,train_name)
        train_xy_predict=pd.read_csv(file_name_hmm_csv)
    
        test_name="train_test_xy_"+factor_use+'_'+str(i)+'_hmm_output.csv'
        file_name_hmm_csv=os.path.join(r_hmm_path,test_name)
        train_test_xy_predict=pd.read_csv(file_name_hmm_csv)
        
        f_name=factor_use+'_hmm_group'
        if i==2011:
            temp=np.reshape(train_test_xy_predict[f_name].values,(train_test_xy_predict[f_name].values.shape[0],1))
            hmm_grouping=temp
        else:
            use1=train_test_xy_predict.loc[train_test_xy_predict['year']==i,f_name].values
            temp=np.reshape(use1,(use1.shape[0],1))
            hmm_grouping=np.vstack((hmm_grouping,temp))
        print("finished ",i)
    
    all_group=np.unique(hmm_grouping).tolist()
    
    hsi_y_x_for_hmm[f_name]=hmm_grouping
    #i=1
    for i in all_group:
        split_name=factor_use+'_split_hmm_group'+str(i)
        hsi_y_x_for_hmm.loc[hsi_y_x_for_hmm[f_name]==i,split_name]=hsi_y_x_for_hmm[factor_use]
        hsi_y_x_for_hmm[split_name]=hsi_y_x_for_hmm[split_name].fillna(0)
        hsi_y_x[split_name]=hsi_y_x_for_hmm[split_name].copy()
        all_hmm_factor_split.append(split_name)





all_hmm_factor_split2=all_hmm_factor_split+non_hmm_factor

temp_string=''
for kk in all_hmm_factor_split2:
    temp_string=temp_string+"'"+kk+"'"+','












writer = pd.ExcelWriter('use_list_dataframe'+'.xlsx', engine='xlsxwriter')
use_list_dataframe.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_dataframe", hsi_y_x, data_columns=hsi_y_x.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x'+'.xlsx', engine='xlsxwriter')
hsi_y_x.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


sys.stderr.close()
sys.stderr = sys.__stderr__





#hsi_y_x=read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hsi_y_x.xlsx','Sheet1')









#import os
#os.chdir(r'C:\Users\jonahthonchan\Desktop\python\stockstats\stockstats-master')
#import stockstats
#
#
#from importlib.machinery import SourceFileLoader
#
#foo = SourceFileLoader("module.name", "/path/to/file.py").load_module()
#foo.MyClass()



































###############hsi afternoon#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'

os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session
folder_path=os.path.join(target_dir,'mis')

fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()

##save for amibroker hav a look
#data_amibroker=data[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
#data_amibroker['hms']=data_amibroker['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))
#data_amibroker=data_amibroker[['date_ymd','hms','Open','High','Low','Close','TotalVolume']].copy()
#data_amibroker=data_amibroker.loc[(data_amibroker['TotalVolume']!=0),:]
#data_amibroker_check=data_amibroker.head(100)
#data_amibroker.to_csv("./mis/FHSI_minute_20051201to_amibroker.txt", header=True, index=None, sep='\t', mode='a')


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data_use.reset_index(drop=True)






def split_morning_afternoon(data_use):
    data_use2=data_use.copy()
    data_use2['Date1_shift1']=data_use2['Date1'].shift(1)
    data_use2['time_diff']=data_use2['Date1']-data_use2['Date1_shift1']
    data_use2['time_diff_min']=data_use2['time_diff'].apply(lambda x:x.total_seconds()/60)

    date_out=data_use2['Date2'].values[0]
    print(date_out)

    ind=data_use2['time_diff_min']>=60
    ind=ind[ind==True]
    ind_size=len(ind)
    
    
    minute_threshold=0
    
    if ind_size!=0:
        ind=ind.index[0]
        
#        #below use threshold 1 min
#        #means morning start from 0915 to 1159, afternoon start from 1159 to last minute
#        data_use2_morning=data_use2.iloc[0:ind-minute_threshold]
#        data_use2_afternoon1=data_use2.iloc[ind-minute_threshold:ind]   
#        data_use2_afternoon2=data_use2.iloc[ind:-minute_threshold]  
#        data_use2_afternoon3=data_use2.iloc[-minute_threshold:]   
#        
#        open_morning=data_use2_morning['Open'].values[0]
#        high_morning=np.max(data_use2_morning['High'].values)
#        low_morning=np.min(data_use2_morning['Low'].values)
#        close_morning=data_use2_morning['Close'].values[-1]
        
#        #open afternoon
#        data_use2_afternoon1=data_use2_afternoon1.head(minute_threshold)
#        data_use2_afternoon1['mean']=(data_use2_afternoon1['High']+data_use2_afternoon1['Low']+data_use2_afternoon1['Open']+data_use2_afternoon1['Close'])/4
#        open_afternoon=np.mean(data_use2_afternoon1['mean'].values)
#        
#        high_afternoon=np.max(data_use2_afternoon2['High'].values)
#        low_afternoon=np.min(data_use2_afternoon2['Low'].values)
#        
#        data_use2_afternoon3=data_use2_afternoon3.head(minute_threshold)
#        data_use2_afternoon3['mean']=(data_use2_afternoon3['High']+data_use2_afternoon3['Low']+data_use2_afternoon3['Open']+data_use2_afternoon3['Close'])/4
#        close_afternoon=np.mean(data_use2_afternoon3['mean'].values)
        
        
#        #below use fix point
#        data_use2_morning=data_use2.iloc[0:ind]    ##use 1154 bar as morning last
#        data_use2_afternoon1=data_use2.iloc[ind:]    
#        
#        open_morning=data_use2_morning['Open'].values[0]     
#        high_morning=np.max(data_use2_morning['High'].values)
#        low_morning=np.min(data_use2_morning['Low'].values)
#        close_morning=data_use2_morning['Close'].values[-1]    #use 1159 close
#        
#        open_afternoon=data_use2_afternoon1['Open'].values[0]   #use 1159 close
#        high_afternoon=np.max(data_use2_afternoon1['High'].values)
#        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
#        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        
        
        
        
        
        
        #below use fix point
        data_use2_morning=data_use2.iloc[0:ind-5]    ##use 1154 bar as morning last
        data_use2_afternoon1=data_use2.iloc[ind-1:]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    #use 1154 close
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Close'].values[0]   #use 1159 close
        high_afternoon=np.max(data_use2_afternoon1['High'].values[1:])
        low_afternoon=np.min(data_use2_afternoon1['Low'].values[1:])
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[1] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'ind_size':[ind_size]})
    
    return output

temp1=data.groupby("Date2").apply(lambda x:split_morning_afternoon(x.reset_index(drop=True)))

#temp1=temp1.loc[~(temp1['open_time2']==0),]
#temp1['time2']=temp1['open_time2'].apply(lambda x: x.strftime('%H:%M:%S'))
#temp_special=temp1.loc[(temp1['Date2']>='2012-05-03'),:]
#temp_special=temp_special.loc[(temp_special['time2']=='13:30:00'),:]

#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['ind_size']>0,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8


#check morning open and close time
check1=temp1[['Date2','Open1','High1','Low1','Close1','open_time1','close_time1']].copy()
check2=temp1[['Date2','Open2','High2','Low2','Close2','open_time2','close_time2']].copy()
check1=pd.merge(check1,check2[['Date2','open_time2','close_time2']].copy(),how='left',on=['Date2'])










#use morning as one of the factor
temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
temp1_morning=temp1_morning.rename(columns={'Open1':'Open_HSI','High1':'High_HSI',
                                                            'Low1':'Low_HSI','Close1':'Close_HSI'})
temp1_morning=temp1_morning.reset_index(drop=True)
                        
#need to change a bit format to dt, because save to index_analsis
temp1_morning['Date2']=temp1_morning['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_morning['DateNum']= (temp1_morning['Date2']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_morning.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_morning.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()






##use morning as Y
#temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
#temp1_morning=temp1_morning.rename(columns={'Date2':'Date','Open1':'Open','High1':'High',
#                                                           'Low1':'Low','Close1':'Close'})
#temp1_morning=temp1_morning.reset_index(drop=True)
#                        
##need to change a bit format to dt, because save to index_analsis
#temp1_morning['Date']=temp1_morning['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#temp1_morning['DateNum']= (temp1_morning['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_morning.to_excel(writer, sheet_name='Sheet1')
#writer.save()



#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                        
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)

temp1_afternoon.dtypes

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_afternoon.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

HSI_afternoon= read_excel('HSI_afternoon.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_afternoon_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#create dependent variable Y
hsi_y_afternoon=HSI_afternoon.loc[:,['Date2','DateNum','Open_HSI_afternoon','Close_HSI_afternoon']]
hsi_y_afternoon['Y_up']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon>=row.Open_HSI_afternoon)*1,axis=1)
hsi_y_afternoon['Y_down']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon<row.Open_HSI_afternoon)*1,axis=1)

writer = pd.ExcelWriter('hsi_y_afternoon.xlsx', engine='xlsxwriter')
hsi_y_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


hsi_y_afternoon=pd.read_excel('hsi_y_afternoon.xlsx','Sheet1')

hsi_y_x_afternoon=hsi_y_afternoon[['Date2','DateNum','Y_up','Y_down']].copy()





##########################hsi afternoon factor##################################

#test break open impact
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()






hsi_y_temp['Close_HSI_lag1']=hsi_y_temp['Close_HSI'].shift(1)

hsi_y_temp['break_open']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])
hsi_y_temp['break_open']=hsi_y_temp['break_open'].fillna(0)

hsi_y_temp['break_open_percent']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])/hsi_y_temp['Close_HSI_lag1']
hsi_y_temp['break_open_percent']=hsi_y_temp['break_open_percent'].fillna(0)

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_y_temp[['Date2','break_open_percent','break_open']],how='left',left_on=['Date2'],right_on=['Date2'])
hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)





#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,"HSI_morning.xlsx"),'Sheet1')
hsi_morning['Date2']=hsi_morning['Date2'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_morning_change_abs']=(hsi_morning['Close_HSI']-hsi_morning['Open_HSI'])
hsi_morning['hsi_morning_change']=(hsi_morning['Close_HSI']-hsi_morning['Open_HSI'])/hsi_morning['Open_HSI']
hsi_morning['hsi_morning_change_indicator']=(hsi_morning['hsi_morning_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date2',
                                                          'hsi_morning_change',
                                                          'hsi_morning_change_indicator',
                                                          'hsi_morning_change_abs']],how='left',left_on=['Date2'],right_on=['Date2'])







#full day prediction
full_day=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))
temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()

#temp=temp.loc[~pd.isnull(temp['Date2']),:]
#temp['Date2']=temp['Date2'].apply(lambda x:dt.strptime(x,"%m/%d/%Y").strftime("%Y-%m-%d"))

from pandas import read_excel
#this need to manually run all in sample fit for 2005 to 2010
in_sample_fitting=pd.read_excel(os.path.join(folder_path,"30013_test_2005_to_2010_insample_model2021.xlsx"),'daily_detail_summary')
in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()

in_sample_fitting=in_sample_fitting.append(temp)


temp['Date2'].dtypes
in_sample_fitting['Date2'].dtypes

hsi_y_x_afternoon['Date2'].dtypes


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,in_sample_fitting[['Date2','up_prediction_prob','Y_up_predict']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

hsi_y_x_afternoon=hsi_y_x_afternoon.rename(columns={'up_prediction_prob':'full_prediction_prob',
                                                    'Y_up_predict':'full_prediction_indicate'})
hsi_y_x_afternoon=hsi_y_x_afternoon.loc[~pd.isnull(hsi_y_x_afternoon['full_prediction_prob']),:]



import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x_afternoon.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_afternoon_dataframe", hsi_y_x_afternoon, data_columns=hsi_y_x_afternoon.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x_afternoon'+'.xlsx', engine='xlsxwriter')
hsi_y_x_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()














































###############hsi_0_to_13 and 0_to_13#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
#folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"

target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'
folder_path=os.path.join(target_dir,'mis')


os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session


fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data_use.reset_index(drop=True)






a=15;b=43;c=45;d=90
def split_custom(data_use,a,b,c,d):
    data_use2=data_use.copy()
    date_out=data_use2['Date2'].values[0]
    #check whether morning exist
    data_use2_check=data_use2.head(1)
    morning_exist=False
    if ((data_use2_check.hms.values[0]=='09:15:00') | (data_use2_check.hms.values[0]=='09:45:00')):
        morning_exist=True
    
    if morning_exist==True:

        #below use fix point
        data_use2_morning=data_use2.iloc[a:b]   
        data_use2_afternoon1=data_use2.iloc[c:d]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]   
        high_afternoon=np.max(data_use2_afternoon1['High'].values)
        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'morning_exist':[morning_exist]})
    print(date_out)
    return output

temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=13,c=0,d=13))
#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['morning_exist']==True,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8




#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
   
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                      
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)


#remove typhoon or no dat, e.g. open high low close all equal zero/ all same
judge1=temp1_afternoon['Open']==temp1_afternoon['High']
judge2=temp1_afternoon['High']==temp1_afternoon['Low']
judge3=temp1_afternoon['Low']==temp1_afternoon['Close']
temp1_afternoon=temp1_afternoon.loc[~((judge1==True) & (judge2==True) & (judge3==True)),:].copy()



temp1_afternoon.dtypes

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_0_to_13.xlsx')
#output_path=os.path.join(target_dir,'HSI_0_to_13_cum.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

HSI_afternoon= read_excel('HSI_0_to_13.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_0_to_13_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#create dependent variable Y
hsi_y_afternoon=HSI_afternoon.loc[:,['Date2','DateNum','Open_HSI_afternoon','Close_HSI_afternoon']]
hsi_y_afternoon['Y_up']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon>=row.Open_HSI_afternoon)*1,axis=1)
hsi_y_afternoon['Y_down']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon<row.Open_HSI_afternoon)*1,axis=1)

writer = pd.ExcelWriter('hsi_y_0_to_13.xlsx', engine='xlsxwriter')
hsi_y_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


hsi_y_afternoon=pd.read_excel('hsi_y_0_to_13.xlsx','Sheet1')

hsi_y_x_afternoon=hsi_y_afternoon[['Date2','DateNum','Y_up','Y_down']].copy()





##########################hsi 0_to_13 factor##################################

#test break open impact
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()


hsi_y_temp['Close_HSI_lag1']=hsi_y_temp['Close_HSI'].shift(1)

hsi_y_temp['break_open']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])
hsi_y_temp['break_open']=hsi_y_temp['break_open'].fillna(0)

hsi_y_temp['break_open_percent']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])/hsi_y_temp['Close_HSI_lag1']
hsi_y_temp['break_open_percent']=hsi_y_temp['break_open_percent'].fillna(0)

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_y_temp[['Date2','break_open_percent','break_open']],how='left',left_on=['Date2'],right_on=['Date2'])
hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)






##full day prediction
#full_day=pd.read_csv(os.path.join(folder_path,'all_prediction.csv'))
#temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()
#
##temp=temp.loc[~pd.isnull(temp['Date2']),:]
##temp['Date2']=temp['Date2'].apply(lambda x:dt.strptime(x,"%m/%d/%Y").strftime("%Y-%m-%d"))
#
#from pandas import read_excel
##this need to manually run all in sample fit for 2005 to 2010
#in_sample_fitting=pd.read_excel(os.path.join(folder_path,'30013_test_2005_to_2010_insample_model2021.xlsx'),'daily_detail_summary')
#in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()
#
#in_sample_fitting=in_sample_fitting.append(temp)
#
#
#temp['Date2'].dtypes
#in_sample_fitting['Date2'].dtypes
#
#hsi_y_x_afternoon['Date2'].dtypes
#
#
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,in_sample_fitting[['Date2','up_prediction_prob','Y_up_predict']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
#
#hsi_y_x_afternoon=hsi_y_x_afternoon.rename(columns={'up_prediction_prob':'full_prediction_prob',
#                                                    'Y_up_predict':'full_prediction_indicate'})
#hsi_y_x_afternoon=hsi_y_x_afternoon.loc[~pd.isnull(hsi_y_x_afternoon['full_prediction_prob']),:]



import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x_0_to_13.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_0_to_13_dataframe", hsi_y_x_afternoon, data_columns=hsi_y_x_afternoon.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x_0_to_13'+'.xlsx', engine='xlsxwriter')
hsi_y_x_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



















###############hsi_15_to_end and 15_to_end#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
#folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"

target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'
folder_path=os.path.join(target_dir,'mis')


os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session


fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data_use.reset_index(drop=True)






a=15;b=43;c=45;d=90
def split_custom(data_use,a,b,c,d):
    data_use2=data_use.copy()
    date_out=data_use2['Date2'].values[0]
    #check whether morning exist
    data_use2_check=data_use2.head(1)
    morning_exist=False
    if ((data_use2_check.hms.values[0]=='09:15:00') | (data_use2_check.hms.values[0]=='09:45:00')):
        morning_exist=True
    
    if morning_exist==True:

        #below use fix point
        data_use2_morning=data_use2.iloc[a:b]   
        data_use2_afternoon1=data_use2.iloc[c:d]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]   
        high_afternoon=np.max(data_use2_afternoon1['High'].values)
        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'morning_exist':[morning_exist]})
    print(date_out)
    return output

temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=15,b=999999,c=15,d=999999))
#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['morning_exist']==True,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8




#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
   
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                      
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)


#remove typhoon or no dat, e.g. open high low close all equal zero/ all same
judge1=temp1_afternoon['Open']==temp1_afternoon['High']
judge2=temp1_afternoon['High']==temp1_afternoon['Low']
judge3=temp1_afternoon['Low']==temp1_afternoon['Close']
temp1_afternoon=temp1_afternoon.loc[~((judge1==True) & (judge2==True) & (judge3==True)),:].copy()



temp1_afternoon.dtypes

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_15_to_999999.xlsx')
#output_path=os.path.join(target_dir,'HSI_0_to_13_cum.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

HSI_afternoon= read_excel('HSI_15_to_999999.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_15_to_999999_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()







































###############hsi_0_to_13 and 15_to_30#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'

os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session
#folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
folder_path=os.path.join(target_dir,"mis")

fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data.loc[data['Date2']=='2021-10-13',:]  #typhoon 8
data_use=data.loc[data['Date2']=='2021-06-28',:]  #no morning
data_use=data_use.reset_index(drop=True)






a=0;b=13;c=15;d=45
def split_custom(data_use,a,b,c,d):
    data_use2=data_use.copy()
    date_out=data_use2['Date2'].values[0]
    #check whether morning exist
    data_use2_check=data_use2.head(1)
    morning_exist=False
    if ((data_use2_check.hms.values[0]=='09:15:00') | (data_use2_check.hms.values[0]=='09:45:00')):
        morning_exist=True
    
    if morning_exist==True:

        #below use fix point
        data_use2_morning=data_use2.iloc[a:b]   
        data_use2_afternoon1=data_use2.iloc[c:d]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]   
        high_afternoon=np.max(data_use2_afternoon1['High'].values)
        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'morning_exist':[morning_exist]})
    print(date_out)
    return output

#temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=13,c=15,d=45))
temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=13,c=15,d=30))
#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['morning_exist']==True,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8


#check morning open and close time
check1=temp1[['Date2','Open1','High1','Low1','Close1','open_time1','close_time1']].copy()
check2=temp1[['Date2','Open2','High2','Low2','Close2','open_time2','close_time2']].copy()
#check1=pd.merge(check1,check2[['Date2','open_time2','close_time2']].copy(),how='left',on=['Date2'])










##use morning as one of the factor
#temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
#temp1_morning=temp1_morning.rename(columns={'Open1':'Open_HSI','High1':'High_HSI',
#                                                            'Low1':'Low_HSI','Close1':'Close_HSI'})
#temp1_morning=temp1_morning.reset_index(drop=True)
#                        
##need to change a bit format to dt, because save to index_analsis
#temp1_morning['Date2']=temp1_morning['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#temp1_morning['DateNum']= (temp1_morning['Date2']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI_0_to_13.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_morning.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#writer.close()




#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                        
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)

temp1_afternoon.dtypes


#remove typhoon or no dat, e.g. open high low close all equal zero/ all same
judge1=temp1_afternoon['Open']==temp1_afternoon['High']
judge2=temp1_afternoon['High']==temp1_afternoon['Low']
judge3=temp1_afternoon['Low']==temp1_afternoon['Close']
temp1_afternoon=temp1_afternoon.loc[~((judge1==True) & (judge2==True) & (judge3==True)),:].copy()


#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_15_to_30.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

output_path=os.path.join(target_dir,'HSI_15_to_30_cum.xlsx')   #daily update will use this
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()




HSI_afternoon= read_excel('HSI_15_to_30.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_15_to_30_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#create dependent variable Y
hsi_y_afternoon=HSI_afternoon.loc[:,['Date2','DateNum','Open_HSI_afternoon','Close_HSI_afternoon']]
hsi_y_afternoon['Y_up']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon>=row.Open_HSI_afternoon)*1,axis=1)
hsi_y_afternoon['Y_down']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon<row.Open_HSI_afternoon)*1,axis=1)

writer = pd.ExcelWriter('hsi_y_15_to_30.xlsx', engine='xlsxwriter')
hsi_y_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


hsi_y_afternoon=pd.read_excel('hsi_y_15_to_30.xlsx','Sheet1')

hsi_y_x_afternoon=hsi_y_afternoon[['Date2','DateNum','Y_up','Y_down']].copy()





##########################hsi 15_to_30 factor##################################

#test break open impact
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()


hsi_y_temp['Close_HSI_lag1']=hsi_y_temp['Close_HSI'].shift(1)

hsi_y_temp['break_open']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])
hsi_y_temp['break_open']=hsi_y_temp['break_open'].fillna(0)





#hsi_y_temp=pd.merge(hsi_y_temp,hsi_morning[['Date2','hsi_0_to_13_change_abs']],how='left',left_on=['Date2'],right_on=['Date2'])
#hsi_y_temp['break_open_percent']=(hsi_y_temp['break_open']+hsi_y_temp['hsi_0_to_13_change_abs'])/hsi_y_temp['Close_HSI_lag1']


hsi_y_temp['break_open_percent']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])/hsi_y_temp['Close_HSI_lag1']
hsi_y_temp['break_open_percent']=hsi_y_temp['break_open_percent'].fillna(0)


hsi_y_temp.loc[hsi_y_temp['break_open_percent']>=0,'break_open_percent1']=hsi_y_temp['break_open_percent']
hsi_y_temp.loc[hsi_y_temp['break_open_percent']<0,'break_open_percent2']=hsi_y_temp['break_open_percent']




hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_y_temp[['Date2','break_open_percent','break_open','break_open_percent1','break_open_percent2']],how='left',left_on=['Date2'],right_on=['Date2'])
hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)


hsi_y_x_afternoon['year_cohord']=hsi_y_x_afternoon['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)

#target_variable='break_open_percent'
#distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
#distinct_year=[i for i in distinct_year if i >=2007]
#yy=2010
#percentile_cum=pd.DataFrame([])
#for yy in distinct_year:
#    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
#    first_percentile_capture=np.nanpercentile(data_use,25)
#    second_percentile_capture=np.nanpercentile(data_use,50)
#    third_percentile_capture=np.nanpercentile(data_use,75)
#    t1='first_percentile_'+target_variable
#    t2='second_percentile_'+target_variable
#    t3='third_percentile_'+target_variable
#    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
#                                                       t1:[first_percentile_capture],
#                                                       t2:[second_percentile_capture],
#                                                       t3:[third_percentile_capture]}))
#
#
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
#a_check=hsi_y_x_afternoon.tail(1000)
#
#new_var=target_variable+'_percentile'
#hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
#hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
#hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
#hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
#hsi_y_x_afternoon.dtypes


target_variable='break_open_percent'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes









#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_0_to_13.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_0_to_13_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_0_to_13_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_0_to_13_change_indicator']=(hsi_morning['hsi_0_to_13_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_0_to_13_change',
                                                          'hsi_0_to_13_change_indicator',
                                                          'hsi_0_to_13_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])





target_variable='hsi_0_to_13_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,10)
    first2_percentile_capture=np.nanpercentile(data_use,30)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,70)
    third_percentile_capture=np.nanpercentile(data_use,90)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes








#full day prediction
full_day=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()

#temp=temp.loc[~pd.isnull(temp['Date2']),:]
#temp['Date2']=temp['Date2'].apply(lambda x:dt.strptime(x,"%m/%d/%Y").strftime("%Y-%m-%d"))

from pandas import read_excel
#this need to manually run all in sample fit for 2005 to 2010
in_sample_fitting=pd.read_excel(os.path.join(folder_path,'30013_test_2005_to_2010_insample_model2021.xlsx'),'daily_detail_summary')
in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()

in_sample_fitting=in_sample_fitting.append(temp)

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,in_sample_fitting[['Date2','up_prediction_prob','Y_up_predict']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

hsi_y_x_afternoon=hsi_y_x_afternoon.rename(columns={'up_prediction_prob':'full_prediction_prob',
                                                    'Y_up_predict':'full_prediction_indicate'})
hsi_y_x_afternoon=hsi_y_x_afternoon.loc[~pd.isnull(hsi_y_x_afternoon['full_prediction_prob']),:]




##0_to_13 prediction
#full_day=pd.read_csv(os.path.join(folder_path,"all_prediction_phase1.csv"))
#temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()
#
##temp=temp.loc[~pd.isnull(temp['Date2']),:]
##temp['Date2']=temp['Date2'].apply(lambda x:dt.strptime(x,"%m/%d/%Y").strftime("%Y-%m-%d"))
#
#from pandas import read_excel
##this need to manually run all in sample fit for 2005 to 2010
#in_sample_fitting=pd.read_excel(os.path.join(folder_path,'30013_test_2005_to_2010_insample_model2021_0_to_13.xlsx'),'daily_detail_summary')
#in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()
#
#in_sample_fitting=in_sample_fitting.append(temp)
#
#in_sample_fitting=in_sample_fitting.rename(columns={'up_prediction_prob':'0_to_13_prediction_prob',
#                                                    'Y_up_predict':'0_to_13_prediction_indicate'})
#
#
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,in_sample_fitting[['Date2','0_to_13_prediction_prob','0_to_13_prediction_indicate']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])
#hsi_y_x_afternoon=hsi_y_x_afternoon.loc[~pd.isnull(hsi_y_x_afternoon['0_to_13_prediction_prob']),:]


hsi_y_x_afternoon.dtypes










#f1
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'break_first15_1']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<=hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'break_first15_1']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['break_first15_1']=hsi_y_x_afternoon['break_first15_1'].fillna(0)

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<=hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'break_first15_2']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'break_first15_2']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['break_first15_2']=hsi_y_x_afternoon['break_first15_2'].fillna(0)



#correct full day pred
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_0_to_13_change']>=0)&(hsi_y_x_afternoon['full_prediction_prob']>=0.5),'full_correct']=1
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_0_to_13_change']<0)&(hsi_y_x_afternoon['full_prediction_prob']<0.5),'full_correct']=1

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_0_to_13_change']>=0)&(hsi_y_x_afternoon['full_prediction_prob']<0.5),'full_wrong']=hsi_y_x_afternoon['hsi_0_to_13_change']
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_0_to_13_change']<0)&(hsi_y_x_afternoon['full_prediction_prob']>=0.5),'full_wrong']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['full_correct']=hsi_y_x_afternoon['full_correct'].fillna(0)
hsi_y_x_afternoon['full_wrong']=hsi_y_x_afternoon['full_wrong'].fillna(0)



hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change'])&
                      (hsi_y_x_afternoon['full_prediction_prob']<0.5),'f1']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<=hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change'])&
                      (hsi_y_x_afternoon['full_prediction_prob']>=0.5),'f1']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['f1']=hsi_y_x_afternoon['f1'].fillna(0)



hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change'])&
                      (hsi_y_x_afternoon['full_prediction_prob']<0.5),'f2']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_0_to_13_change']<=hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change'])&
                      (hsi_y_x_afternoon['full_prediction_prob']>=0.5),'f2']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['f2']=hsi_y_x_afternoon['f2'].fillna(0)





hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<=hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f3']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f4']=hsi_y_x_afternoon['hsi_0_to_13_change']
hsi_y_x_afternoon['f3']=hsi_y_x_afternoon['f3'].fillna(0)
hsi_y_x_afternoon['f4']=hsi_y_x_afternoon['f4'].fillna(0)



hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f5']=hsi_y_x_afternoon['break_open_percent']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f6']=hsi_y_x_afternoon['break_open_percent']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f7']=hsi_y_x_afternoon['break_open_percent']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f8']=hsi_y_x_afternoon['break_open_percent']


hsi_y_x_afternoon['f5']=hsi_y_x_afternoon['f5'].fillna(0)
hsi_y_x_afternoon['f6']=hsi_y_x_afternoon['f6'].fillna(0)
hsi_y_x_afternoon['f7']=hsi_y_x_afternoon['f7'].fillna(0)
hsi_y_x_afternoon['f8']=hsi_y_x_afternoon['f8'].fillna(0)




#read oi
oi_original= read_excel(os.path.join(target_dir,'hang_seng_oi'+'_with_tidy.xlsx'),'Sheet1')
oi_original['year']=oi_original['Date2'].apply(lambda x:int(x[0:4]))


oi_original=oi_original.sort_values(by='DateNum',ascending=False).reset_index(drop=True)

from pandas import read_excel

hsi_y = read_excel('hsi_y.xlsx','Sheet1')
oi_original=pd.merge(oi_original,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
                      on=['Date2'],how='left')

#volume
HSIvolume_source=pd.read_excel(os.path.join(target_dir,'hang_seng_oi_volume_with_tidy.xlsx'),'Sheet1')
hsi_vol=HSIvolume_source.copy()
hsi_vol['year']=hsi_vol['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)

oi_original=pd.merge(oi_original,hsi_vol[['Date2','Close_hang_seng_oi_volume']].copy(),how='left',on=['Date2'])

#for settlement day and one day after it, hsi_vol has no values(removed the row), so in oi_original, it is nan, so remove it.
oi_original=oi_original.loc[~pd.isnull(oi_original['Close_hang_seng_oi_volume']),:]

oi_original['oi_over_volume']=(oi_original['Close_hang_seng_oi']-oi_original['Open_hang_seng_oi'])#/oi_original['Close_hang_seng_oi_volume']


oi_original['diff']=oi_original['Close_HSI']-oi_original['Open_HSI']
oi_original['diff_shift1']=oi_original['diff'].shift(-1)
oi_original['hang_seng_oi_change_shift1']=oi_original['oi_over_volume'].shift(-1)



hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,oi_original[['Date2','diff_shift1','hang_seng_oi_change','hang_seng_oi_change_shift1']],how='left',on=['Date2'])
hsi_y_x_afternoon['diff_shift1']=hsi_y_x_afternoon['diff_shift1'].fillna(0)
hsi_y_x_afternoon['hang_seng_oi_change_shift1']=hsi_y_x_afternoon['hang_seng_oi_change_shift1'].fillna(0)



target_variable='hang_seng_oi_change_shift1'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2008]
yy=2013
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    #OI have value only when 2007
    data_use=hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['year_cohord']>=2007)&(hsi_y_x_afternoon['year_cohord']<yy),target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes










#del hsi_y_x_afternoon['f13']
#del hsi_y_x_afternoon['f14']











hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f13']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f13']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['f13']=hsi_y_x_afternoon['f13'].fillna(0)







##merge temp factr
#tempf= read_excel(os.path.join(target_dir,'hsi_y_x_15_to_30_temp.xlsx'),'Sheet1')
#usef=['Date2','IVOV_change','VOOG_change','VOOV_change','VTHR_change','VNQI_change','HK_XHKG_1299_wsj_change','VIOO_change','EFV_change','SPMB_change','EWG_change',
#      'USTREASURY_REALYIELD_7_change','FDL_change','TNA_change','TAREX_change','VGSCX_change','VGSAX_change',
#      'VGISX_change','MIJFX_change','FJSCX_change','HJPSX_change',
#      'HJPNX_change','IVV_change',
#      'SQQQ_change','TQQQ_change','STIP_change','AORD_change','AXJO_change','VO_change','SPY_change']
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,tempf[usef].copy(),how='left',on=['Date2'])
#
#
#usef.remove('Date2')
#
#k='IVOV_change'
#for k in usef:
#    hsi_y_x_afternoon.loc[((hsi_y_x_afternoon['break_open_percent']<hsi_y_x_afternoon['first_percentile_break_open_percent'])|
#                      (hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent']))|(hsi_y_x_afternoon['Date2']<='2007-01-01'),k]=0


    

    


import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x_15_to_30.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_15_to_30_dataframe", hsi_y_x_afternoon, data_columns=hsi_y_x_afternoon.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x_15_to_30'+'.xlsx', engine='xlsxwriter')
hsi_y_x_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()






























###############hsi 0_to_30 and 30_to_43#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'

os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session
folder_path=os.path.join(target_dir,"mis")

fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data_use.reset_index(drop=True)






a=15;b=43;c=45;d=90
def split_custom(data_use,a,b,c,d):
    data_use2=data_use.copy()
    date_out=data_use2['Date2'].values[0]
    #check whether morning exist
    data_use2_check=data_use2.head(1)
    morning_exist=False
    if ((data_use2_check.hms.values[0]=='09:15:00') | (data_use2_check.hms.values[0]=='09:45:00')):
        morning_exist=True
    
    if morning_exist==True:

        #below use fix point
        data_use2_morning=data_use2.iloc[a:b]   
        data_use2_afternoon1=data_use2.iloc[c:d]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]   
        high_afternoon=np.max(data_use2_afternoon1['High'].values)
        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'morning_exist':[morning_exist]})
    print(date_out)
    return output

temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=30,c=30,d=43))
#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['morning_exist']==True,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8



#check morning open and close time
check1=temp1[['Date2','Open1','High1','Low1','Close1','open_time1','close_time1']].copy()
check2=temp1[['Date2','Open2','High2','Low2','Close2','open_time2','close_time2']].copy()
check1=pd.merge(check1,check2[['Date2','open_time2','close_time2']].copy(),how='left',on=['Date2'])










##use morning as one of the factor
#temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
#temp1_morning=temp1_morning.rename(columns={'Open1':'Open_HSI','High1':'High_HSI',
#                                                            'Low1':'Low_HSI','Close1':'Close_HSI'})
#temp1_morning=temp1_morning.reset_index(drop=True)
#                        
##need to change a bit format to dt, because save to index_analsis
#temp1_morning['Date2']=temp1_morning['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#temp1_morning['DateNum']= (temp1_morning['Date2']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI_0_to_30.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_morning.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#writer.close()




#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                        
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)

temp1_afternoon.dtypes

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_30_to_43.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()

HSI_afternoon= read_excel('HSI_30_to_43.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_30_to_43_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#create dependent variable Y
hsi_y_afternoon=HSI_afternoon.loc[:,['Date2','DateNum','Open_HSI_afternoon','Close_HSI_afternoon']]
hsi_y_afternoon['Y_up']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon>=row.Open_HSI_afternoon)*1,axis=1)
hsi_y_afternoon['Y_down']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon<row.Open_HSI_afternoon)*1,axis=1)

writer = pd.ExcelWriter('hsi_y_30_to_43.xlsx', engine='xlsxwriter')
hsi_y_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()






































###############hsi_30_to_43 and 45_to_75#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'

os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session
#folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
folder_path=os.path.join(target_dir,"mis")

fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data_use.reset_index(drop=True)






a=0;b=13;c=15;d=45
def split_custom(data_use,a,b,c,d):
    data_use2=data_use.copy()
    date_out=data_use2['Date2'].values[0]
    #check whether morning exist
    data_use2_check=data_use2.head(1)
    morning_exist=False
    if ((data_use2_check.hms.values[0]=='09:15:00') | (data_use2_check.hms.values[0]=='09:45:00')):
        morning_exist=True
    
    if morning_exist==True:

        #below use fix point
        data_use2_morning=data_use2.iloc[a:b]   
        data_use2_afternoon1=data_use2.iloc[c:d]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]   
        high_afternoon=np.max(data_use2_afternoon1['High'].values)
        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'morning_exist':[morning_exist]})
    print(date_out)
    return output

#temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=13,c=15,d=45))
temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=30,b=43,c=45,d=75))
#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['morning_exist']==True,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8


#check morning open and close time
check1=temp1[['Date2','Open1','High1','Low1','Close1','open_time1','close_time1']].copy()
check2=temp1[['Date2','Open2','High2','Low2','Close2','open_time2','close_time2']].copy()
check1=pd.merge(check1,check2[['Date2','open_time2','close_time2']].copy(),how='left',on=['Date2'])










##use morning as one of the factor
#temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
#temp1_morning=temp1_morning.rename(columns={'Open1':'Open_HSI','High1':'High_HSI',
#                                                            'Low1':'Low_HSI','Close1':'Close_HSI'})
#temp1_morning=temp1_morning.reset_index(drop=True)
#                        
##need to change a bit format to dt, because save to index_analsis
#temp1_morning['Date2']=temp1_morning['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#temp1_morning['DateNum']= (temp1_morning['Date2']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI_30_to_43.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_morning.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#writer.close()




#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                        
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)

temp1_afternoon.dtypes

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_45_to_75.xlsx')
#output_path=os.path.join(target_dir,'HSI_15_to_30_cum.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





HSI_afternoon= read_excel('HSI_45_to_75.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_45_to_75_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#create dependent variable Y
hsi_y_afternoon=HSI_afternoon.loc[:,['Date2','DateNum','Open_HSI_afternoon','Close_HSI_afternoon']]
hsi_y_afternoon['Y_up']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon>=row.Open_HSI_afternoon)*1,axis=1)
hsi_y_afternoon['Y_down']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon<row.Open_HSI_afternoon)*1,axis=1)

writer = pd.ExcelWriter('hsi_y_45_to_75.xlsx', engine='xlsxwriter')
hsi_y_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


hsi_y_afternoon=pd.read_excel('hsi_y_45_to_75.xlsx','Sheet1')

hsi_y_x_afternoon=hsi_y_afternoon[['Date2','DateNum','Y_up','Y_down']].copy()





##########################hsi 45_to_75 factor##################################

#test break open impact
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()


hsi_y_temp['Close_HSI_lag1']=hsi_y_temp['Close_HSI'].shift(1)

hsi_y_temp['break_open']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])
hsi_y_temp['break_open']=hsi_y_temp['break_open'].fillna(0)

hsi_y_temp['break_open_percent']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])/hsi_y_temp['Close_HSI_lag1']
hsi_y_temp['break_open_percent']=hsi_y_temp['break_open_percent'].fillna(0)


hsi_y_temp.loc[hsi_y_temp['break_open_percent']>=0,'break_open_percent1']=hsi_y_temp['break_open_percent']
hsi_y_temp.loc[hsi_y_temp['break_open_percent']<0,'break_open_percent2']=hsi_y_temp['break_open_percent']

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_y_temp[['Date2','break_open_percent','break_open','break_open_percent1','break_open_percent2']],how='left',left_on=['Date2'],right_on=['Date2'])
hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)


hsi_y_x_afternoon['year_cohord']=hsi_y_x_afternoon['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)


target_variable='break_open_percent'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes









#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_0_to_13.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_0_to_13_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_0_to_13_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_0_to_13_change_indicator']=(hsi_morning['hsi_0_to_13_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_0_to_13_change',
                                                          'hsi_0_to_13_change_indicator',
                                                          'hsi_0_to_13_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])

del hsi_y_x_afternoon['Date']


target_variable='hsi_0_to_13_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_15_to_30.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_15_to_30_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_15_to_30_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_15_to_30_change_indicator']=(hsi_morning['hsi_15_to_30_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_15_to_30_change',
                                                          'hsi_15_to_30_change_indicator',
                                                          'hsi_15_to_30_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])
                
del hsi_y_x_afternoon['Date']

target_variable='hsi_15_to_30_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_30_to_43.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_30_to_43_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_30_to_43_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_30_to_43_change_indicator']=(hsi_morning['hsi_30_to_43_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_30_to_43_change',
                                                          'hsi_30_to_43_change_indicator',
                                                          'hsi_30_to_43_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])

del hsi_y_x_afternoon['Date']

target_variable='hsi_30_to_43_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes


len(set(list(hsi_y_x_afternoon.columns.values)))








#hsi morning change factorfrom 930 to 10:00
hsi_morning1=pd.read_excel(os.path.join(target_dir,'HSI_15_to_30.xlsx'),'Sheet1')
hsi_morning1['Date']=hsi_morning1['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
del hsi_morning1['Close']

hsi_morning2=pd.read_excel(os.path.join(target_dir,'HSI_30_to_43.xlsx'),'Sheet1')
hsi_morning2['Date']=hsi_morning2['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))

hsi_morning1=pd.merge(hsi_morning1,hsi_morning2[['Date','Close']].copy(),how='left',on=['Date'])
hsi_morning=hsi_morning1.copy()


hsi_morning['hsi_15_to_43_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_15_to_43_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_15_to_43_change_indicator']=(hsi_morning['hsi_15_to_43_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_15_to_43_change',
                                                          'hsi_15_to_43_change_indicator',
                                                          'hsi_15_to_43_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])


del hsi_y_x_afternoon['Date']

target_variable='hsi_15_to_43_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,10)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,90)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#full day prediction
full_day=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))
temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()

#temp=temp.loc[~pd.isnull(temp['Date2']),:]
#temp['Date2']=temp['Date2'].apply(lambda x:dt.strptime(x,"%m/%d/%Y").strftime("%Y-%m-%d"))

from pandas import read_excel
#this need to manually run all in sample fit for 2005 to 2010
in_sample_fitting=pd.read_excel(os.path.join(folder_path,'30013_test_2005_to_2010_insample_model2021.xlsx'),'daily_detail_summary')
in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()

in_sample_fitting=in_sample_fitting.append(temp)

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,in_sample_fitting[['Date2','up_prediction_prob','Y_up_predict']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

hsi_y_x_afternoon=hsi_y_x_afternoon.rename(columns={'up_prediction_prob':'full_prediction_prob',
                                                    'Y_up_predict':'full_prediction_indicate'})
hsi_y_x_afternoon=hsi_y_x_afternoon.loc[~pd.isnull(hsi_y_x_afternoon['full_prediction_prob']),:]



#['Date2','hsi_15_to_43_change','hsi_15_to_43_change_percentile','hsi_15_to_43_change_percentile_middle']



hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hsi_15_to_43_change']>=hsi_y_x_afternoon['third_percentile_hsi_15_to_43_change'])|
                      (hsi_y_x_afternoon['hsi_15_to_43_change']<=hsi_y_x_afternoon['first_percentile_hsi_15_to_43_change']),
                      'f20']=hsi_y_x_afternoon['hsi_15_to_43_change']

hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)

hsi_y_x_afternoon_check=hsi_y_x_afternoon.tail(500)










#random factor
dim=hsi_y_x_afternoon.shape[0]
for i in range(2,30,2):
    print(i)
    s=np.random.normal(0,1,dim)
    var1='random'+str(i)
    var2='random'+str(i-1)
    hsi_y_x_afternoon[var1]=s
    hsi_y_x_afternoon[var2]=s*-1







import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x_45_to_75.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_45_to_75_dataframe", hsi_y_x_afternoon, data_columns=hsi_y_x_afternoon.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x_45_to_75'+'.xlsx', engine='xlsxwriter')
hsi_y_x_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



































###############hsi_x_to_x and 45_to_165#########################
import os
import numpy as np
import requests
import zipfile
import io

#target_dir=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis'
target_dir='/home/jonahthonchan/Dropbox/ee/index_analysis'

os.chdir(target_dir)



from pandas import read_excel
from datetime import datetime as dt
from datetime import timedelta
import datetime
import pandas as pd
from time import sleep
import sys
import time




#seperate data into morning and afternoon session
#folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
folder_path=os.path.join(target_dir,"mis")

fn = os.path.join(folder_path,"FHSI_minute_20051201to_cum.hdf5")

#fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()


data_all_final_check=data_all_final.tail(4000)
data=data_all_final[['date_ymd_hms','date_ymd','Open','High','Low','Close','TotalVolume']].copy()
data['hms']=data['date_ymd_hms'].apply(lambda x: x.strftime('%H:%M:%S'))


data=data.rename(columns={'date_ymd_hms':'Date1','date_ymd':'Date2'})



data_use=data.loc[data['Date2']=='2015-01-02',:]
data_use=data.loc[data['Date2']=='2007-12-24',:]
data_use=data.loc[data['Date2']=='2020-11-25',:]
data_use=data.loc[data['Date2']=='2006-03-22',:]
data_use=data.loc[data['Date2']=='2008-06-25',:]
data_use=data.loc[data['Date2']=='2008-06-26',:]
data_use=data_use.reset_index(drop=True)






a=0;b=43;c=45;d=165
def split_custom(data_use,a,b,c,d):
    data_use2=data_use.copy()
    date_out=data_use2['Date2'].values[0]
    #check whether morning exist
    data_use2_check=data_use2.head(1)
    morning_exist=False
    if ((data_use2_check.hms.values[0]=='09:15:00') | (data_use2_check.hms.values[0]=='09:45:00')):
        morning_exist=True
    
    if morning_exist==True:

        #below use fix point
        data_use2_morning=data_use2.iloc[a:b]   
        data_use2_afternoon1=data_use2.iloc[c:d]    
        
        open_morning=data_use2_morning['Open'].values[0]     
        high_morning=np.max(data_use2_morning['High'].values)
        low_morning=np.min(data_use2_morning['Low'].values)
        close_morning=data_use2_morning['Close'].values[-1]    
        open_morning_time=data_use2_morning['Date1'].values[0] 
        close_morning_time=data_use2_morning['Date1'].values[-1]
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]   
        high_afternoon=np.max(data_use2_afternoon1['High'].values)
        low_afternoon=np.min(data_use2_afternoon1['Low'].values)
        close_afternoon=data_use2_afternoon1['Close'].values[-1]
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1]

        
    else:
        open_morning=0
        high_morning=0
        low_morning=0
        close_morning=0
        open_morning_time=0
        close_morning_time=0

        open_afternoon=0
        high_afternoon=0
        low_afternoon=0
        close_afternoon=0
        open_afternoon_time=0
        close_afternoon_time=0
        
    output=pd.DataFrame({'Date2':[date_out],
                         'Open1':[open_morning],
                         'High1':[high_morning],
                         'Low1':[low_morning],
                         'Close1':[close_morning],
                         'open_time1':[open_morning_time],
                         'close_time1':[close_morning_time],
                         'Open2':[open_afternoon],
                         'High2':[high_afternoon],
                         'Low2':[low_afternoon],
                         'Close2':[close_afternoon],
                         'open_time2':[open_afternoon_time],
                         'close_time2':[close_afternoon_time],
                         'morning_exist':[morning_exist]})
    print(date_out)
    return output

#temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=13,c=15,d=45))
temp1=data.groupby("Date2").apply(lambda x:split_custom(x.reset_index(drop=True),a=0,b=43,c=45,d=165))
#if ind_size==0, they are trading date with only morning or only afternoon session
#so remove it. in later pnl test, these case will use full day prediction
#here hsi afternoon only select trading date with both morning and afternoon
temp1=temp1.loc[temp1['morning_exist']==True,:]  
temp1['Open1']=temp1['Open1'].astype(int)
temp1['High1']=temp1['High1'].astype(int)
temp1['Low1']=temp1['Low1'].astype(int)
temp1['Close1']=temp1['Close1'].astype(int)
temp1['Open2']=temp1['Open2'].astype(int)
temp1['High2']=temp1['High2'].astype(int)
temp1['Low2']=temp1['Low2'].astype(int)
temp1['Close2']=temp1['Close2'].astype(int)

temp1=temp1.loc[temp1['Date2']!='2021-10-13',:].copy() #typhoon 8


#check morning open and close time
check1=temp1[['Date2','Open1','High1','Low1','Close1','open_time1','close_time1']].copy()
check2=temp1[['Date2','Open2','High2','Low2','Close2','open_time2','close_time2']].copy()
check1=pd.merge(check1,check2[['Date2','open_time2','close_time2']].copy(),how='left',on=['Date2'])










##use morning as one of the factor
#temp1_morning=temp1[['Date2','Open1','High1','Low1','Close1']].copy()
#temp1_morning=temp1_morning.rename(columns={'Open1':'Open_HSI','High1':'High_HSI',
#                                                            'Low1':'Low_HSI','Close1':'Close_HSI'})
#temp1_morning=temp1_morning.reset_index(drop=True)
#                        
##need to change a bit format to dt, because save to index_analsis
#temp1_morning['Date2']=temp1_morning['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
#temp1_morning['DateNum']= (temp1_morning['Date2']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
#
##also save to index_analsis
#output_path=os.path.join(target_dir,'HSI_30_to_43.xlsx')
#writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
#temp1_morning.to_excel(writer, sheet_name='Sheet1')
#writer.save()
#writer.close()




#use afternoon as Y
temp1_afternoon=temp1[['Date2','Open2','High2','Low2','Close2']].copy()
temp1_afternoon=temp1_afternoon.rename(columns={'Date2':'Date','Open2':'Open','High2':'High',
                                                           'Low2':'Low','Close2':'Close'})                        
temp1_afternoon=temp1_afternoon.reset_index(drop=True)      

temp1_afternoon['Date']=temp1_afternoon['Date'].apply(lambda x:dt.strptime(x,"%Y-%m-%d"))
temp1_afternoon['DateNum']= (temp1_afternoon['Date']-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)

temp1_afternoon.dtypes

#also save to index_analsis
output_path=os.path.join(target_dir,'HSI_45_to_165.xlsx')
#output_path=os.path.join(target_dir,'HSI_15_to_30_cum.xlsx')
writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
temp1_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





HSI_afternoon= read_excel('HSI_45_to_165.xlsx','Sheet1')
HSI_afternoon['Date2']=HSI_afternoon['Date'].dt.date
HSI_afternoon['Date2']=HSI_afternoon['Date2'].astype(str)

HSI_afternoon=HSI_afternoon.loc[~(np.isnan(HSI_afternoon.Open)|np.isnan(HSI_afternoon.Close)),:].reset_index(drop=True)
HSI_afternoon=HSI_afternoon.rename(columns={'Open':'Open_HSI_afternoon','High':'High_HSI_afternoon','Low':'Low_HSI_afternoon','Close':'Close_HSI_afternoon'})
HSI_afternoon=HSI_afternoon.loc[:,['Date2','Open_HSI_afternoon','High_HSI_afternoon','Low_HSI_afternoon','Close_HSI_afternoon']]


#make % change column
HSI_afternoon['HSI_afternoon_change']=(HSI_afternoon['Close_HSI_afternoon']-HSI_afternoon['Open_HSI_afternoon'])/HSI_afternoon['Open_HSI_afternoon']



#create DateNum
HSI_afternoon['Date3']=pd.to_datetime(HSI_afternoon['Date2'])#create a date with datetime format
HSI_afternoon['DateNum'] = (HSI_afternoon.Date3-dt(1970,1,1)).astype("timedelta64[D]").astype(np.int64)
HSI_afternoon=HSI_afternoon.reset_index(drop=True)
del HSI_afternoon['Date3']

#FCHI_check=FCHI.tail(100)
#remove duplicate if date2 are the same, but keep the first record
HSI_afternoon=HSI_afternoon.drop_duplicates(subset='Date2', keep="first")


writer = pd.ExcelWriter('HSI_45_to_165_with_tidy.xlsx', engine='xlsxwriter')
HSI_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()





#create dependent variable Y
hsi_y_afternoon=HSI_afternoon.loc[:,['Date2','DateNum','Open_HSI_afternoon','Close_HSI_afternoon']]
hsi_y_afternoon['Y_up']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon>=row.Open_HSI_afternoon)*1,axis=1)
hsi_y_afternoon['Y_down']=hsi_y_afternoon.apply(lambda row: (row.Close_HSI_afternoon<row.Open_HSI_afternoon)*1,axis=1)

writer = pd.ExcelWriter('hsi_y_45_to_165.xlsx', engine='xlsxwriter')
hsi_y_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()


hsi_y_afternoon=pd.read_excel('hsi_y_45_to_165.xlsx','Sheet1')

hsi_y_x_afternoon=hsi_y_afternoon[['Date2','DateNum','Y_up','Y_down']].copy()





##########################hsi 45_to_165 factor##################################

#test break open impact
hsi_y = read_excel('hsi_y.xlsx','Sheet1')
hsi_y_temp=hsi_y[['Date2','Open_HSI','Close_HSI']].copy()


hsi_y_temp['Close_HSI_lag1']=hsi_y_temp['Close_HSI'].shift(1)

hsi_y_temp['break_open']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])
hsi_y_temp['break_open']=hsi_y_temp['break_open'].fillna(0)

hsi_y_temp['break_open_percent']=(hsi_y_temp['Open_HSI']-hsi_y_temp['Close_HSI_lag1'])/hsi_y_temp['Close_HSI_lag1']
hsi_y_temp['break_open_percent']=hsi_y_temp['break_open_percent'].fillna(0)


hsi_y_temp.loc[hsi_y_temp['break_open_percent']>=0,'break_open_percent1']=hsi_y_temp['break_open_percent']
hsi_y_temp.loc[hsi_y_temp['break_open_percent']<0,'break_open_percent2']=hsi_y_temp['break_open_percent']

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_y_temp[['Date2','break_open_percent','break_open','break_open_percent1','break_open_percent2']],how='left',left_on=['Date2'],right_on=['Date2'])
hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)


hsi_y_x_afternoon['year_cohord']=hsi_y_x_afternoon['Date2'].apply(lambda x:dt.strptime(x,"%Y-%m-%d").strftime("%Y")).astype(int)


target_variable='break_open_percent'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes









#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_0_to_13.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_0_to_13_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_0_to_13_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_0_to_13_change_indicator']=(hsi_morning['hsi_0_to_13_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_0_to_13_change',
                                                          'hsi_0_to_13_change_indicator',
                                                          'hsi_0_to_13_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])

del hsi_y_x_afternoon['Date']


target_variable='hsi_0_to_13_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_15_to_30.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_15_to_30_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_15_to_30_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_15_to_30_change_indicator']=(hsi_morning['hsi_15_to_30_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_15_to_30_change',
                                                          'hsi_15_to_30_change_indicator',
                                                          'hsi_15_to_30_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])
                
del hsi_y_x_afternoon['Date']

target_variable='hsi_15_to_30_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#hsi morning change factor
hsi_morning=pd.read_excel(os.path.join(target_dir,'HSI_30_to_43.xlsx'),'Sheet1')
hsi_morning['Date']=hsi_morning['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
hsi_morning['hsi_30_to_43_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_30_to_43_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_30_to_43_change_indicator']=(hsi_morning['hsi_30_to_43_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_30_to_43_change',
                                                          'hsi_30_to_43_change_indicator',
                                                          'hsi_30_to_43_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])

del hsi_y_x_afternoon['Date']

target_variable='hsi_30_to_43_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    first2_percentile_capture=np.nanpercentile(data_use,40)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,60)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes


len(set(list(hsi_y_x_afternoon.columns.values)))








#hsi morning change factorfrom 930 to 10:00
hsi_morning1=pd.read_excel(os.path.join(target_dir,'HSI_15_to_30.xlsx'),'Sheet1')
hsi_morning1['Date']=hsi_morning1['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
del hsi_morning1['Close']

hsi_morning2=pd.read_excel(os.path.join(target_dir,'HSI_30_to_43.xlsx'),'Sheet1')
hsi_morning2['Date']=hsi_morning2['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))

hsi_morning1=pd.merge(hsi_morning1,hsi_morning2[['Date','Close']].copy(),how='left',on=['Date'])
hsi_morning=hsi_morning1.copy()


hsi_morning['hsi_15_to_43_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_15_to_43_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_15_to_43_change_indicator']=(hsi_morning['hsi_15_to_43_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_15_to_43_change',
                                                          'hsi_15_to_43_change_indicator',
                                                          'hsi_15_to_43_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])


del hsi_y_x_afternoon['Date']

target_variable='hsi_15_to_43_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,10)
    first2_percentile_capture=np.nanpercentile(data_use,30)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,70)
    third_percentile_capture=np.nanpercentile(data_use,90)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#full day prediction
full_day=pd.read_csv(os.path.join(folder_path,"all_prediction.csv"))




temp=full_day[['Date2','Y_up_predict','up_prediction_prob']].copy()

#temp=temp.loc[~pd.isnull(temp['Date2']),:]
#temp['Date2']=temp['Date2'].apply(lambda x:dt.strptime(x,"%m/%d/%Y").strftime("%Y-%m-%d"))

from pandas import read_excel
#this need to manually run all in sample fit for 2005 to 2010
in_sample_fitting=pd.read_excel(os.path.join(folder_path,'30013_test_2005_to_2010_insample_model2021.xlsx'),'daily_detail_summary')
in_sample_fitting=in_sample_fitting[['Date2','Y_up_predict','up_prediction_prob']].copy()

in_sample_fitting=in_sample_fitting.append(temp)

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,in_sample_fitting[['Date2','up_prediction_prob','Y_up_predict']].copy(),how='left',left_on=['Date2'],right_on=['Date2'])

hsi_y_x_afternoon=hsi_y_x_afternoon.rename(columns={'up_prediction_prob':'full_prediction_prob',
                                                    'Y_up_predict':'full_prediction_indicate'})
hsi_y_x_afternoon=hsi_y_x_afternoon.loc[~pd.isnull(hsi_y_x_afternoon['full_prediction_prob']),:]



#['Date2','hsi_15_to_43_change','hsi_15_to_43_change_percentile','hsi_15_to_43_change_percentile_middle']



hsi_y_x_afternoon.loc[((hsi_y_x_afternoon['hsi_15_to_43_change']>hsi_y_x_afternoon['third_percentile_hsi_15_to_43_change'])|
                      (hsi_y_x_afternoon['hsi_15_to_43_change']<hsi_y_x_afternoon['first_percentile_hsi_15_to_43_change']))&(hsi_y_x_afternoon['Date2']>='2007-01-01')
                      ,'f20']=hsi_y_x_afternoon['hsi_15_to_43_change']

hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)

hsi_y_x_afternoon_check=hsi_y_x_afternoon.tail(500)




del hsi_y_x_afternoon['f20']





#hsi morning change factorfrom 915 to 10:00
hsi_morning1=pd.read_excel(os.path.join(target_dir,'HSI_0_to_13.xlsx'),'Sheet1')
hsi_morning1['Date']=hsi_morning1['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))
del hsi_morning1['Close']

hsi_morning2=pd.read_excel(os.path.join(target_dir,'HSI_30_to_43.xlsx'),'Sheet1')
hsi_morning2['Date']=hsi_morning2['Date'].apply(lambda x:x.strftime("%Y-%m-%d"))

hsi_morning1=pd.merge(hsi_morning1,hsi_morning2[['Date','Close']].copy(),how='left',on=['Date'])
hsi_morning=hsi_morning1.copy()


hsi_morning['hsi_0_to_43_change_abs']=(hsi_morning['Close']-hsi_morning['Open'])
hsi_morning['hsi_0_to_43_change']=(hsi_morning['Close']-hsi_morning['Open'])/hsi_morning['Open']
hsi_morning['hsi_0_to_43_change_indicator']=(hsi_morning['hsi_0_to_43_change']>=0)*1

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,hsi_morning[['Date',
                                                          'hsi_0_to_43_change',
                                                          'hsi_0_to_43_change_indicator',
                                                          'hsi_0_to_43_change_abs']],how='left',left_on=['Date2'],right_on=['Date'])


del hsi_y_x_afternoon['Date']

target_variable='hsi_0_to_43_change'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2007]
yy=2010
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,10)
    first2_percentile_capture=np.nanpercentile(data_use,30)
    second_percentile_capture=np.nanpercentile(data_use,50)
    second2_percentile_capture=np.nanpercentile(data_use,70)
    third_percentile_capture=np.nanpercentile(data_use,90)
    t1='first_percentile_'+target_variable
    t12='first2_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t22='second2_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t12:[first2_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t22:[second2_percentile_capture],
                                                       t3:[third_percentile_capture]}))

hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes





hsi_y_x_afternoon.loc[((hsi_y_x_afternoon['hsi_0_to_43_change']>hsi_y_x_afternoon['third_percentile_hsi_0_to_43_change'])|
                      (hsi_y_x_afternoon['hsi_0_to_43_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_43_change']))&(hsi_y_x_afternoon['Date2']>='2007-01-01')
                      ,'f20']=hsi_y_x_afternoon['hsi_0_to_43_change']

hsi_y_x_afternoon=hsi_y_x_afternoon.fillna(0)



del hsi_y_x_afternoon['f20']








'hsi_30_to_43_change','hsi_30_to_43_change_percentile','hsi_30_to_43_change_percentile_middle'

'hsi_0_to_13_change','hsi_0_to_13_change_percentile','hsi_0_to_13_change_percentile_middle'


['Date2','break_open_percent_percentile','break_open_percent_percentile_middle','break_open_percent',
'hsi_15_to_30_change','hsi_15_to_30_change_percentile','hsi_15_to_30_change_percentile_middle',
'hsi_30_to_43_change','hsi_30_to_43_change_percentile','hsi_30_to_43_change_percentile_middle']


'hsi_15_to_43_change','hsi_15_to_43_change_percentile','hsi_15_to_43_change_percentile_middle'




['Date2','random1','random2','random3','random4','random5','random6','random7','random8',
'break_open_percent_percentile','break_open_percent_percentile_middle','break_open_percent',
'hsi_0_to_13_change','hsi_0_to_13_change_percentile','hsi_0_to_13_change_percentile_middle',
'hsi_15_to_30_change','hsi_15_to_30_change_percentile','hsi_15_to_30_change_percentile_middle',
'hsi_30_to_43_change','hsi_30_to_43_change_percentile','hsi_30_to_43_change_percentile_middle',
'hsi_15_to_43_change','hsi_15_to_43_change_percentile','hsi_15_to_43_change_percentile_middle',
'full_prediction_prob']








#read oi
oi_original= read_excel(os.path.join(target_dir,'hang_seng_oi'+'_with_tidy.xlsx'),'Sheet1')
oi_original['year']=oi_original['Date2'].apply(lambda x:int(x[0:4]))


oi_original=oi_original.sort_values(by='DateNum',ascending=False).reset_index(drop=True)

from pandas import read_excel

hsi_y = read_excel('hsi_y.xlsx','Sheet1')
oi_original=pd.merge(oi_original,hsi_y[['Date2','Open_HSI','Close_HSI']].copy(),
                      on=['Date2'],how='left')

#volume
HSIvolume_source=pd.read_excel(os.path.join(target_dir,'hang_seng_oi_volume_with_tidy.xlsx'),'Sheet1')
hsi_vol=HSIvolume_source.copy()
hsi_vol['year']=hsi_vol['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)

oi_original=pd.merge(oi_original,hsi_vol[['Date2','Close_hang_seng_oi_volume']].copy(),how='left',on=['Date2'])

#for settlement day and one day after it, hsi_vol has no values(removed the row), so in oi_original, it is nan, so remove it.
oi_original=oi_original.loc[~pd.isnull(oi_original['Close_hang_seng_oi_volume']),:]

oi_original['oi_over_volume']=(oi_original['Close_hang_seng_oi']-oi_original['Open_hang_seng_oi'])#/oi_original['Close_hang_seng_oi_volume']


oi_original['diff']=oi_original['Close_HSI']-oi_original['Open_HSI']
oi_original['diff_shift1']=oi_original['diff'].shift(-1)
oi_original['hang_seng_oi_change_shift1']=oi_original['oi_over_volume'].shift(-1)



hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,oi_original[['Date2','diff_shift1','hang_seng_oi_change','hang_seng_oi_change_shift1']],how='left',on=['Date2'])
hsi_y_x_afternoon['diff_shift1']=hsi_y_x_afternoon['diff_shift1'].fillna(0)
hsi_y_x_afternoon['hang_seng_oi_change_shift1']=hsi_y_x_afternoon['hang_seng_oi_change_shift1'].fillna(0)



target_variable='hang_seng_oi_change_shift1'
distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
distinct_year=[i for i in distinct_year if i >=2008]
yy=2013
percentile_cum=pd.DataFrame([])
for yy in distinct_year:
    #OI have value only when 2007
    data_use=hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['year_cohord']>=2007)&(hsi_y_x_afternoon['year_cohord']<yy),target_variable].values
    first_percentile_capture=np.nanpercentile(data_use,25)
    second_percentile_capture=np.nanpercentile(data_use,50)
    third_percentile_capture=np.nanpercentile(data_use,75)
    t1='first_percentile_'+target_variable
    t2='second_percentile_'+target_variable
    t3='third_percentile_'+target_variable
    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
                                                       t1:[first_percentile_capture],
                                                       t2:[second_percentile_capture],
                                                       t3:[third_percentile_capture]}))


hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
a_check=hsi_y_x_afternoon.tail(1000)

new_var=target_variable+'_percentile'
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
hsi_y_x_afternoon.dtypes






#hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=0)&#hsi_y_x_afternoon['third_percentile_break_open_percent'])&
#                      (hsi_y_x_afternoon['hang_seng_oi_change_shift1']>=0)&
#                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f13']=hsi_y_x_afternoon['hang_seng_oi_change_shift1']
#
#hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<0)&#hsi_y_x_afternoon['first_percentile_break_open_percent'])&
#                      (hsi_y_x_afternoon['hang_seng_oi_change_shift1']<0)&
#                      (hsi_y_x_afternoon['hsi_0_to_13_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f14']=hsi_y_x_afternoon['hang_seng_oi_change_shift1']
#
#hsi_y_x_afternoon['f13']=hsi_y_x_afternoon['f13'].fillna(0)
#hsi_y_x_afternoon['f14']=hsi_y_x_afternoon['f14'].fillna(0)



del hsi_y_x_afternoon['f13']
del hsi_y_x_afternoon['f14']



del hsi_y_x_afternoon['f15']
del hsi_y_x_afternoon['f16']



hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hang_seng_oi_change_shift1']>=hsi_y_x_afternoon['third_percentile_hang_seng_oi_change_shift1'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f13']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hang_seng_oi_change_shift1']>=hsi_y_x_afternoon['third_percentile_hang_seng_oi_change_shift1'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f14']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['f13']=hsi_y_x_afternoon['f13'].fillna(0)
hsi_y_x_afternoon['f14']=hsi_y_x_afternoon['f14'].fillna(0)


hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hang_seng_oi_change_shift1']>=hsi_y_x_afternoon['third_percentile_hang_seng_oi_change_shift1'])&
                      (hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent']),'f15']=hsi_y_x_afternoon['break_open_percent']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['hang_seng_oi_change_shift1']>=hsi_y_x_afternoon['third_percentile_hang_seng_oi_change_shift1'])&
                      (hsi_y_x_afternoon['break_open_percent']<hsi_y_x_afternoon['first_percentile_break_open_percent']),'f16']=hsi_y_x_afternoon['break_open_percent']

hsi_y_x_afternoon['f15']=hsi_y_x_afternoon['f15'].fillna(0)
hsi_y_x_afternoon['f16']=hsi_y_x_afternoon['f16'].fillna(0)







hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=0),'f13']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<0),'f14']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['f13']=hsi_y_x_afternoon['f13'].fillna(0)
hsi_y_x_afternoon['f14']=hsi_y_x_afternoon['f14'].fillna(0)





hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']>=hsi_y_x_afternoon['third_percentile_hsi_0_to_13_change']),'f13']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['first_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['third_percentile_break_open_percent'])&
                      (hsi_y_x_afternoon['hsi_0_to_13_change']<hsi_y_x_afternoon['first_percentile_hsi_0_to_13_change']),'f13']=hsi_y_x_afternoon['hsi_0_to_13_change']

hsi_y_x_afternoon['f13']=hsi_y_x_afternoon['f13'].fillna(0)









#random factor
dim=hsi_y_x_afternoon.shape[0]
for i in range(2,30,2):
    print(i)
    s=np.random.normal(0,1,dim)
    var1='random'+str(i)
    var2='random'+str(i-1)
    hsi_y_x_afternoon[var1]=s
    hsi_y_x_afternoon[var2]=s*-1




##merge temp factr
#tempf= read_excel(os.path.join(target_dir,'hsi_y_x_45_to_165_f0.xlsx'),'Sheet1')
#usef=['Date2','NUGT_change','ECB_cur_EURCNY_change','ECB_cur_EURUSD_change','3081.HK_change','USTREASURY_REALYIELD_7_change',
#      'USTREASURY_REALYIELD_5_change', 'USTREASURY_REALYIELD_20_change','VOT_change'] 
#
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,tempf[usef].copy(),how='left',on=['Date2'])
#usef.remove('Date2')




import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x_45_to_165.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_45_to_165_dataframe", hsi_y_x_afternoon, data_columns=hsi_y_x_afternoon.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x_45_to_165'+'.xlsx', engine='xlsxwriter')
hsi_y_x_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()



























##volume
#pc_ratio_source=pd.read_excel(os.path.join(target_dir,'pc_ratio_with_tidy.xlsx'),'Sheet1')
#pc_ratio=pc_ratio_source.copy()
#pc_ratio['year']=pc_ratio['Date2'].apply(lambda x: dt.strptime(x,'%Y-%m-%d').year)
#
#pc_ratio.dtypes
#
#pc_ratio['pc_ratio_change_shift1']=pc_ratio['pc_ratio_change'].shift(1)
#pc_ratio=pc_ratio.fillna(0)
#
#
#
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,pc_ratio[['Date2','pc_ratio_change_shift1']],how='left',on=['Date2'])
#hsi_y_x_afternoon['pc_ratio_change_shift1']=hsi_y_x_afternoon['pc_ratio_change_shift1'].fillna(0)
#
#
#
#target_variable='pc_ratio_change_shift1'
#distinct_year=hsi_y_x_afternoon['year_cohord'].unique()
#distinct_year=[i for i in distinct_year if i >=2007]
#yy=2010
#percentile_cum=pd.DataFrame([])
#for yy in distinct_year:
#    data_use=hsi_y_x_afternoon.loc[hsi_y_x_afternoon['year_cohord']<yy,target_variable].values
#    first_percentile_capture=np.nanpercentile(data_use,35)
#    second_percentile_capture=np.nanpercentile(data_use,50)
#    third_percentile_capture=np.nanpercentile(data_use,65)
#    t1='first_percentile_'+target_variable
#    t2='second_percentile_'+target_variable
#    t3='third_percentile_'+target_variable
#    percentile_cum=percentile_cum.append(pd.DataFrame({'year_cohord':[yy],
#                                                       t1:[first_percentile_capture],
#                                                       t2:[second_percentile_capture],
#                                                       t3:[third_percentile_capture]}))
#
#
#hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,percentile_cum,how='left',on=['year_cohord'])
#a_check=hsi_y_x_afternoon.tail(1000)
#
#new_var=target_variable+'_percentile'
#hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]<=hsi_y_x_afternoon[t1])|(hsi_y_x_afternoon[target_variable]>=hsi_y_x_afternoon[t3]),new_var]=hsi_y_x_afternoon[target_variable]
#hsi_y_x_afternoon.loc[(hsi_y_x_afternoon[target_variable]>hsi_y_x_afternoon[t1])&(hsi_y_x_afternoon[target_variable]<hsi_y_x_afternoon[t3]),new_var+'_middle']=hsi_y_x_afternoon[target_variable]
#hsi_y_x_afternoon[new_var]=hsi_y_x_afternoon[new_var].fillna(0)
#hsi_y_x_afternoon[new_var+'_middle']=hsi_y_x_afternoon[new_var+'_middle'].fillna(0)
#hsi_y_x_afternoon.dtypes

















'break_open_percent','hsi_0_to_13_change','0_to_13_prediction_prob','full_prediction_prob'

'break_open_percent_percentile','break_open_percent_percentile_middle'
'hsi_0_to_13_change_percentile','hsi_0_to_13_change_percentile_middle'
'break_first15_1','break_first15_2'
'full_correct','full_wrong'






#merge temp factr
tempf= read_excel(os.path.join(target_dir,'hsi_y_x_45_to_165_f0.xlsx'),'Sheet1')
usef=['Date2','IVOV_change','VOOG_change','VOOV_change','VTHR_change','VNQI_change','HK_XHKG_1299_wsj_change','VIOO_change','EFV_change','SPMB_change','EWG_change',
      'USTREASURY_REALYIELD_7_change','FDL_change','TNA_change','TAREX_change','VGSCX_change','VGSAX_change',
      'VGISX_change','MIJFX_change','FJSCX_change','HJPSX_change',
      'HJPNX_change','IVV_change',
      'SQQQ_change','TQQQ_change','STIP_change','AORD_change','AXJO_change','VO_change','SPY_change']
hsi_y_x_afternoon=pd.merge(hsi_y_x_afternoon,tempf[usef].copy(),how='left',on=['Date2'])
usef.remove('Date2')

#k='IVOV_change'
#for k in usef:
#    hsi_y_x_afternoon.loc[((hsi_y_x_afternoon['break_open_percent']<hsi_y_x_afternoon['first_percentile_break_open_percent'])|
#                      (hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent']))|(hsi_y_x_afternoon['Date2']<='2007-01-01'),k]=0
#
#
#    
#
#    
#hsi_y_x_afternoon2=hsi_y_x_afternoon.copy()
#    
#hsi_y_x_afternoon=hsi_y_x_afternoon2.copy()
#    
#    
#hsi_y_x_afternoon=hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']<=hsi_y_x_afternoon['first_percentile_break_open_percent'])|
#                      (hsi_y_x_afternoon['break_open_percent']>=hsi_y_x_afternoon['third_percentile_break_open_percent']),:].copy()
#
#hsi_y_x_afternoon=hsi_y_x_afternoon.reset_index(drop=True)
#
#
#
#hsi_y_x_afternoon=hsi_y_x_afternoon.loc[(hsi_y_x_afternoon['break_open_percent']>hsi_y_x_afternoon['first_percentile_break_open_percent'])&
#                      (hsi_y_x_afternoon['break_open_percent']<hsi_y_x_afternoon['third_percentile_break_open_percent']),:].copy()
#
#hsi_y_x_afternoon=hsi_y_x_afternoon.reset_index(drop=True)





import numpy as np
from pandas import HDFStore,DataFrame
store = pd.HDFStore("hsi_y_x_15_to_30.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("hsi_y_x_15_to_30_dataframe", hsi_y_x_afternoon, data_columns=hsi_y_x_afternoon.columns)
store.close()

writer = pd.ExcelWriter('hsi_y_x_15_to_30'+'.xlsx', engine='xlsxwriter')
hsi_y_x_afternoon.to_excel(writer, sheet_name='Sheet1')
writer.save()
writer.close()












































































































import sys
sys.exit("stop here")



#checn fhsi change and hsi change

from pandas import read_excel
from datetime import datetime as dt
import pandas as pd
import numpy as np
fhsi = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\FHSI20051104-20131209 Daily_investigate.xlsx','Sheet1')

fhsi['Date2']=fhsi['Date'].dt.date
fhsi['Date2']=fhsi['Date2'].astype(str)
fhsi['change_abs']=fhsi['Close']-fhsi['Open']


hsi = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\HSI_with_tidy.xlsx','Sheet1')

#hsi['Date2']=hsi['Date2'].dt.date
#hsi['Date2']=hsi['Date2'].astype(str)
hsi=hsi.loc[(hsi['Date2']>='2005-11-04')&(hsi['Date2']<='2013-12-09'),:]
hsi['change_abs']=hsi['Close_HSI']-hsi['Open_HSI']
hsi_with_fhsi=pd.merge(hsi,fhsi[['Date2','change_abs']],how='left',on='Date2')
hsi_with_fhsi['change_abs_x_sign']=np.sign(hsi_with_fhsi['change_abs_x'])
hsi_with_fhsi['change_abs_y_sign']=np.sign(hsi_with_fhsi['change_abs_y'])
hsi_with_fhsi['sign_not_match']=hsi_with_fhsi.apply(lambda row: row['change_abs_x_sign']!=row['change_abs_y_sign'],axis=1)
hsi_with_fhsi_not_match=hsi_with_fhsi.loc[hsi_with_fhsi['sign_not_match']==True,:]

















#check if two factors dataframe are equal
import os
os.chdir(r'C:\Users\jonahthonchan\Dropbox\ee\tensorflow-mnist-tutorial-master')
import math
import numpy as np
import pandas as pd
import sys
#read data
fn = r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hsi_y_x.hdf5'
store = pd.HDFStore(fn)
hsi_y_x= store.select('hsi_y_x_dataframe')
store.close()
hsi_y_x=hsi_y_x.reset_index(drop=True)

fn_old=r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\data_back_up_20171013\hsi_y_x.hdf5'
store = pd.HDFStore(fn_old)
hsi_y_x_old= store.select('hsi_y_x_dataframe')
store.close()
hsi_y_x_old=hsi_y_x_old.reset_index(drop=True)

from pandas import read_excel
import ast
data = read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\index_table_v2_for_test_backtest.xlsx','Sheet1')




#non ema factor
mode='' #_standard,_central,_normal
non_ema_factor=[data.Name_use_python[i]+'_change'+mode for i in range(0,len(data.symbol)) if (data.Merge_tgh[i]=='Yes')&(data.UseEMA[i]!='Yes')]
if 'HSI_change'+mode in non_ema_factor:
    non_ema_factor.remove('HSI_change'+mode)
#ema factor
ema_factor=['EMA_'+data.Name_use_python[i]+'_change'+mode for i in range(0,len(data.symbol)) if (data.Merge_tgh[i]=='Yes')&(data.UseEMA[i]=='Yes')]
#ema_factor=[]
#merge together
use_factor_list=non_ema_factor+ema_factor
#use_factor_list=[x+'_Close_direct' for x in use_list]
use_factor_list.insert(0,'Date2')



train_start='2005-10-28';train_end='2017-10-01'
x_all_temp=hsi_y_x_old.loc[:,use_factor_list] #select columns
x_all_old=x_all_temp.loc[(x_all_temp['Date2']>=train_start)&(x_all_temp['Date2']<=train_end),use_factor_list].reset_index(drop=True)

x_all_temp=hsi_y_x.loc[:,use_factor_list] #select columns
x_all=x_all_temp.loc[(x_all_temp['Date2']>=train_start)&(x_all_temp['Date2']<=train_end),use_factor_list].reset_index(drop=True)

use_factor_list_nodate=use_factor_list
use_factor_list_nodate.remove('Date2')
#check if row are different
i=use_factor_list[1]
for i in use_factor_list_nodate:
    x_all_old[i+'check']=round(x_all_old[i],5)-round(x_all[i],5)

factor1=use_factor_list_nodate[0]+'check'
factor2=use_factor_list_nodate[len(use_factor_list_nodate)-1]+'check'
x_all_old_np=x_all_old.loc[:,factor1:factor2].values
x_all_old_np_row_sum=np.sum(x_all_old_np,axis=1)

x_all_old['check_sum']=x_all_old_np_row_sum
x_all_old_not_equal=x_all_old.loc[x_all_old['check_sum']!=0,:]











###########hSI Minute data#################

#from 2007 to 2019 (but 2017 afterward is not reliable), it is from eliter
#effective is 20070131(HSI2007G)-20170728(HSI2017N)
from datetime import datetime as dt
import datetime
from datetime import timedelta
import os
 
folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
 
import pandas as pd
data_hsi_min=pd.read_csv(os.path.join(folder_path,"HSI_1Min","HSI_1Min.csv"),header=None)
data_hsi_min_0708=pd.read_csv(os.path.join(folder_path,"HSI_1Min","HSI_1Min_2007_2008.csv"),header=None)
data_hsi_min=data_hsi_min_0708.append(data_hsi_min)
 
data_hsi_min_0708_check=data_hsi_min_0708.head(30000)
 
data_hsi_min=data_hsi_min.rename(columns={0:'Date',1:'time',
                                          2:'asset',3:'symbol',
                                          4:'Open',5:'High',
                                          6:'Low',7:'Close'})
 
 
 
data_hsi_min=data_hsi_min.reset_index(drop=True)
data_hsi_min['Date']=data_hsi_min['Date'].astype(str)
data_hsi_min['time']=data_hsi_min['time'].astype(str)
data_hsi_min['time_len']=data_hsi_min['time'].apply(lambda x:len(x))
data_hsi_min.loc[data_hsi_min['time_len']==3,'time_digit_6']='0'+data_hsi_min['time']+'00'
data_hsi_min.loc[data_hsi_min['time_len']==4,'time_digit_6']=data_hsi_min['time']+'00'
 
data_hsi_min['time_digit_6_first2']=data_hsi_min['time_digit_6'].str[0:2]
data_hsi_min['time_digit_6_other4']=data_hsi_min['time_digit_6'].str[2:]
 
data_hsi_min_check=data_hsi_min.loc[data_hsi_min['Date']=='20070219',:]
 
#some data in kevin's data is 24:00:00, 24 is wrong, so need to remove it
data_hsi_min_remove=data_hsi_min.loc[(data_hsi_min['time_digit_6_first2']=='24'),:]
data_hsi_min=data_hsi_min.loc[~(data_hsi_min['time_digit_6_first2']=='24'),:]
 
#data_hsi_min_check=data_hsi_min.loc[(data_hsi_min['symbol']=='HSI2017U'),:]
#data_hsi_min_check2=data_hsi_min.loc[(data_hsi_min['Date']=='20171107'),:]
 
data_hsi_min['time_digit_6_edited']=data_hsi_min['time_digit_6_first2']+data_hsi_min['time_digit_6_other4']
 
 
data_hsi_min['Date_time']=data_hsi_min['Date']+':'+data_hsi_min['time_digit_6_edited']
 
 
 
 
 
 
#list(data_hsi_min.columns.values)
#data_hsi_min_check1=data_hsi_min.loc[data_hsi_min['symbol']=='HSI2019G',:]
#data_hsi_min_check2=data_hsi_min.loc[data_hsi_min['symbol']=='HSI2019F',:]
#data_hsi_min_check2=data_hsi_min.loc[data_hsi_min['symbol']=='HSI2013M',:]
#check_unique=data_hsi_min['symbol'].unique().tolist()
data_hsi_min_check1=data_hsi_min.loc[data_hsi_min['symbol']=='HSI2018J',:]
 
 
data_hsi_min['Date_ymd']=data_hsi_min['Date'].apply(lambda x:dt.strptime(x,"%Y%m%d"))
data_hsi_min['Date_hms']=data_hsi_min['time_digit_6_edited'].apply(lambda x:dt.strptime(x,"%H%M%S"))
data_hsi_min['Date2']=data_hsi_min['Date_ymd'].apply(lambda x:x.strftime("%Y-%m-%d"))
 
data_hsi_min['Date_ymd_hms']=data_hsi_min['Date_time'].apply(lambda x:dt.strptime(x,"%Y%m%d:%H%M%S"))
data_hsi_min['month_symbol']=data_hsi_min['symbol'].str[-1:]
data_hsi_min['symbol_year']=data_hsi_min['symbol'].str[3:7]
 
 
 
data_hsi_min=data_hsi_min.sort_values(by=['symbol_year','month_symbol','Date_ymd_hms'],ascending=[True,True,True])
data_hsi_min=data_hsi_min.reset_index(drop=True)
 
data_hsi_min_check=data_hsi_min.head(100000)
#data_hsi_min_check2=data_hsi_min.loc[(data_hsi_min['Date_hms']<=dt(1900,1,1,8,30,0))&(data_hsi_min['Date_hms']>=dt(1900,1,1,8,0,0)),:]
 
 
all_contract=data_hsi_min['symbol'].unique().tolist()
 
 
data_hsi_min_roll_over=pd.DataFrame()
 
#construct continued contract
i='HSI2011U'
last_day='2009-01-29'
 
for i in all_contract[0:147]:
    if i=='HSI2007F':
        data_hsi_min_temp=data_hsi_min.loc[data_hsi_min['symbol']==i,:].copy()
        data_hsi_min_roll_over=data_hsi_min_roll_over.append(data_hsi_min_temp[:-1])#need to remove last row becasue useless, it is at 30mins after settlement
    else:
        data_hsi_min_temp=data_hsi_min.loc[(data_hsi_min['symbol']==i)&(data_hsi_min['Date2']>last_day),:].copy()
 
        #28-09-2011 (HSI2011U), lasr two row is 1513, 1514, 1514 deleted above and same as hsi_y, so add back this row 
        if (i=='HSI2011U'):
            data_hsi_min_roll_over=data_hsi_min_roll_over.append(data_hsi_min_temp)
        else:
            data_hsi_min_roll_over=data_hsi_min_roll_over.append(data_hsi_min_temp[:-1])
    data_hsi_min_roll_over=data_hsi_min_roll_over.reset_index(drop=True)
    last_day=data_hsi_min_temp[-1:]['Date2'].values[0]
    print("finishded ",i)
 
data_hsi_min_roll_over_check2=data_hsi_min_roll_over.loc[data_hsi_min_roll_over['symbol']=='HSI2011U',:]
 
#data_hsi_min_temp=data_hsi_min.loc[(data_hsi_min['symbol']=='HSI2019J')&(data_hsi_min['Date2']>'2009-01-29'),:].copy()
 
 
 
 
#have a look on first and last row for each month
#check_last_two=pd.DataFrame()
#for i in all_contract[0:147]:
#    data_hsi_min_roll_over2_temp=data_hsi_min_roll_over.loc[data_hsi_min_roll_over['symbol']==i,:][0:1]
#    check_last_two=check_last_two.append(data_hsi_min_roll_over2_temp)
#    data_hsi_min_roll_over2_temp=data_hsi_min_roll_over.loc[data_hsi_min_roll_over['symbol']==i,:][-1:]
#    check_last_two=check_last_two.append(data_hsi_min_roll_over2_temp)
 
 
##effective is 20070131(HSI2007G)-20161229(HSI2017N)
data_effective_use=data_hsi_min_roll_over.loc[((data_hsi_min_roll_over['Date2']>='2007-01-31')&(data_hsi_min_roll_over['Date2']<='2017-07-28'))|(data_hsi_min_roll_over['Date2']=='2018-10-02'),:]
 
len(data_effective_use['Date2'].unique())
 
#adjust time, e.g. 8:15am to 9:15am
data_effective_use_check=data_effective_use.loc[data_effective_use['symbol']=='HSI2008H',:]
data_effective_use_check2=data_effective_use.loc[data_effective_use['symbol']=='HSI2016X',:]
#find date with 8:15
date_815=data_effective_use.loc[data_effective_use['Date_hms']==dt(1900,1,1,8,45,0),'Date2'].values
 
 
 
 
data_effective_use_check=data_effective_use.loc[data_effective_use['Date2']=='2016-11-07',:]
#for 05-11-2007(1129),03-11-2008(1129),02-11-2009(1129),08-11-2010(1129),07-11-2011(1059),05-11-2012(1059),04-11-2013(1059),03-11-2014(1059),02-11-2015(1059),07-11-2016(1059)
#only summer time in the morning, so need to only adjust the time in the morning.
special_group1=['2007-11-05','2008-11-03','2009-11-02','2010-11-08']
special_group2=['2011-11-07','2012-11-05','2013-11-04','2014-11-03','2015-11-02','2016-11-07']
 
 
 
 
x=data_effective_use.loc[data_effective_use['Date2']=='2007-11-05',:].reset_index(drop=True)
def adjust815n845_to_915(x):
    #because 20140916 open at noon, so 845,815 cannot find it out, so need to manually find out this date for adjustment
    if (x['Date_hms'][0]==dt(1900,1,1,8,45,0))|(x['Date_hms'][0]==dt(1900,1,1,8,15,0))|(x['Date2'][0]=='2014-09-16'):
        x['Date_ymd_hms_adjusted']=x['Date_ymd_hms'].apply(lambda x:x+timedelta(hours=1))
    else:
        x['Date_ymd_hms_adjusted']=x['Date_ymd_hms'].copy()
 
    if x['Date2'][0] in special_group1:
        x.loc[x['Date_hms']<=dt(1900,1,1,11,29,0),'Date_ymd_hms_adjusted']=x['Date_ymd_hms'].apply(lambda x:x+timedelta(hours=1))
        x.loc[x['Date_hms']>dt(1900,1,1,11,29,0),'Date_ymd_hms_adjusted']=x['Date_ymd_hms'].copy()
 
    if x['Date2'][0] in special_group2:
        x.loc[x['Date_hms']<=dt(1900,1,1,10,59,0),'Date_ymd_hms_adjusted']=x['Date_ymd_hms'].apply(lambda x:x+timedelta(hours=1))
        x.loc[x['Date_hms']>dt(1900,1,1,10,59,0),'Date_ymd_hms_adjusted']=x['Date_ymd_hms'].copy()
 
 
    x['Date_hms_adjusted_str']=x['Date_ymd_hms_adjusted'].apply(lambda x: x.strftime("%H:%M:%S"))
    x['Date_hms_adjusted']=x['Date_hms_adjusted_str'].apply(lambda x: dt.strptime(x,"%H:%M:%S"))
    x.loc[(x['Date_hms_adjusted']>=dt(1900,1,1,6,15,0))&(x['Date_hms_adjusted']<=dt(1900,1,1,16,40,0)),'day_future']=1
    x['day_future']=x['day_future'].fillna(0)
    return x
 
data_effective_use2=data_effective_use.groupby('Date2').apply(lambda x:adjust815n845_to_915(x.reset_index(drop=True)))
data_effective_use2=data_effective_use2.reset_index(drop=True)
 
data_effective_use2["year_adjusted"]=data_effective_use2['Date_ymd_hms_adjusted'].apply(lambda x:x.strftime("%Y"))
data_effective_use2['year_hms_adjusted']=data_effective_use2['year_adjusted']+"_"+data_effective_use2['Date_hms_adjusted_str']
 
 
data_effective_use2_check=data_effective_use2.loc[data_effective_use2['symbol']=='HSI2017N',:]
 
data_effective_use2_dayfuture=data_effective_use2.loc[data_effective_use2["day_future"]==1,:]
data_effective_use2_dayfuture=data_effective_use2_dayfuture.reset_index(drop=True)
 
 
 
#remove problematic rows 
#remove 12-02-2007, because lacking of data from 0945 to 0957
#remove 31-12-2009 last row, is 1430, but should be close at 1229, but the close at 1229 is 15 point diff from hsi_y
#remove 24-12-2012,31-12-2012,27-01-2017 last row 14:03, coz actual close is 1159(but close at 1159 and 1403 also the samw as hsi_Y). so delete or not also ok
#remove first row of 22-5-2013, which is 1059, but market open at 1200, note that open price of 1059 and 1200 also same as hsi_y
#28-08-2014,30-08-2016,30-03-2017 remove 1600
#remove row 1600 in 27-11-2008, 26-02-2009, there is 1600 row and 1630 row (last row deleted above), but 1359 close to hsi_y
#remove row 1600 in 25-02-2010,29-04-2010, there is 1600 row and 1615 row (last row deleted above), but 1600 still here. although 1615 price equal to hsi_y, but 1559 is also very close to hsi_y(1 point diff)
data_effective_use2_dayfuture=data_effective_use2_dayfuture.loc[~(data_effective_use2_dayfuture['Date2']=='2007-02-12'),:]
data_effective_use2_dayfuture=data_effective_use2_dayfuture.loc[~((data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2009,12,31,14,30,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2012,12,24,14,3,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2012,12,31,14,3,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2017,1,27,14,3,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2013,5,22,10,59,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2014,8,28,16,0,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2016,8,30,16,0,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2017,3,30,16,0,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2008,11,27,16,0,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2009,2,26,16,0,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2010,2,25,16,0,0))|
                                                                   (data_effective_use2_dayfuture['Date_ymd_hms_adjusted']==dt(2010,4,29,16,0,0))),:]
 
 
data_effective_use2_dayfuture=data_effective_use2_dayfuture.reset_index(drop=True)
 
 
 
 
 
 
 
 
 
 
date_distinct=data_effective_use2_dayfuture['Date2'].unique().tolist()
#have a look on first and last row of each day
check_first=pd.DataFrame()
for i in date_distinct:
    data_effective_use2_dayfuture_temp=data_effective_use2_dayfuture.loc[data_effective_use2_dayfuture['Date2']==i,:][0:1]
    check_first=check_first.append(data_effective_use2_dayfuture_temp)
    data_effective_use2_dayfuture_temp=data_effective_use2_dayfuture.loc[data_effective_use2_dayfuture['Date2']==i,:][-1:]
    check_first=check_first.append(data_effective_use2_dayfuture_temp)
    print("finished ",i)
 
check_first=check_first.reset_index(drop=True)
 
#frequency count
check_first_check=check_first.groupby(["year_hms_adjusted"]).size()
check_first_check=pd.DataFrame(check_first_check)
check_first_check['year_hms_adjusted']=check_first_check.index
check_first_check=check_first_check.rename(columns={0:'count'})
check_first_check_investigate=check_first_check[check_first_check['count']<=3]['year_hms_adjusted'].values.tolist()
 
 
#find all year problem
selection=check_first['year_hms_adjusted'].apply(lambda x:x in check_first_check_investigate)
selection_date2=check_first.loc[selection,'Date2'].values.tolist()
data_effective_use2_dayfuture_check=data_effective_use2_dayfuture[data_effective_use2_dayfuture.Date2.isin(selection_date2)]
 
data_effective_use2_dayfuture['Date_ymd_adjusted']=data_effective_use2_dayfuture['Date_ymd_hms_adjusted'].apply(lambda x: x.strftime("%Y-%m-%d"))
 
data_effective_use2_dayfuture=data_effective_use2_dayfuture.rename(columns={9:'TotalVolume'})
data_effective_use2_dayfuture_final=data_effective_use2_dayfuture[['Date_ymd_hms_adjusted','Date_ymd_adjusted','Date_hms_adjusted_str','Open','High','Low','Close','TotalVolume']].copy()
data_effective_use2_dayfuture_final=data_effective_use2_dayfuture_final.rename(columns={'Date_ymd_hms_adjusted':'date_ymd_hms','Date_ymd_adjusted':'date_ymd','Date_hms_adjusted_str':'date_hms'})

#20070219 only one row, so remove it
data_effective_use2_dayfuture_final=data_effective_use2_dayfuture_final.loc[~(data_effective_use2_dayfuture_final['date_ymd']=='2007-02-19'),:]
data_effective_use2_dayfuture_final=data_effective_use2_dayfuture_final.reset_index(drop=True)
 
#10-08-2007 close at 1444, but close price same as hsi_y, so keep it
#24-12-2007, 31-12-2007,06-02-2008, 24-12-2008,31-12,2008,24-12-2009,24-12-2010,31-12-2010,02-02-2011, close at 1229, ok
#31-12-2013,24-12-2014,31-12-2014,18-02-2015,24-12-2015,31-12-2015,30-01-2014 last is 1159, so ok
#25-06-2008,15-09-2009 open at 1330, but open same as hsi_y, so ok
#29-06-2011, last two is 1558(close at 22116) and 1614, 1614(22117) removed above, hsi_y same as 1614, but 1558 only 1 point diff so ok
#24-07-2012, 23-09-2013 open at 1200, same as hsi_y so ok
#30-05-2013 no 1559, but 1558 same as hsi_y, so ok
#16-09-2014 start at 1200, ok
 
#2007-02-19 only have one row, need to merge from other source
 
 
 
 
 
 
 
 
 
data_hsi_min_check=data_hsi_min.loc[data_hsi_min['Date']=='20070219',:]
data_effective_use2_dayfuture_check=data_effective_use2_dayfuture.loc[data_effective_use2_dayfuture['Date']=='201810012',:]
data_hsi_min_check=data_hsi_min.loc[data_hsi_min['symbol']=='HSI2016X',:]
 
 
data_effective_use2_dayfuture_check=data_effective_use2_dayfuture.loc[data_effective_use2_dayfuture['symbol']=='HSI2018V',:]
 

 
 
 
 
##write h5
#import numpy as np
#from pandas import HDFStore,DataFrame
#import pandas as pd
#os.chdir(folder_path)
#store = pd.HDFStore("fhsi_2005-20140313(edited version).hdf5", "w", complib=str("zlib"), complevel=5)
#store.put("fhsi_2005-20140313", data_20140313, data_columns=data_20140313.columns)
#store.close()
 
 
 
 
#read h5 of 2005 and 2006
fn = os.path.join(folder_path,"fhsi_2005-20140313(edited version).hdf5")
store = pd.HDFStore(fn)
print(store)
data_0506= store.select('fhsi_2005-20140313')
list(data_0506.columns.values)
store.close()
 
 
 
 
#effective is20051201 to 20070130(only this period is reliable)
data_0506=data_0506.loc[(data_0506['Date']>=dt(2005,12,1,0,0,0))&(data_0506['Date']<=dt(2007,1,30,0,0,0)),:]
data_0506['Date2']=data_0506['Date'].apply(lambda x: dt.strftime(x,"%Y-%m-%d"))
data_0506=data_0506.reset_index(drop=True)
 
 
#all minor 1min
data_0506['Time_str']=data_0506['Time'].apply(lambda x: str(x))
data_0506['date_ymd_hms_str']=data_0506['Date2']+" "+data_0506['Time_str']
data_0506['date_ymd_hms']=data_0506['date_ymd_hms_str'].apply(lambda x:dt.strptime(x,"%Y-%m-%d %H:%M:%S"))
data_0506['date_ymd_hms_revised']=data_0506['date_ymd_hms'].apply(lambda x:x-timedelta(minutes=1))
data_0506['date_ymd_revised']=data_0506['date_ymd_hms_revised'].apply(lambda x: x.strftime("%Y-%m-%d"))
data_0506['date_hms_revised']=data_0506['date_ymd_hms_revised'].apply(lambda x: x.strftime("%H:%M:%S"))
 
 
 
#REMOVE 2006-12-27 becasue only one hour data availabel
data_0506=data_0506.loc[~(data_0506['Date2']=='2006-12-27'),:]
data_0506=data_0506.loc[~(data_0506['date_ymd_hms_revised']==dt(2006,7,28,16,0,0)),:]
data_0506=data_0506.loc[~(data_0506['date_ymd_hms_revised']==dt(2006,5,29,16,0,0)),:]
#2005-12-29 only 1557 but close to hsi_Y
data_0506=data_0506.reset_index(drop=True)
 
check_last_two=pd.DataFrame()
i='2005-12-01'
for i in data_0506['Date2'].unique().tolist():
    data_0506_temp=data_0506.loc[data_0506['Date2']==i,:][0:1]
    check_last_two=check_last_two.append(data_0506_temp)
    data_0506_temp=data_0506.loc[data_0506['Date2']==i,:][-1:]
    check_last_two=check_last_two.append(data_0506_temp)
 
data_0506_final=data_0506[['date_ymd_hms_revised','date_ymd_revised','date_hms_revised','Open','High','Low','Close','TotalVolume']].copy()
data_0506_final=data_0506_final.rename(columns={'date_ymd_hms_revised':'date_ymd_hms','date_ymd_revised':'date_ymd','date_hms_revised':'date_hms'})
data_0506_final=data_0506_final.sort_values(by=['date_ymd_hms'],ascending=[True])
 
#list(data_0506.columns.values)
#
#
#data_0506.to_csv(os.path.join(folder_path,'HSI_1Min',"look2.csv"))
 
 
 
 
 
 
 
 
 
#read h5 of IB
import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
fn = os.path.join(folder_path,"ib_historical20170731.hdf5")
store = pd.HDFStore(fn)
print(store)
data_ib= store.select('ib_data')
 
store.close()
 
check_last_two=pd.DataFrame()
i='2019-03-27'
for i in data_ib['Date'].unique().tolist():
    data_ib_temp=data_ib.loc[data_ib['Date']==i,:][0:1]
    check_last_two=check_last_two.append(data_ib_temp)
    data_ib_temp=data_ib.loc[data_ib['Date']==i,:][-1:]
    check_last_two=check_last_two.append(data_ib_temp)
 
check_last_two['hms']=check_last_two['date'].apply(lambda x: dt.strftime(x,"%H:%M:%S"))
 
data_ib['date_hms']=data_ib['date'].apply(lambda x: dt.strftime(x,"%H:%M:%S"))
data_ib['date_ymd']=data_ib['date'].apply(lambda x: dt.strftime(x,"%Y-%m-%d"))
 
#20181002 hv problem need to merge from other source
 
data_ib_final=data_ib[['date','date_ymd','date_hms','open','high','low','close','volume']].copy()
data_ib_final=data_ib_final.rename(columns={'date':'date_ymd_hms','open':'Open','high':'High','low':'Low','close':'Close','volume':'TotalVolume'})
 
 
 
 
#combine three sources
data_all_final=data_0506_final.append(data_effective_use2_dayfuture_final)
data_all_final=data_all_final.append(data_ib_final)
data_all_final=data_all_final.reset_index(drop=True)
data_all_final=data_all_final.loc[data_all_final['date_ymd']<='2019-03-26',:]
data_all_final=data_all_final.reset_index(drop=True)
data_all_final_check=data_all_final.head(10)

data_all_final

#write h5
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
os.chdir(folder_path)
store = pd.HDFStore("FHSI_minute_20051201to20190326.hdf5", "w", complib=str("zlib"), complevel=5)
store.put("FHSI_minute", data_all_final, data_columns=data_all_final.columns)
store.close()


#read h5
import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime
fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()



check=data_all_final['date_ymd'].unique()
 
check2=data_all_final.head(10)
 
 
 
 
 
 
 
date_distinct=data_all_final['date_ymd'].unique().tolist()
#have a look on first and last row of each day
check_first=pd.DataFrame()
for i in date_distinct:
    data_all_final_temp=data_all_final.loc[data_all_final['date_ymd']==i,:][0:1]
    check_first=check_first.append(data_all_final_temp)
    data_all_final_temp=data_all_final.loc[data_all_final['date_ymd']==i,:][-1:]
    check_first=check_first.append(data_all_final_temp)
    print("finished ",i)
 
check_first=check_first.reset_index(drop=True)
 
 
 
x=check_first.loc[check_first['date_ymd']=='2005-12-01',:].reset_index(drop=True)
def find_open_close(x):
    date=x['date_ymd'].values[0]
    open_time=x['date_ymd_hms'].values[0]
    open_price=x['Open'].values[0]
    close_time=x['date_ymd_hms'].values[1]
    close_price=x['Close'].values[1]
    output=pd.Series([date,open_time,open_price,close_time,close_price])
    return output
 
check_first_daily=check_first.groupby(['date_ymd']).apply(lambda x:find_open_close(x.reset_index(drop=True)))
check_first_daily=check_first_daily.rename(columns={0:'Date',1:'open_time',2:'open_price',3:'close_time',4:'close_price'})    
 
 
 
 
from pandas import read_excel
hsi_y=read_excel(r'C:\Users\jonahthonchan\Dropbox\ee\index_analysis\hsi_y.xlsx','Sheet1')
hsi_y_compare=pd.merge(hsi_y,check_first_daily,how='left',left_on=['Date2'],right_on=['Date'])  

hsi_y_compare['open_diff']=hsi_y_compare['open_price']-hsi_y_compare['Open_HSI']

hsi_y_compare['close_diff']=hsi_y_compare['close_price']-hsi_y_compare['Close_HSI']

hsi_y_compare['HSI_Change']=hsi_y_compare['Close_HSI']-hsi_y_compare['Open_HSI']

hsi_y_compare['HSI_min_data_Change']=hsi_y_compare['close_price']-hsi_y_compare['open_price']

hsi_y_compare['change_Change']=hsi_y_compare['HSI_min_data_Change']-hsi_y_compare['HSI_Change']

hsi_y_compare['HSI_sign']=(hsi_y_compare['HSI_Change']>=0)*1

hsi_y_compare['HSI_min_sign']=(hsi_y_compare['HSI_min_data_Change']>=0)*1

hsi_y_compare['sign_not_equal']=(hsi_y_compare['HSI_sign']!=hsi_y_compare['HSI_min_sign'])*1

hsi_y_compare.to_csv(os.path.join(folder_path,'HSI_1Min',"compare2.csv"))








#read FHSI_minute_20051201to20190326.hdf5
import os
import numpy as np
from pandas import HDFStore,DataFrame
import pandas as pd
from datetime import datetime as dt
import datetime

folder_path=r"C:\Users\jonahthonchan\Dropbox\ee\index_analysis\mis"
fn = os.path.join(folder_path,"FHSI_minute_20051201to20190326.hdf5")
store = pd.HDFStore(fn)
print(store)
data_all_final= store.select('FHSI_minute')
 
store.close()














#check late open
data_use=data.loc[data['Date2']=='2007-12-24',:]
def split_check(data_use):
    output=pd.DataFrame([])
    data_use2=data_use.copy()
    data_use2['Date1_shift1']=data_use2['Date1'].shift(1)
    data_use2['time_diff']=data_use2['Date1']-data_use2['Date1_shift1']
    data_use2['time_diff_min']=data_use2['time_diff'].apply(lambda x:x.total_seconds()/60)

    date_out=data_use2['Date2'].values[0]

    ind=data_use2['time_diff_min']>=60
    ind=ind[ind==True]
    ind_size=len(ind)
    
    
    minute_threshold=0
    
    if ind_size==0:
        
        data_use2_afternoon1=data_use2
        
        
        open_afternoon=data_use2_afternoon1['Open'].values[0]  
        open_afternoon_time=data_use2_afternoon1['Date1'].values[0] 

        close_afternoon=data_use2_afternoon1['Close'].values[-1]  
        close_afternoon_time=data_use2_afternoon1['Date1'].values[-1] 
        
        output=pd.DataFrame({'Date2':[date_out],
                             'Open2':[open_afternoon],
                             'open_time2':[open_afternoon_time],
                             'close2':[close_afternoon],
                             'close_time2':[close_afternoon_time],
                             'ind_size':[ind_size]})
    print(date_out)
    
    return output

temp1=data.groupby("Date2").apply(lambda x:split_check(x.reset_index(drop=True)))
temp1=temp1.loc[temp1['open_time2']!=0,:]

temp1['time2']=temp1['open_time2'].apply(lambda x: x.strftime("%H:%M:%S"))


data_check=data.loc[(data['Date2']<='2009-12-31')&(data['Date2']>='2007-12-31'),:]








 
#from random import *
# 
#from datetime import datetime as dt
#import datetime
#from collections import OrderedDict
#import pandas as pd
#import numpy as np
# 
#import_file_name=r'C:\Users\jonahthon.chan\Desktop\python\hsi.csv'
#data=pd.read_csv(import_file_name)
#data['Date1']=data['Date Time'].apply(lambda x: dt.strptime(x,"%m/%d/%Y"))
#data['Date2']=data['Date Time.1'].apply(lambda x: dt.strptime(x,"%H:%M:%S"))
#data['year']=data['Date1'].apply(lambda x: int(x.strftime("%Y")))
#data['month']=data['Date1'].apply(lambda x: int(x.strftime("%m")))
#data['day']=data['Date1'].apply(lambda x: int(x.strftime("%d")))
#data['hour']=data['Date2'].apply(lambda x: int(x.strftime("%H")))
#data['min']=data['Date2'].apply(lambda x: int(x.strftime("%M")))
#data['sec']=data['Date2'].apply(lambda x: int(x.strftime("%S")))
#data['Date3']=data.apply(lambda row:dt(row['year'],row['month'],row['day'],row['hour'],row['min'],row['sec']),axis=1)
#data=data.rename(columns={'Last':'Close'})
# 
# 
#time_start=dt(2019,3,13,9,15,0)
# 
# 
#data['Date4']=data['Date3'].apply(lambda x:x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d"))
#del data['Date1'];del data['Date2']
#data=data.rename(columns={'Date3':'Date1','Date4':'Date2'})
##so Date1 is Ymd hms (dt) and Date2 is Ymd(string)
#data=data[['Date1','Date2','Open','High','Low','Close']].copy()
#data=data.sort_values(by=['Date1'],ascending=[True]).reset_index(drop=True)
# 
#original_guess=pd.DataFrame({'Date2':data['Date2'].unique().tolist(),'prediction':np.random.randint(0, 2, size=len(data['Date2'].unique())).tolist()})
# 
# 
# 
#morning_signal=0
#profit_target=200
#stop_level=100
#after_stop_target=100
#after_stop_stop=100
#date_use="2007-10-26"
#date_ymd_col_name='Date2'
#date_ymd_hms_col_name='Date1'
#second_stage_trade=True
# 
#def strategy1(data,date_use,date_ymd_col_name,date_ymd_hms_col_name,morning_signal,profit_target,stop_level,after_stop_target,after_stop_stop,second_stage_trade):
#    data_use=data.loc[data[date_ymd_col_name]==date_use,:].copy()
#    data_use=data_use.reset_index(drop=True)
# 
#    entry_price=data_use[0:1]['Open'][0]
#    exit_price=data_use[0:1]['Open'][0]
#    second_entry_price=999999
#    second_exit_price=999999
#    trigger_first_stop=False
#    trigger_second_stop=False
#    date_use_dt=dt.strptime(date_use,"%Y-%m-%d")
#    exit_time=dt(int(date_use_dt.strftime("%Y")),int(date_use_dt.strftime("%m")),int(date_use_dt.strftime("%d")),16,30,0)
#    achieve_profit=999999
#    achieve_stop=999999
#    achieve_profit2=999999
#    achieve_stop2=999999    
# 
#    if morning_signal==1:
#        #find when achieve profit target
#        data_use.loc[data_use['High']>=entry_price+profit_target,'indicate_profit']=1
#        data_use['indicate_profit']=data_use['indicate_profit'].fillna(0)
#        if sum(data_use['indicate_profit']==1)>0:
#            achieve_profit=data_use.index[data_use['indicate_profit']==1][0]
#        else:
#            achieve_profit=999999
# 
#        #find when achieve stop target        
#        data_use.loc[data_use['Low']<=entry_price-stop_level,'indicate_stop']=1
#        data_use['indicate_stop']=data_use['indicate_stop'].fillna(0)
#        if sum(data_use['indicate_stop']==1)>0:
#            achieve_stop=data_use.index[data_use['indicate_stop']==1][0]
#        else:
#            achieve_stop=999999
# 
#        #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#        if (achieve_profit==999999)&(achieve_stop==999999):
#            if exit_time in data_use[date_ymd_hms_col_name]:
#                exit_price=data_use.loc[data_use['Date1']==exit_time,'Close'].values[0]
#            else:
#                exit_price=data_use.loc[data_use['Date1']==max(data_use['Date1']),'Close'].values[0]
# 
# 
#        #case2 or case 5, second trade
#        if ((achieve_profit==999999)&(achieve_stop!=999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit>achieve_stop)):
#            trigger_first_stop=True
#            exit_price=entry_price-stop_level
# 
#        #case3 or case 4, exit at profit target
#        if ((achieve_profit!=999999)&(achieve_stop==999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit<achieve_stop)):
#            exit_price=entry_price+profit_target
# 
#        #case6, second trade
#        if (achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit==achieve_stop):
#            trigger_first_stop=True
#            exit_price=entry_price-stop_level
# 
#        if (trigger_first_stop==True)&(second_stage_trade==True):
#            data_use2=data_use[achieve_stop:].copy()  
#            data_use2=data_use2.reset_index(drop=True)
#            second_entry_price=entry_price-stop_level-1
# 
#            #find when achieve profit target
#            data_use2.loc[data_use2['Low']<=second_entry_price-after_stop_target,'indicate_profit2']=1
#            data_use2['indicate_profit2']=data_use2['indicate_profit2'].fillna(0)
#            if sum(data_use2['indicate_profit2']==1)>0:
#                achieve_profit2=data_use2.index[data_use2['indicate_profit2']==1][0]
#            else:
#                achieve_profit2=999999
# 
#            #find when achieve stop target        
#            data_use2.loc[data_use2['High']>=(second_entry_price+after_stop_stop),'indicate_stop2']=1
#            data_use2['indicate_stop2']=data_use2['indicate_stop2'].fillna(0)
#            if sum(data_use2['indicate_stop2']==1)>0:
#                achieve_stop2=data_use2.index[data_use2['indicate_stop2']==1][0]
#            else:
#                achieve_stop2=999999
# 
#            #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#            if (achieve_profit2==999999)&(achieve_stop2==999999):
#                if exit_time in data_use2[date_ymd_hms_col_name]:
#                    second_exit_price=data_use2.loc[data_use2['Date1']==exit_time,'Close'].values[0]
#                else:
#                    second_exit_price=data_use2.loc[data_use2['Date1']==max(data_use2['Date1']),'Close'].values[0]
# 
#            #case2 or case 5, second trade
#            if ((achieve_profit2==999999)&(achieve_stop2!=999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2>achieve_stop2)):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price+after_stop_stop
# 
#            #case3 or case 4, exit at profit target
#            if ((achieve_profit2!=999999)&(achieve_stop2==999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2<achieve_stop2)):
#                second_exit_price=second_entry_price-after_stop_target
# 
#            #case6, achieve_profit2==achieve_stop2, second trade
#            if (achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2==achieve_stop2):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price+after_stop_stop
# 
#    if morning_signal==0:
#        #find when achieve profit target
#        data_use.loc[data_use['Low']<=entry_price-profit_target,'indicate_profit']=1
#        data_use['indicate_profit']=data_use['indicate_profit'].fillna(0)
#        if sum(data_use['indicate_profit']==1)>0:
#            achieve_profit=data_use.index[data_use['indicate_profit']==1][0]
#        else:
#            achieve_profit=999999
# 
#        #find when achieve stop target        
#        data_use.loc[data_use['High']>=entry_price+stop_level,'indicate_stop']=1
#        data_use['indicate_stop']=data_use['indicate_stop'].fillna(0)
#        if sum(data_use['indicate_stop']==1)>0:
#            achieve_stop=data_use.index[data_use['indicate_stop']==1][0]
#        else:
#            achieve_stop=999999
# 
#        #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#        if (achieve_profit==999999)&(achieve_stop==999999):
#            if exit_time in data_use[date_ymd_hms_col_name]:
#                exit_price=data_use.loc[data_use['Date1']==exit_time,'Close'].values[0]
#            else:
#                exit_price=data_use.loc[data_use['Date1']==max(data_use['Date1']),'Close'].values[0]
# 
#        #case2 or case 5, second trade
#        if ((achieve_profit==999999)&(achieve_stop!=999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit>achieve_stop)):
#            trigger_first_stop=True
#            exit_price=entry_price+stop_level
# 
#        #case3 or case 4, exit at profit target
#        if ((achieve_profit!=999999)&(achieve_stop==999999))|((achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit<achieve_stop)):
#            exit_price=entry_price-profit_target
# 
#        #case6, second trade
#        if (achieve_profit!=999999)&(achieve_stop!=999999)&(achieve_profit==achieve_stop):
#            trigger_first_stop=True
#            exit_price=entry_price-stop_level
# 
#        if (trigger_first_stop==True)&(second_stage_trade==True):
#            data_use2=data_use[achieve_stop:].copy()
#            data_use2=data_use2.reset_index(drop=True)
#            second_entry_price=entry_price+stop_level+1
# 
#            #find when achieve profit target
#            data_use2.loc[data_use2['High']>=second_entry_price+after_stop_target,'indicate_profit2']=1
#            data_use2['indicate_profit2']=data_use2['indicate_profit2'].fillna(0)
#            if sum(data_use2['indicate_profit2']==1)>0:
#                achieve_profit2=data_use2.index[data_use2['indicate_profit2']==1][0]
#            else:
#                achieve_profit2=999999
# 
#            #find when achieve stop target        
#            data_use2.loc[data_use2['Low']<=(second_entry_price-after_stop_stop),'indicate_stop2']=1
#            data_use2['indicate_stop2']=data_use2['indicate_stop2'].fillna(0)
#            if sum(data_use2['indicate_stop2']==1)>0:
#                achieve_stop2=data_use2.index[data_use2['indicate_stop2']==1][0]
#            else:
#                achieve_stop2=999999
# 
#            #case1: achieve_profit=999999, achieve_stop=999999, leave at close
#            if (achieve_profit2==999999)&(achieve_stop2==999999):
#                if exit_time in data_use2[date_ymd_hms_col_name]:
#                    second_exit_price=data_use2.loc[data_use2['Date1']==exit_time,'Close'].values[0]
#                else:
#                    second_exit_price=data_use2.loc[data_use2['Date1']==max(data_use2['Date1']),'Close'].values[0]
# 
# 
#            #case2 or case 5, second trade
#            if ((achieve_profit2==999999)&(achieve_stop2!=999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2>achieve_stop2)):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price-after_stop_stop
# 
#            #case3 or case 4, exit at profit target
#            if ((achieve_profit2!=999999)&(achieve_stop2==999999))|((achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2<achieve_stop2)):
#                second_exit_price=second_entry_price+after_stop_target
# 
#            #case6, achieve_profit2==achieve_stop2, second trade
#            if (achieve_profit2!=999999)&(achieve_stop2!=999999)&(achieve_profit2==achieve_stop2):
#                trigger_second_stop=True
#                second_exit_price=second_entry_price-after_stop_stop
# 
#    output=pd.Series([date_use,morning_signal,entry_price,exit_price,trigger_first_stop,second_entry_price,second_exit_price,trigger_second_stop,
#                      profit_target,stop_level,after_stop_target,after_stop_stop,second_stage_trade,achieve_profit,achieve_stop,achieve_profit2,achieve_stop2])
#    return output
# 
# 
# 
# 
# 
# 
#import os
#parameter_df=pd.DataFrame(OrderedDict({'profit_target':     [200,200,150,150,100,100],
#                                       'stop_level'   :     [100,100,75,75,50,50],
#                                       'after_stop_target': [100,100,75,75,50,50],
#                                       'after_stop_stop':   [100,100,75,75,50,50],
#                                       'second_stage_trade':[True,True,True,True,True,True]}))
# 
#summary=pd.DataFrame()
# 
# 
#start_time=dt.now()
#i=30
#j=1
#for j in range(0,parameter_df.shape[0]):
#    parameter_df_use=parameter_df[j:j+1]
#    pt1=parameter_df_use['profit_target'].values[0]
#    st1=parameter_df_use['stop_level'].values[0]
#    pt2=parameter_df_use['after_stop_target'].values[0]
#    st2=parameter_df_use['after_stop_stop'].values[0]
#    second_stage_trade=parameter_df_use['second_stage_trade'].values[0]
# 
#    store_result=pd.DataFrame(columns=["Date","Prediction","entry_price","exit_price","trigger_first_stop",
#                                       "second_entry_price","second_exit_price","trigger_second_stop",
#                                       "profit_target","stop_level","after_stop_target","after_stop_stop","second_stage_trade",'achieve_profit','achieve_stop','achieve_profit2','achieve_stop2'])    
#    for i in range(0,original_guess.shape[0]):
#        row_use=original_guess[i:i+1]
#        temp=strategy1(data,row_use['Date2'].values[0],'Date2','Date1',row_use['prediction'].values[0],pt1,st1,pt2,st2,second_stage_trade)
#        temp=temp.values.reshape(1,temp.shape[0])
#        temp=pd.DataFrame(temp)
#        temp.columns=("Date","Prediction","entry_price","exit_price","trigger_first_stop","second_entry_price","second_exit_price",
#                        "trigger_second_stop","profit_target","stop_level","after_stop_target","after_stop_stop","second_stage_trade",'achieve_profit','achieve_stop','achieve_profit2','achieve_stop2')
#        store_result=store_result.append(temp)
# 
# 
#    store_result['year']=store_result['Date'].str[0:4]    
#    store_result['first_commission']=12
#    store_result.loc[store_result['second_entry_price']!=999999,'second_commission']=12
#    store_result.loc[store_result['second_entry_price']==999999,'second_commission']=0
#    store_result.loc[store_result['Prediction']==0,'Prediction']=-1
#    store_result['Prediction_second']=store_result['Prediction']*-1
#    store_result['pnl_first_trade']=(store_result['exit_price']-store_result['entry_price'])*store_result['Prediction']-store_result['first_commission']
#    store_result['pnl_second_trade']=(store_result['second_exit_price']-store_result['second_entry_price'])*store_result['Prediction_second']-store_result['second_commission']
#    store_result['pnl']=store_result['pnl_first_trade']+store_result['pnl_second_trade']
# 
#    file_name="hsi_investigate2_"+str(pt1)+"_"+str(st1)+"_"+str(pt2)+"_"+str(st2)+".csv"
#    save_path=os.path.join(r"C:\Users\jonahthon.chan\Desktop\yulong",file_name)
#    store_result.to_csv(save_path,index=False)
# 
#    def pnl_function(x):
#        year_name=x['year'].values[0]
#        x['Cum_pnl_peryear']=x['pnl'].cumsum()
#        MDD=max(np.maximum.accumulate(x['Cum_pnl_peryear']) - x['Cum_pnl_peryear'])
#        max_downside=min(x['Cum_pnl_peryear'])
#        final_cum_pnl=x['Cum_pnl_peryear'].values[-1]
#        accuracy=sum(x['pnl']>0)/x.shape[0]
#        return pd.Series([year_name,final_cum_pnl,MDD,max_downside,accuracy])
# 
#    temp=store_result.groupby(["year"]).apply(lambda x:pnl_function(x.reset_index(drop=True)))
#    temp.columns = ('year',"FinalCumPnl","MDD","MaxDownside","accuracy")
# 
#    temp['profit_target']=pt1
#    temp['stop_level']=st1
#    temp['after_stop_target']=pt2
#    temp['after_stop_stop']=st2
#    temp['second_stage_trade']=second_stage_trade
# 
#    summary=summary.append(temp)
#    save_path=os.path.join(r"C:\Users\jonahthon.chan\Desktop\yulong\summary_pnl.csv")
#    summary.to_csv(save_path,index=False)
# 
# 
#end_time=dt.now()
#total_time=(end_time-start_time).total_seconds()
#total_time
# 
# 
##store_result.to_csv(r"C:\Users\jonahthon.chan\Desktop\yulong\hsi_investigate2.csv",index=False)
# 
# 
# 
# 
##create HSI_with_tidy.xlsx
#
# 
#
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
#import numpy as np
#import matplotlib.pyplot as plt
#from matplotlib import dates, ticker
#import matplotlib as mpl
#from mpl_finance import candlestick_ohlc
# 
#mpl.style.use('default')
# 
# 
#data['Date1_string']=data['Date1'].apply(lambda x:x.strftime("%Y-%m-%d %H:%M:%S"))
#data_for_plot=data.loc[data['Date2']=='2007-10-22',['Date1_string','Open','High','Low','Close']].copy()
#data_for_plot['Open']=data_for_plot['Open'].astype(str)
#data_for_plot['High']=data_for_plot['High'].astype(str)
#data_for_plot['Low']=data_for_plot['Low'].astype(str)
#data_for_plot['Close']=data_for_plot['Close'].astype(str)
#data_for_plot=[tuple(r) for r in data_for_plot.values]
# 
#ohlc_data = []
# 
#for line in data_for_plot:
#    ohlc_data.append((dates.datestr2num(line[0]), np.float64(line[1]), np.float64(line[2]), np.float64(line[3]), np.float64(line[4])))
# 
#fig, ax1 = plt.subplots()
#candlestick_ohlc(ax1, ohlc_data, width = 0.5/(24*60), colorup = 'g', colordown = 'r', alpha = 0.8)
# 
#ax1.xaxis.set_major_formatter(dates.DateFormatter('%d/%m/%Y %H:%M'))
#ax1.xaxis.set_major_locator(ticker.MaxNLocator(10))
# 
#plt.xticks(rotation = 30)
#plt.grid()
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.title('Historical Data')
#plt.tight_layout()
#plt.show()
 
 
 
 
 









