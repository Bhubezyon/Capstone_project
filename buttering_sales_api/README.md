# Buttering & Sales API

A full-featured Django REST API for users to barter/sell items, and communicate securely built with Django, DRF, Django Channels, and stripe.

---

## FEATURES

- User registration, login, and token-based authentication
- Post items for sale or barter with summeries, categories, tags, and images
- Comment on poosts with threaded replies
- Like posts and comments
- Real time notifications via WebSockets
- Direct messaging (DMs) for barter/payment coordination
- Stripe payment integration (not yet included)
- Security Hardening: XSS, CSRF, SQL injection protection
- Static files and HTML templates for frontend support

---

## Tech Stag

- Django + Django REST Framework
- Django Channels + Redis (WebSockets)
- Stripe (Payment)
- Pillow (Image upload)
- django-taggit (tags)

## Setup Instructions

'''bash
git clone https://github.com/Bhubezyon/Capstone_project.git
cd butturing_sales_api

python -m venv vevn
source vevn/bin/activate

pip install -r requirements.txt

python manage.py makemigrations
python manage,py migrate
python manage.py runserver

## API FUNCTIONALITIES

- User_Register:
{
    "name": "calvin",
    "email": "calvin@example.com"
    "password": "12345"
}
Response = "User created successfully"

- User_Login:
{
    "email": "calvin@example.com"
    "password": "12345"
}
Response = "Login successful"

- Post item (is_for_sale/ exchange_item/ item_description/ Price, or trade_item)
{
    "vintage guiter",
    "description": "classic acoustic guitar from the 70s, good condition"
    "category": "music",
    "is_for_sale": true,
    "price": "600"
    "exchange_item": "piano"
    "image": (j.peg, jpg, png)
}
Response = "Posted_successfuly"

- Message for negotiations (Direct_message)
{
    "sender_id": 1,
    "sender_id": 2,
    "listing_id: 12,
    "message": "Hi! I saw vintage guitar, Would you be open to exchanging it for my upright piano. If interested contact me via my cell, phone number in my bio thank you."
}
Response = "message_sent"

- Follow_user/Unfollow_unfollow.

- Like_user/Unlike_user.
