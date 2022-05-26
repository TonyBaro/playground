from ast import Return
from flask import Flask, render_template 
app = Flask(__name__)  

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:boxes>')
def playnum(boxes):
    return render_template('playground2.html',boxes = boxes)

@app.route('/play/<int:boxes>/<string:color>')
def playnumcolor(boxes,color):
    return render_template('playground3.html',boxes = boxes, color = color)


if __name__=="__main__":   
    app.run(debug=True) 