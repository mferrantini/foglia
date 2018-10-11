from flask import Flask

# Flask webserver setup
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello!"

# Run server
if __name__ == '__main__':
    app.run()