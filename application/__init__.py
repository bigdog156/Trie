from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['POST','GET'])
def trie(search=None):
    if request.method == 'POST':
        searchQuery = request.form.get('search')
        print(searchQuery)
    return render_template('index.html')

if __name__ =='__main__':
    app.run(debug=True)