from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "hello"
        
@app.route("/index") 
def hello():
    name = request.args.get("name")
    age = request.args.get("age")
    return render_template("index.html", name=name, age=age)

@app.route("/calculate")
def calculate():
    num1 = request.args.get("num1", type = int)
    num2 = request.args.get("num2", type = int)
    
    result = None
    if num1 is not None and num2 is not None:
        result = num1 + num2
    return render_template("calculate.html", num1=num1, num2=num2, result = result)    
    
if __name__ == "__main__":
    app.run(debug=True)