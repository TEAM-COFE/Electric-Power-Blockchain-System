'''
title           : blockchain_client.py
description     : A blockchain client implemenation, with the following features
                  - Wallets generation using Public/Private key encryption (based on RSA algorithm)
                  - Generation of transactions with RSA encryption      
author          : Adil Moujahid
date_created    : 20180212
date_modified   : 20180309
version         : 0.3
usage           : python blockchain_client.py
                  python blockchain_client.py -p 8080
                  python blockchain_client.py --port 8080
python_version  : 3.6.1
Comments        : Wallet generation and transaction signature is based on [1]
References      : [1] https://github.com/julienr/ipynb_playground/blob/master/bitcoin/dumbcoin/dumbcoin.ipynb
'''

from collections import OrderedDict

import binascii

import Crypto
import Crypto.Random
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5

import requests
from flask import Flask, jsonify, request, render_template


class Transaction:

    def __init__(self, sender_address, sender_private_key, recipient_address,  value,  value_b,value_c,value_d):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value = value
        self.value_b= value_b
        self.value_c= value_c
        self.value_d= value_d
        print('\n\n class  ############=')
        print('\n\n class  value=',value)
        print('\n\n class  value_b =',value_b)
        #print('\n\n class  value=',value)
        print('\n')

    #def __getattr__(self, attr):
       # return self.data[attr]


    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value': self.value,
                            'value_b': self.value_b,
                            'value_c': self.value_c,
                            'value_d': self.value_d})

    def sign_transaction(self):
        """
        Sign transaction with private key
        """
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')



app = Flask(__name__)

@app.route('/')
def index():
	return render_template('./index.html')

@app.route('/make/transaction')
def make_transaction():
    return render_template('./make_transaction.html')

@app.route('/view/transactions')
def view_transaction():
    return render_template('./view_transactions.html')

@app.route('/wallet/new', methods=['GET'])
def new_wallet():
	random_gen = Crypto.Random.new().read
	private_key = RSA.generate(1024, random_gen)
	public_key = private_key.publickey()
	response = {
		'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
		'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
	}

	return jsonify(response), 200

@app.route('/generate/transaction', methods=['POST'])

def generate_transaction():
    sender_address=request.form['sender_address']
    sender_private_key=request.form['sender_private_key']
    recipient_address=request.form['recipient_address']
    value=request.form['amount']
    value_b=request.form['amount_2']
    value_c=request.form['amount_3']
    value_d=request.form['amount_4']
    print('\naaaa')
    print('\n\n sender_address=',sender_address)
    print('\n\n sender_private_key=',sender_private_key)
    print('\n\n recipient_address=',recipient_address)
    print('\n\n value=',value)
    print('\n\n value_b=',value_b)
    print('\n\n value_c=',value_c)
    print('\n\n value_d=',value_d)
    print('\n')
    transaction = Transaction(sender_address, sender_private_key, recipient_address,  value, value_b, value_c,value_d)
    print('\nbbbb')
    #print('\n\n transaction.value_2 ===',transaction.value_2)
    print('\n')
    
    print('\n\n type (transaction) =',type(transaction))
    print('\n\n transaction.sender_address ===',transaction.sender_address )
    print('\n@@@@@@@')
    #print('\n\n type (transaction) =',type(transaction))
    print('\n\n transaction.recipient_address ===',transaction.recipient_address )
    print('\n\n transaction.value ===',transaction.value)
    print('\n')
    print('\nccc')
    print('\n\n transaction.value_b ===',transaction.value_b)
    print('\n\n transaction.value_c ===',transaction.value_c)
    print('\n\n transaction.value_d ===',transaction.value_d)
    print('\n')
    print('\n')
    
    #print('\n\n transaction.value_2 ===',transaction.value_2)
    #print('\n\n signature ===',transaction.sign_transaction())
    print('\n')
    print('\nddd')
    response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}
    print('\n')
    print('\nfff')
    print('\n\n type (transaction) =',type(transaction))
    print('\n\n transaction.value_b ===',transaction.value_b)
    print('\n\n transaction.value_c ===',transaction.value_c)
    print('\n\n transaction.value_d ===',transaction.value_d)
    print('\n')
    print('\n')
    
    #print('\n\n response ===',response)
    #print('\n')
    return jsonify(response), 200


if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=8080, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app.run(host='127.0.0.1', port=port)