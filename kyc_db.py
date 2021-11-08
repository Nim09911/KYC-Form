
#! Use WSL/Linux
from flask import Flask, render_template, request, escape
import validator
import logging, sys, random
from flaskext.mysql import MySQL

logging.basicConfig(level=logging.DEBUG)

'''
    #TODO:
        #* Images
        #! Date of Birth
        #! Generate Application Number
        #* DataBase
        #? View Data page -> input application number
        #? Update Data page -> time consuming
'''

app = Flask(__name__)

#* MySQL conection and configuration
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


@app.route('/')
@app.route('/kycform')
def entry():  
    return render_template('/home.html',
                            the_title = 'KYC Form Entry')

@app.route('/result', methods = ['POST', 'GET'])
def data():
    name = request.form['name']
    father_spouse_name = request.form['fsname']
    gender = request.form['gender']
    marital_status = request.form['maritalstatus']
    pan = request.form['pan']
    aadhar = request.form['aadhar']
    address = request.form['address']
    city = request.form['city']
    state = request.form['state']
    pincode = request.form['pincode']
    address_proof = request.form['poa']
    telephone = str(request.form['tel1']) + str(request.form['tel2']) + str(request.form['tel3']) or None
    mobile = str(request.form['mobile1']) + str(request.form['mobile2']) or None
    email = request.form['mail']
    income = request.form['income']
    occupation = request.form['occupation']
    title = 'KYC Form filled'


    if(validator.name_validation(name) and validator.name_validation(father_spouse_name) and validator.pan_validation(pan)):
        
        kycno = random.randint(10000000000000, 99999999999999)
        #! randomly generate KYCNO and check if its not already in table
        
        query = f"INSERT INTO IDENTITY_DETAILS (KYCNO, CUSTOMER_NAME, FS_NAME, GENDER, MARITAL_STATUS, PAN, AADHAR) VALUES ('{kycno}', '{name}', '{father_spouse_name}', '{gender}', '{marital_status}', '{pan}', '{aadhar}');"
        try:
            db.execute(query)
            conn.commit()
        except:
            return render_template('/home.html', error='Invalid Identity details filled', the_title='KYC Form Entry')
        
        query = f"INSERT INTO ADDRESS_DETAILS (KYCNO, HOME_ADDRESS, CITY, STATE_NAME, POSTAL_CODE, EMAIL, TELEPHONE, MOBILE) VALUES ('{kycno}', '{address}', '{city}', '{state}', '{pincode}', '{email}', '{telephone}', '{mobile}');"
        try:
            db.execute(query)
            conn.commit()
        except:
            return render_template('/home.html', error='Invalid Address details filled', the_title='KYC Form Entry')
        
        query = f"INSERT INTO OTHER_DETAILS (KYCNO, PAN, INCOME, OCCUPATION) VALUES ('{kycno}', '{pan}', '{income}', '{occupation}');"
        try:
            db.execute(query)
            conn.commit()
        except:
            return render_template('/home.html', error='Invalid Identity details filled', the_title='KYC Form Entry')
        
        return render_template('result.html',
                                s_name = name,
                                s_fsname = father_spouse_name, 
                                s_gender = gender,
                                s_marital = marital_status,
                                s_pan = pan,
                                s_aadhar = aadhar,
                                s_address = address,
                                s_city = city,
                                s_state = state,
                                s_pincode = pincode,
                                s_poa = address_proof,
                                s_income = income,
                                s_occupation = occupation,
                                the_title = title, 
        )
    else:
        return render_template('/home.html', error='Invalid information filled', the_title='KYC Form entry')

if __name__ ==  '__main__': 
    app.run(debug=True)
