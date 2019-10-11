
#!/usr/bin/env python                
import sys
## USER[users(nom, prenom, tel, dept, ville)]
# input comes from STDIN (standard input)
for line in sys.stdin:
  # remove leading and trailing whitespace
    line = line.strip()
    words = line.split(",")

    if (len(words)==5):#users data excepted phone user(columm)
              infoUsers=words[0]+" "+words[1]+" "+words[3]+" "+words[4]
              print '%s^%s'%(words[2], infoUsers)
    else:#calls data excepted phone call(columm)
              infoCalls=words[1]+" "+words[2]
              print '%s^%s'% (words[0],infoCalls)
