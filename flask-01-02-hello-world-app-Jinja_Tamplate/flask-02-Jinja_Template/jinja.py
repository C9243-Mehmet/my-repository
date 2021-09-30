from flask import Flask,render_template

app =Flask(__name__)

@app.route("/")
def head():
    return render_template("index.html",number1=12, number2=15)

@app.run("/karil")
def number():
    num1,num2 = 23 ,45








if __name__"__main__:
    app.run(debug=True)