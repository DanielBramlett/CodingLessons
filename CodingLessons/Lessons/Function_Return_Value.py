my_len = len('Daniel')
print(type(my_len))

def add_numbers(a,b):
    result = a+b
    return result
add_numbers(1,2)

new_number = add_numbers(1,2)
print(new_number)

def make_dictionary(first,last,phone,zip):
    return{
        "first_name":first,
        "last_name":last,
        "phone_number":phone,
        "zip_code":zip
    }
Daniel_data=make_dictionary("Daniel","Bramlett","555-555-5555",30152)
print(Daniel_data['zip_code'])