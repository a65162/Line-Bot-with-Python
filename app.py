import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('6RlFnXAt0g5Of+yNAyoJtFKh5TZIbHT7RU5cTLwg1L06ootQiQyWm2xlXuDtru7EAIxafRgo14ipNvEs9t1Hvhd1xaCS5EBxWmEX48CvsySC5UgP1ivazKErmgp1lP6K0BaDRU2Yo0+VhfZzf+AQswdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('8c9524b0e7862911904b507eca935ecc')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()