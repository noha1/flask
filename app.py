from flask import Flask, render_template

app = Flask(__name__)
blog = {
    'name': 'My awesome blog',
    'posts': {
        0: {
            'title': " my first post",
            'content': 'content is here',
        }
    }
}


@app.route('/')
def home():
    return render_template('home.html', blog=blog)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog['posts'].get(post_id)
    print(post)
    if not post:
        return render_template('404.html', message=f'A post with id {post_id} was not found.')

    return render_template('post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True)
