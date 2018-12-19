import os
import requests


GRAPH_URL = "https://graph.facebook.com/v2.6"
ACCESS_TOKEN = "EAAf7MZAZBKZBBABAC1wCmJyRHkxtDqxsB3YGkZColnCLSPJzYmzAb1d6B2NLJGTfJB6CUCFMmuHwqZCClBhYPDyIOGDrBf0K8Fh4ZCSfhQUpHFTEBeXFIvxk5v8PWJJaIfrsWFHaGtezmZAnGZAxp5Kie3TfJegUWtocsSZC6zGRFPspnqXCBjfG2"

def send_text_message(id, text):
    url = "{0}/me/messages?access_token={1}".format(GRAPH_URL, ACCESS_TOKEN)
    payload = {
        "recipient": {"id": id},
        "message": {"text": text}
    }
    response = requests.post(url, json=payload)

    if response.status_code != 200:
        print("Unable to send message: " + response.text)
    return response


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
