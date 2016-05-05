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
        data.append(self.data1)
        data.append(self.data2)
        data.append(self.data3)

        data.append(self.data1)
        data.append(self.data2)
        data.append(self.data3)


        """保存数据对象到硬盘"""
        f = shelve.open(filename='data.vt',writeback=False)
        f['data'] = data
        f.close()