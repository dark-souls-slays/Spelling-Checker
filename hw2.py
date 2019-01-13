#insertion, deletion or substitution

global words

def edit_distance(s1,s2):
    m=len(s1)+1
    n=len(s2)+1

    tbl = {}
    for i in range(m): tbl[i,0]=i
    for j in range(n): tbl[0,j]=j
    for i in range(1, m):
        for j in range(1, n):
            cost = 0 if s1[i-1] == s2[j-1] else 1
            tbl[i,j] = min(tbl[i, j-1]+1, tbl[i-1, j]+1, tbl[i-1, j-1]+cost)
    return tbl[i,j]

def spelling_checker():
    length = len(mispelled_word)
    potential_words = {}

    for word in words:
        if(len(word)<=length+3 and len(word)>=length-3):
            ED = edit_distance(mispelled_word,word)
            if(ED<=3):
                potential_words[word] = ED

    for key, value in sorted(potential_words.iteritems(), key=lambda (k,v): (v,k)):
        print "%s: %s" % (key, value)

words = open("dictionary.txt").readlines()
words = [word.strip() for word in words]
mispelled_word = raw_input("type a word: ")
while(mispelled_word!="end spelling checker"):
    print("check for: " + mispelled_word)
    if(mispelled_word in words):
        print("Word is properly spelled.")
    else:
        spelling_checker()
    mispelled_word = raw_input("type a word: ")
