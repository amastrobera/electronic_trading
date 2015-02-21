from rules import Rule

class MatchMaker:

  """this class creates matches between a list and a map according to the criteria tbd by the user
     the list of request can be anything, and must be consistent with the Rules provided
     the map represents all available options, which can satisfy the request according to the Rules"""

  #constructor
  def __init__(self,rule):
    assert isinstance(rule,Rule)
    print "matchmaker created"
    self.__rule = rule

  #retuns the list of matches, according to the rules
  def match(self,req_list=[], choice_map={}):
    assert type(req_list) is list
    assert type(choice_map) is dict
    ret_list = []
    for request in req_list:
      ret_list.append(self.__rule.apply_rule(request,choice_map))
    return ret_list

