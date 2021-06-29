from flask import Flask, render_template, request
from static.recommend import recommend_movie

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    movie_name = request.form.get('Movie Name')
    pred = recommend_movie(movie=movie_name)
    return render_template('index.html',
                            prediction_text='Recommended Movies {}'.format(pred),
                            data=pred, len=len(pred))

if __name__ == "__main__":
    app.run()

    