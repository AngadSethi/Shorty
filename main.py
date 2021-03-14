from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def root():
    if request.args.get('summary'):
        return render_template('index.html', summary=request.args.get('summary'))
    return render_template('index.html')


@app.route('/shorten', methods=['POST'])
def shorten():
    if request.method == 'POST':
        from summarizer import Summarizer
        model = Summarizer('bert-base-uncased')
        result = model(request.values.get('text'))
        full = ''.join(result)
        return full

    return render_template('index.html')


@app.route('/summary', methods=['GET'])
def summary():
    return render_template('summary.html', summary=request.args.get('summary'))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)