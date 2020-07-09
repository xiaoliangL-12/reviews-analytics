#data = []
#with open('reviews.txt', 'r') as f:
#	for line in f:
#		data.append(line)
#print(len(data))
#print(data[0])                  #印出第一笔

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:             #%是求余数的
		    print(len(data))              #use count to count the number when count % 1000 == 0