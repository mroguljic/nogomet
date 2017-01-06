

file = open("podaci.txt", "r")
output=open("post_podaci.txt","rw+")


lines = file.readlines()

for i,line in enumerate(lines):
	if i==0:
		line=line[:-1]
		line+=',Home FT goals,Away FT goals,Home HT goals,Away HT goals'
		line_to_write=''.join(line)
		line_to_write+='\n'
	else:
		FT_score=line.split(",")[3].split("-") #FT je 4. podatak u tablici, odmah ga podijeli na golove domacini, gosti
		HT_score=line.split(",")[4].split("-") #HT je 5.
		line=line[:-1]
		add_str=','+str(FT_score[0])+','+str(FT_score[1])+','+str(HT_score[0])+','+str(HT_score[1])
		line+=add_str
		#print line
		line_to_write=''.join(line)
		line_to_write+='\n'
	output.write(line_to_write)


file.close()
output.close()