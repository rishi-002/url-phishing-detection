from flask import Flask, render_template, request, jsonify, redirect, url_for
import pickle
import re
import os

app = Flask(__name__)

vector = pickle.load(open("vectorizer.pkl", 'rb'))
model = pickle.load(open("phishing.pkl", 'rb'))

# counters
scan_count = 0
phishing_count = 0
safe_count = 0


@app.route("/", methods=['GET', 'POST'])
def index():

    global scan_count, phishing_count, safe_count

    predict = ""

    if request.method == "POST":

        url = request.form['url']

        cleaned_url = re.sub(r'^https?://(www\.)?', '', url)

        result = model.predict(vector.transform([cleaned_url]))[0]

        scan_count += 1

        if result == 'bad':
            predict = "This is a Phishing website !!"
            phishing_count += 1

        elif result == 'good':
            predict = "This is a healthy and safe website !!"
            safe_count += 1

        else:
            predict = "Something went wrong !!"

    return render_template("index.html", predict=predict)


import json
import os

# In-memory URL store (use a database for production)
url_store = {}

@app.route("/shortener")
def shortener():
    return render_template("urlshortener.html")


@app.route("/shorten", methods=["POST"])
def shorten():
    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = data["url"]
    alias = data.get("alias", "")

    # Generate random alias if not provided
    if not alias:
        import random, string
        alias = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    # Check if alias already taken
    if alias in url_store and url_store[alias] != url:
        return jsonify({"error": "Alias already taken"}), 409

    url_store[alias] = url
    short_url = request.host_url + "s/" + alias
    return jsonify({"short_url": short_url, "alias": alias})


@app.route("/s/<alias>")
def redirect_short(alias):
    from flask import redirect as flask_redirect
    if alias in url_store:
        return flask_redirect(url_store[alias])
    return "Short URL not found", 404


@app.route("/qr")
def qr_scanner():
    return render_template("qr.html")


# QR code URL checker — called by the QR scanner on the frontend
@app.route("/qr-check", methods=["POST"])
def qr_check():
    global scan_count, phishing_count, safe_count

    data = request.get_json()
    if not data or "url" not in data:
        return jsonify({"error": "No URL provided"}), 400

    url = data["url"]
    cleaned_url = re.sub(r'^https?://(www\.)?', '', url)
    result = model.predict(vector.transform([cleaned_url]))[0]
    scan_count += 1

    if result == "bad":
        phishing_count += 1
        label = "phishing"
    else:
        safe_count += 1
        label = "safe"

    return jsonify({"url": url, "result": label})


# API for live stats
@app.route("/stats")
def stats():
    return jsonify({
        "scans": scan_count,
        "phishing": phishing_count,
        "safe": safe_count
    })


# contact form route
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print("Support Request")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        # Redirect with success flag so the page can show a confirmation
        return redirect(url_for('contact') + '?sent=1')

    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


@app.route("/cookies")
def cookies():
    return render_template("cookies.html")


@app.route("/subscribe", methods=["POST"])
def subscribe():

    email = request.form["email"]

    with open("subscribers.txt", "a") as f:
        f.write(email + "\n")

    return render_template("index.html", predict="✓ Subscribed successfully!")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
