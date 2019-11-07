from trie import Node, Trie

import re

def makeTrie(words,CreateTrie):
  
    for word in words:

        CreateTrie.insert(word[1],word[0])
        
    return CreateTrie


#Xử lí file data.txt thành mảng các phần tử gồm seekIndex và từ khoá

def processFileToArray(PATH):

    data = open(PATH,'r+')

    listData = list(data)

    for i in range(len(listData)):

        listData[i] = re.split(":",listData[i][:-1])

        listData[i][0] = int(listData[i][0])

    return listData

#Tiền xử lí 2 file: File nghĩa và file Text

def preProcessFile(pathText, pathMean):

    listText = list(open(pathText,'r+'))

    listMean = list(open(pathMean, 'r+'))

    fileData = open("repository/data.txt",'w+')

    indexSeek = 0

    for i in range(len(listMean)):

        if i != 0:

            indexSeek = indexSeek + len(listMean[i-1])

        fileData.write(str(indexSeek)+':'+listText[i])

        indexFinal = len(listMean[i])

    fileData.close()

    return indexSeek + indexFinal

#Thêm node vào Trie

def addNodeTrie(word, mean,trieCurrent):

    fileMean = open("repository/mean.txt",'a+')

    fileData = open("repository/data.txt",'a+')

    checkInData = trieCurrent.searchTrie(word)

    if checkInData == -1 or checkInData == -2:

        #Thêm vào Mean.txt

        fileMean.seek(0,2)

        lenMean = len(mean)

        fileMean.write(mean+"\n")

        indexMean = fileMean.tell() - lenMean -1

        #Tiếp tục thêm vị trí SeekFile của file Data 

        fileData.seek(0,2)

        fileData.write(str(indexMean)+":"+word+"\n")

        fileData.close()

        fileMean.close()

        trieCurrent.insert(word,indexMean)

        return 1

    return 0

#Xử lí khi muốn update Trie
def updateTrie(word, mean, trie):

    fileMean = open("repository/mean.txt",'wb+')

    fileData = open("repository/data.txt",'a+')

    search = trie.searchTrie(word)

    if search >=0 :

        fileMean.seek(search)

        print(search)

        fileMean.writelines(mean)

        return 1
    
    return 0
    
