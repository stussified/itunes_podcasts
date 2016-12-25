from flask import Flask, render_template, url_for
from scraper import podcast_episode_parser, podcast_parser, genre_scraper
app = Flask(__name__)

@app.route('/')
def genres():
	genre_list = genre_scraper()
	return render_template("genre_list.html", genre_list = genre_list)

# @app.route("/episode_list")
# def episode():

# 	episode_list = podcast_episode_parser("https://itunes.apple.com/ca/podcast/the-joe-rogan-experience/id360084272?mt=2")
# 	return render_template("episode_list.html", episode_list = episode_list)

@app.route("/episode_list/<itunes_url>")
def episodes(itunes_url):
	episode_list = podcast_episode_parser(itunes_url)
	return render_template("episode_list.html", episode_list = episode_list)


@app.route("/podcast_list/<itunes_url>")
def podcasts(itunes_url):
	podcast_list = podcast_parser(itunes_url)
	return render_template("podcast_list.html", podcast_list = podcast_list)

if __name__ == "__main__":
	app.run()