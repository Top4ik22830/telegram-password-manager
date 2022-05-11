class AccountData:
    def __init__(self,
                service_name, 
                web_site=None, 
                login=None, 
                mail=None, 
                password=None, 
                keys=""):

        self.service_name = service_name
        self.web_site = web_site
        self.login = login
        self.mail = mail
        self.password = password
        self.keys = keys

    def set_web_site(self, newSite):
        self.web_site = newSite.lower()

    def set_login(self, newLogin):
        self.login = newLogin.lower()

    def set_mail(self, newMail):
        self.mail = newMail.lower()

    def set_password(self, newPassw):
        self.password = newPassw

    def add_key(self, newKey):
        self.keys += f"{newKey} "
