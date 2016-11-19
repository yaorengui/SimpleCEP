#encoding: UTF-8
import shelve
class dataSources():
    def __init__(self):
        self.data1 = {}
        self.data1['id'] = 'E1'
        self.data1['name'] = 'yao'
        self.data1['password']=123

        self.data2 = {}
        self.data2['id'] = 'E2'
        self.data2['name'] = 'yang'
        self.data2['password']=123

        self.data3 = {}
        self.data3['id'] = 'E1'
        self.data3['name'] = 'yang'
        self.data3['password']=123


        data = []
        #data.append(self.data1)
        #data.append(self.data2)
        #data.append(self.data3)

        #data.append(self.data1)
        #data.append(self.data2)
        #data.append(self.data3)

if __name__ =='__main__':
    print 'dfdfd'
    data = []
    f = shelve.open('../code/tickData.vt')
    print '2'
    if 'data' in f:
      print 'f'
      d = f['data']
      #print d.length
      for i in range(7):
        for j in range(10000):
          cc = d[i*10000+j]
          temp = {}
          temp['id'] = cc['InstrumentID']
          temp['HighestPrice'] = cc['HighestPrice']
          temp['LowestPrice']  = cc['LowestPrice']
          temp['OpenPrice'] = cc['OpenPrice']
          temp['ClosePrice'] = cc['ClosePrice']
          temp['TradingDay'] = cc['TradingDay']
          temp['LastPrice'] = cc['LastPrice']
          temp['InstrumentID']  = cc['InstrumentID']
          temp['Symbol'] = cc['InstrumentID']
          temp['LowerLimitPrice'] = cc['LowerLimitPrice']
          temp['UpperLimitPrice'] = cc['UpperLimitPrice']
          data.append(temp)
          #print i*10000+j
          #%print i*10000+j
          print temp['InstrumentID']
        #f1 = shelve.open(filename='../data/stock'+str(i)+'.vt',writeback=False)
        #f1['data'] = data
        #f1.close()
        #data = []
    f.close()