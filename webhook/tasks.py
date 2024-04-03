import time
import requests


def process_subscription_payment(payment_info, callback_url):
    print('Processing payment')
    # simulating a slow process
    time.sleep(5)
    payment_id = str(payment_info['payment_id'])
    body = {
        'payment_id': str(payment_id),
        'processed_value': payment_info['value'],
        'product': payment_info['product'],
        'status': 'success'
    }
    print('Sending Request')
    response = requests.post(callback_url, json=body)
    if response.ok:
        print('Payment processed')
    else:
        print(f'Payment Failed with response: {response.content}')
