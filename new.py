from flask import Flask
from flask import request
from flask import render_template
from flask import abort, redirect, url_for
from flask import make_response
from datetime import datetime, date, time
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, DateTime
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
from sqlalchemy import distinct


engine = create_engine('sqlite:///mybase.db')

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)

metadata = MetaData()

users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('second_name', String),
    Column('login', String),
    Column('password', String),
    Column('create_date', DateTime),
    Column('e_mail', String)
)


uuids_table = Table('uuids', metadata,
    Column('id', Integer, primary_key=True),
    Column('cookie_date', DateTime),
    Column('cookie_uuid', String),
    Column('user_id', Integer, ForeignKey('users.id'))
)


basket_table = Table('baskets', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('create_basket_date', DateTime),
    Column('user_id', Integer, ForeignKey('users.id'))
)

purchase_table = Table('purchase', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('quantity', Integer),
    Column('price', Integer),
    Column('id_basket', Integer, ForeignKey('baskets.id')),
    Column('type', Integer),
    Column('subtype', Integer)
)

type_table = Table('types', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String)
)

subtype_table = Table('subtypes', metadata,
    Column('id', Integer, primary_key = True),
    Column('name', String),
    Column('id_type', Integer, ForeignKey('types.id'))
)

table_types_and_subtypes_upload_process = Table('upload_process', metadata,
    Column('id', Integer, primary_key = True),
    Column('table_name', String),
    Column('result_of_upload', String)
)

metadata.create_all(engine)

class User:
    def __init__(self, name, second_name, login, password, e_mail):
        self.name = name
        self.second_name = second_name
        self.login = login
        self.password = password
        self.create_date = datetime.now()
        self.e_mail = e_mail

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

class Uuid_class:
    def __init__(self, cookie_date, cookie_uuid):
        self.cookie_date = cookie_date
        self.cookie_uuid = cookie_uuid

class Basket:
    def __init__(self, name, user_id):
        self.name = name
        self.create_basket_date = datetime.datetime.now()
        self.user_id = user_id

class Purchase:
    def __init__(self, name, quantity, price, id_basket, _type, subtype):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.id_basket = id_bakset
        self._type = _type
        self.subtype = subtype

class Types:
    def __init__ (self, name):
        self.name = name

class Subtype:
    def __init__(self, name, id_type):
        self.name = name
        self.id_type = id_type

class Types_and_subtypes_upload_process:
    def __init__(self, table_name):
        self.table_name = table_name
        self.result_of_upload = 0


mapper(User, users_table)
mapper(Basket, basket_table)
mapper(Purchase, purchase_table)
mapper(Types, type_table)
mapper(Subtype, subtype_table)
mapper(Types_and_subtypes_upload_process, table_types_and_subtypes_upload_process)

#служебные функции для подготовки работы базы

def verify_table_types_and_subtypes_upload_process():
    list_uploads = []
    session1 = Session()
    for row in session1.query(Types_and_subtypes_upload_process):
        list_uploads.append(row.table_name)
    if len(list_uploads) == 0:
        zapolnenie_table_types_and_subtypes_upload_process()
    session1.close()

def zapolnenie_table_types_and_subtypes_upload_process():
    session2 = Session()
    session2.add_all([Types_and_subtypes_upload_process('Types'), Types_and_subtypes_upload_process('Subtype')])
    session2.commit()
    session2.close()

def zapolnenie_table_types():
    session4 = Session()
    session4.add_all([Types('Товар'), Types('Услуга')])
    session4.commit()
    session4.close()

def zapolnenie_table_subtype():
    session6 = Session()
    session6.add_all([Subtype('Овощи и фрукты', 1), Subtype('Образование', 2)])
    session6.commit()
    session6.close()

def verify_table_types():
    session3 = Session()
    for row in session3.query(Types_and_subtypes_upload_process):
        #if Types_and_subtypes_upload_process.table_name == 'Types' and Types_and_subtypes_upload_process.result_of_upload == 0:
         #   zapolnenie_table_types()
        if Types_and_subtypes_upload_process.table_name == 'Subtype' and Types_and_subtypes_upload_process.result_of_upload == 0:
            zapolnenie_table_subtype()
    session3.close()

verify_table_types_and_subtypes_upload_process()
verify_table_types()

session8 = Session()# работает
for row in session8.query(Types_and_subtypes_upload_process):
    print(row.id, row.table_name, row.result_of_upload)
session8.close()

session9 = Session() #НЕРАБОТАЕТ
for row in session9.query(Subtype):
    print(row)
session8.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authenter', methods=['GET','POST'])
def authenter():
    if request.method == 'POST':
        user_login = request.form['newlogin']
        user_password = request.form['newpassword']
        if verify_login_password(user_login, user_password):
            resp = make_response(redirect(url_for('.general')))
            resp.set_cookie('username', user_login, max_age=60*60*24)
            return resp
        else:
            return render_template('index.html')

def verify_login_password(user_login, user_password):
    file = open(r'C:\Users\sli-sergej\Desktop\PythonLearn\myflask2\venv\static\loginpassword.txt', 'r')
    for line in file:
        list1 = line.split()
        if list1[0] == user_login:
            if list1[1] == user_password:
                return True
            else:
                return False
    return False

def verify_time_cookie():
    pass


@app.route('/registration')
def registration():
    return render_template('registration.html')
    
@app.route('/auth', methods=['GET','POST'])
def auth():
    if request.method == 'POST':
        username = request.form['newname']
        user_secondname = request.form['newsecondname']
        user_login = request.form['newlogin']
        user_password = request.form['newpassword']
        user_e_mail = request.form['e_mail']
        if verify_login_password_for_create_new_user(user_login):
            save_new_user(username, user_secondname, user_login, user_password, user_e_mail)
            return render_template('general.html')
        else:
            return render_template('registration2.html')

def verify_login_password_for_create_new_user(user_login):
    session = Session()
    for row in session.query(User):
        if row.login == user_login:
            session.close()
            return False
    session.close()
    return True

def save_new_user(username, user_secondname, user_login, user_password, user_e_mail):
    session = Session()
    newUser = User(username, user_secondname, user_login, user_password, user_e_mail)
    session.add(newUser)
    session.commit()
    session.close()


def create_current_data_and_time():
    pass

def generate_uid():
    return uuid.uuid4().hex

def verify_uuid():
    pass

        
@app.route('/general')
def general():
    username = request.cookies.get('username')
    if verify_login_for_cookies(username):
        return render_template('general.html')
    else:
        return redirect(url_for('index'))


    
def verify_login_for_cookies(user_login):
    file = open(r'C:\Users\sli-sergej\Desktop\PythonLearn\myflask2\venv\static\loginpassword.txt', 'r')
    for line in file:
        list1 = line.split()
        if list1[0] == user_login:
            return True
    return False

@app.route('/listuser')
def listuser():
    session = Session()
    list1 = []
    for row in session.query(User):
        list1.append(row.login)
        list1.append(row.create_date)
    session.close()
    return render_template('userlist.html', listuser=list1)





