from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    movies =[4,2,3,4]
    return render_template("homepage.html", movies=movies)
app.run()

if __name__ == '__main__':
    app.run(debug=True)
