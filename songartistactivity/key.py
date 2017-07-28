from google.appengine.ext import ndb

class CreateArtist(ndb.Model):
      artist_name = ndb.StringProperty()
      birthday = ndb.DateProperty()

class Song(ndb.Model):
      title = ndb.StringProperty()
      release_year = ndb.IntegerProperty()
      performer = ndb.KeyProperty(CreateArtist)
