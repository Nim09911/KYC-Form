
from validator import *


pan_test = {
    "AAAAA1245A" : True,
    "sddvd" : False,
    "aaaaa1245a" : False,
    "12456aaaa1" : False,
    "125" : False,
    "AAAAA1245AA" : False,
    "AAAAA/1245A" : False
    
}
    
aadhar_test = {
    "123456789156" : True,
    "ac5555555555" : False,
    "12365" : False,
    "aaaaaaaaaaaa" : False,
    "aaa555" : False,
    "aaa--555" : False 
}

name_test = {
    "Tiya Thomas" : True,
    "56888" : False,
    "Hi" : False,
    "SAni5" : False,
    "Ti+ya" : False
}
    
phone_test = {
    "9874563215" : True,
    "" : True,
    "15698" : False,
    "abcdefghij" : False,
    "acddb12345" : False,
    "abcde" : False,
    "12345678915" : False,
    "12345/6789" : False
}
    
dob_test = {
    "2001-05-26" :True,  
    "2016-02-29" :False,
    "2001-02-31" :False,
    "2001-02-29" :False,
    "2026-03-22" :False,
    "2001-04-31" :False,
    "2001-13-02" :False,
    "1810-03-02" :False,
    "2001-0k-02" :False,
    "200l-02-ml" :False
}
    
pin_test = {
    "695582" : True,
    "123" : False,
    "abc" : False,
    "abcdef" : False,
    "123-34" : False,
    "1236547" : False
}

 
def test_pan(pan,status):
    try :
        assert pan_validation(pan) == status
        print(f'Test case:  \"{pan}\" : PASSED.\nExpected : {status}\nAsserted : {pan_validation(pan)}\n')
    except:
        print(f'Test case:  \"{pan}\" : FAILED.\nExpected : {status}\nAsserted : {pan_validation(pan)}\n')

def test_aadhar(aadhar,status):
    try :
        assert aadhar_validation(aadhar) == status
        print(f'Test case:  \"{aadhar}\" : PASSED.\nExpected : {status}\nAsserted : {aadhar_validation(aadhar)}\n')
    except:
        print(f'Test case:  \"{aadhar}\" : FAILED.\nExpected : {status}\nAsserted : {aadhar_validation(aadhar)}\n')
 
def test_name(name,status):
    try :
        assert name_validation(name) == status
        print(f'Test case:  \"{name}\" : PASSED.\nExpected : {status}\nAsserted : {name_validation(name)}\n')
    except:
        print(f'Test case:  \"{name}\" : FAILED.\nExpected : {status}\nAsserted : {name_validation(name)}\n')

def test_phone(phno,status):
    try :
        assert phone_validation(phno) == status
        print(f'Test case:  \"{phno}\" : PASSED.\nExpected : {status}\nAsserted : {phone_validation(phno)}\n')
    except:
        print(f'Test case:  \"{phno}\" : FAILED.\nExpected : {status}\nAsserted : {phone_validation(phno)}\n')
 
def test_dob(dob,status):
    try :
        assert dob_validation(dob) == status
        print(f'Test case:  \"{dob}\" : PASSED.\nExpected : {status}\nAsserted : {dob_validation(dob)}\n')
    except:
        print(f'Test case:  \"{dob}\" : FAILED.\nExpected : {status}\nAsserted : {dob_validation(dob)}\n')
    

def test_pin(pin,status):   
    try :
        assert pin_validation(pin) == status
        print(f'Test case:  \"{pin}\" : PASSED.\nExpected : {status}\nAsserted : {pin_validation(pin)}\n')
    except:
        print(f'Test case:  \"{pin}\" : FAILED.\nExpected : {status}\nAsserted : {pin_validation(pin)}\n')





def main():
    
    
    print("\nTESTING PAN NUMBER\n")
    for pan in pan_test:
        test_pan(pan,pan_test[pan])
        

    print("\nTESTING AADHAR NUMBER\n")
    for ano in aadhar_test:
        test_aadhar(ano,aadhar_test[ano])
        
    print("\nTESTING NAME\n")
    for name in name_test:
        test_aadhar(name,name_test[name])
    
    print("\nTESTING PHONE NUMBER\n")
    for pno in phone_test:
        test_phone(pno,phone_test[pno])
   
    print("\nTESTING DATE OF BIRTH\n")
    for dob in dob_test:
        test_dob(dob,dob_test[dob])
            
    print("\nTESTING PIN\n")
    for pin in pin_test:
        test_pin(pin,pin_test[pin])
if __name__ == "__main__":
    main()
