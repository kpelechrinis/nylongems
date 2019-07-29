import os
import sys
import choix

f = open("../results.txt","r")

pairs = dict()

for line in f:
	if "::" in line:
		linef = line.rstrip().rsplit("::")
		pairs[linef[0]] = {'id': linef[0], 'left': int(linef[1].rstrip().rsplit("-")[0].rsplit(".")[0])-1, 'right': int(linef[1].rstrip().rsplit("-")[1].rsplit(".")[0])-1}
	else:
		pairs[line.rstrip()[:-2]]['choice'] = line.rstrip()[-1] 

data = []

for k in pairs.keys():
	if 'choice' in pairs[k]:
		if pairs[k]['choice'] == 'A':
			el = (pairs[k]['left'],pairs[k]['right'])
		else:
			el = (pairs[k]['right'],pairs[k]['left'])
		data.append(el)

print("Nylon\tGemScore")
skills = choix.ilsr_pairwise(8, data, alpha=0.01)
print("=====================")
for i in range(len(skills)):
	print(i+1,"\t",skills[i])
