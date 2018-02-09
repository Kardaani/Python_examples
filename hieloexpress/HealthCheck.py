from modules import FileUtils
from modules import ListUtils
from modules import MailUtils

from time import sleep
from datetime import datetime
import urllib.request

class HealthCheck:
    APP_URL = {
        "hieloexpress-dbs": "http://backoffice-hieloexpress.rhcloud.com/version",
        "hieloexpress-search-manager": "http://sm-hieloexpress.rhcloud.com/version",
        "hieloexpress-crud-gui": "http://hieloexpress-backoffice.net/version"
    }
    def health_check(self, app_name):
        url = self.APP_URL[app_name]
        try: 
            health = urllib.request.urlopen(url).read().decode("utf-8")
        except urllib.error.HTTPError:
            health = "Service Temporarily Unavailable"
        if not app_name in health:
            date = str(datetime.now())
            subject = app_name + " health_check"
            body = app_name + " health check did not finish succesfully at " + date
            MailUtils.send_mail(subject, body)
    def health_check_dbs(self):
        dbs_name = "hieloexpress-dbs"
        self.health_check(dbs_name)       
    def health_check_sm(self):
        sm_name = "hieloexpress-search-manager"
        self.health_check(sm_name)  
    def health_check_gui(self):
        gui_name = "hieloexpress-crud-gui"
        self.health_check(gui_name)   
