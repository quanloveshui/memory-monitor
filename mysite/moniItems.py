#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import inspect
import time
import json
import socket
import pymysql

class mon:
    def __init__(self):
        self.data = {}

    def getTime(self):
        return str(int(time.time()) + 8 * 3600)
        #return str(int(time.time()))

    def getHost(self):
        return socket.gethostname()

    def getLoadAvg(self):
        with open('/proc/loadavg') as load_open:
            a = load_open.read().split()[:3]
            return ','.join(a)
    
    def getMemTotal(self):
        with open('/proc/meminfo') as mem_open:
            a = int(mem_open.readline().split()[1])
            return a / 1024
    
    def getMemUsage(self, noBufferCache=True):
        if noBufferCache:
            with open('/proc/meminfo') as mem_open:
                T = int(mem_open.readline().split()[1])
                F = int(mem_open.readline().split()[1])
                B = int(mem_open.readline().split()[1])
                C = int(mem_open.readline().split()[1])
                return (T-F-B-C)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                a = int(mem_open.readline().split()[1]) - int(mem_open.readline().split()[1])
                return a / 1024
    
    def getMemFree(self, noBufferCache=True):
        if noBufferCache:
            with open('/proc/meminfo') as mem_open:
                T = int(mem_open.readline().split()[1])
                F = int(mem_open.readline().split()[1])
                B = int(mem_open.readline().split()[1])
                C = int(mem_open.readline().split()[1])
                return (F+B+C)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                mem_open.readline()
                a = int(mem_open.readline().split()[1])
                return a / 1024
    
    def runAllGet(self):
        #自动获取mon类里的所有getXXX方法，用XXX作为key，getXXX()的返回值作为value，构造字典
        for fun in inspect.getmembers(self, predicate=inspect.ismethod):
            if fun[0][:3] == 'get':
                self.data[fun[0][3:]] = fun[1]()
        return self.data

if __name__ == "__main__":
    while True:
        m = mon()
        data = m.runAllGet()
        print (data)
        db = pymysql.connect(host='192.168.149.129', port=3306, user='root', passwd='1qazXDR%', db='yunwei', charset='utf8')
        db.autocommit(True)
        c = db.cursor()
        sql = "INSERT INTO `stat` (`host`,`mem_free`,`mem_usage`,`mem_total`,`load_avg`,`time`) VALUES('%s', '%d', '%d', '%d', '%s', '%d')" % (data['Host'], data['MemFree'], data['MemUsage'], data['MemTotal'], data['LoadAvg'], int(data['Time']))
        ret = c.execute(sql)
        time.sleep(2)
        
