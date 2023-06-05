import requests

def initiate_payment(amount, email, reference):
    endpoint = 'https://api.paystack.co/transaction/initialize'
    headers = {
        'Authorization': 'Bearer YOUR_PAYSTACK_SECRET_KEY',
        'Content-Type': 'application/json',
    }
    data = {
        'amount': amount,
        'email': email,
        'reference': reference,
        # Additional parameters as required by the Paystack API
    }
    response = requests.post(endpoint, json=data, headers=headers)
    return response.json()