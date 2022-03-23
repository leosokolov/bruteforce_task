from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def main():
    number = request.args.get('number')
    if not number:
        return render_template("index.html")

    if number != "7998":
        return render_template("fail.html")
    else:
        return render_template("success.html")


if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
