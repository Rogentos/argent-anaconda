'''
Created on May 26, 2012

@author: victor
'''
import glob
import re
import sys
import os
import fnmatch
import string

def matchStrInFile(str,filename):
    if filename == "./rebrand.py":
        return
    file = open(filename,'r')
    fileTxt = file.read()
    replaced = fileTxt
    for x in str:
        replaced = re.sub('(?P<M>'+x[1]+')',x[0],replaced,0)
    file.close()
    file = open(filename,'w')
    file.write(replaced)
    return
def matchStrInFile2(str,filename):
    if filename == "./rebrand.py":
        return
    file = open(filename,'r')
    fileTxt = file.read()
    replaced = fileTxt
    for x in str:
        replaced = re.sub('(?P<o>".*?)('+x[0]+')(?P<t>.*?")','\g<o>'+x[1]+'\g<t>',replaced,0)
    file.close()
    file = open(filename,'w')
    file.write(replaced)
    return
def globReplace(map,dirname):
    regexx = re.findall(".*(\.git).*", dirname, re.IGNORECASE)
    if regexx:
        return
    muie = glob.glob(dirname+"/*")
    for x in muie:
        if os.path.isdir(x) == False:
            matchStrInFile2(map,x)
    
    return

caseMap=[]
caseMap.append(('SABAYON','ROGENTOS'))
caseMap.append(('Sabayon','Rogentos'))
caseMap.append(('sabayon','rogentos'))

matches = []
for root,dirnames,filenames in os.walk("./"):
    repl = str(root)
    globReplace(caseMap,root)
    for x in caseMap:
        repl = repl.replace(str(x[1]),str(x[0]))
    print repl
    regex = re.findall(".*(sabayon).*", repl, re.IGNORECASE)
    regex2 = re.findall(".*(\.git).*", repl, re.IGNORECASE)
    if regex and not regex2:
        os.rename(root, repl)
print 'hello world'