import urllib.request

# print(urllib.parse.quote("a b"))

url = "https://ca.search.yahoo.com/search;_ylt=A2KLfRmdAaBh9TkAZxjqFAx.;_ylc=X1MDMjExNDcyMTAwMgRfcgMyBGZyAwRmcjIDc2ItdG9wLXNlYXJjaARncHJpZANvaHhadFFSY1RxT040c2ZWTThpNndBBG5fcnNsdAMwBG5fc3VnZwM5BG9yaWdpbgNjYS5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDMARxc3RybAMzBHF1ZXJ5A2NhdAR0X3N0bXADMTYzNzg3NjEyOA--?p={term}&fr=sfp&iscqry=&fr2=sb-top-search" 

f = urllib.request.urlopen(url.format(term="dog"))
page = f.read()
page = page.split()

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