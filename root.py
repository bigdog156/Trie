from flask import Flask, render_template, request
from trie import Node,Trie
import run

app = Flask(__name__)

trie = Trie()
    
fileMean = open("repository/mean.txt",'r+')

fileData = open("repository/data.txt",'r+')
    
data = run.processFileToArray("repository/data.txt")

trie = run.makeTrie(data,trie)



@app.route('/', methods = ['POST','GET'])

def trieIndex(name=None):

    search = request.args.get('name', '')
    print(search)
    if request.method == "POST":
        word = request.form['newWord']

        mean = request.form['mean']

        check = run.addNodeTrie(word,mean,trie)

        if check ==1 :
            return render_template('index.html',name="Thêm thành công... !!!")

        else:
            return render_template('index.html',name="Thêm thất bại...")
    if request.method == 'GET':

        if search != None:
           
            x = trie.searchTrie(search.lower())

            if x <0 :

                name="Không tìm thấy " 
                print(x)

            else:

                fileMean.seek(x)
                
                print(x)

                name = fileMean.readline()
        
    return render_template('index.html',name=name,search=search)


if __name__ =='__main__':

    app.run(debug=True)
