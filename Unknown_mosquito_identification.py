import torch.nn as nn
def msi(output):
	#Mosquito species label
	aedes = [10,11,12,13,16,17,18,19,20,21,34,35]
	culex = [2,3,4,5,6,7,8,9,14,15,26,27,28,29]
	mansonia = [30,31]
	armigeres = [22,23]
	anopheles = [0,1,32,33]
	coquillettidia = [24,25]
	toxorhynchites = [36,37]

	label = [aedes,culex,mansonia,armigeres,anopheles,coquillettidia,toxorhynchites]
	label_name = ['aedes','culex','mansonia','armigeres','anopheles','coquillettidia','toxorhynchites']

	label_softmax = nn.Softmax(dim=1)
	pred_label = label_softmax(output)
	pred_size = pred_label.size()

	novel_mosquito_number = 0
	identified_mosquito_number = 0
	for i in range(pred_size[0]):
		pred_label1 = max(pred_label[i])
		label_index = int((pred_label[i]==pred_label1).nonzero())
		#Get the index of mosquito species
		if pred_label1 < 0.85:
			for j in range(len(label)):
				if label_index in label[j]:
					novel_mosquito_number += 1
					print(i,'Novel mosquito',label_name[j]) 
		else:
			identified_mosquito_number += 1
			print(i,'Identified mosquito',label_index)
	return novel_mosquito_number,identified_mosquito_number