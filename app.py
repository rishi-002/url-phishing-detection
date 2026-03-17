from flask import Flask, render_template, request, jsonify
import pickle
import re

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


# API for live stats
@app.route("/stats")
def stats():
    return jsonify({
        "scans": scan_count,
        "phishing": phishing_count,
        "safe": safe_count
    })


# contact form route
@app.route("/contact", methods=["GET","POST"])
def contact():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        print("Support Request")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        return "Message sent successfully!"

    return render_template("contact.html")

@app.route("/subscribe", methods=["POST"])
def subscribe():

    email = request.form["email"]

    with open("subscribers.txt","a") as f:
        f.write(email + "\n")

    return render_template("index.html", predict="Subscribed successfully!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)