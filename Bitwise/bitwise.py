
# compute the category
categories = [3, 4]
computed = 0
for c in categories:
	computed = computed | (1<<c)
print 'computed category = '  + str(computed)

# check if a bit is set
val = 10
cat = 1
print "set" if val & (1<<cat) > 0 else "not set"

# does a movie contain any of these categories
pref = 3   # action/comedy
movie = 24  # a few good
print 'matches your pref' if movie & pref else ' does not match '




