from application import app, db
from datetime import datetime
import pytz
import time
from flask_login import UserMixin






class user( db.Model,UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  uid = db.Column(db.String(50),  unique=True)
  name = db.Column(db.String(50))
  email = db.Column(db.String(50), unique=True)
  mobile = db.Column(db.String(20))
  password = db.Column(db.String(15))
  profile_img = db.Column(db.String(200))
  address1 = db.Column(db.String(200))
  address2 = db.Column(db.String(200))
  address3 = db.Column(db.String(200))
  current_cart_value= db.Column(db.String(15))
  current_cart_items= db.Column(db.String(15))

  def __init__(self, uid, name, email, mobile, password,\
               profile_img="NA",address1= "NA",address2= "NA",address3= "NA", current_cart_value= "NA", current_cart_items= "NA"):
      self.uid= uid
      self.name= name
      self.email= email
      self.mobile= mobile
      self.password= password
      self.profile_img =profile_img
      self.address1 = address1
      self.address2 = address2
      self.address3 = address3
      self.current_cart_value= current_cart_value
      self.current_cart_items= current_cart_items

class user_review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    mobile = db.Column(db.String(20))
    password = db.Column(db.String(15))

    def __init__(self, uid, name, email, mobile, password):
        self.uid = uid
        self.name = name
        self.email = email
        self.mobile = mobile
        self.password = password

class product_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(50),unique=True)
    product_name = db.Column(db.String(100))
    product_price = db.Column(db.Integer)
    product_path = db.Column(db.String(300))
    Gemstone = db.Column(db.String(50))
    plating_used = db.Column(db.String(50))
    Base_material = db.Column(db.String(50))
    product_description = db.Column(db.Text)
    product_available_quantity = db.Column(db.Integer)
    product_detail = db.Column(db.Text)

    def __init__(self,product_code,product_name,product_price,product_path,Gemstone,plating_used,Base_material,product_description,product_available_quantity,product_detail):
        self.product_code = product_code
        self.product_name = product_name
        self.product_price = product_price
        self.product_path = product_path
        self.Gemstone = Gemstone
        self.plating_used = plating_used
        self.Base_material = Base_material
        self.product_description = product_description
        self.product_available_quantity = product_available_quantity
        self.product_detail = product_detail

class merchantInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    merchant_id = db.Column(db.String(40), nullable= False, unique= True)
    merchant_secret_key = db.Column(db.String(40), nullable= False)
    def __init__(self, merchant_id, merchant_secret_key):
        self.merchant_id = merchant_id
        self.merchant_secret_key = merchant_secret_key

