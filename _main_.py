# -*- coding: UTF-8 -*-
'''
Created on 2015/4/23
Author: duwb
Email: wenbindu@yeah.net
'''
#import the dstock.py and use the function to get the information of the single stock.
#dstock.get_stock(key) key->str
#return the dict of the stock.
import time
import dthread
import dstock
import threading
import dtime
import datetime


def _main_():
         
         startTime = '9:25:00'
         endTime = '16:30:59'
         nowTime = dtime.get_now()['time']
         timeS=datetime.datetime.strptime(startTime,'%H:%M:%S')
         timeE=datetime.datetime.strptime(endTime,'%H:%M:%S')
         timeN=datetime.datetime.strptime(nowTime,'%H:%M:%S')
         timeY = datetime.datetime.strptime('23:59:59','%H:%M:%S')
         timeD = datetime.datetime.strptime('0:00:00','%H:%M:%S')
         if dtime.compareTime(nowTime,startTime):
                  t = (timeS-timeN).seconds
         elif dtime.compareTime(endTime,nowTime):
                  t = (timeY-timeN).seconds+(timeS-timeD).seconds                  
         else:
                  t=0
         print(t)
         time.sleep(t)

         p=threading.Thread(target=dthread.timeThread,name="计时线程") 
         p.start()


_main_()
