import hashmap

states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

cities = hashmap.new()
hashmap.set(cities, 'CA', 'San Fran')
hashmap.set(cities, 'MI', 'Detroit')
hashmap.set(cities, 'FL', 'Jacksonville')

hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

print '_' * 10
print "NY state has: %s" % hashmap.get(cities, 'NY')
print "OR state has %s" % hashmap.get(cities, 'OR')

print '_' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')

print '_' * 10
print "Michigan has %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))

print '_' * 10
hashmap.list(states)

print '_' * 10
hashmap.list(cities)

print '_' * 10
state = hashmap.get(states, 'Texas')

if not state:
  print "sorry, no Texas."
  
print "The city for the state 'TX' is: %s" % hashmap.get(cities, 'TX', 'Does Not Exist')
