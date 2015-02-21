

class Trade:

  def __init__(self,d_trader=None,d_side=None,d_stock=None,d_qty=None,d_price=None):
    print "new trade"
    self.__trader = d_trader
    self.__side = d_side
    self.__stock = d_stock
    self.__quantity = d_qty
    self.__price = d_price

  @property
  def trader(self):
    return self.__trader
  @property
  def side(self):
    return self.__side
  @property
  def stock(self):
    return self.__stock
  @property
  def quantity(self):
    return self.__quantity
  @property
  def price(self):
    return self.__price

  @trader.setter
  def trader(self,val):
    old = self.__trader
    self.__trader = val
    return (old != self.__trader)

  #and so on, all setter todo
  



