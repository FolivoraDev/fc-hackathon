import json
import os

import requests
from django.http import HttpResponse

from config.settings import SECRET_DIR


def kakao_view(request):
    headers = {
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    secrets = json.load(open(os.path.join(SECRET_DIR, 'keys.json')))
    header = secrets['Authorization']

    params = {
        'cid': 'TC0ONETIME',
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
    }

    response = json.load(open(os.path.join(SECRET_DIR, '1.json')))
    params['tid'] = response['tid']
    params['pg_token'] = request.GET['pg_token']

    response = requests.post(
        'https://kapi.kakao.com/v1/payment/approve', headers=headers, params=params)

    print(response)

    return HttpResponse(response.text)
