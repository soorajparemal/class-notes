#first method
newlist = sorted(list_to_be_sorted, key=lambda k: k['name']) 

#second method
from operator import itemgetter
newlist = sorted(list_to_be_sorted, key=itemgetter('name')) 
