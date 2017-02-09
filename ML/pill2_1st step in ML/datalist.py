import numpy as np

def is_number(x):
    try:
        return float(x)
    except ValueError:
        return x
    

def isfloat(x):
    try:
        float(x)
        return True
    except:
        return False


class DataList(object):

    def __DataList__(self, datalist = []):
        self.data = datalist
    
    def read_csv(self, filename, has_header=False):
        def is_number(x):
            try:
                return float(x)
            except ValueError:
               return x
     
        self.header = []
        self.data = []
        with open(filename) as fp:
            lines = fp.readlines()
            if has_header:
                self.header = lines[0].split(",")
            for line in lines[int(has_header):]:                
                self.data.append(map(is_number, line.split(",")))
        return self

        
    def get_column(self, column):
        if not isfloat(column):
            column = self.header.index(column)
            
        return np.array([l[column] for l in self.data])
    
    def get_values(self):
        return np.array(self.data)
