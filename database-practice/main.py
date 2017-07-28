#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#from rating import VideoRating
#import webapp2

#class MainHandler(webapp2.RequestHandler):
#    def get(self):
#        rating = VideoRating(id = 'Thelma and Louise', likes = 2,dislikes = 1)
#        key = rating.put()
#        stored = key.get()
#        VideoRating(id='Gangnam Style',likes = 23, dislikes = 6).put()
#        VideoRating(id= 'Cute Cats',likes = 23, dislikes = 0).put()
#        VideoRating(id= 'Cute Dogs',likes = 50, dislikes = 0).put()
#        VideoRating(id= 'Weird Al',likes = 0, dislikes = 27).put()

#        self.response.write("Done!")

        #self.response.write(stored.id + ' has ' + str(stored.likes) + ' likes.')
from rating import SongInfo
import webapp2
import date


#class SongsHandler(webapp2.RequestHandler):
#    def get(self):
#        song = SongInfo(title = 'Fireflies', artist = 'Owl City', year = 2009)
#        key = song.put()
#        stored = key.get()
        SongInfo(title = 'Shape of You ', artist = 'Ed Sheeran', year = 2017).put()
        SongInfo(title = 'Bye Bye Bye', artist = 'Nsync', year = 2000).put()
        SongInfo(title = 'Love the Way You Lie ', artist = 'Eminem', year = 2010).put()

        self.response.write("Done!")

    #    all_songs_query = SongInfo.query()
    #    songs_year = all_songs_query.fetch()
         all_songs_query = SongInfo.query().order
         songs_year = all_songs_query.fetch()
    #    for change in songs_year:
    #        change.year = 100000000
    #        change.put()



app = webapp2.WSGIApplication([
    ('/', SongsHandler)
], debug=True)
