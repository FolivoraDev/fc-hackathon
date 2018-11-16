# Create your views here.
import json
import os

import requests
from django.shortcuts import redirect

from config.settings import SECRET_DIR
from post.models import Comment, Post


def pay_view(request, pk):
    if request.method == 'POST':
        headers = {
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
        }
        params = {
            'cid': 'TC0ONETIME',
            'partner_order_id': 'partner_order_id',
            'partner_user_id': 'partner_user_id',
            'item_name': '후원하기',
            'quantity': '1',
            'tax_free_amount': '0',
            'approval_url': 'http://localhost:8000',
            'fail_url': 'http://localhost:8000',
            'cancel_url': 'http://localhost:8000',
        }

        secrets = json.load(open(os.path.join(SECRET_DIR, 'keys.json')))
        headers['Authorization'] = secrets['Authorization']

        params['total_amount'] = request.POST['price']
        params['vat_amount'] = round(int(request.POST['price']) / 11)

        response = requests.post(
            'https://kapi.kakao.com/v1/payment/ready', headers=headers, params=params)

        params['pk'] = pk

        with open(os.path.join(SECRET_DIR, '1.json'), 'w') as fp:
            json.dump(response.json(), fp)

        # print(response.__dict__.get('next_redirect_pc_url'))

        data = json.loads(response.text)

        Comment.objects.create(
            post=Post.objects.get(pk=pk),
            author=request.user,
            content="%s님이 %s원 후원!" % (request.user, params['total_amount']),
            password=123,
        )

        # return HttpResponse(response.text)
        return redirect(data['next_redirect_pc_url'])
        # return HttpResponse(data['next_redirect_pc_url'])
