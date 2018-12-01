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
from sqlalchemy import update


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
    Column('e_mail', String),
    Column('role', String)                
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
    Column('result_of_upload', Integer)
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
        self.role = 'User'

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

class Uuid_class:
    def __init__(self, cookie_date, cookie_uuid, user_id):
        self.cookie_date = cookie_date
        self.cookie_uuid = cookie_uuid
        self.user_id = user_id

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

class Controler:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def return_model_name(self):
        return self.model.return_name()

    def verify_time_uuid(self, user_uuid):
        return self.model.verify_time_uuid(user_uuid)

    def verify_login_password(self, user_login, user_password):
        return self.model.verify_login_password(user_login, user_password)

    def create_new_uuid(self, user_login):
        return self.model.create_new_uuid(user_login)

    def update_uuid(self, user_login):
        return self.model.update_uuid(user_login)

    def find_uuid(self, user_login):
        return self.model.find_uuid(user_login)

class Model:
    def __init__(self, name):
        self.name = name

    def return_name(self):
        return self.name

    def verify_time_uuid(self, user_uuid):
        session = Session()
        my_uuid = session.query(Uuid_class).filter(Uuid_class.cookie_uuid == user_uuid).first()
        delta = datetime.now() - my_uuid.cookie_date
        if delta.days > 1:
            session.close()
            return True
        else:
            session.close()
            return False

    def verify_login_password(self, user_login, user_password):
        session = Session()
        for row in session.query(User):
            if row.login == user_login:
                if row.password == user_password:
                    session.close()
                    return True
                else:
                    session.close()
                    return False
        session.close()
        return False

    def create_new_uuid(self, user_login):
        session = Session()
        my_user = session.query(User).filter(User.login == user_login).first()
        session2 = Session()
        my_uuid = Uuid_class(datetime.now(), self.generate_uid(), my_user.id)
        session2.add(my_uuid)
        session2.commit()
        session2.close()
        session.close()        
        return True

    def generate_uid(self):
        return uuid4().hex

    def update_uuid(self, user_login):
        session = Session()
        my_user = session.query(User).filter(User.login == user_login).first()
        session33 = Session()
        old_uuid = session33.query(Uuid_class).filter(Uuid_class.user_id == my_user.id).first()
        old_uuid.cookie_uuid = self.generate_uid()
        old_uuid.cookie_date = datetime.now()
        session33.add(old_uuid)
        session33.commit()
        session33.close()
        session.close()
        return True

    def find_uuid(self, user_login):
        session = Session()
        my_user = session.query(User).filter(User.login == user_login).first()
        session33 = Session()
        my_uuid = session33.query(Uuid_class).filter(Uuid_class.user_id == my_user.id).first()
        session33.close()
        session.close()
        return my_uuid.cookie_uuid        


mapper(User, users_table)
mapper(Uuid_class, uuids_table)
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
    session5 = Session()
    session5.add_all([Types('Товар'), Types('Услуга')])
    session5.commit()
    session5.close()

def zapolnenie_table_subtype():
    session6 = Session()
    session6.add_all([Subtype('Овощи и фрукты', 1), Subtype('Хлебобулочные изделия', 1), Subtype('Кондитерские изделия', 1), Subtype('Вино-водочные изделия', 1),
                      Subtype('Безалкогольные напитки', 1), Subtype('Молоко-масляные изделия', 1), Subtype('Маяные и колбасные изделия', 1), Subtype('Рыбные изделия', 1), Subtype('Яичные изделия', 1),
                      Subtype('Пищевые жиры', 1), Subtype('Табачные изделия', 1), Subtype('Хозяйственные и галантерейные изделия', 1), Subtype('Бытовая химия', 1), Subtype('Стеклянные товары', 1),
                      Subtype('Керамические товары', 1), Subtype('Строительные материалы', 1), Subtype('Мебель', 1), Subtype('Металлические товары', 1), Subtype('Электротовары и бытовая техника', 1),
                      Subtype('Текстиль', 1), Subtype('Одежда, обувь, аксессуары', 1), Subtype('Ювелирные изделия', 1), Subtype('Бумажные изделия, книги, канцелярия', 1),
                      Subtype('Музыка, Кино', 1), Subtype('Игрушки', 1), Subtype('Спортивные товары', 1), Subtype('Другие товары', 1), 
                      Subtype('Образование', 2), Subtype('Клининг', 2), Subtype('Перевозка вещей', 2), Subtype('Перевозка людей', 2), Subtype('Юридические услуги', 2), Subtype('Медицинские услуги', 2),
                      Subtype('Банковские услуги', 2), Subtype('Косметология и парикмахерская', 2), Subtype('Туристические услуги', 2), Subtype('Рекламные услуги', 2), Subtype('Другие услуги', 2)])
    session6.commit()
    session6.close()

