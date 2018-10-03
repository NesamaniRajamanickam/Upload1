from flask import Flask, request, render_template
import pandas as pd
from pandas import DataFrame

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_excel(request.files.get('file'))
        df = pd.DataFrame(df)
        return render_template('upload.html', shape=df.to_html())
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
