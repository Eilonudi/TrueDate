from flask import Flask, request, render_template, send_from_directory
app = Flask(__name__)

@app.route("/getDate/<username>")
def getDate(username : str):
    return "your date is shahar"

@app.route("/register/<username>/<password>")
def registerNewUser(username : str, password : str):
    return username + " registered"

@app.route("/unregister/<username>/<password>")
def unregisterUser(username : str, password : str):
    return username + " unregistered"

def getMetadata():
    return  ("\n" + str(request.method))

@app.route("/")
def hello():
    return send_from_directory(directory="static", filename="html/main.html")

@app.route("/testSimpleParam/<name>")
def fuckString(name : str):
    return "Fuck you {0}".format(name)

@app.route("/testIntParam/<int:count>")
def fuckInt(count : int):
    return "Fuck you {0} times".format(count)


@app.route("/methods", methods = ['GET', 'POST'])
def methodTypeTester():
    return "You are using {0}".format(getMetadata())

@app.route("/twoparams/<name>/<int:age>")
def twoParamTester(name : str, age : int):
    return "The age of {name} is {age}".format(name=name, age=age)

if __name__ == "__main__":
    app.run(host='0.0.0.0')