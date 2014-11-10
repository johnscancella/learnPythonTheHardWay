directions = ["north", "south", "east", "west"]
verbs = ["go", "kill", "eat"]
stops = ["the", "in", "of"]
nouns = ["bear", "princess"]



def scan(string):
  return_list = []
  words = string.split(' ')
  
  for word in words:
    try:
      return_list.append(('number', int(word)))
    except ValueError:
      if word in directions:
        return_list.append(('direction', word))
      elif word in verbs:
        return_list.append(('verb', word))
      elif word in stops:
        return_list.append(('stop', word))
      elif word in nouns:
        return_list.append(('noun', word))
      else:
        return_list.append(('error', word))
  
  return return_list
