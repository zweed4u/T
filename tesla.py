#!/usr/bin/python3
import requests


class Tesla:
    def __init__(self):
        self.session = requests.session()
        self.bearer_token = None

    def login(self, username_email, password):
        headers = {
            'Host':                'owner-api.teslamotors.com',
            'Content-Type':        'application/json',
            'Connection':          'keep-alive',
            'x-tesla-user-agent':  'TeslaApp/3.6.2-354/61aad2d47/ios/10.2',
            'Accept':              '*/*',
            #'Content-Encoding':    'gzip', CAUSED 500?
            'User-Agent':          'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92',
            'Accept-Language':     'en-us',
            'Accept-Encoding':     'gzip, deflate'
        
        }
        # @ZWeed4U's iOS device
        payload = {
            "client_id": "81527cff06843c8634fdc09e8ac0abefb46ac849f38fe1e431c2ef2106796384",
            "client_secret": "c7257eb71a564034f9419ee651c7d0e5f7aa6bfbd18bafb5c5c033b093bb2fa3",
            "email": username_email,
            "grant_type": "password",
            "password": password
        }
        # access_token, refresh_token
        login_response = self.session.post('https://owner-api.teslamotors.com/oauth/token', json=payload, headers=headers)
        login_response.raise_for_status()
        login_response = login_response.json()
        self.bearer_token = login_response['access_token']
        return login_response

    def get_user_products(self):
        headers = {
            'Host':                'owner-api.teslamotors.com',
            'Content-Type':        'application/json; charset=utf-8',
            'Accept-Encoding':     'gzip, deflate',
            'Connection':          'keep-alive',
            'x-tesla-user-agent':  'TeslaApp/3.6.2-354/61aad2d47/ios/10.2',
            'Accept':              '*/*',
            'Content-Encoding':    'gzip',
            'User-Agent':          'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92',
            'Authorization':       f'Bearer {self.bearer_token}',
            'Accept-Language':     'en-us'
        }
        user_product_response = self.session.get('https://owner-api.teslamotors.com/api/1/products', headers=headers).json()
        return user_product_response

    def revoke_token(self):
        headers = {
            'Host':                'owner-api.teslamotors.com',
            'Content-Type':        'application/json; charset=utf-8',
            'Accept-Encoding':     'gzip, deflate',
            'Connection':          'keep-alive',
            'x-tesla-user-agent':  'TeslaApp/3.6.2-354/61aad2d47/ios/10.2',
            'Accept':              '*/*',
            #'Content-Encoding':    'gzip', CAUSED 500?
            'User-Agent':          'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92',
            'Authorization':       f'Bearer {self.bearer_token}',
            'Accept-Language':     'en-us'
        }
        payload = {
            "token": f"{self.bearer_token}"
        }
        revoke_token_response = self.session.post('https://owner-api.teslamotors.com/oauth/revoke', json=payload, headers=headers).json()
        return revoke_token_response

    def get_onboarding_data(self):
        headers = {
            'Host':                'owner-api.teslamotors.com',
            'Content-Type':        'application/json; charset=utf-8',
            'Accept-Encoding':     'gzip, deflate',
            'Connection':          'keep-alive',
            'x-tesla-user-agent':  'TeslaApp/3.6.2-354/61aad2d47/ios/10.2',
            'Accept':              '*/*',
            'Content-Encoding':    'gzip',
            'User-Agent':          'Mozilla/5.0 (iPhone; CPU iPhone OS 10_2 like Mac OS X) AppleWebKit/602.3.12 (KHTML, like Gecko) Mobile/14C92',
            'Authorization':       f'Bearer {self.bearer_token}',
            'Accept-Language':     'en-us'
        }
        query_string = {
            'language': 'en',
            'country':  'US'
        }
        onboarding_data_response = self.session.get('https://owner-api.teslamotors.com/api/1/users/onboarding_data', params=query_string, headers=headers).json()
        return onboarding_data_response


t = Tesla()
t.login('ACCOUNT_USERNAME/EMAIL_HERE', 'ACCOUNT_PASSWORD_HERE')
