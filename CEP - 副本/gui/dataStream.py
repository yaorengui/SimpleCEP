# encoding: UTF-8
from threading import *
import urllib2
import time
class dataStream():
    def __init__(self):
        self.threadPool = []
        self.target = None
        pass

    def addStream(self,symbol):

        thread = streamThread()
        thread.setSymbol(symbol)
        thread.start()

        if self.target != None:
          thread.setTarget(self.target)

        self.threadPool.append(thread)
        pass

    def removeStream(self,symbol):
        pass

    def setTarget(self,value):

        self.target = value

    def printInfo(self,stockInfo):
        print stockInfo,'tt'
        pass

class streamThread(Thread):
    def run(self):
        self.target = None
        self.flag = True
        self.time = .001
        #self.symbol = None
        while True:
            while self.flag == True:
                data = self.getStockInfo(self.symbol)
                #print data
                self.target(data)
                time.sleep(self.time)

    def setFlag(self,value):
        self.flag = value
        pass

    def setTarget(self,value):
        #print value
        self.target = value
        pass

    def setSpeed(self,value):
        if(value>.001):
            self.time = value
        pass

    def setSymbol(self,value):
        self.symbol = value
        pass

    def getStockInfo(self,code):
        #根据url获取股票信息
        data = {}
        url = self.getUrlByCode(code)
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        stockStr = response.read()
        stockList = stockStr.split(',')
        if len(stockList) >= 4:
            data['id'] = code
            data['symbol'] = code
            data['openPrice'] = float(stockList[1])
            data['closePrice'] = float(stockList[2])
            data['lastPrice'] = float(stockList[3])
            data['hightestPrice'] = float(stockList[4])
            data['lowestPrice'] = float(stockList[5])
            #data['bidPrice1'] = float(stockList[6])
            #data['askPrice2'] = float(stockList[7])
            data['volume'] = float(stockList[8])
            data['turnOver'] = float(stockList[9])

            data['bidVolume1'] = float(stockList[10])
            data['bidPrice1'] = float(stockList[11])
            data['bidVolume2'] = float(stockList[12])
            data['bidPrice2'] = float(stockList[13])
            data['bidVolume3'] = float(stockList[14])
            data['bidPrice3'] = float(stockList[15])
            data['bidVolume4'] = float(stockList[16])
            data['bidPrice4'] = float(stockList[17])
            data['bidVolume5'] = float(stockList[18])
            data['bidPrice5'] = float(stockList[19])

            data['askVolume1'] = float(stockList[20])
            data['askPrice1'] = float(stockList[21])
            data['askVolume2'] = float(stockList[22])
            data['askPrice2'] = float(stockList[23])
            data['askVolume3'] = float(stockList[24])
            data['askPrice3'] = float(stockList[25])
            data['askVolume4'] = float(stockList[26])
            data['askPrice4'] = float(stockList[27])
            data['askVolume5'] = float(stockList[28])
            data['askPrice5'] = float(stockList[29])
            data['dateTime'] = str(stockList[30]) + str(stockList[31])

        return data
        pass
    def getUrlByCode(self,code):
        return 'http://hq.sinajs.cn/list='+str(code)



if __name__ =='__main__':
    stream = dataStream()
    stream.setTarget(stream.printInfo)
    stream.addStream('sh601006')
    stream.addStream('sh601007')

    pass