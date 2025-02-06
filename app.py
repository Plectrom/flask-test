from flask import Flask, render_template

app = Flask(__name__)

# Define a class with a method
class MyClass:
    def __init__(self, name):
        self.name = name

    def somemethod(self):
        return f"Hello from {self.name}'s method!"

# Create an instance of the class
myobj = MyClass("Ahmed")

mydictionary = {'key1': 'value1', 'key2': 'value2'}
mylist = [1, 2, 3, 4, 5]

@app.route('/')
@app.route('/<int:myintvar>')
def index(myintvar=0):
    if myintvar >= len(mylist) or myintvar < 0:
        return "Index out of range", 400
    return render_template('index.html', mydictionary=mydictionary, mylist=mylist, myintvar=myintvar, myobj=myobj)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
