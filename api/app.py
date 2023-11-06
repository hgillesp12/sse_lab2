from flask import Flask, render_template, send_from_directory, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/home")
def hello_world():
    return render_template("index.html")


@app.route("/user")
def hello_world():
    return render_template("GitHub.html")


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


@app.route('/username_submit', methods=["POST"])
def username_submit():
    username = request.form.get("username")
    return render_template("username_response.html",
                           username=username)


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
    elif "square and a cube" in input_text:
        return str(process_square_and_cube(input_text))
    elif "minus" in input_text:
        return str(subtraction(input_text))
    elif "multiplied" in input_text:
        return multiply(input_text)
    elif "primes" in input_text:
        return find_prime(input_text)
    else:
        return "Unknown"


def process_square_and_cube(input_text):
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

    for number in numbers:
        square_root = round(number ** (1/2))
        cube_root = round(number ** (1/3))
        if (cube_root ** 3 == number) and (square_root ** 2 == number):
            return number


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


def subtraction(input_text):
    x = input_text.split()
    num1 = x[2]
    num2 = x[4][:-1]
    temp = int(num1) - int(num2)
    return str(temp)


def multiply(input_text):
    x = input_text.split()
    num1 = x[2]
    num2 = x[5][:-1]
    temp = int(num1) * int(num2)
    return str(temp)


def find_prime(input_text):
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
    prime_numbers = []
    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
