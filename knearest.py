import csv
import numpy as np

with open('trainLabels.csv', 'rb') as csvTrainLabels:
	trainLabels = csv.reader(csvTrainLabels, delimiter=',')
	labels = []
	for row in trainLabels:
		labels.append(int(row[0]))
	# print labels

with open('trainFeatures.csv', 'rb') as csvTrainFeatures:
	trainFeatures = csv.reader(csvTrainFeatures, delimiter=',')
	i = 0
	dic = {}
	for row in trainFeatures:
		dic[tuple(row)] = labels[i]
		i += 1

# with open('digitsOutput1.csv', 'wb') as csv1:
# 	writer1 = csv.writer(csv1, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	with open('digitsOutput2.csv', 'wb') as csv2:
# 		writer2 = csv.writer(csv2, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 		with open('digitsOutput5.csv', 'wb') as csv5:
# 			writer5 = csv.writer(csv5, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 			with open('digitsOutput10.csv', 'wb') as csv10:
# 				writer10 = csv.writer(csv10, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 				with open('digitsOutput25.csv', 'wb') as csv25:
# 					writer25 = csv.writer(csv25, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
with open('digitsOutput.csv', 'wb') as csvW:
	writer = csv.writer(csvW, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	with open('testFeatures.csv', 'rb') as csvVal:
		valFeatures = csv.reader(csvVal, delimiter=',')
		iteration = 0
		for valRow in valFeatures:
			a = np.array(map(float, valRow))
			# lst: first element = Euclidean distance, second element = corresponding digit
			lst = []
			with open('trainFeatures.csv', 'rb') as csvTrain:
				trainFeatures = csv.reader(csvTrain, delimiter=',')
				for trainRow in trainFeatures:
					b = np.array(map(float, trainRow))
					curr_distance = float(sum(np.sqrt((a-b) * (a-b))))
					if len(lst) < 25:
						lst.append((curr_distance, dic[tuple(trainRow)]))
						lst = sorted(lst, key=lambda x: x[0])
					elif curr_distance < lst[len(lst)-1][0]:
						lst.pop()
						lst.append((curr_distance, dic[tuple(trainRow)]))
						lst = sorted(lst, key=lambda x: x[0])

			# k = 1, 2
			guess = lst[0][1]
			print("k=1  Iteration " + str(iteration) + ": " + str(guess))
			writer.writerow([guess])

			# writer1.writerow([guess])
			# writer2.writerow([guess])

			# # k = 5,10,25
			# for k in [5,10,25]:
			# 	values = [[0.0,0,i] for i in range(10)]
			# 	for item in lst[:k]:
			# 		dist = item[0]
			# 		digit = item[1]
			# 		values[digit][0] += dist
			# 		values[digit][1] += 1
			# 	for i in values:
			# 		avg_dist = i[0]
			# 		num = i[1]
			# 		if num != 0:
			# 			i[0] = avg_dist / num
			# 	# print values
			# 	max_occurrences = 0
			# 	tie = []
			# 	for i in values:
			# 		if i[1] > max_occurrences:
			# 			tie = [i]
			# 			max_occurrences = i[1]
			# 		elif i[1] == max_occurrences:
			# 			tie.append(i)
			# 	tie = sorted(tie, key=lambda x: x[0])
			# 	# print tie
			# 	guess = tie[0][2]
			# 	if k == 5:
			# 		print("k=" + str(k) + "  Iteration " + str(iteration) + ": " + str(guess))
			# 	# elif k==10 or k==25:
			# 	# 	print("k=" + str(k) + " Iteration " + str(iteration) + ": " + str(guess))
			# 	if k == 5:
			# 		writer5.writerow([guess])
			# 	elif k == 10:
			# 		writer10.writerow([guess])
			# 	elif k == 25:
			# 		writer25.writerow([guess])
			iteration += 1