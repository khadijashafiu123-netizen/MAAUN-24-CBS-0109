from flask import Flask, render_template, request, redirect
from models import Business, BusinessDirectory

app = Flask(__name__, template_folder='assginment4')

directory = BusinessDirectory()

@app.route('/')
def home():
    return render_template(
        "index.html",
        businesses=directory.businesses,
        recent=directory.get_recent()
    )


@app.route('/add', methods=['GET', 'POST'])
def add_business():
    if request.method == 'POST':
        name = request.form['name']
        category = request.form['category']

        new_business = Business(name, category)
        directory.add_business(new_business)

        return redirect('/')

    return render_template("add_business.html")


if __name__ == '__main__':
    app.run(debug=True)