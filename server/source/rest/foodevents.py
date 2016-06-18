import json
import logging

from lib.bottle import get, post, request, response

import models

@get('/events/')
def get_all_events():
    logging.info("Getting all food Events!")
    foods = models.Event.query().order(models.Event.created).fetch(100)
    to_return = [models.event_to_json(food) for food in foods]
    response.content_type = 'application/json'
    logging.info(to_return)
    return json.dumps(to_return)


@post('/event')
def create_new_event():
    logging.info("creating new food event")
    logging.info(request.json)
    event = models.Event(
        foodType=request.json.get('food'),
        address=request.json.get('address'),
        image64 = request.json.get('image'),
        time = request.json.get('time')
    )
    event.put()
    response.content_type = 'application/json'
    return models.foodEvent_to_json(event)
