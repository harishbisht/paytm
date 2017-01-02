from django.shortcuts import render
from django.http import HttpResponse
from paytm import Checksum
from paytm.payments import PaytmPaymentPage,VerifyPaytmResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import random,string
# Create your views here.


def home(request):
    return HttpResponse("<html><a href='http://localhost:8000/payment'>PayNow</html>")


def payment(request):
    # Generating unique order id
    order_id = Checksum.__id_generator__()
    bill_amount = "100"
    data_dict = {
                'ORDER_ID':order_id,
                'TXN_AMOUNT': bill_amount,
            }
    return PaytmPaymentPage(data_dict)


@csrf_exempt
def response(request):
    resp = VerifyPaytmResponse(request)
    print resp
    if resp['verified']:
        # save success details to db
        return JsonResponse(resp['paytm'])
    else:
        return HttpResponse("Verification Failed")
    return HttpResponse(status=200)