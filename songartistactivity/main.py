
from key import CreateArtist
from key import Song
import webapp2
import datetime
import jinja2
import os

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

artist = CreateArtist(artist_name = "hhgfdh", birthday = datetime.date(1992, 12, 1))
artist_key = artist.put()

class ArtistHandler(webapp2.RequestHandler):
    def get(self):
        stored_artistkey = artist_key.get()
        self.response.write('Hello world!')

class SongHandler(webapp2.RequestHandler):
    def get(self):
        song_title = Song(title = 'kjhgkjdh', release_year = 2004, performer = artist_key)
        song_key = song_title.put()
        stored_songkey = song_key.get()
        self.response.write('Hello world!')

class ListSongsHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('static/song_template.html')
        self.response.out.write(template.render())


app = webapp2.WSGIApplication([
    ('/create_artist', ArtistHandler),
    ('/create_song', SongHandler),
    ('/list_songs', ListSongsHandler)
], debug=True)
