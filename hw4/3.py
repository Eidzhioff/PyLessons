password = input()
symbols_upper = "ABCDEFGHJKLMNPQRSTUVWXYZ"
symbols_lower='abcdefghijkmnpqrstuvwxyz'
digits='23456789'
term1 = term2 = term3 = False
for i in password:
    if i in digits:
        term1 = True
    if i in symbols_upper:
        term2 = True
    if i in symbols_lower:
        term3 = True
if term1 and term2 and term3 == True and len(password)>=8:
    print("Сильный пароль")
else:
    print("Слабый пароль")
