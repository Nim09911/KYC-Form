
from validator import *

def test_pan(pan,status):
    try :
        assert pan_validation(pan) == status
        print(f'Test cased \"{pan}\" passed.\nExpected : {status}\nAsserted {pan_validation(pan)}\n')
    except:
        print(f'Test cased \"{pan}\" failed.\nExpected : {status}\nAsserted {pan_validation(pan)}\n')

def test_aadhar(aadhar,status):
    try :
        assert aadhar_validation(aadhar) == status
        print(f'Test cased \"{aadhar}\" passed.\nExpected : {status}\nAsserted {aadhar_validation(aadhar)}\n')
    except:
        print(f'Test cased \"{aadhar}\" failed.\nExpected : {status}\nAsserted {aadhar_validation(aadhar)}\n')
 
def test_name(name,status):
    try :
        assert name_validation(name) == status
        print(f'Test cased \"{name}\" passed.\nExpected : {status}\nAsserted {name_validation(name)}\n')
    except:
        print(f'Test cased \"{name}\" failed.\nExpected : {status}\nAsserted {name_validation(name)}\n')

def test_phone(phno,status):
    try :
        assert phone_validation(phno) == status
        print(f'Test cased \"{phno}\" passed.\nExpected : {status}\nAsserted {phone_validation(phno)}\n')
    except:
        print(f'Test cased \"{phno}\" failed.\nExpected : {status}\nAsserted {phone_validation(phno)}\n')
 
def test_dob(day,month,year,status):
    try :
        assert dob_validation(day, month, year) == status
        print(f'Test cased \"{day}-{month}-{year}\" passed.\nExpected : {status}\nAsserted {dob_validation(day, month, year)}\n')
    except:
        print(f'Test cased \"{day}-{month}-{year}\" failed.\nExpected : {status}\nAsserted {dob_validation(day, month, year)}\n')
    

def test_pin(pin,status):   #Format : 6 integers
    try :
        assert pin_validation(pin) == status
        print(f'Test cased \"{pin}\" passed.\nExpected : {status}\nAsserted {pin_validation(pin)}\n')
    except:
        print(f'Test cased \"{pin}\" failed.\nExpected : {status}\nAsserted {pin_validation(pin)}\n')





def main():
    
    
    print("\nTESTING PAN NUMBER\n")
    test_pan("AAAAA1245A",True)
    test_pan("sddvd",False)
    test_pan("aaaaa1245a",False)
    test_pan("12456aaaa1",False)
    test_pan("125",False)
    test_pan("AAAAA1245AA",False)#test failed !
    test_pan("AAAAA/1245A",False)
    
    print("\nTESTING AADHAR NUMBER\n")
    test_aadhar("123456789156",True)
    test_aadhar("ac5555555555",False)
    test_aadhar("12365",False)
    test_aadhar("aaaaaaaaaaaa",False)
    test_aadhar("aaa555",False)
    test_aadhar("aaa--555",False)
    
    print("\nTESTING NAME\n")
    test_name("Tiya",True)
    test_name("56888",False)
    test_name("Hi",False)
    test_name("SAni5",False)#test failed !
    test_name("Ti+/ya",False)#test failed !
    
    print("\nTESTING PHONE NUMBER\n")
    test_phone("9874563215",True)
    test_phone("15698",False)
    test_phone("abcdefghij",False)
    test_phone("acddb12345",False)
    test_phone("abcde",False)
    test_phone("12345678915",False)#test failed !
    test_phone("12345/6789",False)
    
    print("\nTESTING DATE OF BIRTH\n")
    test_dob(26,5,2001,True)
    test_dob(29,2,2016,True)
    test_dob(31,2,2001,False)
    test_dob(29,2,2001,False)
    test_dob(22,3,2026,False)#test failed
    test_dob(31,4,2001,False)
    test_dob(2,13,2001,False)
    test_dob(2,3,1810,False)#test failed
    test_dob(2,-5,2001,False)
    test_dob(2,13,200-4,False)
    
    print("\nTESTING PIN\n")
    test_pin("695582",True)
    test_pin("123",False)
    test_pin("abc",False)
    test_pin("abcdef",False)
    test_pin("123-34",False)
    test_pin("1236547",False)#test failed
    
if __name__ == "__main__":
    main()
