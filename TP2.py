# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 21:25:19 2019

@author: PERSO
"""
def main():
##RECUPERER LE NOM DE LA PERSONNE
 personne = str( input("Quel est votre nom? "))
 ##RECUPERER AGE DE LA PERSONNE
 age = int(input("Donner votre age "))
 if age < 1 or age >90:
     print("erreur de saisie , donnez un age correct")
 else:

 ##INITIALISER PRIX
  prix = 0
  if age < 18:
     prix = 7 
  else:    
         prix = 10
 ## DEMANDER POPCORN
 pop_corn_request = input("Souhaitez-vous du pop corn ? (Oui, Non) ")
 if pop_corn_request == "Oui" :
    prix += 5
    
   
    
 print(personne +": vous nous devez : " + str(prix) + " euros")
 print(personne +": vous nous devez : {}€".format(prix))
 
 
      
if __name__ == '__main__':
    main()