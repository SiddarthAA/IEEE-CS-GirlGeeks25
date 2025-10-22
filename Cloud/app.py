from flask import Flask, render_template, request
import os
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    app.logger.info("Home page accessed")
    return render_template("home.html")

@app.route('/about')
def about():
    app.logger.info("About page accessed")
    return render_template("about.html")

@app.route('/healthz')
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
