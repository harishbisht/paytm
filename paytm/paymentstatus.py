import requests
import json
from django.conf import settings

MERCHANT_ID = settings.PAYTM_MERCHANT_ID
URL = settings.PAYTM_TRANSACTION_STATUS_URL


def get_paytm_payment_transactions_details(paytm_order_id):
    URL += 'JsonData={"MID":"%s","ORDERID":"%s"}'%(MERCHANT_ID,paytm_order_id)
    response_data = json.loads(requests.get(URL).text)
    if "MID" in response_data:
        response_data.pop("MID")
    if "REFUNDAMT" in response_data:
        response_data.pop("REFUNDAMT")
    return response_data