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

from flask import render_template


IP_self='127.0.0.1'
port_self=1000
#global public_key
#Public_key_save=Public_key
class Transaction:

    def __init__(self, sender_address, sender_private_key, recipient_address,  value_voltage,  value_current,value_power,value_energy,value_transaction_energy,value_datatime,value_public_key_to_master):
        self.sender_address = sender_address
        self.sender_private_key = sender_private_key
        self.recipient_address = recipient_address
        self.value_voltage = value_voltage
        self.value_current= value_current
        self.value_power= value_power
        self.value_energy= value_energy
        self.value_transaction_energy= value_transaction_energy
        self.value_datatime= value_datatime
                        
        self.value_public_key_to_master= value_public_key_to_master
        print('\n\n class  ############=')
        print('\n\n class  value_voltage=', value_voltage)
        print('\n\n class  value_current =',value_current)
        #print('\n\n class  value=',value)
        print('\n')

    #def __getattr__(self, attr):
       # return self.data[attr]


    def to_dict(self):
        return OrderedDict({'sender_address': self.sender_address,
                            'recipient_address': self.recipient_address,
                            'value_voltage': self.value_voltage,
                            'value_current': self.value_current,
                            'value_power': self.value_power,
                            'value_energy': self.value_energy,
                            'value_datatime': self.value_datatime,
                            'value_transaction_energy': self.value_transaction_energy,
                            'value_public_key_to_master': self.value_public_key_to_master})

    def sign_transaction(self):
        """
        Sign transaction with private key
        """
        private_key = RSA.importKey(binascii.unhexlify(self.sender_private_key))
        signer = PKCS1_v1_5.new(private_key)
        h = SHA.new(str(self.to_dict()).encode('utf8'))
        return binascii.hexlify(signer.sign(h)).decode('ascii')

"""
class Public_Key:  
        #self.public_key_class 
        #print('\n\n @@@@@@@@@@@  lass Public_Key: =',self.public_key_class)
        #return 
    def __init__(self, public_key):
        self.key_temp = []
        #golbal self.key_temp = []
        self.key_generate = 0
        self.public_key_class = public_key
        
        print('\n\n aaa=',666)    
        print('\n\n @@@@@@@@@@@  class Public_Key: =',self.public_key_class)
        #return 
    #def key_call(self):
        if self.public_key_class!=111 :
            print('\n\n bbbb=',777) 
            #global self.key_temp 
            #self.key_temp = []
            self.key_temp.append(self.public_key_class)
           #return
            print('\n\n#######   self.public_key_class!=''   key(self)====',self.key_temp[0])
        #return self.public_key_class 
        #return 999999
        else:
            print('\n\n cccccc=',888888)
            print('\n\n self.key_temp[0]=',self.key_temp) 
            self.key_generate=self.key_temp[0]
            
            print('\n\n %%%%%%%%   self.public_key_class!   x===',self.key_generate)
            #self.key_temp.remove
            #return x
"""
def private_public_key(num,private_key):
    global private_key_a,private_key_write,public_key_b,public_key_tran
    private_key_a=private_key
    print('\n\n %%%%%%%%   def private_public_key(private_key): private_key_a  ===',private_key_a)
    #print('\n\n %%%%%%%%   def private_public_key(private_key): type(private_key_a)  #===',type(private_key_a))
    #private_key_a_hex=binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    if  num ==0 :
        print('\n\n @@@@   def private_public_key(private_key):num  ===',num )
        #print('\n\n %%%%%%%%   dif private_key_a !=111')
        #private_key_a=private_key
        #public_key = private_key.publickey()
        public_key_b = private_key_a.publickey()
        private_key_write=private_key
        #public_key_b = private_key_a
        #public_key_b_hex_=public_key_b
        #print('\n\n %%%%%%%%   def private_public_key(private_key): public_key_b  ===',public_key_b)
        #print('\n\n %%%%%%%%   def private_public_key(private_key):public_key_b_hex  ===',public_key_b_hex)
        return public_key_b
    if  num ==1 :
        public_key_tran=public_key_b 
        print('\n\n @@@@   num ==1,  num ===',num )
        #print('\n\n %%%%%%%%   def private_public_key(private_key): x ===',public_key_tran)
        return public_key_tran
    if  num ==22 :
        print('\n\n @@@@  @@@@   num ==100 , num===',num )
        print('\n\n @@@@  @@@@ num== 22 private_key_a ',private_key_a )
        return private_key_write
 
