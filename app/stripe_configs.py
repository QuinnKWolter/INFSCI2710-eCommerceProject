import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(product_id):
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': product_id,
                'quantity': 1,
            }],
            mode='payment',
            success_url='YOUR_SUCCESS_URL',
            cancel_url='YOUR_CANCEL_URL',
        )
        return checkout_session
    except Exception as e:
        print(e)
        return None
