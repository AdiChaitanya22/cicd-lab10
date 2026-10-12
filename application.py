from flask import Flask

application = Flask(__name__)

@application.route("/")
def home():
    return """
    <html>
        <head>
            <title>CI/CD Lab 10</title>
        </head>
        <body>
            <h1>CI/CD Pipeline Successfully Deployed!</h1>
            <p>Lab 10 - Application Deployment using AWS</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8000)
