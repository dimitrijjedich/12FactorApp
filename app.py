from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcomeToTwelveFactorApp():
  return "Welcome to twelve factor app!"
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
