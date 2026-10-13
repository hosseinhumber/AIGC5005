import os, sys
import json
from pathlib import Path

def Total(a,b ):
    unused = 5
    l = [1,2,3]
    if a == None:
        return b
    return a+b

def read(path, items = []):
    items.append(path)
    return   items

x = {'a':1,
  'b':2 }
print( Total(1,2) )
