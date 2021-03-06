
#! Use WSL/Linux
from flask import Flask, render_template, request, escape
from validator import *
import logging, sys, random
from flaskext.mysql import MySQL

logging.basicConfig(level=logging.DEBUG)

'''
    #TODO:
        #? Update Data page -> time consuming
'''

app = Flask(__name__)

#* MySQL conection and configuration
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = 'Ashumysql@10'
# app.config['MYSQL_DATABASE_DB'] = 'kyc'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'kyc'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL(app)

try:
    conn = mysql.connect()
except:
    logging.ERROR('Unsuccesfull connection to Database')
    sys.exit()
db = conn.cursor()


# @app.route('/')
# def home():
#     return render_template('/homepage.html', the_title = 'Home Page')
@app.route('/')
@app.route('/kycform')
def entry():  
    return render_template('/home.html',
                            the_title = 'KYC Form Entry')

@app.route('/result', methods = ['POST'])
def data():
    name = request.form['name']
    father_spouse_name = request.form['fsname']
    gender = request.form['gender']
    marital_status = request.form['maritalstatus']
    dob = request.form['dob']
    pan = request.form['pan']
    aadhar = request.form['aadhar']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    pincode = request.form['pincode']
    address_proof = request.form['poa']
    telephone = str(request.form['tel1']) or ""
    mobile = str(request.form['mobile1']) or ""
    email = request.form['mail']
    income = request.form['income']
    occupation = request.form['occupation']
    title = 'KYC Form filled'

    def validation_identity():
        a = name_validation(name)
        b = name_validation(father_spouse_name)
        c = pan_validation(pan)
        d = aadhar_validation(aadhar)
        e = dob_validation(dob)
        return   a and b and c and d and e

    def validation_address():
        a = phone_validation(mobile)
        b = telephone_validation(telephone)
        c = pin_validation(pincode)
        return a and b and c

    def validation_others():
        return True        
        
    kycno = random.randint(10000000000000, 99999999999999)
    query = "SELECT KYCNO FROM IDENTITY_DETAILS;"
    db.execute(query)
    nums = [item[0] for item in db.fetchall()]
    while(kycno in nums):
        logging.info('kycno already exists')
        kycno = random.randint(10000000000000, 99999999999999)

    query = f"SELECT PAN FROM IDENTITY_DETAILS;"
    db.execute(query)
    pans = [item[0] for item in db.fetchall()]
    if(pan in pans):
        logging.info('PAN already exists')
        return render_template('/home.html', error='Data already exists', the_title='KYC Form Entry')
    
    if(validation_identity()):
        query = f"INSERT INTO IDENTITY_DETAILS (KYCNO, CUSTOMER_NAME, FS_NAME, GENDER, MARITAL_STATUS, DOB, PAN, AADHAR) VALUES ('{kycno}', '{name}', '{father_spouse_name}', '{gender}', '{marital_status}', '{dob}', '{pan}', '{aadhar}');"
        try:
            db.execute(query)
        except:
            return render_template('/home.html', error='Invalid Identity details filled', the_title='KYC Form Entry')
        if(validation_address()):
            query = f"INSERT INTO ADDRESS_DETAILS (KYCNO, HOME_ADDRESS, CITY, STATE_NAME, POSTAL_CODE, EMAIL, TELEPHONE, MOBILE) VALUES ('{kycno}', '{address}', '{city}', '{state}', '{pincode}', '{email}', '{telephone}', '{mobile}');"
            try:
                db.execute(query)
            except:
                return render_template('/home.html', error='Invalid Address details filled', the_title='KYC Form Entry')
            if(validation_others()):
                query = f"INSERT INTO OTHER_DETAILS (KYCNO, INCOME, OCCUPATION) VALUES ('{kycno}', '{income}', '{occupation}');"
                try:
                    db.execute(query)
                except:
                    return render_template('/home.html', error='Invalid Other details filled', the_title='KYC Form Entry')
                conn.commit()
                return render_template('result.html',
                                s_kyc = kycno,
                                s_name = name,
                                s_fsname = father_spouse_name, 
                                s_gender = gender,
                                s_marital = marital_status,
                                s_dob = dob,
                                s_pan = pan,
                                s_aadhar = aadhar,
                                s_address = address,
                                s_city = city,
                                s_state = state,
                                s_pincode = pincode,
                                s_poa = address_proof,
                                s_email = email,
                                s_tel = telephone,
                                s_mobile = mobile,
                                s_income = income,
                                s_occupation = occupation,
                                the_title = title, 
        )
            else:
                return render_template('/home.html', error='Invalid Other details filled', the_title='KYC Form Entry')
        else:
            return render_template('/home.html', error='Invalid Address details filled', the_title='KYC Form Entry')
    else:
        return render_template('/home.html', error='Invalid Identity information filled', the_title='KYC Form entry')


