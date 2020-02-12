from flask import Flask

app = Flask(__name__)


@app.route("/")

def hello():

  return "HelloWorldLaihhCI"


if __name__ == "__main__":
  app.run(host='0.0.0.0')

