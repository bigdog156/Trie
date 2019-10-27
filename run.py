from trie import Node, Trie

def makeTrie(words):
    index = 0
    trie = Trie()
    for word in words:
        trie.insert(word,index)
        index = index + 1 
    return trie

if __name__ == "__main__":

    f= open("data.txt",'a')
    
    f.seek(20)
    f.write("\nokela lakeo")
    f.close()
    f= open("data.txt")
    contentNext = f.read()
    print(contentNext)



    trie = makeTrie(['hello', 'hat', 'her', 'haaaa','ha'])
    x = trie.searchTrie('h')
    print(x)
