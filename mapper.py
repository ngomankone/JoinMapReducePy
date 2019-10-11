
#!/usr/bin/env python
 
import sys
 ## USER[users(nom, prenom, tel, dept, ville)]
# input comes from STDIN (standard input)
for line in sys.stdin:
    try: #sometimes bad data can cause errors use this how you like to deal with lint and bad data
         
        nom = "-1" #default sorted as first
        prenom = "-1" #default sorted as first
        tel = "-1" #default sorted as first
        dept = "-1" #default sorted as first
        ville = "-1" #default sorted as first
        tel2 = "-1" #default sorted as first
         
        # remove leading and trailing whitespace
        line = line.strip()
         
        splits = line.split(",")
         
        if len(splits) == 4: #users data
            tel = splits[2]
            nom = splits[0]
            prenom = splits[1]
            dept = splits[3]
            ville = splits[4]
              
        else: #user data
            num1 = splits[0]
            tel2 = splits[1]
            dept2 = splits[2]          
         
        print '%s^%s^%s^%s' % (tel,nom,prenom,dept,ville,dept2)
    except: #errors are going to make your job fail which you may or may not want
        pass