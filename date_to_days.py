from datetime import date

# d0 = date(2016, 1, 1)
# d1 = date(2016, 1, 5)
# delta = d0 - d1
# print delta.days

def string_to_date(date_string):	#pretvori string u date type
	temp=date_string.split("-")
	d=date(int(temp[0]),int(temp[1]),int(temp[2]))
	return d


file = open("podaci.txt", "r")
output=open("post_podaci.txt","rw+")


lines = file.readlines()

first_date_string=lines[1].split(",")[0] #[1] jer je prvi red naziv stupaca, split da listu stringova iz reda
first_date=string_to_date(first_date_string)

for i,line in enumerate(lines):
	if i==0:
		line=line[:-1]
		line+=',Days from start'
		line_to_write=''.join(line)
		line_to_write+='\n'
	else:
		date_string=line.split(",")[0]
		match_date=string_to_date(date_string)
		delta=match_date-first_date
		n_of_days=delta.days
		print n_of_days
		line=line[:-1]
		add_str=','+str(n_of_days)
		line+=add_str
		#print line
		line_to_write=''.join(line)
		line_to_write+='\n'
	output.write(line_to_write)


file.close()
output.close()