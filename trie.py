
class Node:

    def __init__(self):

        self.key = None

        self.value = -1

        self.children = {}

    def setNode(self, key):

        self.key = key


class Trie:

    def __init__(self):

        self.root = Node()
    
    def insert(self, word ,value):

        currentWord = word

        currentNode = self.root

        while len(currentWord) > 0:

            if currentWord[0] in currentNode.children:

                currentNode = currentNode.children[currentWord[0]]

                currentWord = currentWord[1:]

                if len(currentWord) == 0:

                    currentNode.value = value

            else:

                newNode = Node()

                newNode.key = currentWord[0]

                if len(currentWord) == 1:

                    newNode.value = value
                    
                currentNode.children[currentWord[0]] = newNode

                currentNode = newNode

                currentWord = currentWord[1:]
    
    #Tìm node trong trie

    def searchTrie(self, word):

        currentWord = word

        currentNode = self.root

        while len(currentWord) > 0 :

            if currentWord[0] in currentNode.children:

                currentNode = currentNode.children[currentWord[0]]

                currentWord = currentWord[1:]
                
            else:

                return -1 # Không có trong từ điển

        if currentNode.value == -1:

            return -2   # Có trong từ điển nhưng chưa có giá trị tại vị trí đang xét
        
        return currentNode.value
    
    def deleteNode(self, word):

        currentWord = word

        currentNode = self.root

        while len(currentWord) > 0:

            if currentWord[0] in currentNode.children:

                currentNode = currentNode.children[currentWord[0]]

                currentWord = currentWord[1:]

            else:

                return -1

        currentNode.value = -1
        
        return 1