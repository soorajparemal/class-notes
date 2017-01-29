import re
email='srjps202#gmail.com , abc@gmail.com'
match = re.findall(r'[\w\.-]+@[\w\.-]+',email)
match
