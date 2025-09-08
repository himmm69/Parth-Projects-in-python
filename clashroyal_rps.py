import random

def clashroyal():
 
 parth_deck = input('xbow, hogrider, e-golem,')
 daksh_choices = [ 'royal giant', 'golem', 'miner', ]
 daksh_deck = random.choice(daksh_choices)
 battle = {"parth" : parth_deck, "daksh" : daksh_deck}

 return battle

def checkbattle(parth, daksh):
 print(f" parth used {parth}, daksh used {daksh}")
 if parth == 'xbow' and daksh == 'miner':
   return "Parth wins by 1 crown"
 elif parth == 'xbow' and daksh == 'golem':
  return "Daksh wins by 3 crown hehehhah"
 elif parth == 'xbow' and daksh == 'royal giant':
  return "Daksh wins by 1 crown"
 
 elif parth == 'hogrider' and daksh == 'royal giant':
  return "Daksh wins"
 elif parth == 'hogrider' and daksh == 'golem':
  return "Parth wins by 1 crown "
 elif parth == 'hogrider' and daksh == 'miner':
  return "Parth wins in sudden death"
 
 elif parth == 'e-golem' and daksh == 'golem':
  return "Daksh wins"
 elif parth == 'e-golem' and daksh == 'miner':
  return "Parth wins by 3 crown hehehahah"
 elif parth == 'e-golem' and daksh == 'royal giant':
  return"Daksh wins by 1 crown" 
 
battle = clashroyal()
winstreak = checkbattle(battle["parth"], battle["daksh"])
print(winstreak)