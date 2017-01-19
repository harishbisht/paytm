[![PyPI version](https://badge.fury.io/py/paytm.svg)](https://badge.fury.io/py/paytm)
[![Build Status](https://api.travis-ci.org/harishbisht/paytm.svg?branch=master)](https://api.travis-ci.org/harishbisht/paytm.svg?branch=master)


# Paytm

## paytm Django package


* First install the package

```python
pip install paytm
```

* Then go to your django settings page and paste the below code and change it according to your need

```python
PAYTM_MERCHANT_COMPANY_NAME = "<YOUR-COMPANY-NAME>"
PAYTM_CHANNEL_ID = "WEB"
PAYTM_EMAIL  = "<YOUR-EMAIL-ID>"
PAYTM_MOBILE = "<YOUR-MOBILE-NUMBER>"
PAYTM_STAGING = True
if PAYTM_STAGING:
    PAYTM_MERCHANT_KEY = "<YOUR-STAGING-MERCHANT-KEY>"
    PAYTM_INDUSTRY_TYPE_ID = "Retail"
    PAYTM_MERCHANT_ID = "<YOUR-MERCHANT-ID>"
    PAYTM_CALLBACK_URL = "http://localhost:8000/wallet/response/" if DEBUG else "http://www.yourwebsite.com/wallet/response/"
    PAYTM_WEBSITE = "WEB_STAGING"
    PAYTM_TRANSACTION_STATUS_URL = "https://pguat.paytm.com/oltp/HANDLER_INTERNAL/TXNSTATUS"
    PAYTM_PAYMENT_GATEWAY_URL = "https://pguat.paytm.com/oltp-web/processTransaction"
else:
    PAYTM_MERCHANT_KEY = "<YOUR-LIVE-MERCHANT-KEY>"
    PAYTM_MERCHANT_ID = "<YOUR-LIVE-MERCHANT-ID>"
    PAYTM_CALLBACK_URL = "<YOUR-LIVE-CALLBACK-URL>"
    PAYTM_INDUSTRY_TYPE_ID = "Retail92"
    PAYTM_WEBSITE = "<PAYTM-WEBSITE-ID>"
    PAYTM_TRANSACTION_STATUS_URL = "https://secure.paytm.in/oltp/HANDLER_INTERNAL/TXNSTATUS"
    PAYTM_PAYMENT_GATEWAY_URL = "https://secure.paytm.in/oltp-web/processTransaction"

```

* For paytm payment page pass unique OrderId and BillAmount

```python
#views.py
from paytm.payments import PaytmPaymentPage
from paytm import Checksum
def payment(request):
    # provide your unique order id
    # if you don't have your unique order id then
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    cust_id = "payment_maker@email.com"
    data_dict = {
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
                'CUST_ID': cust_id
            }
    return PaytmPaymentPage(data_dict)
    
#urls.py
url(r'^payment/', 'views.payment', name='payment'),
```

* After the completion of payment process, paytm return the response in callback URL for that first authenticate the return request
```python
#views.py
from django.http import HttpResponse
from paytm.payments import VerifyPaytmResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    if resp['verified']:
        # save success details to db
        print resp['paytm']['ORDERID']  #SAVE THIS ORDER ID TO DB FOR TRANSACTION HISTORY
        return JsonResponse(resp['paytm'])
    else:
        return HttpResponse("Verification Failed")
    return HttpResponse(status=200)
    
#urls.py
url(r'^response/', 'views.response', name='response'),
```

* Now run the server 
```python
python manage.py runserver 0.0.0.0:8000
```
