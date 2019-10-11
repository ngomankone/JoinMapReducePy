# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 22:40:42 2019

@author: PERSO
"""
##importation de la bib statitstic
import statistics
##importation de random
import random
def main():
    #DECLARER UNE LISTE
    online_players= ["dama", "traore"]
    print(online_players)
    ##AJOUTER UN ELEMENT
    online_players.append("selr")
    print(online_players)
    ##RECUPERER LE DERNIER ELEMENT
    print(online_players[len(online_players)-1])
    ##INSERTION
    online_players.insert(2, "connard")
    print(online_players)
    online_players.extend(["damamay", "conaté"])
    print(online_players)
    ##effacer un element
    online_players.pop(1)
    print(online_players)
    online_players.remove("dama")
    print(online_players)
    online_players.clear()
    print(online_players)
    note = [ 1 , 3 , 45 ,
              
             3 , 45 , 2]
    
    print("{} " .format(note[1]))
    result = statistics.mean(note)
    print("{} ".format(result))
    random.shuffle(note)
    print("{} ".format(note))
    text = input("Entrer ").split("-")
    print(text)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
 
      
if __name__ == '__main__':
    main()