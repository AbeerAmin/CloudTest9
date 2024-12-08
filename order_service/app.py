from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_order():
    return 'Hello from Order Service'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
