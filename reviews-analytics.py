#data = []
#with open('reviews.txt', 'r') as f:
#	for line in f:
#		data.append(line)
#print(len(data))
#print(data[0])                                       #印出第一笔

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:                        #%是求余数的
		    print(len(data))                         #use count to count the number when count % 1000 == 0
print('档案读取完毕, 一共有', len(data), '笔资料')

sum_len = 0
for zl in data:
	sum_len = sum_len + len(zl)                    #读第一个zl, 加进sum_len. 然后读第二个zl, 再加进新的sum_len
print('每笔留言平均数是', sum_len/len(data))