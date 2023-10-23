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
