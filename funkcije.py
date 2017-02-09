# klubovi={14:'Newcastle', 1:'Liverpool', 19:'Man United', 2:'Norwich',
# 9:'Man City', 15:'Southampton', 6:'West Ham', 10:'Aston Villa', 
# 0:'Arsenal', 8:'Crystal Palace', 17:'Cardiff', 3:'Sunderland', 
# 12:'Fulham', 13:'Hull', 11:'Everton', 16:'Stoke', 5:'West Brom', 
# 4:'Swansea', 7:'Chelsea', 18:'Tottenham'}




def calculate_error(X,Y1,Y2,napad,obrana):	#izracuna koliko nam je model kriv
	#X - lista utakmica - svaka utakmica je predstavljena listom od 20 brojeva,
	#na rednom broju kluba domacina je 1, za gosta -1, 0 ostali, redni brojevi su dani na pocetku filea
	#Y1 - lista koja sadzi koliko je domacin dao golova koju utakmicu
	#Y2 - isto za goste
	#napad,obrana - koeficijenti za napad,obranu
	#klub - kojem klubu prilagodavamo koeficijente

	#ideja - dodati tezinu zadnjim utakmicama
	total_error=0.
	for no,game in enumerate(X):
		domacin=int(game.index(1)) #koji tim je domacin/gost, uzimamo int jer nas zanima koje je njegov red u listama napad/obrana
		gost=int(game.index(-1))

		domacin_golovi=int(Y1[no][0])
		gost_golovi=int(Y2[no][0])
		predvideno_ht_golovi=napad[domacin]-obrana[gost] 	#ht - home team , at - away team
		predvideno_at_golovi=napad[gost]-obrana[domacin]
		#game_error=abs(predvideno_ht_golovi-domacin_golovi)+abs(predvideno_at_golovi-gost_golovi) 	#velicina koja mjeri koliko smo pogrijesili
		game_error=(predvideno_ht_golovi-domacin_golovi)*(predvideno_ht_golovi-domacin_golovi)	
		+(predvideno_at_golovi-gost_golovi)*(predvideno_at_golovi-gost_golovi)	#alternativna mjera greske, vise kaznjava kad jako pogrijesimo
		total_error+=game_error
	return total_error


def calculate_change_in_attack(X,Y1,Y2,napad,obrana,klub,threshold=-0.,step=0.01):	#izracuna isplati li se mijenjati koeficijente napada
	#threshold je tu da ne mijenjamo ako jako malo dobijemo mijenjanjem (mislio sam da ce biti problem ako stavim samo 0., ali cini se ok)
	#step je velicina promjene koeficijenta, ako je mala, sporo ce konvergirati, ako je velika necemo naci najbolji koef. 0.01 je ok
	
	pocetni_error=calculate_error(X,Y1,Y2,napad,obrana)						
	napad[klub]+=step
	povecan_napad_error=calculate_error(X,Y1,Y2,napad,obrana)-pocetni_error #koliko dobijemo (ili izgubimo) kada povecamo napad za "step"
	
	napad[klub]-=step*2
	smanjen_napad_error=calculate_error(X,Y1,Y2,napad,obrana)-pocetni_error
	napad[klub]+=step #vrati na pocetnu vrijednost

	if(povecan_napad_error>threshold and smanjen_napad_error>threshold):	#nemoj mijenjati ako se "ne isplati"
		return 0
	else:
		if povecan_napad_error<=smanjen_napad_error:
			return step
		else:
			return -step


def calculate_change_in_defense(X,Y1,Y2,napad,obrana,klub,threshold=-0.,step=0.01):	
	pocetni_error=calculate_error(X,Y1,Y2,napad,obrana)	
	obrana[klub]+=step
	povecan_obrana_error=calculate_error(X,Y1,Y2,napad,obrana)-pocetni_error
	
	obrana[klub]-=step*2
	smanjen_obrana_error=calculate_error(X,Y1,Y2,napad,obrana)-pocetni_error
	obrana[klub]+=step

	if(povecan_obrana_error>threshold and smanjen_obrana_error>threshold):
		return 0
	else:
		if povecan_obrana_error<=smanjen_obrana_error:
			return step
		else:
			return -step


def predvidi_rezultat(klub1,klub2):
	#ucita podatke iz koeficijent_napad/obrana.txt i da predvidi rezultate
	#klub1/2 je string kluba, npr 'Newcastle'

	klubovi={14:'Newcastle', 1:'Liverpool', 19:'Man United', 2:'Norwich',
9:'Man City', 15:'Southampton', 6:'West Ham', 10:'Aston Villa', 
0:'Arsenal', 8:'Crystal Palace', 17:'Cardiff', 3:'Sunderland', 
12:'Fulham', 13:'Hull', 11:'Everton', 16:'Stoke', 5:'West Brom', 
4:'Swansea', 7:'Chelsea', 18:'Tottenham'}

	invetirani_klubovi={v: k for k, v in klubovi.iteritems()}

	koeficijenti_napad=open( 'koeficijenti_napad.txt' , 'r' )
	koeficijenti_obrana=open( 'koeficijenti_obrana.txt' , 'r' )


	napad = [float(line[:-1]) for line in koeficijenti_napad]
	obrana = [float(line[:-1]) for line in koeficijenti_obrana]

	napad_1=napad[invetirani_klubovi[klub1]]	#invertirani klubovi je rjecnik koji povezuje ime kluba s rednim brojem
	obrana_1=obrana[invetirani_klubovi[klub1]]

	napad_2=napad[invetirani_klubovi[klub2]]	
	obrana_2=obrana[invetirani_klubovi[klub2]]

	home_goals=napad_1-obrana_2
	away_goals=napad_2-obrana_1

	print klub1+'-'+klub2
	print str(home_goals)+'-'+str(away_goals)

	#return [home_goals,away_goals]