from funkcije import predvidi_rezultat

#idemo vidjeti koliko je dobar model

klubovi={14:'Newcastle', 1:'Liverpool', 19:'Man United', 2:'Norwich',
9:'Man City', 15:'Southampton', 6:'West Ham', 10:'Aston Villa', 
0:'Arsenal', 8:'Crystal Palace', 17:'Cardiff', 3:'Sunderland', 
12:'Fulham', 13:'Hull', 11:'Everton', 16:'Stoke', 5:'West Brom', 
4:'Swansea', 7:'Chelsea', 18:'Tottenham'}

invetirani_klubovi={v: k for k, v in klubovi.iteritems()}

f = open ('post_podaci_backup.txt','r')

lines = f.readlines()
n_of_lines=len(lines)
print n_of_lines

broj_kola=20 #na koliko kola zelimo trenirati
broj_utakmica=10*broj_kola #svako kolo ima 10 utakmica

for i in xrange(broj_utakmica,broj_utakmica+10):
	line=lines[i]
	line=line.split(',')

	home_team=line[5]
	away_team=line[6]	

	actual_home_goals=line[-4]
	actual_away_goals=line[-3]
	
	predvidi_rezultat(klubovi[int(home_team)],klubovi[int(away_team)])

	print actual_home_goals+'-'+actual_away_goals
	print '--------------\n'