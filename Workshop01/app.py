from flask import Flask, render_template
import random

app = Flask(__name__)

# List of possible dynamic texts
dynamic_texts = [
    "Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who know binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies, and the other is to make it so complicated that there are no obvious deficiencies."
]

@app.route("/")
def index():
    random_text = random.choice(dynamic_texts)
    return render_template("index.html", dynamic_text=random_text)

if __name__ == "__main__":
    app.run(debug=True)