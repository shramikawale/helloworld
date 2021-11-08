from flask import Flask
server = Flask(__name__)

@server.route("/")
def hello():
    return "TechAxis Team!!!"


if __name__ == "__main__":
    server.run(debug=False,host= '0.0.0.0', port='80')
