import requests
from requests.utils import quote, unquote
from bs4 import BeautifulSoup

class Episode:

	def __init__(self, artist_name, podcast_name, episode_name, episode_url):
		self.artist_name = artist_name
		self.podcast_name = podcast_name
		self.episode_name = episode_name
		self.episode_url = episode_url



def podcast_episode_parser(url):
	url = unquote(url)
	episode_list = []
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		table_row = soup.find_all("tr")
		for row in table_row:
			try:
				new_episode = Episode(row["preview-artist"],
									  row["preview-album"],
									  row["preview-title"],
									  row["audio-preview-url"])
				episode_list.append(new_episode)
			except KeyError:
				pass
	return episode_list

def podcast_parser(url):
	url = unquote(url)
	list_of_parsed_podcasts = []
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		podcast_div = soup.find("div", {"id":"selectedcontent"})
		podcast_list = podcast_div.find_all("li")
		for podcast in podcast_list:
			podcast_url = podcast.find("a")
			podcast_url = quote(podcast_url.get("href"), safe='')
			podcast_name = podcast.text 

			podcast_info = {
				"podcast_name": podcast_name,
				"podcast_url": podcast_url
			}
			list_of_parsed_podcasts.append(podcast_info)

	return list_of_parsed_podcasts


def genre_scraper():
	list_of_genres = []
	url = "https://itunes.apple.com/ca/genre/podcasts/id26?mt=2"
	r = requests.get(url)
	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		genre_div = soup.find("div", {"id": "genre-nav"})
		top_level_genres = genre_div.find_all("a", {"class":"top-level-genre"})

		for top_level_genre in top_level_genres:
			genre_url = quote(top_level_genre.get("href"), safe='')
			genre_name = top_level_genre.text

			genre_info = {
				"genre_name": genre_name,
				"genre_url": genre_url
			}
			list_of_genres.append(genre_info)

	return list_of_genres



def main():

	# podcast_episode_parser("https://itunes.apple.com/ca/podcast/the-joe-rogan-experience/id360084272?mt=2")
	# podcast_parser("https://itunes.apple.com/ca/genre/podcasts-comedy/id1303?mt=2")
	print genre_scraper()
if __name__ == "__main__":
	main()