class ecomm_payment_status(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id= db.Column(db.String(64))
    txn_id = db.Column(db.String(64))
    txn_date= db.Column(db.String(64))
    txn_amount= db.Column(db.String(16))
    txn_status= db.Column(db.String(32))
    txn_resp_msg = db.Column(db.Text)
    txn_resp_code= db.Column(db.String(8))
    txn_payment_mode= db.Column(db.String(8))
    ecomm_mid= db.Column(db.String(64))
    txn_currency = db.Column(db.String(16))
    txn_bank_id = db.Column(db.String(64))
    txn_checksum_hash= db.Column(db.Text)
    ecomm_merchant_name= db.Column(db.String(64))
    timestamp = db.Column(db.DateTime())
    txn_time= db.Column(db.String(45))
    signature= db.Column(db.Text)
    sign_type= db.Column(db.String(16))

    def __init__(self, order_id, txn_id, txn_date, txn_amount, txn_status, txn_resp_msg,\
                 txn_resp_code, txn_payment_mode, ecomm_mid, txn_currency, txn_bank_id,\
                 txn_checksum_hash, ecomm_merchant_name, txn_time, signature, sign_type):

        self.order_id= order_id
        self.txn_id= txn_id
        self.txn_date= txn_date
        self.txn_amount= txn_amount
        self.txn_status= txn_status
        self.txn_resp_msg= txn_resp_msg
        self.txn_resp_code= txn_resp_code
        self.txn_payment_mode= txn_payment_mode
        self.ecomm_mid= ecomm_mid
        self.txn_currency= txn_currency
        self.txn_bank_id= txn_bank_id
        self.txn_checksum_hash= txn_checksum_hash
        self.ecomm_merchant_name= ecomm_merchant_name
        self.timestamp = datetime.now(tz=pytz.timezone('Asia/Kolkata'))
        self.txn_time= txn_time
        self.signature= signature
        self.sign_type= sign_type



class ecomm_merchant_details(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    ecomm_mid= db.Column(db.String(64))
    ecomm_url= db.Column(db.String(200))
    ecomm_jsurl = db.Column(db.String(200))
    ecomm_mch_name= db.Column(db.String(120))
    ecomm_mch_secret_key = db.Column(db.String(120))
    ecomm_callback_url= db.Column(db.String(120))

    def __init(self, ecomm_mid, ecomm_url, ecomm_jsurl, ecomm_mch_name,\
               ecomm_mch_secret_key, ecomm_callback_url):
        self.ecomm_mid= ecomm_mid
        self.ecomm_url= ecomm_url
        self.ecomm_jsurl= ecomm_jsurl
        self.ecomm_mch_name= ecomm_mch_name
        self.ecomm_mch_secret_key= ecomm_mch_secret_key
        self.ecomm_callback_url= ecomm_callback_url



class review_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_code = db.Column(db.String(50))
    reviewer_name = db.Column(db.String(100))
    reviewer_email = db.Column(db.String(100))
    review = db.Column(db.Text)
    review_time =db.Column(db.String(100))

    def __init__(self, product_code, reviewer_name, reviewer_email, review,review_time):
        self.product_code = product_code
        self.reviewer_name = reviewer_name
        self.reviewer_email = reviewer_email
        self.review = review
        self.review_time = review_time

class cart_orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_uid = db.Column(db.String(50))
    product_id= db.Column(db.String(50))
    product_price= db.Column(db.String(10))
    product_status= db.Column(db.String(50))
    product_quantity= db.Column(db.INT)
    timestamp= db.Column(db.Float(precision = 32))
    datetime= db.Column(db.DateTime())
    order_id= db.Column(db.String(50))
    def __init__(self, user_uid, product_id, product_price, product_status,\
                 product_quantity, timestamp, order_id= "NA"):
        self.user_uid= user_uid
        self.product_id= product_id
        self.product_price= product_price
        self.product_status= product_status
        self.product_quantity= product_quantity
        self.timestamp= timestamp
        self.order_id= order_id
        self.datetime= datetime.now(tz=pytz.timezone('Asia/Kolkata'))


class checkout_orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_uid = db.Column(db.String(50))
    order_id = db.Column(db.String(50))
    products = db.Column(db.Text)
    cart_amt= db.Column(db.String(15))
    shipping_amt= db.Column(db.String(15))
    checkout_amt= db.Column(db.String(15))
    txn_id = db.Column(db.String(90))
    txn_token = db.Column(db.String(300))
    bank_txn_id= db.Column(db.String(40))
    txn_amount= db.Column(db.String(15))
    txn_date= db.Column(db.String(50))
    txn_status= db.Column(db.String(15))
    txn_mode= db.Column(db.String(15))
    txn_currency= db.Column(db.String(10))
    txn_hash= db.Column(db.String(250))
    txn_resp_code= db.Column(db.String(15))
    txn_resp_msg= db.Column(db.String(300))
    checkout_timestamp= db.Column(db.Float(precision = 32))
    shipping_addr= db.Column(db.String(250))
    billing_name= db.Column(db.String(80))
    billing_company= db.Column(db.String(80))
    billing_phone= db.Column(db.String(25))
    billing_email= db.Column(db.String(80))
    billing_addr= db.Column(db.String(250))
    order_notes= db.Column(db.Text)
    payment_status= db.Column(db.String(25))
    delivery_date= db.Column(db.String(45))

    def __init__(self, user_uid, order_id, products, txn_token, txn_id, bank_txn_id, txn_amount, txn_date, txn_status,\
                 txn_mode, txn_currency, txn_hash, shipping_addr, billing_name,\
                 billing_company, billing_phone, billing_email, billing_addr, order_notes, payment_status,\
                 cart_amt, shipping_amt, checkout_amt, txn_resp_code= "NA", txn_resp_msg= "NA", delivery_date= "NA"):

        self.user_uid= user_uid
        self.order_id= order_id
        self.products= products
        self.txn_token= txn_token
        self.txn_id= txn_id
        self.bank_txn_id= bank_txn_id
        self.txn_amount= txn_amount
        self.txn_date= txn_date
        self.txn_status= txn_status
        self.txn_mode= txn_mode
        self.txn_currency= txn_currency
        self.txn_hash= txn_hash
        self.txn_resp_msg= txn_resp_msg
        self.txn_resp_code= txn_resp_code
        self.checkout_timestamp= round(time.time(), 3)
        self.shipping_addr= shipping_addr
        self.billing_name= billing_name
        self.billing_company= billing_company
        self.billing_phone= billing_phone
        self.billing_email= billing_email
        self.billing_addr= billing_addr
        self.order_notes= order_notes
        self.payment_status= payment_status
        self.cart_amt= cart_amt
        self.shipping_amt= shipping_amt
        self.checkout_amt= checkout_amt
        self.delivery_date= delivery_date
