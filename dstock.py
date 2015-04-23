# -*- coding: UTF-8 -*-
'''
Created on 2015/04/23
Author:duwb
Email: wenbindu@yeah.net
'''
#根据stock key获取当前的stock info。
#input: key -> str
#output: stock_information -> dict

import urllib.request

#get the string from api of sina for stock.
#input: key of the stock ->str
#return: string of the stock information ->str
def http_get(key):
    try:
        #key is the id of the stock
        #fe: sh600241
        url = 'http://hq.sinajs.cn/list='+key
        response = urllib.request.urlopen(url).read()
        text = response.decode('GBK')
        return text
    except Exception as e:
        return str(e)
#analyse the string of the return data from the api of the sina with the key.
#input:data -> str
#output:stock information -> list
def get_list(data):
    arr = data.split('"')
    #get the information in the complex string.
    stock_info = arr[1].split(',')    
    return stock_info

#map the values to the keys.
#input:arr of values ->list
#output:dict
def map_str(arr):
    arr_cn = ('name','todStarPri','yesEndPri','nowPri','todMaxPri','todMinPri',
              'nowBuyPri','nowSelPri','dealNum','dealMoney','buyOneNum','buyOnePri',
              'buyTwoNum','buyTwoPri','buyThrNum','buyThrPri','buyForNum',
              'buyForPri','buyFivNum','buyFivPri',
              'selOneNum','selOnePri','selTwoNum','selTwoPri','selThrNum',
              'selThrPri','selForNum','selForPri','selFivNum','selFivPri',
              'date','time','noMean')
    dictionary = dict(zip(arr_cn, arr))
    return dictionary
#the main function to line the functions.
#input: key of the stock -> str
#output: information ot the stock with sina api -> dict
def get_stock(key):
         data = http_get(key)
         text = get_list(data)
         dict_stock = map_str(text)
         return dict_stock