@app.route('/view')
def view():
    logging.debug('now rendering view.html')
    return render_template('/view.html')

@app.route('/viewresult', methods = ['POST'])
def viewresult():
    logging.debug('viewresult has been called')
    kycno = int(request.form['kycno'])
    #* NATURAL JOIN OF ALL TABLES ISNOT WORKING

    try:
        query = f"SELECT * FROM IDENTITY_DETAILS WHERE KYCNO = '{kycno}';"
        db.execute(query)
        for (KYCNO, CUSTOMER_NAME, FS_NAME, MARITAL_STATUS, GENDER, DOB, PAN, AADHAR) in db:
            kycno, name, father_spouse_name, marital_status, gender, dob, pan, aadhar = KYCNO, CUSTOMER_NAME, FS_NAME, MARITAL_STATUS, GENDER, DOB, PAN, AADHAR
        
        query = f"SELECT * FROM ADDRESS_DETAILS WHERE KYCNO = '{kycno}';"
        db.execute(query)
        for(KYCNO, HOME_ADDRESS, CITY, STATE_NAME, POSTAL_CODE, EMAIL, TELEPHONE, MOBILE) in db:
            address, city, state, pincode, email = HOME_ADDRESS, CITY, STATE_NAME, POSTAL_CODE, EMAIL
            telephone = TELEPHONE
            if(telephone is None):
                telephone = 'None'
            mobile = MOBILE
            if(mobile is None):
                mobile = 'None'
        
        query = f"SELECT * FROM OTHER_DETAILS WHERE KYCNO = '{kycno}';"
        db.execute(query)
        for(KYCNO, INCOME, OCCUPATION) in db:
            income, occupation = INCOME, OCCUPATION
        title = f'Form Data for {kycno}'
        return render_template('/viewresult.html',
                        s_kyc = kycno,
                        s_name = name,
                        s_fsname = father_spouse_name, 
                        s_gender = gender,
                        s_marital = marital_status,
                        s_dob = dob,
                        s_pan = pan,
                        s_aadhar = aadhar,
                        s_address = address,
                        s_city = city,
                        s_state = state,
                        s_pincode = pincode,
                        s_poa = 'Pending for approval',
                        s_email = email,
                        s_tel = telephone,
                        s_mobile = mobile,
                        s_income = income,
                        s_occupation = occupation,
                        the_title = title, 
        )
    except:
        logging.info('Record does not exist -> enter error message')
        return render_template('/view.html', error='Invalid KYC Number')

@app.route('/updateform')
def update():
    return render_template('/updateform.html')

