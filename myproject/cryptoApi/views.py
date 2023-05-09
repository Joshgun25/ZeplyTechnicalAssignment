import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bitcoinlib.wallets import Wallet
from eth_account import Account

from .models import Address

@csrf_exempt
def generate_address(request):
    if request.method == 'POST':
        request_data = json.loads(request.body.decode('utf-8'))
        currency = request_data.get('currency')

        if currency == 'BTC':
            try:
                wallet = Wallet('mywallet')
            except:
                # If the wallet does not exist, create it
                wallet = Wallet.create('mywallet')
                wallet.new_account()
            private_key = wallet.get_key()
            address = private_key.address
        elif currency == 'ETH':
            account = Account.create()
            private_key = account.key.hex()
            address = account.address
        else:
            return JsonResponse({'error': 'Invalid currency'}, status=400)

        addressObj = Address.objects.create(coin=currency, address=address)
        return JsonResponse({'id': addressObj.id, 'address': addressObj.address}, status=201)

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def list_addresses(request):
    addresses = Address.objects.all().values()
    return JsonResponse({'addresses': list(addresses)})

def retrieve_address(request, id):
    try:
        address_obj = Address.objects.get(id=id)
        return JsonResponse({'id': address_obj.id, 'coin': address_obj.coin, 'address': address_obj.address})
    except Address.DoesNotExist:
        return JsonResponse({'error': 'Address not found'})
