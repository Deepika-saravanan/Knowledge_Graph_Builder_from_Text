from flask import Flask, render_template, request
import os

app = Flask(__name__)

DATA_PATH = "data/raw_text/tech_articles.txt"

@app.route("/", methods=["GET", "POST"])
def index():
    message = None

    if request.method == "POST":
        user_text = request.form.get("text")

        if user_text.strip():
            # overwrite dataset with user input
            with open(DATA_PATH, "w", encoding="utf-8") as f:
                f.write(user_text)

            # run pipeline
            os.system("python src/pipeline.py")

            message = "Knowledge graph created successfully."

    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
