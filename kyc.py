from flask import Flask, render_template, request, escape
import validator
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
@app.route('/kycform')
def entry():  
    return render_template('/home.html',
                            the_title = 'KYC Form Entry')

@app.route('/result', methods = ['POST'])
def search():
    name = request.form[ 'name' ]
    father_spouse_name = request.form[ 'fsname' ]
    pan = request.form[ 'pan' ]
    title = 'KYC Form filled'

    if(validator.name_validation(name) and validator.name_validation(father_spouse_name) and validator.pan_validation(pan)):
        return render_template('result.html', 
                                s_name = name, 
                                s_fsname = father_spouse_name, 
                                s_pan = pan,
                                the_title = title, 
        )
    else:
        return render_template('/home.html', error='Invalid information filled')

if __name__ ==  '__main__': 
    app.run(debug=True)
