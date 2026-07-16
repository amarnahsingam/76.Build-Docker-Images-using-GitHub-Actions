from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route('/')
def welcome():
    return "<h1>Welcome to GitHub Actions!</h1>"

# Run the application on all available network interfaces
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
