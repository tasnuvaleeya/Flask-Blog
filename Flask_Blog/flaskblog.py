from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm


app = Flask(__name__)
app.config["SECRET_KEY"] = '7d48d9f69a6282507470658332bc1ab7'

posts = [
    {
        'author' : 'Tasnuva Zaman',
        'title' : 'Blog Post 1',
        'content' : 'first post content',
        'date_posted' : 'September 14, 2018'
    },
    {
        'author': 'Shahriar Siddik',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'September 17, 2018'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('blog/home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('blog/about.html', title='About')


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # flash('Account Created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))

    return render_template('blog/register.html', title='Register', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You\'ve been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. please check username and password ', 'danger')
    return render_template('blog/login.html', title='Login', form=form)




if __name__ == '__main__':
    app.run(debug=True)
