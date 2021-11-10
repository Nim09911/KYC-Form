
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

telephone_test = {
    "9874563215" : True,
    "" : True,
    "15698" : False,
    "09876789876" : True,
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
        print(f'Test case:  \"{pan}\" : PASSED.\nExpected : {status}\tAsserted : {pan_validation(pan)}\n')
        return True
    except:
        print(f'Test case:  \"{pan}\" : FAILED.\nExpected : {status}\tAsserted : {pan_validation(pan)}\n')
        return False

def test_aadhar(aadhar,status):
    try :
        assert aadhar_validation(aadhar) == status
        print(f'Test case:  \"{aadhar}\" : PASSED.\nExpected : {status}\tAsserted : {aadhar_validation(aadhar)}\n')
        return True
    except:
        print(f'Test case:  \"{aadhar}\" : FAILED.\nExpected : {status}\tAsserted : {aadhar_validation(aadhar)}\n')
        return False
 
def test_name(name,status):
    try :
        assert name_validation(name) == status
        print(f'Test case:  \"{name}\" : PASSED.\nExpected : {status}\tAsserted : {name_validation(name)}\n')
        return True
    except:
        print(f'Test case:  \"{name}\" : FAILED.\nExpected : {status}\tAsserted : {name_validation(name)}\n')
        return False

def test_phone(phno,status):
    try :
        assert phone_validation(phno) == status
        print(f'Test case:  \"{phno}\" : PASSED.\nExpected : {status}\tAsserted : {phone_validation(phno)}\n')
        return True
    except:
        print(f'Test case:  \"{phno}\" : FAILED.\nExpected : {status}\tAsserted : {phone_validation(phno)}\n')
        return False

def test_telephone(phno,status):
    try :
        assert telephone_validation(phno) == status
        print(f'Test case:  \"{phno}\" : PASSED.\nExpected : {status}\tAsserted : {telephone_validation(phno)}\n')
        return True
    except:
        print(f'Test case:  \"{phno}\" : FAILED.\nExpected : {status}\tAsserted : {telephone_validation(phno)}\n')
        return False
 
def test_dob(dob,status):
    try :
        assert dob_validation(dob) == status
        print(f'Test case:  \"{dob}\" : PASSED.\nExpected : {status}\tAsserted : {dob_validation(dob)}\n')
        return True
    except:
        print(f'Test case:  \"{dob}\" : FAILED.\nExpected : {status}\tAsserted : {dob_validation(dob)}\n')
        return False
    

def test_pin(pin,status):   
    try :
        assert pin_validation(pin) == status
        print(f'Test case:  \"{pin}\" : PASSED.\nExpected : {status}\tAsserted : {pin_validation(pin)}\n')
        return True
    except:
        print(f'Test case:  \"{pin}\" : FAILED.\nExpected : {status}\tAsserted : {pin_validation(pin)}\n')
        return False


def main():
    
    max_count = len(pan_test)
    count, countpass, countfail = 0, 0, 0    
    print("\nTESTING PAN NUMBER\n")
    for pan in pan_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")        
        val = test_pan(pan,pan_test[pan])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"Passed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")
        
    max_count = len(aadhar_test)
    count, countpass, countfail = 0, 0, 0 
    print("\nTESTING AADHAR NUMBER\n")
    for ano in aadhar_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")
        val = test_aadhar(ano,aadhar_test[ano])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"Passed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")

    max_count = len(name_test)
    count, countpass, countfail = 0, 0, 0       
    print("\nTESTING NAME\n")
    for name in name_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")
        val = test_name(name,name_test[name])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"\nPassed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")

    max_count = len(phone_test)
    count, countpass, countfail = 0, 0, 0  
    print("\nTESTING MOBILE NUMBER\n")
    for pno in phone_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")
        val = test_phone(pno,phone_test[pno])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"\nPassed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")

    max_count = len(telephone_test)
    count, countpass, countfail = 0, 0, 0  
    print("\nTESTING TELEPHONE NUMBER\n")
    for pno in telephone_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")
        val = test_telephone(pno,telephone_test[pno])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"\nPassed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")

    max_count = len(dob_test)
    count, countpass, countfail = 0, 0, 0   
    print("\nTESTING DATE OF BIRTH\n")
    for dob in dob_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")
        val = test_dob(dob,dob_test[dob])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"\nPassed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")

    max_count = len(pin_test)
    count, countpass, countfail = 0, 0, 0             
    print("\nTESTING PIN\n")
    for pin in pin_test:
        count += 1
        print(f"Case{count}/{max_count}:", end=" ")
        val = test_pin(pin, pin_test[pin])
        if(val):
            countpass += 1
        else:
            countfail +=1
    print(f"\nPassed:{countpass}/{max_count}, Failed:{countfail}/{max_count}\n")

if __name__ == "__main__":
    main()