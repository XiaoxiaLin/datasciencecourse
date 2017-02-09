def tryfloat(x):
    try:
        return float(x)
    except:
        return x
    
    
import numpy as np
class DataList(object):
    def __DataList__(self, datalist = []):
        self.data = datalist
        
        
    def read_csv(self, filename, has_header=False):
        self.header = []
        self.data = []
        with open(filename) as fp:
            lines = fp.readlines()

            if has_header:
                self.header = lines[0].split(",")

            for line in lines[int(has_header):]:                
                self.data.append(map(tryfloat, line.split(",")))

        return self
        
        
    def get_column(self, column):
        if not isfloat(column):
            column = self.header.index(column)

        return np.array([l[column] for l in self.data])

    
    def get_values(self):
        return np.array(self.data)