import pandas
import sklearn

file = 'podaci.txt'
#columns=['Date','Team 1','Team 2','FT','HT']

dataset = pandas.read_csv(file)

print(dataset.shape)
print(dataset.head(20))


club_names=[]
club_dict={}
#pretvori nazive klubova u brojeve (npr. Arsenal = 1, Everton = 2,...)
#------------------------------------------#
for index, row in dataset.iterrows():
    #print(row['Team 1'])
    flag=1
    for club in club_names:
    	if row['Team 1']==club:
    		flag=0
    		break
    if flag==1:
    	club_names.append(row['Team 1'])


for i,club in enumerate(club_names):
	club_dict[club]=i

print club_dict #Ovako znamo koji broj pripada kojem klubu
#------------------------------------------#

