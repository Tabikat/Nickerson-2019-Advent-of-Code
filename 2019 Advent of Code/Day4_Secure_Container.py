pwlist=[]

for password in range(136818,685979):
    password=str(password)
    if int(password[0])<=int(password[1])<=int(password[2])<=int(password[3])<=int(password[4])<=int(password[5]):
        if int(password[0])==int(password[1]) or int(password[1])==int(password[2]) or int(password[2])==int(password[3]) or int(password[3])==int(password[4]) or int(password[4])==int(password[5]):
            if int(password[0])==int(password[1]) and int(password[1])!=int(password[2]):
                password=int(password)
                pwlist.append(password)
            elif int(password[0])!=int(password[1]) and int(password[1])==int(password[2]) and int(password[2])!=int(password[3]):
                password=int(password)
                pwlist.append(password)
            elif int(password[1])!=int(password[2]) and int(password[2])==int(password[3]) and int(password[3])!=int(password[4]):
                password=int(password)
                pwlist.append(password)
            elif int(password[2])!=int(password[3]) and int(password[3])==int(password[4]) and int(password[4])!=int(password[5]):
                password=int(password)
                pwlist.append(password)
            elif int(password[3])!=int(password[4]) and int(password[4])==int(password[5]):
                password=int(password)
                pwlist.append(password)

print('Number of Possible Passwords:',len(pwlist))
