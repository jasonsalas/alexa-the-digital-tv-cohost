# Alexa, the digital co-host
-------
This skill is an on-air/online assistant using [Alexa](https://developer.amazon.com/alexa) for the [Amazon Echo](https://www.amazon.com/Amazon-Echo-And-Alexa-Devices/b?ie=UTF8&node=9818047011) family of smartspeakers. It was built using the [Flask-Ask](http://flask-ask.readthedocs.io/en/latest/) microframework for Python. The service debuted on KUAM's pop culture show [_In the Mix_](https://youtu.be/7FDfpSDh1Mo) with [Sabrina Salas Matanane](https://www.instagram.com/sabrinasalasmatanane/) on January 11, 2018 on KUAM, featuring canned responses spoken during bi-directional dialogue with Sabrina as the episode's presenter. 

A one-off question/response conversational flow defines the [VUI](https://en.wikipedia.org/wiki/Voice_user_interface) between Sabrina and the responding digital device. The human talent announces a series of specific questions with the Alexa skill rendering the appropriate voice template response.

While the featured interaction was simple utterances and spoken canned statements, as a demo a more dynamic function shows off a lookup feature to query showtimes for KUAM special productions tapping a simple inline Python dictionary as a data store. 

![Sabrina &amp; Alexa](http://jasonsalas.com/kuam/bri-alexa.jpg "Sabrina & Alexa")

## Usage
-------
INVOCATION:

```
Alexa, start digital cohost

Alexa, ask digital cohost 
what do we have on this week's show
where can people go to find out more
who's your favorite star wars character
what's your ride or die makeup product
we're cool right
take us home
when does {show} come on our channels
```

Notice how because the default audience for the skill is the Guam-centric news market, the phonemes of municipalities, surnames and certain words are adjusted to Chamorro pronunciation using [SSML](https://developer.amazon.com/docs/custom-skills/speech-synthesis-markup-language-ssml-reference.html). In addition, several adjustments are made within the voice user interface template to read-back words in a more clear fashion (i.e., "bar net" instead of "Barnett").


## Architecture
-------
This skill uses the [hosting pattern](https://developer.amazon.com/blogs/post/Tx14R0IYYGH3SKT/Flask-Ask-A-New-Python-Framework-for-Rapid-Alexa-Skills-Kit-Development) of [tunneling access to a localhost HTTP server](https://pythonprogramming.net/testing-deploying-alexa-skill-flask-ask-python-tutorial/) via [ngrok](https://ngrok.com/) rather an an [AWS Lambda function](https://aws.amazon.com/lambda/).
