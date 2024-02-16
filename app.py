from flask import Flask, render_template
import win32print

app = Flask(__name__)

def get_default_printer():
    try:
        default_printer = win32print.GetDefaultPrinter()
        return default_printer
    except Exception as e:
        return str(e)

@app.route('/')
def index():
    default_printer = get_default_printer()
    return render_template('index.html', default_printer=default_printer)

if __name__ == '__main__':
    app.run(debug=True)
