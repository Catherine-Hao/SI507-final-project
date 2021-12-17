from flask import render_template, request, Flask
# from SI507_FP import *
import random
from random import choice
from Recommending import *
import json
import requests

# movies = get_movies()
movies_json = movies_json()
app = Flask(__name__)


@app.route("/")
def movie():
    return render_template("movie_recommendation.html")


@app.route('/movie', methods=['POST'])
def recommend_movie():
    html_certificate = request.form["certificate"]
    html_genre1 = request.form["genre1"]
    html_genre2 = request.form["genre2"]
    html_genre3 = request.form["genre3"]
    html_year_min = request.form["year_min"]
    html_year_max = request.form["year_max"]
    html_rating = request.form["rating"]
    html_director = request.form["director"]
    html_cast = request.form["cast"]
    html_runtime_min = request.form["runtime_min"]
    html_runtime_max = request.form["runtime_max"]
    # recommend_urls = recommending_in_progress(movies, html_certificate, html_genre1, html_genre2, html_genre3,
    #                                           html_year_min, html_year_max, html_rating,
    #                                           html_director, html_cast, html_runtime_min, html_runtime_max)
    recommend_urls = recommending_classes(movies_json, html_certificate, html_genre1, html_genre2, html_genre3,
                                              html_year_min, html_year_max, html_rating,
                                              html_director, html_cast, html_runtime_min, html_runtime_max)
    if recommend_urls:
        # r_movie = choice(recommend_urls)
        # r_url = movies['imdb_url'][r_movie]
        # r_review_url = 'https://imdb-api.com/en/API/Reviews/k_z95hbpgk/' + movies['imdb_id'][r_movie]
        # r_title = movies['title'][r_movie]
        r_movie = choice(recommend_urls)
        r_url = r_movie['imdb_url']
        r_review_url = 'https://imdb-api.com/en/API/Reviews/k_z95hbpgk/' + r_movie['imdb_id']
        r_title = r_movie['title']
        response = requests.get(r_review_url)
        r_reviews = response.json()
        if r_reviews['items']:
            # r_review = choice(r_reviews['items'])
            r_renum = len(r_reviews['items'])
            # r_retitle = r_review['title']
            # r_recontent = r_review['content']
            r_review_titles = list(i['title'] for i in r_reviews['items'])
            r_review_contents = list(i['content'] for i in r_reviews['items'])
        else:
            r_renum=1
            r_review_titles = ['Sorry!']
            r_review_contents = ["There\'s no review for this movie!"]

    return render_template('movie_response.html', valid_urls=recommend_urls, title=r_title, review_url=r_review_url,
                           url=r_url, renum = r_renum, reviews = r_reviews, review_contents=r_review_contents, review_titles=r_review_titles)


if __name__ == "__main__":
    app.run(debug=True)