"""
def private_public_key(private_key):
    global private_key_a,x
    private_key_a=private_key
    print('\n\n %%%%%%%%   def private_public_key(private_key): private_key_a  ===',private_key_a)
    print('\n\n %%%%%%%%   def private_public_key(private_key): type(private_key_a)  ===',type(private_key_a))
    private_key_a_hex=binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    if private_key_a_hex !=111 :
        print('\n\n %%%%%%%%   dif private_key_a !=111')
        #private_key_a=private_key
        #public_key = private_key.publickey()
        public_key_b = private_key_a.publickey()
        #public_key_b = private_key_a
        public_key_b_hex_=public_key_b
        print('\n\n %%%%%%%%   def private_public_key(private_key): public_key_b  ===',public_key_b)
        #print('\n\n %%%%%%%%   def private_public_key(private_key):public_key_b_hex  ===',public_key_b_hex)
        return public_key_b
    else:
        x=public_key
        print('\n\n %%%%%%%%   def private_public_key(private_key): x ===',x)
        return x
"""


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
    global public_key
    #a=100
    #print('\na===',a)
    random_gen = Crypto.Random.new().read
    
    private_key = RSA.generate(1024, random_gen)
    private_key_hex=binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii')
    print('\n\n @@@ new_wallet(): private_key_hex=',private_key_hex)
    #private_key_hex=55555
    #public_key = private_key.publickey()
    #public_key = private_public_key(private_key_hex)
    public_key = private_public_key(0,private_key)
    public_key_hex=binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
    #Public_key_save=Public_Key(public_key_hex)
    print('\n\n @@@ new_wallet(): private_key=',private_key)
    print('\n\n @@@ new_wallet(): public_key=',public_key)
    print('\n\n @@@ new_wallet(): public_key_hex=',public_key_hex)
    #print('\n\n @@@ new_wallet(): Public_key_save=',Public_key_save.public_key_class)
    #print('\n\n @@@ new_wallet(): self.key_temp[0]=',Public_key_save.key_temp[0])
    #Public_key_save=binascii.hexlify(Public_key_save.decode('ascii')
    #print('\n\n Public_key_save=',Public_key_save.key)
    response = {'private_key': binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'),
		        'public_key': binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')
               }
    return jsonify(response), 200






"""  
   
def wallet_public(self):
        global aa
        aa=private_key
        return aa
    return jsonify(response), 200
def new_wallet():
	a=1000
    print('\na===',a)
    return 
"""




#@app.route('/wallet/new', methods=['GET'])



