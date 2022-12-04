import pandas as pd
from matplotlib.figure import Figure
from flask import Flask, render_template
from io import BytesIO
import base64

app = Flask(__name__)

@app.route("/")

@app.route("/classification")
def index():
    # DATAFRAME
    df = pd.read_csv('iris.csv')
    df = df.sample(n=5)
    info = df.describe().to_html()  # Render a DataFrame as an HTML table.
    x = df.copy()
    y = x.pop('Species')

    # PLOT
    # Generate the figure without using pyplot.
    fig = Figure()
    ax = fig.subplots()
    ax.scatter(x.iloc[:, 0], x.iloc[:, 1])  # first and second columns
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")

    return render_template("class.html", plot=data, info=info, df=df.head().to_html())


if __name__ == "__main__":
    app.run(debug=True)
