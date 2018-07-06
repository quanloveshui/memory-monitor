from django.shortcuts import render
import pymysql,json
from django.http import HttpResponse
from pyecharts import Line
from django.template import loader

tmp = 0

def getdata(request):
    global tmp
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1qazXDR%', db='yunwei', charset='utf8')
    cursor = conn.cursor()
    if tmp > 0:
        sql = "select `time`,`mem_usage` FROM `stat`  where time > %s" % (tmp/1000)
    else:
        sql = "SELECT `time`,`mem_usage` FROM `stat`"
    cursor.execute(sql)
    arr = []
    row = cursor.fetchall()
    ones = [[i[0]*1000, i[1]] for i in row]
    for i in ones:
        arr.append(i)
    if len(arr)>0:
        tmp=arr[-1][0]
    data = json.dumps(arr)
    #print(data1)
    return HttpResponse(data)
    #return render(request,'index.html',{'data':data})
    #return render(request,'index.html')

def main(request):
    return render(request,'mon.html')


