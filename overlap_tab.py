import re
import pandas as pd

with open("overlap_30_output","r") as r:
	file=[a for a in r.readlines() if a[0] == ">"]
output = pd.DataFrame()
line=0
while line < len(file):
	dict={}
	sign=file[line].split("|")[2].split(" ")[1]
	dict["cord_"+sign]=file[line].split("|")[1].split("=")[1]
	n_reads=int(re.split('=|\n',file[line].split("|")[4])[1])
	while (file[line].split("|")[1] == file[line+1].split("|")[1]) and (file[line].split("|")[2] == file[line+1].split("|")[2]):
		line+=1
		n_reads+=int(re.split('=|\n',file[line].split("|")[4])[1])
	dict["n_reads_"+sign]=n_reads
	line+=1
	sign=file[line].split("|")[2].split(" ")[1]
	dict["cord_"+sign]=file[line].split("|")[1].split("=")[1]
	if line != len(file)-1:
		while (file[line].split("|")[1] == file[line+1].split("|")[1]) and (file[line].split("|")[2] == file[line+1].split("|")[2]):
			line+=1
			n_reads+=int(re.split('=|\n',file[line].split("|")[4])[1])
			if line == len(file)-1:
				break
	dict["n_reads_"+sign]=n_reads

output = output.append(dict, ignore_index=True)

	
