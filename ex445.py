import hashmap
# create a mapping of state abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities,'CA', 'San Francisco' )
hashmap.set(cities,'MI', 'Detroit')
hashmap.set(cities,'FL', 'Jacksonville')


# add some cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

#print out some cities
print '-' * 10
print "NY state has: %s" % hashmap.get(cities, 'NY')
print "OR state has: %s" % hashmap.get(cities, 'OR')

#print states
print '-' * 10
print "Michigan's abbreviation is: %s" % hashmap.get(states, 'Michigan')
print "Florida's abbreviation is: %s" % hashmap.get(states, 'Florida')


#states then cities
print '-' * 10
print "Michigian has: %s" % hashmap.get(cities, hashmap.get(states, 'Michigan'))
print "Florida has: %s" % hashmap.get(cities, hashmap.get(states, 'Florida'))


#every state abbreviation
print '-' * 10
hashmap.list(states)
#every city in state
print '-' * 10
hashmap.list(cities)


state = hashmap.get(states, 'Texas')

if not state:
    print "Sorry, no Texas"
#get city w/ a default value
city = hashmap.get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city
