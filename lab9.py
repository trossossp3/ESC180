import urllib.request

f = open(r"C:\Users\jason\OneDrive\Desktop\lab 9\pridejustice.txt", encoding="utf-8").read().split()

test = ["I", "am", "a", "sick", "man.", "I", "am", "a", "spiteful", "man.", "I", "am", "an", "unattractive", "man.", "I", "believe", "my", "liver", "is", "diseased.", "However,", "I", "know", "nothing", "at", "all", "about", "my", "disease,", "and", "do", "not", "know", "for", "certain", "what", "ails", "me."]



# PROBLEM 1A

def word_counts(f):
    global dictionary
    dictionary = {}
    for word in f:
        if word not in dictionary:
            dictionary.update({word:1})
        else:
            dictionary[word] += 1

    print(dictionary)

    word_counts(f)


# PROBLEM 1B
L = [1,9,7,67,67,67,6,76,76,76,345344,746,746,76,76,76,3,63,5,322353455,3,7,2,72,78,3,568,3,46,568,3464,567]

def top10(L):
    top_list = []
    L.sort()
    L = L[::-1]
    top_list = L[1:11]
    print(top_list)

    top10(L)

# PROBLEM 1C

#inv_freq = {6: "the", 12: "a", 1:"hi"}
#print(sorted(inv_freq.items()))


def word_counts(f):
    ''' returns dictionary of number of times each word appears '''
    dictionary = {}
    for word in f:
        if word not in dictionary:
            dictionary.update({word:1})
        else:
            dictionary[word] += 1
    return dictionary

def inverse(dictionary):
    ''' returns an inversed dictionary '''
    inversed_dictionary= {}

    for keys, values in dictionary.items():
        if values not in inversed_dictionary:  # if not already in the inversed dictionary
            inversed_dictionary[values] = keys
        else:
            inversed_dictionary[values] += ", "+ keys

    return inversed_dictionary

inversed_dictionary = inverse(dictionary)
sorted(inversed_dictionary.items())         # sorts the inversed dictionary


most_freq =[]
L = list(inversed_dictionary.keys())       # list of the number of times each word appears


for i in range(10):
    most_freq.append(max(L))
    L.remove(L[L.index(max(L))])

print(most_freq)

for i in most_freq:                 # prints the inversed dictionary
    print(inversed_dictionary[i])


# PROBLEM 2 (HTML)

# <!-- saved from url=(0055)http://www.cs.toronto.edu/~guerzhoy/180/labs/hello.html -->
# <html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">

# <link rel="shortcut icon" href="http://www.cs.toronto.edu/~guerzhoy/180_2016/labs/lab09/favicon.ico" type="image/x-icon">

# <title>Hello, World</title>
# </head><body><p>Hi!</p>

# <p>Hello EngSci 1F! <b>A link to U of T's homepage:</b> <a href="http://www.utoronto.ca/">link</a>.</p>

# <p>Here's the link to a Yahoo! search with the keyword "python": <a href="https://ca.search.yahoo.com/search?p=engineering+science&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8">click here</a></p>
# <p>Here's the link to a Yahoo! search with the keyword "python": <a href="Microsoft-edge:https://ca.search.yahoo.com/search?p=engineering+science&fr=yfp-t&fp=1&toggle=1&cop=mss&ei=UTF-8">click here (open in Microsoft edge)</a></p>

# <p>Praxis for<b>ever</b></p>

# </body></html>


# url = "https://ca.search.yahoo.com/search;_ylt=A2KLfRmdAaBh9TkAZxjqFAx.;_ylc=X1MDMjExNDcyMTAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANvaHhadFFSY1RxT040c2ZWTThpNndBBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNjYS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMzBHF1ZXJ5A2NhdAR0X3N0bXADMTYzNzg3NjEyOA--?p={term}&fr=sfp&iscqry=&fr2=sb-top-search" 

# problem 3

def choose_variant(arr):
    lengths = []
    for i in arr:
        # print(urllib.parse.quote(i))
        lengths.append(find_results(urllib.parse.quote(i)))
    
    maxx = max(lengths)
    index = lengths.index(maxx)
    return arr[index]


def find_results(term):
    url = "https://ca.search.yahoo.com/search;_ylt=A2KLfRmdAaBh9TkAZxjqFAx.;_ylc=X1MDMjExNDcyMTAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANvaHhadFFSY1RxT040c2ZWTThpNndBBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNjYS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMzBHF1ZXJ5A2NhdAR0X3N0bXADMTYzNzg3NjEyOA--?p={term}&fr=sfp&iscqry=&fr2=sb-top-search" 
    url = url.format(term=term)

    f = urllib.request.urlopen(url)
    page = f.read()
    page = page.split()

    num = str((page[(page.index(b'lh-22">About'))+1]))
    num = num[2:-1]
    num = (int(num.replace(",","")))
    # print(num)
    return int(num)

print(choose_variant(["five-year anniversary", "fifth anniversary"]))