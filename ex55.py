name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown.'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "Actually that's not too heavy."
print "he's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)

inches = int(input("Please enter the # of inches here: "))
centimeters = inches * 2.54
print "Entered number of %r inches is equal to %r centimeters" % (inches, centimeters)

pounds = int(input("Please enter the lbs: "))
kilograms = pounds / 2.2
print "Entered amount of %r pounds is equal to %r kilograms" % (pounds, kilograms)
