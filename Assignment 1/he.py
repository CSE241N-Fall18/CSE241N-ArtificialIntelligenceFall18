
	"""for sentence in test_words:
		pi = defaultdict(dict)
		tag_dict = defaultdict(dict)
		for i in range(len(sentence)):
			for j in tags:
				pi[i][j]=0
				tag_dict[i][j] = None

		for t in tags:
			if t not in dict2_tag_follow_tag['*']:
				continue
			if t not in dict2_word_tag[sentence[0]]:
				continue
			pi[0][t] = dict2_tag_follow_tag['*'][t] * dict2_word_tag[sentence[0]][t]
			tag_dict[0][t] = '*'
		#Viterbi algorithm
		
		store_tags=[]
		


		for i in range(1,len(sentence)):
			for current_tag in tags:
				for prev_tag in tags:
					 if current_tag not in dict2_tag_follow_tag[prev_tag]:
					 	continue
					 if current_tag not in dict2_word_tag[sentence[i]]:
					 	continue
					 temp_probability = pi[i-1][prev_tag] * dict2_tag_follow_tag[prev_tag][current_tag] * dict2_word_tag[sentence[i]][current_tag]
					 if temp_probability > pi[i][current_tag]:
					 	pi[i][current_tag] = temp_probability
					 	tag_dict[i][current_tag] = prev_tag


		c = '.'
		j = len(sentence) - 1
		maxp = 0
		for t in tags:
			if pi[j][t] > maxp:
				maxp = pi[j][t]
				c = t
		while c != '*':
			store_tags.append(c)
			c = tag_dict[j][c]
			j = j - 1

		store_tags.reverse()
		output_test_tags.append(store_tags)"""