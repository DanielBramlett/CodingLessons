name = 'Avery'
def function(message):
    global name
    print(f'{name}, {message}')

function('English Pirate')
function('Frigate named Fancy')
function('Secret service with Daniel Defoe for King William III and Queen Anne')

#End 1
print()

name = 'Vane'

def function1(rename):
    global name
    name = rename
    print(name)

function1('Rackham')
function1('Bonney')
function1('Reed')

#End 2