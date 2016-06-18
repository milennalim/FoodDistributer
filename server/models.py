import logging
from google.appengine.ext import ndb

class Comment(ndb.Model):
    created = ndb.DateTimeProperty(auto_now_add=True)
    text = ndb.StringProperty()
    author = ndb.StringProperty()

class FoodEvent(ndb.Model):
    foodType = ndb.StringProperty()
    address = ndb.StringProperty()
    image64 = ndb.StringProperty()
    created = ndb.DateTimeProperty(auto_now_add=True)

def comment_to_json(comment):
    return {
        'key': comment.key.urlsafe(),
        'created': str(comment.created),
        'text': comment.text,
        'author': comment.author
    }
def FoodEvent_to_json(event):
    return {
        'key': event.key.urlsafe(),
        'food': event.foodType,
        'address': event.address,
        'image': event.image64,
        'time': event.created
    }