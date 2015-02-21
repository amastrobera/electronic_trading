#! /usr/bin/python

from sys import argv
from parser import Parser
from rules import TradeRule
from match_maker import MatchMaker
from order_book import OrderBook

def main(a_argv):
	

    #part one: read files
    p = Parser()    
    market = p.ReadToDict(a_argv[0], a_argv[1])    
    orders = p.ReadToList(a_argv[2],a_argv[3])	
  
    #part two: create a rule and load the matchmaker    
    r = TradeRule()
    m = MatchMaker(r)
    execs = m.match(orders,market)
    
    #part three: make P&L
    b = OrderBook(execs)
    b.MakeExecReportByStock()
    b.Print()    
    

if __name__ == "__main__":
  if len(argv) <= 1:
    a_argv = ["data/sec.dat", "|", "data/req.dat", "|"]
  else:
    a_argv = argv[1:]
  main(a_argv)
