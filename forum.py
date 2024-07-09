from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

# Ein einfacher Speicher für Posts und deren Antworten
posts = []


@app.route('/', methods=['GET'])
def index():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>Simple Forum</title>
        </head>
        <body>
            <h1>Simple Forum</h1>
            <form action="/new_post" method="post">
                <textarea name="content" placeholder="Write your post here..." rows="4" cols="50"></textarea><br><br>
                <button type="submit">Post</button>
            </form>
            <h2>Posts:</h2>
            <ul>
                {% for post in posts %}
                <li>
                    {{ post['content'] }}
                    <form action="/reply/{{ post['id'] }}" method="post">
                        <textarea name="reply_content" placeholder="Reply to this post..." rows="2" cols="50"></textarea><br><br>
                        <button type="submit">Reply</button>
                    </form>
                    {% if post['replies'] %}
                        <ul>
                            {% for reply in post['replies'] %}
                                <li>{{ reply }}</li>
                            {% endfor %}
                        </ul>
                    {% endif %}
                </li>
                {% endfor %}
            </ul>
        </body>
        </html>
    ''', posts=posts)


@app.route('/new_post', methods=['POST'])
def new_post():
    content = request.form['content']
    if content:
        # Jeder Post erhält eine eindeutige ID und eine Liste für Antworten
        posts.append({'id': len(posts) + 1, 'content': content, 'replies': []})
    return redirect(url_for('index'))


@app.route('/reply/<int:post_id>', methods=['POST'])
def reply(post_id):
    reply_content = request.form['reply_content']
    if reply_content:
        # Antwort dem entsprechenden Post zuordnen
        for post in posts:
            if post['id'] == post_id:
                post['replies'].append(reply_content)
                break
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
