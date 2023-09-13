import os

path = os.curdir
pathfile = os.path.join(path, 'foda.txt')
open(pathfile, "w").write('foda-se, luiza sonza fazendo musica boa')
print( open(pathfile, "r").read())