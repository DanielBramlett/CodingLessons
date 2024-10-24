my_len = len('Daniel')
print(type(my_len))

def add_numbers(a,b):
    result = a+b
    return result
add_numbers(1,2)

new_number = add_numbers(1,2)
print(new_number)

def make_dictionary(first,last,phone,zip):
    an_entry ={
        "first_name":first,
        "last_name":last,
        "phone_number":phone,
        "zip_code":zip
    }
    if an_entry['phone_number'] != '555-555-5555':
        an_entry['phone_number'] = '***-***-****'

    return an_entry
Daniel_data=make_dictionary("Daniel","Bramlett","555-555-5555",'30152')
print(Daniel_data['first_name'])
print(Daniel_data['zip_code'])

length = len([2,3,4])
print(length)
print(len[1,3,4])

def add_numbers(a,b):
    return a + b

result = add_numbers(2,add_numbers(1,1))

print(result)