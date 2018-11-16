# Create your views here.
import json
import os

import requests
from django.shortcuts import redirect

from config.settings import SECRET_DIR


def pay_view(request):
    header = {
        "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
    }
    secrets = json.load(open(os.path.join(SECRET_DIR, 'keys.json')))
    header = secrets['Authorization']

    params = {
        'cid': 'TC0ONETIME',
        'partner_order_id': 'partner_order_id',
        'partner_user_id': 'partner_user_id',
        'item_name': '초코파이',
        'quantity': '1',
        'total_amount': '2200',
        'vat_amount': '200',
        'tax_free_amount': '0',
        'approval_url': 'http://localhost:8000',
        'fail_url': 'http://localhost:8000',
        'cancel_url': 'http://localhost:8000',
    }

    response = requests.post(
        'https://kapi.kakao.com/v1/payment/ready', headers=header, params=params)

    with open(os.path.join(SECRET_DIR, '1.json'), 'w') as fp:
        json.dump(response.json(), fp)

    # print(response.__dict__.get('next_redirect_pc_url'))

    data = json.loads(response.text)

    return redirect(data['next_redirect_pc_url'])
    # return HttpResponse(data['next_redirect_pc_url'])
