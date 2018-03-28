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
        for k in range(len(a)):
            if a[k] == train_list_tags[i][j]:
                z = z + 1
    return z


def c2(train_list_tags, i, j):
    z = 0
    for a in train_list_tags:
        for k in range(len(a)):
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

t3 = [['A','boy','is','running'],['Pick','the','red','cube'],['One','ring','to','rule','the','all']]
t4 = [['D','N','V','V'],['V','D','A','N'],['D','N','T','V','D','P']]
t1 = read_train_file()[0]
t2 = read_train_file()[1]

print(t3)
print(t4)

print(t1)
print(t2)


print(train_func(t1, t2)[0])
