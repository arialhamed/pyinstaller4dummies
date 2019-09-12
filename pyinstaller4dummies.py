import os

py_list = [x for x in os.listdir('.') if x[len(x)-3:len(x)] == '.py']
icon_list = [x for x in os.listdir('.') if x[len(x)-3:len(x)] in ['.png','.ico','.jpg']]

for x in range(len(py_list)):
    print(str(x+1)+': '+py_list[x])
    
print()
print("Name of file (press Enter to enter as index shown): ")
name = input(">>> ")

print()
if name == '':
    print("Index of file: ")
    name = py_list[int(input(">>> "))-1]
    print()
if_standalone = input("You want it standalone? (Y/N): ")
if_tkinter = input("You want to remove console (for Tkinter)? (Y/N): ")
print()


if len(icon_list) == 0:
    print('No icons detected in directory. Using default PyInstaller icon')
    if_icon = 'N'
elif len(icon_list) == 1:
    print('Only one viable icon detected.')
    print('Use icon? (Y/N)')
    if_icon = input('>>> ')
    if if_icon in 'Nn':
        print('Using default PyInstaller icon')
else:
    print('List of icons:')
    for x in range(len(icon_list)):
        print(str(x+1)+': '+icon_list)
    print("Enter index of icon (leave empty for no icon )")
    icon_name = icon_list[int(input(">>> "))]

if ' ' in name:
    name = '\"'+name+'\"'

input_str = 'pyinstaller {}{}{}{}'.format('--onefile ' if if_standalone in 'Yy' else '',
                                       '-w ' if if_tkinter in 'Yy' else '',
                                       '--icon={} '.format(icon_name) if if_icon in 'Yy' else '',
                                       name)
print()
print('Input into console: '+input_str)
print('Confirm output? (Y/N):')
confirm = input('>>> ')

if confirm in 'Yy':
    os.system(input_str)
    print('Process will take some time, depending how big your Python script is.')
else:
    print()
    print('Cancelling Process...')
    print('Exiting program... ')
