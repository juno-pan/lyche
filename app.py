from flask import Flask,render_template

app = Flask(__name__)

@app.route('/index.html')
def index():  # put application's code here
    return render_template("index.html")

@app.route('/wordcloud.html')
def wordcloud():  # put application's code here
    return render_template("wordcloud.html")

@app.route('/about.html')
def about():  # put application's code here
    return render_template("about.html")


@app.route('/email-template.html')
def email_template():  # put application's code here
    return render_template("email-template.html")


@app.route('/zhu.html')
def zhu():  # put application's code here
    return render_template("zhu.html")

@app.route('/error.html')
def error():  # put application's code here
    return render_template("error.html")

@app.route('/bin.html')
def bin():  # put application's code here
    return render_template("bin.html")

if __name__ == '__main__':
#     debug
    app.run(debug=True)

