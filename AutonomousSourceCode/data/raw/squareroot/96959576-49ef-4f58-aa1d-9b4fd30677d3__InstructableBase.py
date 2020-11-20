import jsonpickle

from datetime import datetime
from django.conf import settings
from InstructableAuthor import InstructableAuthor


class InstructableBase(object):
    API_QUERY_TYPE = "id"
    API_ID_PARAM = "id"
    API_GET_ACTION = "showInstructable"
    
    def __init__(self,
                 siteid="",
                 url="",
                 title="",
                 author=InstructableAuthor(),
                 category="",
                 channel="",
                 squareThumb="",
                 rectangleThumb="",
                 views=0,
                 favorites=0,
                 type="",
                 date=None):
        self.siteid = siteid
        self.url = url
        self.title = title
        self.author = author
        self.category = category
        self.channel = channel
        self.bigSquareImage = squareThumb
        self.squareImage = squareThumb.replace("SQUARE3", "SQUARE")
        self.rectangleThumb = rectangleThumb
        self.views = views
        self.favorites = favorites
        cdnstring = "http://cdn.instructables.com"
        if settings.REMOTE_ROOT_URL not in self.rectangleThumb and cdnstring not in self.rectangleThumb:
            self.rectangleThumb = settings.REMOTE_ROOT_URL + self.rectangleThumb
        self.type = type
        self.date = date

    def json(self):
        return jsonpickle.encode(self)

    def __unicode__(self):
        return self.title + " by " + self.author
