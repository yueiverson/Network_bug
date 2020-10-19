#郵寄機器人
import smtplib 
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bug import request_weather
# server=smtplib.SMTP('smtp.gmail.com',25) #port 25為最基本伺服器對伺服器的通訊port
server=smtplib.SMTP('smtp.gmail.com',587) #port 587為安全電子郵件通訊port

server.ehlo()    #查看SMTP有無正常
server.starttls() #以TLS方式連接
pwd=input('輸入密碼')
location=str(input('輸入查詢地點'))
location=location.replace('台','臺')
server.login('user@gmail.com',pwd)
message=MIMEMultipart()   #信箱格式 寄件人,收件人,密件,主旨
message['From']='user' 
message['To']='To_user@gmail.com'
message['CC']='CC_user@123.com'
message['Subject']='Hi i am e-rebot'
weather=request_weather(location)
message.attach(MIMEText('目前{}\n天氣:{}\n氣溫:{}'.format(weather[0],weather[1],weather[2])))
server.send_message(message)
server.quit()