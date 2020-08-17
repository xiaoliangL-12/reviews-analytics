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
print('每笔留言平均数是', sum_len/len(data))         #算出每笔留言的平均数

"*找出小于100的每笔留言"
new = []
for zl in data:
	if len(zl) < 100:
		new.append(zl)
print('一共有', len(new), '笔留言长度小于100')       #for loop做完才print
print(new[0])
print(new[1])

"*找出有good的每笔留言"
good = []
for zl in data:
	if 'good' in zl:
		good.append(zl)
print('一共有', len(good), '笔留言含有good')
print(good[0])


"*list comprehension(快写法)"
good = [1 for zl in data if 'good' in zl]            #这一行等于上面四行, 这个1指的是每多一个good不加一个留言, 而是加一个1
print('一共有', len(good), '笔留言含有good')
print(good)

good = [zl + '123' for zl in data if 'good' in zl]     #每一个留言后面加个123   
print('一共有', len(good), '笔留言含有good')
print(good[0])

bad = ['bad' in zl for zl in data]                       #'bad' in zl: 是非题/留言里面有'bad', 是True. 没有, 是False
print(bad)

bad = []
for zl in data:
	bad.append('bad' in zl)

#文字计数
print(data[0])
w_c = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in w_c:                            #not in: 不在里面
			w_c[word] += 1
		else:
			w_c[word] = 1

for word in w_c:
	if w_c[word] > 100:
		print(word, w_c[word])
print(w_c['Allen'])

while True:
	word = input('请问你想查询什么字: ')
	if word == 'q':
		break
	if word in w_c:
		print(word, '出现过的次数为', w_c[word])
	else:
		print('这个字没有出现过')

print('感谢使用!')