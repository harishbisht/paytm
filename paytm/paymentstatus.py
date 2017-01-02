import requests
import json
from django.conf import settings

def get_paytm_payment_transaction_details(paytm_order_id):
	url = settings.PAYTM_TRANSACTION_STATUS_URL
	MERCHANT_ID = settings.PAYTM_MERCHANT_ID
	url = "https://pguat.paytm.com/oltp/HANDLER_INTERNAL/TXNSTATUS"
	MERCHANT_ID = ""
	data = {'MID': MERCHANT_ID, 'ORDERID': paytm_order_id}
	data_json = json.dumps(data)
	payload = {'JsonData': data_json}
	return json.loads(requests.get(url,data=payload).text)
