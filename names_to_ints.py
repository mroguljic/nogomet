
file = open("podaci.txt", "r")
output=open("post_podaci.txt","rw+")


club_dict={}
club_names=[]
lines = file.readlines()

for i in xrange(1,100):
	temp=lines[i].split(",")
	club=temp[1]
	flag=1
	for club_name in club_names:
		if club==club_name:
			flag=0
			break
	if flag==1:
		club_names.append(club)	



for i,club in enumerate(club_names):
	club_dict[club]=i

print club_dict #Ovako znamo koji broj pripada kojem klubu


for i,line in enumerate(lines):
	if i==0:
		line=line[:-1]
		line+=',iTeam 1,iTeam 2'
		line_to_write=''.join(line)
		line_to_write+='\n'
	else:
		temp=line.split(",")
		club1=temp[1]
		club2=temp[2]
		line=line[:-1]
		add_str=','+str(club_dict[club1])+','+str(club_dict[club2])
		line+=add_str
		print line
		line_to_write=''.join(line)
		line_to_write+='\n'
	output.write(line_to_write)


file.close()
output.close()