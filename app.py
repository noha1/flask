from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
blog = {
    'name': 'My awesome blog',
    'posts': {
        0: {
            'post_id': 0,
            'title': " my first post",
            'content': 'content is here',
        }
    }
}


@app.route('/')
def home():
    return render_template('home.jinja2', blog=blog)


@app.route('/post/<int:post_id>')
def post(post_id):
    post = blog['posts'].get(post_id)
    print(post)
    if not post:
        return render_template('404.jinja2', message=f'A post with id {post_id} was not found.')

    return render_template('post.jinja2', post=post)


@app.route('/post/form')
def form():
    return render_template('create.jinja2')


@app.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        title = request.form.get('title')  # This takes the 'Hello' from the title query string parameter
        content = request.form.get('content')
        post_id = len(blog['posts'])
        # This just gives us a new post_id as the number of posts currently existing (thing of it as an auto-increment).
        blog['posts'][post_id] = {'id': post_id, 'title': title, 'content': content}
        return redirect(url_for('post', post_id=post_id))
    render_template('create.jinja2')


if __name__ == '__main__':
    app.run(debug=True)
