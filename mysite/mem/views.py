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
    sql = "SELECT `time`,`mem_usage` FROM `stat`"
    cursor.execute(sql)
    row = cursor.fetchall()
    ones = [[i[0]*1000, i[1]] for i in row]
    data = json.dumps(ones)
    #return "%s(%s);" % (request.args.get('callback'), json.dumps(ones))  
    return HttpResponse(data)

def main(request):
    return render(request,'mon.html')


