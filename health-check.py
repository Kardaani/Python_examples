#!/usr/bin/python
import urllib.request
from time import sleep
from datetime import datetime

import sys
from select import select

TIME_INTERVAL = 900 #15 minutes - 96 excecutions per day

APP_URL = {
	"com.coupii.service": "http://sweet-coupii.rhcloud.com/health-check"
}

def send_mail(subject, body):
    import smtplib
    print("sending mail: {subject: " +
          subject +
          ", body: " +
          body +
          "}");
    username = 'sgvinci@gmail.com'
    password = '98ikj7uiol'
    subject = "Subject: " + subject
    msg = "\r\n".join([
      "From: sgvinci@gmail.com",
      "To: sgvinci@gmail.com",
      subject,
      "",
      body
      ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(username, username, msg)
    server.quit()

def health_check(app_name):
    url = APP_URL[app_name] 
    print("checking " +
          app_name +
          " with " +
          url)
    try: 
        health = urllib.request.urlopen(url).read().decode("utf-8")
    except urllib.error.HTTPError:
        health = "Service Temporarily Unavailable"
    except urllib.error.URLError:
        health = "Name or service not known"
    print("response: " + health)
    if not app_name in health:
        date = str(datetime.now())
        send_mail(app_name +
                  " health_check",
                  app_name +
                  " health check did not finish succesfully at " +
                  date + ". Health response: " + health)
    print("\n");

def main(i):
    print("current system time: " +
          str(datetime.now()))
    health_check("com.coupii.service")
    print('excecution',
          i,
          '\n')
    print('press enter to quit excecution (900 seconds timeout)')
    rlist, wlist, xlist = select([sys.stdin], [], [], TIME_INTERVAL)
    if rlist:
          print("bye")
          exit()
    main(i + 1)

i = 0
main(i)
