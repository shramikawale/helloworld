from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "<h1>TechAxis Team!!!</h1>"


if __name__ == "__main__":
    server.run(debug=False,host= '0.0.0.0', port='80')
