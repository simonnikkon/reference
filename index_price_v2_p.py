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



