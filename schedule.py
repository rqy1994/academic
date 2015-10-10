# -*- coding: utf-8 -*-
__author__ = 'rqy'

import re
import login

schedule_url = 'http://202.118.201.228/academic/teacher/teachresource/roomschedule.jsdo'

def saveData(name,id):
    f = open('data.txt','a')
    f.write(name + ' ' + id + '\n')
    f.close()

def getData():
    #room_id = 1689,1801
    for i in range(1689,1801):
        room_data = {'aid':'353','buildingid':'1688','room':str(i),'Submit2':u'\u786e \u5b9a','whichweek':'-1','week':'1'}
        html = login.s.post(url = schedule_url,data = room_data)
        tmp  = re.search(r'<div>(.*?)</div>',html.text,re.S).group(1)
        room_name = re.search(r'2015秋西-新(.*?)( |（一体机） )教室时间占用维护'.decode('utf-8'),tmp,re.S).group(1)
        saveData(room_name,str(i))
        print room_name,i,tmp

login.loginAS()
getData()

