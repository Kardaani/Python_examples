from modules import FileUtils
from modules import ListUtils
from modules import MailUtils

from time import sleep
from datetime import datetime
import urllib.request

TIME_INTERVAL = 900 #15 minutes - 96 excecutions per day

APP_URL = {
    "hieloexpress-dbs": "http://backoffice-hieloexpress.rhcloud.com/version",
    "hieloexpress-search-manager": "http://sm-hieloexpress.rhcloud.com/version",
    "hieloexpress-crud-gui": "http://hieloexpress-backoffice.net/version"
}

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
    print("response: " + health)
    if not app_name in health:
        date = str(datetime.now())
        MailUtils.send_mail(app_name +
                  " health_check",
                  app_name +
                  " health check did not finish succesfully at " +
                  date)
    print("\n");

def health_check_dbs():
    dbs_name = "hieloexpress-dbs"
    health_check(dbs_name)       

def health_check_sm():
    sm_name = "hieloexpress-search-manager"
    health_check(sm_name)  

def health_check_gui():
    gui_name = "hieloexpress-crud-gui"
    health_check(gui_name)    

def main(i):
    print("current system time: " +
          str(datetime.now()))
    health_check_dbs()
    health_check_sm()
    health_check_gui()
    print('excecution',
          i,
          '\n')
    sleep(TIME_INTERVAL)
    main(i + 1)

i = 0
main(i)
