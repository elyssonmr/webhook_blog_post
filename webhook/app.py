from uuid import uuid4
import flask

from flask import request, make_response

from webhook.scheduler import scheduler
from webhook.tasks import process_subscription_payment


app = flask.Flask('webhook_post')

@app.post('/payment')
def process_payment():
    payment_request = request.json
    payment_info = {
        'payment_id': str(uuid4()),
        'value': payment_request['value'],
        'product': payment_request.get('product', 'No product')
    }
    callback_url = payment_request.get('callback_url')
    if not callback_url:
        return make_response({
            "message": "Invalid callback URL"
        }, 400)

    scheduler.add_job(
        process_subscription_payment,
        args=[payment_info, callback_url]
    )

    return make_response({
        "payment_id": payment_info['payment_id'],
        "status": "processing"
    })
