# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 18:28:19 2019

@author: PERSO
"""

import statistics
import random
def main():
    
  text = input ("entrer une chaine de la forme (mot1/mot2/...../motN)").split("/")
  print(text)
  random.shuffle(text)
  if len(text)<=10:
      print(text[0:10])
     
        
      
       ##   print(text[text.len() -4:text.length()-1])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    main()
     