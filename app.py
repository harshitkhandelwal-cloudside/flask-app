from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def hello():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello World</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }

        .hello-world {
            font-size: 48px;
            color: #ff0000; /* Red color */
        }
    </style>
    </head>
    <body>
        <div class="hello-world">Hello World</div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

