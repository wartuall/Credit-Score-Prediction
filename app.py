from flask import Flask, render_template, redirect, request

friend={"ram","sam","kam"}
creditNum=0
# _name_=_main
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['POST'])
def submit():
    if request.method=='POST':
        n1=int(request.form['No1'])
        n2=int(request.form['No2'])
        n3=int(request.form['No3'])
        n4=float(request.form['No4'])
        n5=int(request.form['No5'])
        creditNum=int((n5 * 0.35) + (n4 * 0.30) + (n3 * 0.15) + (n2 * 0.10) + (n1 * 0.10))
        return render_template('index.html', number=creditNum) 
if __name__=='__main__':
    app.run(debug=True)