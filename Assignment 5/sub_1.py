from operator import itemgetter       # this functionality is NOT needed. It may help slightly, but you can definitely ignore it completely.
import math

# DO NOT CHANGE!
def read_train_file():
    '''
	HELPER function: reads the training files containing the words and corresponding tags.
	Output: A tuple containing 'words' and 'tags'
	'words': This is a nested list - a list of list of words. See it as a list of sentences, with each sentence itself being a list of its words.
	For example - [['A','boy','is','running'],['Pick','the','red','cube'],['One','ring','to','rule','them','all']]
	'tags': A nested list similar to above, just the corresponding tags instead of words.
	'''
    f = open('train', 'r')
    words = []
    tags = []
    lw = []
    lt = []
    for line in f:
        s = line.rstrip('\n')
        w, t = s.split('/')[0], s.split('/')[1]
        if w == '###':
            words.append(lw)
            tags.append(lt)
            lw = []
            lt = []
        else:
            lw.append(w)
            lt.append(t)
    words = words[1:]
    tags = tags[1:]
    assert len(words) == len(tags)
    f.close()
    return (words, tags)


def c1(train_list_tags, i, j):
    z = 0
    for a in train_list_tags:
        for k in range(len(a)-1):
            if a[k] == train_list_tags[i][j]:
                z = z + 1
    return z


def c2(train_list_tags, i, j):
    z = 0
    for a in train_list_tags:
        for k in range(1, len(a)):
            if a[k] == train_list_tags[i][j] and a[k - 1] == train_list_tags[i][j - 1]:
                z = z + 1
    return z


def c3(train_list_words, i, j, train_list_tags):
    z = 0
    for l in range(len(train_list_words)):

        for k in range(len(train_list_words[l])):

            if train_list_words[l][k] == train_list_words[i][j] and train_list_tags[l][k+1] == train_list_tags[i][j+1]:
                z = z + 1
    return z



#NEEDS TO BE FILLED!
def train_func(train_list_words, train_list_tags):
    '''
    This creates dictionaries storing the transition and emission probabilities - required for running Viterbi.
    INPUT: The nested list of words and corresponding nested list of tags from the TRAINING set. This passing of correct lists and calling the function
    has been done for you. You only need to write the code for filling in the below dictionaries. (created with bigram-HMM in mind)
    OUTPUT: The two dictionaries

    HINT: Keep in mind the boundary case of the starting POS tag. You may have to choose (and stick with) some starting POS tag to compute bigram probabilities
    for the first actual POS tag.
    '''

    dict2_tag_follow_tag = {}
    """Nested dictionary to store the transition probabilities
    each tag X is a key of the outer dictionary with an inner dictionary as the corresponding value
    The inner dictionary's key is the tag Y following X
    and the corresponding value is the number of times Y follows X - convert this count to probabilities finally before returning
    for example - { X: {Y:0.33, Z:0.25}, A: {B:0.443, W:0.5, E:0.01}} (and so on) where X,Y,Z,A,B,W,E are all POS tags
    so the first key-dictionary pair can be interpreted as "there is a probability of 0.33 that tag Y follows tag X, and 0.25 probability that Z follows X"
    """
    dict2_word_tag = {}
    """Nested dictionary to store the emission probabilities.
    Each word W is a key of the outer dictionary with an inner dictionary as the corresponding value
    The inner dictionary's key is the tag X of the word W
    and the corresponding value is the number of times X is a tag of W - convert this count to probabilities finally before returning
    for example - { He: {A:0.33, N:0.15}, worked: {B:0.225, A:0.5}, hard: {A:0.1333, W:0.345, E:0.25}} (and so on) where A,N,B,W,E are all POS tags
    so the first key-dictionary pair can be interpreted as "there is a probability of 0.33 that A is the POS tag for He, and 0.15 probability that N is the POS tag for He"
    """


    #      *** WRITE YOUR CODE HERE ***

    dict3_tft = {}
    dict3_wt = {}

    for i in range(len(train_list_tags)) :
        train_list_tags[i].insert(0, '*')
        train_list_tags[i].append('STOP')

    for i in range(len(train_list_tags)):
        for j in range(len(train_list_tags[i]) - 1):

            if train_list_tags[i][j] not in dict3_tft :
                dict3_tft[train_list_tags[i][j]] = {train_list_tags[i][j + 1]: c2(train_list_tags, i, j + 1) / c1(train_list_tags, i, j)}


            else:
                dict3_tft[train_list_tags[i][j]][train_list_tags[i][j + 1]] = c2(train_list_tags, i, j + 1) / c1(train_list_tags, i, j)





    for i in range(len(train_list_words)):
        for j in range(len(train_list_words[i])):

            if train_list_words[i][j] in dict3_wt:
                dict3_wt[train_list_words[i][j]][train_list_tags[i][j]] = c3(train_list_words, i, j, train_list_tags)/c1(train_list_tags, i, j+1)

            else:
                dict3_wt[train_list_words[i][j]] = {train_list_tags[i][j+1]: c3(train_list_words, i, j, train_list_tags)/c1(train_list_tags, i, j+1)}


    # END OF YOUR CODE
    return (dict3_tft, dict3_wt)