@app.route('/generate/transaction', methods=['POST'])
def generate_transaction():
    #global public_key
    #public_key=11111111111111
    call_public_key=111
    public_key_save_2 = private_public_key(1,call_public_key)
    print('\n\n @@@  generate_transaction(): public_key_save_2=',public_key_save_2)
    public_key_save_2_hex=binascii.hexlify(public_key_save_2.exportKey(format='DER')).decode('ascii')
    #Public_key_save=Public_Key(public_key_hex)
    print('\n\n @@@ generate_transaction(): public_key_save_2_hex=', public_key_save_2_hex)
    #Public_key_save_2=Public_Key(call_public_key)
    #print('\n\n ************    def generate_transaction():    Public_key_save=', Public_key_save_2.key_generate )
    #Public_key_save_2_hex=Public_Key(call_public_key)
    #print('\n\n ************    def generate_transaction():    Public_key_save=', Public_key_save_2_hex)
    sender_address=request.form['sender_address']
    sender_private_key=request.form['sender_private_key']
    recipient_address=request.form['recipient_address']
    value_voltage=request.form['amount_voltage']
    value_current=request.form['amount_current']
    value_power=request.form['amount_power']
    value_energy=request.form['amount_energy']
    #value_d=request.form['amount_4']
    value_datatime=request.form['amount_datatime']
    value_transaction_energy=request.form['amount_transaction_energy']
    #value_public_key_to_master=sender_private_key
    value_public_key_to_master= public_key_save_2_hex
    #value_public_key_to_master=public_key
    #value_public_key_to_master= wallet_public(self)
    #value_public_key_to_master= 111
    #print('\n\n public_key=',public_key)
    print('\naaaa')
    print('\n\n sender_address=',sender_address)
    print('\n\n sender_private_key=',sender_private_key)
    print('\n\n recipient_address=',recipient_address)
    print('\n\n value=',value_voltage)
    print('\n\n value_current=',value_current)
    print('\n\n value_power=',value_power)
    print('\n\n   value_datatime=',value_datatime)
    print('\n\n   value_transaction_energy=',value_transaction_energy)
   # print('\n\n  transaction.value_public_key_to_master ===',transaction.value_public_key_to_master)
    
    print('\n\n value_public_key_to_master=',value_public_key_to_master)
    print('\n')
    transaction = Transaction(sender_address, sender_private_key, recipient_address,  value_voltage, value_current,value_power,value_energy,value_transaction_energy,value_datatime,value_public_key_to_master)
    print('\nbbbb')
    #print('\n\n transaction.value_2 ===',transaction.value_2)
    print('\n')
    
    print('\n\n type (transaction) =',type(transaction))
    print('\n\n transaction.sender_address ===',transaction.sender_address )
    print('\n@@@@@@@')
    #print('\n\n type (transaction) =',type(transaction))
    print('\n\n transaction.recipient_address ===',transaction.recipient_address )
    print('\n\n transaction.value ===',transaction.value_voltage)
    print('\n')
    print('\nccc')
    print('\n\n transaction.value_current ===',transaction.value_current)
    print('\n\n transaction.value_power ===',transaction.value_power)
    
    print('\n')
    print('\n')
    
    #print('\n\n transaction.value_2 ===',transaction.value_2)
    #print('\n\n signature ===',transaction.sign_transaction())
    print('\n')
    print('\nddd')
    response = {'transaction': transaction.to_dict(), 'signature': transaction.sign_transaction()}
    """
    print('\n')
    print('\nfff')
    print('\n\n type (transaction) =',type(transaction))
    print('\n\n transaction.value_current ===',transaction.value_current)
    print('\n\n transaction.value_power ===',transaction.value_power)
    print('\n\n transaction.value_public_key_to_master ===',transaction.value_public_key_to_master)
    print('\n')
    print('\n')
    """
    print('\n\n ###   value_datatime=',value_datatime)
    print('\n\n ###   value_transaction_energy=',value_transaction_energy)
    print('\n\n ### transaction.value_public_key_to_master ===',transaction.value_public_key_to_master)
    #print('\n\n response ===',response)
    #print('\n')
    return jsonify(response), 200








@app.route('/Write_Private_key', methods=['GET'])

def Write_Private_key():
    print('\n\n Write_Private_key  10000')
    call_private_key=222
    private_key_save_3= private_public_key(22,call_private_key)
    print('\n\n Write_Private_key()===',binascii.hexlify(private_key_save_3.exportKey(format='DER')).decode('ascii'))
    response = {'Write_Private_key':binascii.hexlify(private_key_save_3.exportKey(format='DER')).decode('ascii')}
		       
    return jsonify(response), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    print('\n\n Mysql_user_data /transactions/new ')
    data=['aaa','2',3,4,5,6,7,8]
    
    #transactions = data
    transactions.append(data)
    #print('\n\n Mysql_user_data /get_transactions ',transactions)
    #data=['a','b',3,4,5,6,7,8,9]
    #transactions.append(data)
    #print('\n\n Mysql_user_data /get_transactions ',transactions)
    transactions = OrderedDict({
                                    'recipient_address': data[0],
                                    'value_voltage': data[1],
                                    'value_current': data[2],
                                    'value_power': data[3],
                                    'value_energy':data[4],
                                    'value_transaction_energy':data[5],                                   
                                    'value_datatime':data[6],
                                    })
    response = {'message': 'Transaction will be added to Block '+ str(transactions)}
    return jsonify(response), 201

