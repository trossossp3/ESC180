'''Semantic Similarity: starter code

Author: Michael Guerzhoy. Last modified: Nov. 14, 2016.
'''

import math
dic1 = {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}
dic2 = {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}

def norm(vec):
    '''Return the norm of a vector stored as a dictionary,
    as described in the handout for Project 3.
    '''
    
    sum_of_squares = 0.0  
    for x in vec:
        sum_of_squares += vec[x] * vec[x]
    
    return math.sqrt(sum_of_squares)


def cosine_similarity(vec1, vec2):
    sum = 0
    for key, value in vec1.items():
        if key in vec2.keys():
            sum += value * vec2[key]
    return sum /(norm(vec1) * norm(vec2))


# print(cosine_similarity(dic1, dic2))

def build_semantic_descriptors(sentences):
    """
    take 2d array of sentances returns disctionary of dictionary where the key coresponds to a distionary of the amount of words it is in a sentance with
    """
    dic = {}
    for sentance in sentences:
        sentance = list(dict.fromkeys(sentance)) #this line removes all duplicates from the line idk if we want to or not
        for word in sentance:
            if word not in dic.keys():
                dic[word] = {}
            
            temp1 = sentance.copy()
            # temp1.remove(word)
            temp1 = list(filter((word).__ne__, temp1))
            # print(temp1)
            for i in range (len(temp1)):
                if temp1[i] not in dic[word].keys(): 
                    dic[word][temp1[i]] = 1
                else:
                    dic[word][temp1[i]] +=1
    return dic

temp = [["i", "am", "a",], ["i", "am"]]

# print(build_semantic_descriptors(temp))
            

def build_semantic_descriptors_from_files(filenames):
    """
    take in array of filename
    go through seperate the sentances out into an 2-d array 
    """
    sentances = []
    for i in range(len(filenames)):
        words = open(filenames[i], "r", encoding="latin1").read() #array of all words
        words = processWords(words)
        arr_words = words.split(".")
        
        for i in range(len(arr_words)):
            sentances.append(arr_words[i].split())

        
    return build_semantic_descriptors(sentances)
    


def processWords(s1):
    s1 = s1.lower()
    s1 = s1.replace("!", ".")
    s1 = s1.replace(",", "")
    s1 = s1.replace("?", ".")
    s1 = s1.replace("--", " ")
    s1 = s1.replace("-", " ")
    s1 = s1.replace(":", "")
    s1 = s1.replace(";","")

    return s1


# print(build_semantic_descriptors_from_files(["temp.txt", "text.txt"]))


def most_similar_word(word, choices, semantic_descriptors, similarity_fn):
    """find which element from choices is most similar to word using the semantic_descriptors"""
    
    top_score = 0
    top_index = -1
    word_dic = semantic_descriptors[word]
    for i in range(len(choices)):
        if(choices[i] in semantic_descriptors.keys()):
            temp_dic = semantic_descriptors[choices[i]]
            score = similarity_fn(word_dic, temp_dic)
            if score > top_score:
                top_score = score
                top_index = i

    return choices[top_index]

def run_similarity_test(filename, semantic_descriptors, similarity_fn):
    text = open(filename, "r", encoding="latin1").read()
    lines = text.splitlines() #array of each line in the entry
    print(lines)
    num_correct = 0
    num_incorrect = 0
    for i in range(len(lines)):
        words = lines[i].split()
        guess_word = most_similar_word(words[0], words[2:], semantic_descriptors,similarity_fn)
        if guess_word == words[1]:
            num_correct+=1
        else:
            num_incorrect+=1
    return num_correct/(num_correct+num_incorrect) *100

