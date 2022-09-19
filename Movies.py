from crypt import methods
import json
from flask import Flask,jsonify,request
import csv

all_movies = []
liked_movies = []
disliked_movies = []
not_watched_movies = []

with open("movies.csv",encoding="utf-8") as f:
    csv_reader = csv.reader(f)
    data = list(csv_reader)
    all_movies = data[1:]

app = Flask(__name__)

@app.route("/get_movie")
def get_movie():
    return jsonify({
        "data" : all_movies[0],
        "status" : "success",
    })

@app.route("/liked_movie",methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    return jsonify({
        "status" : "success"
    })

@app.route("/disliked_movie",methods=["POST"])
def disliked_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    disliked_movies.append(movie)
    return jsonify({
        "status" : "success"
    })

@app.route("/not_watched_movie",methods=["POST"])
def not_watched_movies():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    not_watched_movies.append(movie)
    return jsonify({
        "status" : "success"
    })



app.run()