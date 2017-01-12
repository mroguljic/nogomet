import numpy as np
from funkcije import *

f = open ('post_podaci_backup.txt','r')

lines = f.readlines()
n_of_lines=len(lines)
print n_of_lines

X=[]  #lista ciji su elementi liste iz koje izvlacim informaciju tko je domacin (1), tko je gost(-1)
Y1=[] #Home goals
Y2=[] #Away goals

klubovi={14:'Newcastle', 1:'Liverpool', 19:'Man United', 2:'Norwich',
9:'Man City', 15:'Southampton', 6:'West Ham', 10:'Aston Villa', 
0:'Arsenal', 8:'Crystal Palace', 17:'Cardiff', 3:'Sunderland', 
12:'Fulham', 13:'Hull', 11:'Everton', 16:'Stoke', 5:'West Brom', 
4:'Swansea', 7:'Chelsea', 18:'Tottenham'}

for i in xrange(1,201):
	line=lines[i]
	line=line.split(',')

	x = [0]*20	
	home_team=line[5]
	away_team=line[6]	
	x[int(home_team)]=1
	x[int(away_team)]=-1
	y1=[]
	y2=[]
	y1.append(np.float(line[8]))
	y2.append(np.float(line[9]))
	X.append(x)
	Y1.append(y1)
	Y2.append(y2)

#Ucitali smo podatke o 200 utakmica

napad=[0.]*20 #koeficijenti napada i obrane. broj golova = napad[i]-obrana[j] i obratno
obrana=[0.]*20


error=calculate_error(X,Y1,Y2,napad,obrana)
print 'Starting error ', error

#namjestanje koeficijenata
for iteration in xrange(500):
	for klub in xrange(20):
		napad_change=calculate_change_in_attack(X,Y1,Y2,napad,obrana,klub)
		napad[klub]+=napad_change
		obrana_change=calculate_change_in_defense(X,Y1,Y2,napad,obrana,klub)
		obrana[klub]+=obrana_change
	if(iteration%50==0):
		print calculate_error(X,Y1,Y2,napad,obrana)
		print '----------'


print napad
print obrana
