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
import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')
class IndexHandler(webapp2.RequestHandler):
    def get(self):
        html = """<html>
  <head>
    <title> Jasmine's Blogasaurus </title>
    <link rel="stylesheet" href="stylesheet.css"></link>
    <script src="java.js"></script>
  </head>

  <body background = "https://s-media-cache-ak0.pinimg.com/originals/99/73/34/997334584aa2bbda7f4c7adc83aa03d5.jpg">
  <h1 id="header"> Hi! My name is Jasmine! </h1>
    <div id="linkedPosts">
      <h2> Check out what I am doing: </h2>
            <a href="/Users/demouser/Jasminechau2/profile.html"> About me!</a>
        <p>
            <a href="/Users/demouser/Jasminechau2/post.html"> What I did this Summer!</a>
        </p>
      </div>
      <div id="contact">
        <h3 class="randomheaders"> Contact me:<br> </h3>
          <a href="https://twitter.com/jasmocat"> Twitter </a>
        </div>
  </body>
</html>
         """
        self.response.write(html);

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index.html', IndexHandler)
], debug=True)
