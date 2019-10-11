# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:37:38 2019

@author: PERSO
"""

import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

record = open(sys.argv[1]) # this read input, given by instructor

def mapper(record):
 key = record[1] # assign order_id from each record as key
 value = list(record) # assign whole record as value for each key
 mr.emit_intermediate(key, value) # emit key-value pairs

def reducer(key, value):
    new_dict = {} # create dict to keep track of records
    if not key in new_dict:
        new_dict[key] = value
    else:
        new_dict[key].extend(value)
    for key in new_dict:
        if len(new_dict[key]) == 27:
            mr.emit(new_dict[key])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)