from flask import Flask, render_template

#create a Flask Instance
app = Flask(__name__)
app.config['SECRET_KEY'] = 'lotanmania'

# create a route decorator
@app.route('/')
#def index():
  #return "<h1>Hello World!</h1>"

def index():
  first_name = 'lotan'
  stuff = "This is <strong>Bold</strong> Text"
  staff = "this is strong text"
  stop = "this is strong text,  i have no idea what    i'm doing"
  made = "This is <strong>Bold</strong> Text"

  favorite_pizza = ["Pepperoni", "Cheese", "Mushrooms", 41]
  return render_template("index.html", first_name=first_name,stuff=stuff,staff=staff,stop=stop, made=made, favorite_pizza=favorite_pizza)


#localhost:5000/user/lotan
@app.route('/user/<name>')
def user(name):
  return render_template('user.html',name=name)

# create custom error pages

# invalid url
@app.errorhandler(404)
def page_not_found(e):
  return render_template("404.html"), 404

# internal server url
@app.errorhandler(500)
def page_not_found(e):
  return render_template("500.html"), 500

if __name__ == '__main__':
  app.run(debug=True)