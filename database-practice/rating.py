from google.appengine.ext import ndb

#class VideoRating(ndb.Model):
#    id = ndb.StringProperty()
#    likes = ndb.IntegerProperty()
#    dislikes = ndb.IntegerProperty()

class SongInfo(ndb.Model):
    title = ndb.StringProperty()
    artist = ndb.StringProperty()
    year = ndb.IntegerProperty()
