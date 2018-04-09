from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('QBGl/cJZyZA9QMc+TcTikbtDMLQvwt7V8zbFng/11WByoeSUyUgZrYReBt9AHpDKAIxafRgo14ipNvEs9t1Hvhd1xaCS5EBxWmEX48CvsyTLtuipj+6DVDU+5hMPlAXbWIbt8cawOtQo77cjGRURbQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('77f7f3417f5b1bab0bee05357e0b3935')


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