from collections import Counter
from xml.etree.ElementTree import parse
import csv
import sys

# Get the .csv file to strip data from
print 'Enter the .csv file you\'d like to use: ',
file = raw_input('')
f = open(file)
keys = []

# Convert .csv file to list of Dictionary items
data = list(csv.DictReader(f))

# Get sample of first List item so we can separate the 'keys' from the 'values' 
raw = data[0]
print '\nHere are the avialable KEYS from {0}\n'.format(file)


# Format the output to be in user friendly format
print '{:<30} {:<30}'.format('******* KEY *******', '******* EXAMPLE DATA *******')
for k, v in raw.iteritems():
    print '{:<30} {:<30}'.format(k, v)
    keys.append(k)
key = str(raw_input('\nSelect a KEY from one of the options found in {0}: '.format(file)))
while key not in keys:    
    if key.lower() == 'exit':
        sys.exit()
    else:
        print 'Please select a valid option'
        print '\nExample KEY is \'{0}\'\nType \'exit\' to quit'.format(keys[0])
        key = str(raw_input('\nSelect a KEY from one of the options found in {0}: '.format(file)))
else:
    pass

# Getting all items that match the 'key' you've selected from above
value = [hole[key] for hole in data]
tab = Counter(value)

# Showing the results in descending order  
count = len(tab)
num = raw_input('\nThere are {0} entries that match your query.\
  How many would you like to see? \n\n> '.format(count))
number = int(num)
l = tab.most_common(number)

# Convert returned List of Tuples to a Dictionary
d = dict(l)

# Iterate through the Dictionary to return values in a user friendly format
for k, v in d.iteritems():
    print '{0}: \'{1}\' has returned {2} results.'.format(key, k, v)
