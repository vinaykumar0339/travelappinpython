from flask import Flask, request, render_template_string, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

# In-memory storage for notes (in a real app, you would use a database)
notes = []

@app.route('/')
def home():
    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
            <title>Note Taking App</title>
          </head>
          <body>
            <div class="container mt-5">
              <h1 class="mb-4">Notes</h1>
              <a href="/add" class="btn btn-primary mb-3">Add Note</a>
              <ul class="list-group">
                {% for note in notes %}
                <li class="list-group-item">
                  <h5>{{ note.title }}</h5>
                  <p>{{ note.content }}</p>
                </li>
                {% else %}
                <li class="list-group-item">No notes yet.</li>
                {% endfor %}
              </ul>
            </div>
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
          </body>
        </html>
    ''', notes=notes)

@app.route('/add', methods=['GET', 'POST'])
def add_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        # Validate form fields
        if not title or not content:
            flash('Title and content cannot be empty!', 'danger')
        else:
            notes.append({'title': title, 'content': content})
            flash('Note added successfully!', 'success')
            return redirect(url_for('home'))

    return render_template_string('''
        <!doctype html>
        <html lang="en">
          <head>
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
            <title>Add Note</title>
          </head>
          <body>
            <div class="container mt-5">
              <h1 class="mb-4">Add Note</h1>
              <form method="post">
                <div class="form-group">
                  <label for="title">Title</label>
                  <input type="text" class="form-control" id="title" name="title" placeholder="Enter Title">
                </div>
                <div class="form-group">
                  <label for="content">Content</label>
                  <textarea class="form-control" id="content" name="content" rows="3" placeholder="Enter Content"></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Add Note</button>
              </form>
            </div>
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
          </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
