# -*- coding: UTF-8 -*-
'''
Created on 2015/4/23
Author: duwb
Email: wenbindu@yeah.net
'''
#run the function every 5 minutes or other time.

import datetime
import threading



##def runInterval():
##         t=threading.Timer(seconds,runInterval())
##         t.start()
##         print('nihao')
##         if compareTime():
##                 t.cancel()

def compareTime(a,b):        
         time_a = datetime.datetime.strptime(a,'%H:%M:%S')
         time_b = datetime.datetime.strptime(b,'%H:%M:%S')
         return time_a < time_b
     


 a=get_now()['time']
 b='15:05:01'


def get_now():
         now = datetime.datetime.now()
         date = now.strftime('%Y-%m-%d')
         time =  now.strftime('%H:%M:%S')
         week = now.isocalendar()
         year = week[0]
         week_num = week[1]
         week_day = week[2]
         dic = {}
         dic['date']=date
         dic['time']=time
         dic['weekNum']=week_num
         dic['weekDay']=week_day
         dic['year']=year

         return dic
