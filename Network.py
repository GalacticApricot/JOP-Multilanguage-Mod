import os

system_path = os.environ.get('JOPML')
m = None
with open(system_path + '\\mode.txt') as a:
    m = a.read()
match m:
    case 'javascript':
        os.system(f"{system_path[0]}: & cd {system_path} & cd JS & node Network.js")
    case 'rust':
        os.system(f"{system_path[0]}: & cd {system_path} & cd Rust & start Network.exe")