def viterbi(s, dict2_tag_follow_tag, dict2_word_tag):
    curr = [('*', [], 0)]

    prev = []

    prev = curr

    curr = []

    c = -2
    t = 'N'

    if s[0] in dict2_word_tag :

        for j in ['C', 'D', 'E', 'F', 'I', 'J', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', '###', ',', '.', ':',
                  '-', '\'', '$']:

            e = dict2_word_tag[s[0]][j]
            d = math.log(dict2_tag_follow_tag[j]['*']) + math.log(e)
            curr.append((j, prev, d))

    else :
        curr.append(('N', prev, math.log(dict2_tag_follow_tag['N']['*'])))

    print(prev)

    for i in range(1, len(s)):

        prev = curr

        print(prev)

        curr = []

        if s[0] in dict2_word_tag :

            for j in ['C', 'D', 'E', 'F', 'I', 'J', 'L', 'M', 'N', 'P', 'R', 'S', 'T', 'U', 'V', 'W', '###', ',', '.', ':',
                      '-', '\'', '$']:
                curr.append(find_best(dict2_tag_follow_tag, dict2_word_tag, s[i], j, prev))


        else :
            c = -2

            for i in prev:



                d = math.log(dict2_tag_follow_tag['N'][i[0]]) + math.log(i[2])

                if c < d:
                    c = d
                    t = i

            curr.append('N', t, c)

    prev = curr
    print(prev)

    curr = []

    c = -2
    t = 'N'

    for i in prev :

        d = math.log(dict2_tag_follow_tag['STOP'][i[0]]) + math.log(i[2])

        if c < d:
            c = d
            t = i
    curr.append(('STOP', t, c))

    prev = curr
    print(prev)

    return prev


def find_best(dict2_tag_follow_tag, dict2_word_tag, word, tag, prev):
    e = dict2_word_tag[word][tag]

    c = -2

    for i in prev:
        if tag in dict2_word_tag[word] :

            d = math.log(e) + math.log(dict2_tag_follow_tag[tag][i[0]]) + math.log(i[2])

        else :

            d = math.log(dict2_tag_follow_tag[tag][i[0]]) + math.log(i[2])

        if c < d:
            c = d
            t = i

    return (tag, t, c)


def retrace(end_item):
    tags = []

    item = end_item[1]

    while item[0] == '*':
        tags.append(item[0])
        item = item[1]

    tags = tags.reverse()

    return tags


