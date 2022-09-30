from datetime import date
from datetime import datetime
#from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, AnonymousUserMixin
from . import db
#, login_manager

#将数据库中的所有表映射到Python中

class Databases(db.Model):
    __tablename__ = 'databases'



class Amazon_Product(db.Model):
    __tablename__ = 'amazon_product'

    #ID,PID,Category,Price,Brand,Color,Quality
    #product_id = db.Column(db.String(20),db.Foreignkey(''))
    #client_id = db.Column(db.String(20), db.ForeignKey(
    #    'clients.id'), primary_key=True)
    #loan_id = db.Column(db.String(20), db.ForeignKey(
    #    'loans.id'), primary_key=True)

class Product:
    def __init__(self, id, name, price, available):
        self.id = id
        self.name = name
        self.price = price
        self.available = available

    @staticmethod
    def get(id):
        rows = app.db.execute('''
SELECT id, name, price, available
FROM Products
WHERE id = :id
''',
                              id=id)
        return Product(*(rows[0])) if rows is not None else None

    @staticmethod
    def get_all(available=True):
        rows = app.db.execute('''
SELECT id, name, price, available
FROM Products
WHERE available = :available
''',
                              available=available)
        return [Product(*row) for row in rows]


class Purchase:
    def __init__(self, id, uid, pid, time_purchased):
        self.id = id
        self.uid = uid
        self.pid = pid
        self.time_purchased = time_purchased

    @staticmethod
    def get(id):
        rows = app.db.execute('''
SELECT id, uid, pid, time_purchased
FROM Purchases
WHERE id = :id
''',
                              id=id)
        return Purchase(*(rows[0])) if rows else None

    @staticmethod
    def get_all_by_uid_since(uid, since):
        rows = app.db.execute('''
SELECT id, uid, pid, time_purchased
FROM Purchases
WHERE uid = :uid
AND time_purchased >= :since
ORDER BY time_purchased DESC
''',
                              uid=uid,
                              since=since)
        return [Purchase(*row) for row in rows]