@app.route('/Mysql_user_data', methods=['GET'])  
def Mysql_user_data():
    transactions_aa=[]
    #Get transactions from transactions pool
    print('\n\n Mysql_user_data /get_transactions ')
    #data=['test','2',3,4,5,6,7,8,9]
    
    #data_1=['aa','2',3,4,5,6,7,8,9]
    #data=['Wang','Hsieh',  111.2, 3.2, 55.4, 0.1360, '2018/12/12 09:12:22']
   # data_total=[data_1,data_2,data_3]
    #data_2=['bbb','2',3,4,5,6,7,8,9]
    #data_3=['cccc','2',3,4,5,6,7,8,9]
    #data_total=[data_1,data_2,data_3]
    #transactions = data
    #transactions_aa.append(data)
    #print('\n\n Mysql_user_data /get_transactions ====',transactions_aa)
    #data=['a','b',3,4,5,6,7,8,9]
    #transactions.append(data)
    #print('\n\n Mysql_user_data /get_transactions ',transactions)   response['transactions'][i]["sender_address"],
    """ 
    
    """
    #transactions_total.transactions.append(transactions_aa)
    
    """ 
    
    """ 
    #print('\n\n @@@@    Mysql_user_data /get_transactions_aa  again   ====',transactions_aa)
    #print('\n\n @@@@    Mysql_user_data /type(transactions_aa)   ====',type(transactions_aa))
    #print('\n\n @@@@    Mysql_user_data /transactions_aa[0]  ====',transactions_aa[1])
    #data=['a','b',3,4,5,6,7,8,9]
    trans_b =[]
    transactions_total=[]
    """ 
    
    """  
    trans_b=[]
    transactions_aa= []
    
    transactions_total=[]
    """
    data_1=[1, 'Chen','Lee',    110.7, 2.5, 52.5, 4.7, '2018/12/12 08:53:11']
    data_2=[2, 'Lin' ,'Huang',  112.3, 1.7, 29.1, 2.1, '2018/12/12 09:07:45']
    data_3=[3, 'Wang','Hsieh',  111.2, 3.2, 55.4, 7.4, '2018/12/12 09:12:22']
    data_4=[4, 'Yang','Wu',     109.1, 7.5, 100.5, 9.8, '2018/12/12 08:53:11']
    data_5=[5, 'Hsu' ,'Guo',   108.8, 10.7, 301.1, 10.2, '2018/12/12 09:07:45']
    """
    data_1=[1, 'Admin','Chen',    110.7, 2.5, 52.5, 4.7, '2018/12/12 08:53:11']
    data_2=[2, 'Lin' ,'Huang',  '', '', '', '', '2018/12/12 09:07:45']
    data_3=[3, 'Admin','Chen',  111.2, 3.2, 55.4, 7.4, '2018/12/12 09:12:22']
    data_4=[4, 'Admin','Yang',  '', '', '', '', '2018/12/12 08:53:11']
    data_5=[5, 'Hsu' ,'Guo',   108.8, 10.7, 301.1, 10.2, '2018/12/12 09:07:45']
    data_6=[6, 'Admin','Lin' ,  110.9, 12.7, 100.2, 22.3, '2018/12/7 14:13:35']
    
    data_total=[data_1,data_2,data_3,data_4,data_5,data_6]
    
    #transactions_aa= [3, 'Wang','Hsieh',  111.2, 3.2, 55.4, 0.1360, '2018/12/12 09:12:22']
   
    

    for i in range(len(data_total))  :
        #print('\n\n @@@@    i  ====',i )
        for j in range(len(data_total[i])) :
        #print('\n\n @@@@    (len(data_total[i])  ====',len(data_total[i]) )
        #print('\n\n @@@@   j ====',j )
        #print('\n\n @@@@   data_total[i][j] ====',data_total[i][j] )
            trans_b.append(data_total[i][j])
            #print('\n\n @@@@    trans_b ====',trans_b)   
        transactions_total.append(trans_b)
        trans_b=[]
    print('\n\n @@@@    Mysql_user_data transactions_total   ====',transactions_total)
   # transactions_total.append(trans_b)
    #print('\n\n @@@@    Mysql_user_data transactions_total   ====',transactions_total)        
    print('\n\n @@@@    Mysql_user_data transactions_total length(transactions_total)  ====',len(transactions_total))   
    transactions_aa= [transactions_total[len(transactions_total)-1]]
    print('\n\n @@@@    transactions_aa  ====', transactions_aa)        

    response = {'transactions_aa':transactions_aa,'transactions_total':transactions_total}
    return jsonify(response), 200
    
    
    
    
    

if __name__ == '__main__':
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=port_self, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port
    
    app.run(host=IP_self, port=port)