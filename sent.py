import smtplib


to = 'mehrdad.mahdavinya@gmail.com'
email = 'qaboosveshmgir@gmail.com'
password = 'Mehrdad@1370'
sms = 'hello'


try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()

    server.login(email, password)
    server.sendmail(email , to , sms)

    server.quit()

    print("sent mail")
except:
    print("false!")