def verify_table_types():
    session3 = Session()
    for row in session3.query(Types_and_subtypes_upload_process):
        if row.table_name == 'Types' and row.result_of_upload == 0:
            zapolnenie_table_types()       
    session3.close()
    session = Session()
    table_update = session.query(Types_and_subtypes_upload_process).filter(Types_and_subtypes_upload_process.table_name=='Types').first()
    table_update.result_of_upload = 1
    session.add(table_update)
    session.commit()
    session.close()

def verify_table_subtypes():
    session = Session()
    for row in session.query(Types_and_subtypes_upload_process):
        if row.table_name == 'Subtype' and row.result_of_upload == 0:
            zapolnenie_table_subtype()            
    session.close()
    session = Session()
    table_update = session.query(Types_and_subtypes_upload_process).filter(Types_and_subtypes_upload_process.table_name=='Subtype').first()
    table_update.result_of_upload = 1
    session.add(table_update)
    session.commit()
    session.close()

verify_table_types_and_subtypes_upload_process()
verify_table_types()
verify_table_subtypes()

model = Model('model')
controler = Controler('controler', model)

session = Session()
for row in session.query(Uuid_class):
    print(row.id, row.cookie_date, row.cookie_uuid, row.user_id)
session.close()

app = Flask(__name__)


@app.route('/')
def index():
    user_uuid = request.cookies.get('user_uuid')
    if user_uuid == '' or user_uuid == None:
        return render_template('index.html')
    else:
        if controler.verify_time_uuid(user_uuid) == False:
            resp = make_response(redirect(url_for('.general')))
            return resp
        else:
            return render_template('index.html')

@app.route('/authenter', methods=['GET','POST'])
def authenter():
    if request.method == 'POST':
        user_login = request.form['newlogin']
        user_password = request.form['newpassword']
        if controler.verify_login_password(user_login, user_password):
            controler.update_uuid(user_login)
            my_uuid = controler.find_uuid(user_login)
            resp = make_response(redirect(url_for('.general')))           
            resp.set_cookie('user_uuid', my_uuid, max_age=60*60*24)
            return resp
        else:
            return render_template('index.html')


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
            controler.create_new_uuid(user_login)
            new_uuid = controler.find_uuid(user_login)
            resp = make_response(redirect(url_for('.general')))
            resp.set_cookie('user_uuid', new_uuid, max_age=60*60*24)
            return resp
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

    
@app.route('/general')
def general():
    my_uuid = request.cookies.get('user_uuid')
    if my_uuid == '' or my_uuid == None or controler.verify_time_uuid(my_uuid) == True:
        return redirect(url_for('index'))
    else:
        return render_template('general.html')
    
def verify_login_for_cookies(user_login):
    session = Session()
    for row in session.query(User):
        if row.login == user_login:
            session.close()
            return True
    session.close()
    return False

@app.route('/listuser')
def listuser():
    my_uuid = request.cookies.get('user_uuid')
    session = Session()
    list1 = []
    for row in session.query(User):
        list1.append(row.login)
        list1.append(row.create_date)
    session.close()
    return render_template('userlist.html', listuser=list1)

@app.route('/logout')
def logout():
    my_uuid = request.cookies.get('user_uuid')
    session = Session()
    old_uuid = session.query(Uuid_class).filter(Uuid_class.cookie_uuid == my_uuid).first()
    old_uuid.cookie_date = datetime(1900, 1, 1, 1, 1, 1)
    session.add(old_uuid)
    session.commit()
    session.close()
    if controler.verify_time_uuid(my_uuid) == False:
        resp = make_response(redirect(url_for('.general')))
        return resp
    else:
        resp = make_response(redirect(url_for('.index')))
        return resp    
    
    


