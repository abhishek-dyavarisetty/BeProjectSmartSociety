from __future__ import print_function
import numpy as np
import urllib
import logging
import json
import socket
socket.setdefaulttimeout(15)

# Helpers that build all of the responses
def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
}

def recognize(event, context):
    card_title = "Recognition"
    try:
        response = urlopen('http://$TUNNELNAME.localtunnel.me/faces')
        data = response.read()
        if (data== "Not Found"):
            speech_output = "i cannot able to see any face" 
        else:
                person, gender, emotion = data.split(",")
                if person == "" or person is None:
                    speech_output = "i have not recognized you"
                else:
                    speech_output = "i have recognized you welcome to to the society %s" % person

                
    except urllib.error.HTTPError as e:
        speech_output = "Some thing went worng"
    except socket.timeout as e:
        speech_output = "system Timed out"

    else:
        speech_output = "i am not getting what you are saying about"
        
    should_end_session = False
    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))

def cancel_intent():
    return build_response({}, build_speechlet_response("cancel_intent", "You want to cancel", None, "true"))


def help_intent():
    return build_response({}, build_speechlet_response("cancel_intent", "You want help", None, "true"))


def stop_intent():
    return build_response({}, build_speechlet_response("stop_intent", "You want to stop", None, "true"))

def on_launch(event, context):
	return build_response({}, build_speechlet_response("title", "body", None, "true"))

def intent_router(event, context):
    intent = event['request']['intent']['name']

    # Custom Intents

    if intent == "recognize_intent":
        return recognize(event, context)

    # Required Intents

    if intent == "AMAZON.CancelIntent":
        return cancel_intent()

    if intent == "AMAZON.HelpIntent":
        return help_intent()

    if intent == "AMAZON.StopIntent":
        return stop_intent()

#Lambda Hnadler
def lambda_handler(event, context):
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event, context)

    elif event['request']['type'] == "IntentRequest":
        return intent_router(event, context)