#NEEDS TO BE FILLED!
def assign_POS_tags(test_words, dict2_tag_follow_tag, dict2_word_tag):
    '''
    This is where you write the actual code for Viterbi algorithm.
    INPUT: test_words - this is a nested list of words for the TEST set
           dict2_tag_follow_tag - the transition probabilities (bigram), filled in by YOUR code in the train_func
           dict2_word_tag - the emission probabilities (bigram), filled in by YOUR code in the train_func
    OUTPUT: a nested list of predicted tags corresponding to the input list test_words. This is the 'output_test_tags' list created below, and returned after your code
    ends.

    HINT: Keep in mind the boundary case of the starting POS tag. You will have to use the tag you created in the previous function here, to get the
    transition probabilities for the first tag of sentence...
    HINT: You need not apply sophisticated smoothing techniques for this particular assignment.
    If you cannot find a word in the test set with probabilities in the training set, simply tag it as 'N'.
    So if you are unable to generate a tag for some word due to unavailibity of probabilities from the training set,
    just predict 'N' for that word.

    '''

    output_test_tags = []  #list of list of predicted tags, corresponding to the list of list of words in Test set (test_words input to this function)


    #      *** WRITE YOUR CODE HERE ***


    for i in test_words :

        output_test_tags.append(retrace(viterbi(i, dict2_tag_follow_tag, dict2_word_tag)))


    # END OF YOUR CODE

    return output_test_tags


# DO NOT CHANGE!
def public_test(predicted_tags):
    '''
	HELPER function: Takes in the nested list of predicted tags on test set (prodcuced by the assign_POS_tags function above)
	and computes accuracy on the public test set. Note that this accuracy is just for you to gauge the correctness of your code.
	Actual performance will be judged on the full test set by the TAs, using the output file generated when your code runs successfully.
	'''

    f = open('test_public_labeled', 'r')
    words = []
    tags = []
    lw = []
    lt = []
    for line in f:
        s = line.rstrip('\n')
        w, t = s.split('/')[0], s.split('/')[1]
        if w == '###':
            words.append(lw)
            tags.append(lt)
            lw = []
            lt = []
        else:
            lw.append(w)
            lt.append(t)
    words = words[1:]
    tags = tags[1:]
    assert len(words) == len(tags)
    f.close()
    public_predictions = predicted_tags[:len(tags)]
    assert len(public_predictions) == len(tags)

    correct = 0
    total = 0
    flattened_actual_tags = []
    flattened_pred_tags = []
    for i in range(len(tags)):
        x = tags[i]
        y = public_predictions[i]
        if len(x) != len(y):
            print(i)
            print(x)
            print(y)
            break
        flattened_actual_tags += x
        flattened_pred_tags += y
    assert len(flattened_actual_tags) == len(flattened_pred_tags)
    correct = 0.0
    for i in range(len(flattened_pred_tags)):
        if flattened_pred_tags[i] == flattened_actual_tags[i]:
            correct += 1.0
    print('Accuracy on the Public set = ' + str(correct / len(flattened_pred_tags)))


# DO NOT CHANGE!
if __name__ == "__main__":
    words_list_train = read_train_file()[0]
    tags_list_train = read_train_file()[1]

    dict2_tag_tag = train_func(words_list_train, tags_list_train)[0]
    dict2_word_tag = train_func(words_list_train, tags_list_train)[1]

    f = open('test_full_unlabeled', 'r')

    words = []
    l = []
    for line in f:
        w = line.rstrip('\n')
        if w == '###':
            words.append(l)
            l = []
        else:
            l.append(w)
    f.close()
    words = words[1:]
    test_tags = assign_POS_tags(words, dict2_tag_tag, dict2_word_tag)
    assert len(words) == len(test_tags)

    public_test(test_tags)

    #create output file with all tag predictions on the full test set

    f = open('output', 'w')
    f.write('###/###\n')
    for i in range(len(words)):
        sent = words[i]
        pred_tags = test_tags[i]
        for j in range(len(sent)):
            word = sent[j]
            pred_tag = pred_tags[j]
            f.write(word + '/' + pred_tag)
            f.write('\n')
        f.write('###/###\n')
    f.close()

    print('OUTPUT file has been created')

