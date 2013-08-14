# @UnresolvedImport
from google.appengine.ext import ndb
import cgi # @UnresolvedImport
import urllib # @UnresolvedImport
import json  # @UnresolvedImport
import webapp2


class WeatherEntry(ndb.Model):
  zipcode = ndb.StringProperty()
  date = ndb.StringProperty()
  temp = ndb.StringProperty()
  dateTime = ndb.DateTimeProperty(auto_now=True)


  @classmethod
  def queryZip(cls, zip):
    return cls.query(cls.zipcode==zip).order(-cls.dateTime)


class QueryWeather(webapp2.RequestHandler):
  def get(self):
     zipcode = self.request.get('zipcode')
     weaths = WeatherEntry.queryZip(zipcode).fetch(20)
     
     self.response.headers['Content-Type'] = 'application/json'  
     for weath in weaths: 
        obj = {
           'zipcode': weath.zipcode, 
           'date': weath.date,
           'temperature' : weath.temp
        } 
        self.response.out.write(json.dumps(obj))
     

class InsertWeather(webapp2.RequestHandler):  # @IndentOk
  def get(self):
    # We set the parent key on each 'Greeting' to ensure each guestbook's
    # greetings are in the same entity group.
    zip = self.request.get('zipcode')
    temp = self.request.get('temp')
    date = self.request.get('date')
    weath = WeatherEntry(zipcode=zip, date=date, temp=temp )
    weath.put()

app = webapp2.WSGIApplication([
  ('/query', QueryWeather),
  ('/modify', InsertWeather),
])