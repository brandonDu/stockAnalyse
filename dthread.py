import time 
import threading 
import dstock
import dtime
#
#
def timeThread(): 
    name=threading.current_thread().getName() 
    print(name+":线程启动......")
    a=dtime.get_now()['time']
    b='17:05:59'
    c = dtime.compareTime(a,b)
    while c:
        t = dtime.get_now()
        p = threading.Thread(target = co,name=t['time'])
        p.start()
        c = dtime.compareTime(a,b)
        time.sleep(300)
    input("press return to exit  ^_^")

#
def co(): 
    name=threading.current_thread().getName()
    print('{'+name+"}线程启动......")
   #dstock.get_stock('sz000829') -> dict
    print(dstock.get_stock('sz000829'))
    print('[ '+name+' ] 数据获取完成 !')

    


