
class OrderBook:

  def __init__(self,execs=[]):
    assert type(execs) is list
    self.__header=""
    self.__sub_header=""
    self.__execs = execs    
    self.__dict={}

  def AddExec(self,exect=()):
    assert type(exect) is tuple
    old = len(self.__execs)
    if exect is not ():
      self.__execs.append(exect)
    return (len(self.__execs) > old)

  def MakeExecReportByStock(self):
    self.__header = "Stock : "
    self.__sub_header = "\tTrader\tSide\tPrice\tShares"    
    for trd in self.__execs:
      if trd is ():
        continue
      stock = trd[2]
      trader = trd[0]
      side = trd[1]
      qty = trd[3]
      prc = trd[4]
      rec = (trader,side,prc,qty)
      if stock not in self.__dict:  
        self.__dict[stock] = []
      self.__dict[stock].append(rec)

  def Print(self):
    for k in self.__dict.keys():
      print ""
      print self.__header + str(k)
      print self.__sub_header
      for elem in self.__dict[k]:
        st = "\t"
        for e in elem:
          st += str(e) + "\t"
        print st
