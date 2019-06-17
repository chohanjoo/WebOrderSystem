import requests
headers = {
    'Authorization':'KakaoAK 3f5b63af3e3b694fba0f2bbd4ad341ef',
    'Content-type':'application/x-www-form-urlencoded;charset=utf-8',
}

data={
    'cid':'TC0ONETIME',
    'partner_order_id':'partner_order_id',
    'partner_user_id':'partner_user_id',
    'item_name':'americano',
    'quantity':1,
    'total_amount': 2000,
    'vat_amount' : 200,
    'tax_free_amount' : 0,
    'approval_url' : 'http://127.0.0.1:8000/orderingQueue/',
    'fail_url' : 'http://127.0.0.1:8000/accounts/login/',
    'cancel_url' : 'http://127.0.0.1:8000/accounts/join/'
}

def insert_shop_name(shopName):
    data['item_name'] = shopName
    return data


def insert_success_url(success_url):
    data['approval_url'] = success_url
    return data


def kakaopay_request(self):
    result = requests.post("https://kapi.kakao.com/v1/payment/ready",headers=headers,data=data)
    return result.json()['next_redirect_pc_url']



# result = requests.post("https://kapi.kakao.com/v1/payment/ready",headers=headers,data=data)



# def post_init():
#     data['vat_amount'] = 200
#     data['tax_free_amount'] = 0
#     data['approval_url'] = 'http://127.0.0.1:8000/menu/'
#     data['fail_url'] = 'http://127.0.0.1:8000/accounts/login/'
#     data['cancel_url'] = 'http://127.0.0.1:8000/accounts/join/'
#     return data