from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    
    context = {
        'nums': list(range(9+1)),
        'like': {
            '好きな色' : '青',
            '好きな音楽' : 'KPOP',
            '好きな映画' : 'シザーハンズ',
        },
        'flag': True,
    }
    
    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(port=8080)
