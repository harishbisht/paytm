import Checksum
from django.conf import settings
from django.http import HttpResponse
import json

MERCHANT_KEY = settings.PAYTM_MERCHANT_KEY
MERCHANT_ID = settings.PAYTM_MERCHANT_ID
COMPANY_NAME = settings.PAYTM_COMPANY_NAME
CALLBACK_URL = settings.PAYTM_CALLBACK_URL
PAYTM_PAYMENT_GATEWAY_URL = settings.PAYTM_PAYMENT_GATEWAY_URL
PAYTM_TRANSACTION_STATUS_URL = settings.PAYTM_TRANSACTION_STATUS_URL
PAYTM_CUSTOMER_ID = settings.PAYTM_CUSTOMER_ID
PAYTM_INDUSTRY_TYPE_ID = settings.PAYTM_INDUSTRY_TYPE_ID
PAYTM_WEBSITE = settings.PAYTM_WEBSITE
PAYTM_CHANNEL_ID = settings.PAYTM_CHANNEL_ID

def GeneratePaymentPage(param_dict):
    HTML = """<html>
    <h1>%s<br><br> Merchant Check Out Page<br><br> 
        Please Do Not Refresh The Page</h1></br>
    <form method="post" action="%s" name="f1">
    <table border="1">
    <tbody> """%(COMPANY_NAME,PAYTM_PAYMENT_GATEWAY_URL)     
    for key,value in param_dict.iteritems():
        HTML += """<input type="hidden" name="%s" value="%s">"""%(key,value)
    HTML +="""</tbody>
    </table>
    <script type="text/javascript">
    document.f1.submit();
    </script>
    </form>
    </html>"""
    return HTML




def PaytmPaymentPage(param_dict):
    param_dict['MID'] = MERCHANT_ID
    param_dict['CUST_ID'] = PAYTM_CUSTOMER_ID
    param_dict['INDUSTRY_TYPE_ID'] = PAYTM_INDUSTRY_TYPE_ID
    param_dict['WEBSITE'] = PAYTM_WEBSITE
    param_dict['CHANNEL_ID'] = PAYTM_CHANNEL_ID
    param_dict['CALLBACK_URL'] = CALLBACK_URL
    param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
    return HttpResponse(GeneratePaymentPage(param_dict))


def VerifyPaytmResponse(response):
    response_dict = {}
    if response.method == "POST":
        data_dict = {}
        for key in response.POST:
            data_dict[key] = response.POST[key]
        verify = Checksum.verify_checksum(data_dict, MERCHANT_KEY, data_dict['CHECKSUMHASH'])
        if verify:
            response_dict['verified'] = True
            response_dict['paytm'] = data_dict
            return (response_dict)
        else:
            response_dict['verified'] = False
            return (response_dict)
    response_dict['verified'] = False
    return (response_dict)



def JsonResponse(responseData):
    import django
    if float(django.get_version()) >= 1.7:
        from django.http import JsonResponse
        return JsonResponse(responseData)
    else:
        return HttpResponse(json.dumps(responseData), content_type="application/json")

