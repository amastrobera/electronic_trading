

class Rule:

  def __init__(self):
    print "rule created"
  #  what would be the best way to abstract this class ?

  def apply_rule(self,arg1,arg2):
    pass #virtual function tbd in the child classes
 

class TradeRule(Rule): #inherits from Rule
  
  """ 1) order = tuple(trader,buy/sell,stock,qty,price)
      2) market = dict { stock, price  } 
      3) exec_trd = tuple(trader,buy/sell,stock,qty,price)"""

  def __init__(self):
      Rule.__init__(self)

  def __valid_trd(self, order=(), market={}):
    assert type(order) is tuple
    assert type(market) is dict
    if order == () or market == {}:
      print "null order, or null market provided"
      return False
    else:
      stock = order[2]
      if stock not in market:
        print "stock " + str(stock) + " not available on the market"
        return False
      price = float(order[4])
      market_price = float(market[stock][0])
      side = order[1]      
      if side == "B":
        if price >= market_price:
          return True
        else:
          print "trade invalid: buy " + str(stock) + " for " + str(price) + " vs market " + str(market_price)
          return False
      elif side == "S":
        if price <= market_price:
          return True
        else:
          print "trade invalid: sell " + str(stock) + " for " + str(price) + " vs market " + str(market_price)
          return False
      else:
        print "trade side not valid : " + str(side)
        return False
        
  def apply_rule(self,order=(),market={}):
    if self.__valid_trd(order, market) is True:
      price = float(order[4])
      mkt_price = float(market[order[2]][0])
      trd_price = round((price + mkt_price) / 2.,2)
      return (order[0],order[1],order[2],order[3],trd_price)
    else:
      print "exec failed on : " + str(order)
      return ()
