from flask import Flask, render_template

app = Flask(__name__)

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
    return render_template('blog/about.html')










if __name__ == '__main__':
    app.run(debug=True)
