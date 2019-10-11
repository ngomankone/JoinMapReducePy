# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 19:40:32 2019

@author: PERSO
"""

#GRAVEN 1ER TP
def main ():
#DEFINIR UNE VARIABLE PERSONNE 
 ##personne = "DamaMaimouna"
## LIRE SA MONNAIE
 while (1):
  personne = "DamaMaimouna"
  portemonnaie = int(input("Donner la somme que tu as "))
 ## creation d'un produit
  produit = 50
##ACHAT D'UN PRODUIt
## 
  if portemonnaie >= produit :
   portemonnaie = portemonnaie - produit
   print(str(portemonnaie) + " c'est ce  qui te reste " + personne)
  else:
     print("vous n'avez pas assze d'argent desolé")
     
     
if __name__ == '__main__':
    main()