# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:40:59 2019

@author: PERSO
"""

#!/usr/bin/env python
  
import sys
  
# maps words to their counts
foundKey = ""
foundValue = ""
isFirst = 1
currentCount = 0
currentCountry2digit = "-1"
currentCountryName = "-1"
isCountryMappingLine = False
 
# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
     
    try:
        # parse the input we got from mapper.py
        tel,nom,prenom,dept,ville,dept2 = line.split('^')
        """ 
        #the first line should be a mapping line, otherwise we need to set the currentCountryName to not known
        if personName == "-1": #this is a new country which may or may not have people in it
            currentCountryName = countryName
            currentCountry2digit = country2digit
            isCountryMappingLine = True
        else:
            isCountryMappingLine = False # this is a person we want to count
         
        if not isCountryMappingLine: #we only want to count people but use the country line to get the right name
 
            #first check to see if the 2digit country info matches up, might be unkown country
            if currentCountry2digit != country2digit:
                currentCountry2digit = country2digit
                currentCountryName = '%s - Unkown Country' % currentCountry2digit
             
            currentKey = '%s\t%s' % (currentCountryName,personType)
             
            if foundKey != currentKey: #new combo of keys to count
                if isFirst == 0:
                    print '%s\t%s' % (foundKey,currentCount)
                    currentCount = 0 #reset the count
                else:
                    isFirst = 0
             
                foundKey = currentKey #make the found key what we see so when we loop again can see if we increment or print out
             
            currentCount += 1 # we increment anything not in the map list
    except:
        pass
 
try:
    print '%s\t%s' % (foundKey,currentCount)
except:
    pass







############cat customers.dat countries.dat|./smplMapper.py|sort|./smplReducer.py
    ##### algorithme:::: on a envoyer les donnees sen arrageant de sorte que le numero de télephone sorte en premier okkkk
    ###### on sait que la taille des deux enregistrements sont differentes mais on a remplacé par des -1, ce quon peut faire
    #### on regarde si les numeros de telephone sont les memes , super cela suppose deja que c'est la meme personne de toute facon le 
    ### mapper ne vas pas envoyer la meme valeur deux fois a moins que ce ne fut dupliquer 
    ### et donc on pourrait quand meme verifier que les autres attributs (dept,ville etc) sont à -1 dans au moins une liste
    #### et donc on pourras faire notre jointure dans ce cas .............;;;
    ### si les numeros de telephones ne sont pas les memes, bah deja il faut au moins s'assurer de tester avec tous les autres 
    ###du coup on continu
    