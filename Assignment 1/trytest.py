f = open('test_full_unlabeled','r')

words = []
l=[]
for line in f:
		w = line.rstrip('\n')
		if w=='###':
			words.append(l)
			l=[]
		else:
			l.append(w)
f.close()
words = words[1:]
print("\n",words);
