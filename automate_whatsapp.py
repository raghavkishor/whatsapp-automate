import pywhatkit as kt

print("Let's Automate Whatsapp!")
p_num = 'the target phone number goes here!'


import getpass as gp
p_num = gp.getpass(prompt='Phoneumber: ', stream=None)
msg = "hey how are you!!!!!!!!!"
kt.sendwhatmsg(p_num, msg,22,25)