@app.route('/updateresult', methods=['POST'])
def updateform():
    kycno = request.form['kycno']
    marital_status = request.form['maritalstatus']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    pincode = request.form['pincode']
    address_proof = request.form['poa'] 
    telephone = str(request.form['tel1']) or ""
    mobile = str(request.form['mobile1']) or ""
    email = request.form['mail']
    income = request.form['income']
    occupation = request.form['occupation']

    if(address != '' and city != '' and state !='' and pin_validation(pincode) and address_proof !=''):
        query= f"UPDATE ADDRESS_DETAILS SET HOME_ADDRESS = '{address}', CITY = '{city}', STATE_NAME = '{state}', POSTAL_CODE = '{pincode}' WHERE KYCNO = '{kycno}';"
        try:
            db.execute(query)
        except:
            return render_template('/updateform.html', error='Invalid information in Address details')
    if(telephone_validation(telephone)):
        query= f"UPDATE ADDRESS_DETAILS SET TELEPHONE = '{telephone}' WHERE KYCNO = '{kycno}';"
        try:
            db.execute(query)
        except:
            return render_template('/updateform.html', error='Invalid information in telephone details')
    if(phone_validation(mobile)):
        query= f"UPDATE ADDRESS_DETAILS SET MOBILE = '{mobile}' WHERE KYCNO = '{kycno}';"
        try:
            db.execute(query)
        except:
            return render_template('/updateform.html', error='Invalid information in mobile details')

    query= f"UPDATE ADDRESS_DETAILS SET EMAIL = '{email}' WHERE KYCNO = '{kycno}';"
    try:
        db.execute(query)
    except:
        return render_template('/updateform.html', error='Invalid information in Email details')

    query= f"UPDATE OTHER_DETAILS SET INCOME = '{income}' WHERE KYCNO = '{kycno}';"
    try:
        db.execute(query)
    except:
        return render_template('/updateform.html', error='Invalid information in Income details')

    query= f"UPDATE OTHER_DETAILS SET OCCUPATION = '{occupation}' WHERE KYCNO = '{kycno}';"
    try:
        db.execute(query)
    except:
        return render_template('/updateform.html', error='Invalid information in Occupation details')

    query= f"UPDATE IDENTITY_DETAILS SET MARITAL_STATUS = '{marital_status}' WHERE KYCNO = '{kycno}';"
    try:
        db.execute(query)
    except:
        return render_template('/updateform.html', error='Invalid information in Marital_Status details')
    
    conn.commit()

    try:
        query = f"SELECT * FROM IDENTITY_DETAILS WHERE KYCNO = '{kycno}';"
        db.execute(query)
        for (KYCNO, CUSTOMER_NAME, FS_NAME, MARITAL_STATUS, GENDER, DOB, PAN, AADHAR) in db:
            kycno, name, father_spouse_name, marital_status, gender, dob, pan, aadhar = KYCNO, CUSTOMER_NAME, FS_NAME, MARITAL_STATUS, GENDER, DOB, PAN, AADHAR
        
        query = f"SELECT * FROM ADDRESS_DETAILS WHERE KYCNO = '{kycno}';"
        db.execute(query)
        for(KYCNO, HOME_ADDRESS, CITY, STATE_NAME, POSTAL_CODE, EMAIL, TELEPHONE, MOBILE) in db:
            address, city, state, pincode, email = HOME_ADDRESS, CITY, STATE_NAME, POSTAL_CODE, EMAIL
            telephone = TELEPHONE
            if(telephone is None):
                telephone = 'None'
            mobile = MOBILE
            if(mobile is None):
                mobile = 'None'
        
        query = f"SELECT * FROM OTHER_DETAILS WHERE KYCNO = '{kycno}';"
        db.execute(query)
        for(KYCNO, INCOME, OCCUPATION) in db:
            income, occupation = INCOME, OCCUPATION
        title = f'Form Data for {kycno}'
        return render_template('/updateresult.html',
                        s_kyc = kycno,
                        s_name = name,
                        s_fsname = father_spouse_name, 
                        s_gender = gender,
                        s_marital = marital_status,
                        s_dob = dob,
                        s_pan = pan,
                        s_aadhar = aadhar,
                        s_address = address,
                        s_city = city,
                        s_state = state,
                        s_pincode = pincode,
                        s_poa = 'Pending for approval',
                        s_email = email,
                        s_tel = telephone,
                        s_mobile = mobile,
                        s_income = income,
                        s_occupation = occupation,
                        the_title = title, 
        )
    except:
        logging.info('Record does not exist -> enter error message')
        return render_template('/updateform.html', error='Invalid KYC Number')

if __name__ ==  '__main__': 
    app.run(debug=True)