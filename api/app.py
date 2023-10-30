from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/images/<path:path>')
def serve_static(path):
    return send_from_directory('static/images', path)


@app.route('/submit', methods=["POST"])
def submit():
    input_name = request.form.get("name")
    flavor_rating = request.form.get("rating")
    return render_template("flavor_response.html",
                           name=input_name,
                           flavor=flavor_rating,
                           image_link=load_image(flavor_rating))


def load_image(flavor_rating):
    if flavor_rating == "Chocolate":
        return "images/chocolate.jpg"
    elif flavor_rating == "Mint Chocolate":
        return "images/mint.jpg"
    elif flavor_rating == "Pistachio":
        return "images/pistachio.jpg"
    elif flavor_rating == "Strawberry":
        return "images/strawberry.jpg"
    else:
        return "images/imperial_logo.png"


@app.route("/query")
def query():
    input_text = request.args.get('q')
    return process_query(input_text)


def process_query(input_text):
    if "dinosaurs" in input_text:
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif "name" in input_text:
        return "Ctrl+Alt+Defeat"
    elif "plus" in input_text:
        return sumof(input_text)
    elif "Which of the following numbers is the largest" in input_text:
        return str(find_largest(input_text))
    else:
        return "Unknown"


def sumof(input_text):
    x = input_text.split()
    num1 = x[2]
    num2 = x[4][:-1]
    temp = int(num1) + int(num2)
    return str(temp)

    
def find_largest(input_text):
    numbers = []
    current_number = ''
    for char in input_text:
        if char.isdigit():
            current_number += char
        elif current_number:
            numbers.append(int(current_number))
            current_number = ''

    # Add the last number if there is one
    if current_number:
        numbers.append(int(current_number))
    return max(numbers)

    
