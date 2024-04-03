from flask import Flask, render_template_string
import time

app = Flask(__name__)

@app.route('/')
def hello_earth():
    # Introduce a delay of 5 seconds
    time.sleep(5)
    
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hello Earth</title>
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }

        .hello-earth {
            font-size: 48px;
            color: #0000ff; /* Blue color */
        }
    </style>
    </head>
    <body>
        <div class="hello-earth">Hello Earth</div>
    </body>
    </html>
    """
    return render_template_string(html_content)

if __name__ == '__main__':
    app.run(debug=True)

