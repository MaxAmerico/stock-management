import json
import random
dic_accounts = {'joao':'ehwh8',
        'maria':'eneee2',
        'pedro':'rn3r3',
        'jose':'fferfge5'
                        }                    

file_json = json.dumps(dic_accounts, indent=4)

with open('users.json', 'w') as file:
    file.write(file_json)
 
#Start code
print('- - - Welcome to stock menagement - - -')

login_or_register = input('What would you wish? A. Login. B. Register:').upper()

if login_or_register == 'A':
 username = input('Put your username here:')
 password = input('Put your password here:')

 if (username in dic_accounts and dic_accounts[username] == password):
         def main_code():
           randomnumber = random.randint(1,999)
           print('Name: {username} ')
           print(f'Temporary user code: {randomnumber}')



                