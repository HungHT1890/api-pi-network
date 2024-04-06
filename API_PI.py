import captcha
import requests,random,string

def id_generator(size=6, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

class API_PI:
    def __init__(self,phone,password=False,referral_link=""):
        self.s = requests.Session()
        self.headers = {
            "accept":"application/json, text/plain, */*",
            "Content-Type":"application/json;charset=utf-8",
            "Host":"socialchain.app",
            "User-Agent":"okhttp/3.12.12",
        }
        name = ['Calantha','Rosalind','Lilybelle','Juhi','Daisy','Sunflower',
                'Camellia','Willow','Lilian','Rose','Lotus','Dahlia','Morela','Jasmine','Flora',
                'Gemma','Ruby','Odette','Margaret','Felicity','Beatrix','Jade','Olwen','Pearl',
                'Amanda','Hypatia','Elysia','Mirabel','Gwyneth','Felicia','Yashita','Naila',
                'Yashashree','Valeria','Andrea','Louisa','Edith','Matilda','Alexandra','Doris',
                'Rowan','Aurelia','Mabel','Kaylin','Hebe','Isolde','Delwyn','Christabel','Calliope',
                'Amabel','Charmaine','Calliope','Brenna','Fidelma','Roxana','Maris','Lucasta','Sterling','Genevieve']

        self.phone = phone
        self.username = id_generator(19)
        self.first_name = random.choice(name)
        self.last_name = random.choice(name)
        if password == False:
            self.password = self.first_name+str(random.randint(1000,9999))+"@"
        else:
            self.password = password
        self.referral_link = referral_link
        self.access_token = "access_token"

    def users_phone(self):
        data = {"continue_in_webview_ui_supported":True,"phone_number":self.phone}
        datato = self.s.post("https://socialchain.app/api/users/phone",headers=self.headers,json=data).json()
        self.id = datato["id"]
        datato["password"] = self.password
        return datato

    def signin(self):
        data = {"phone_number":self.phone,"password":self.password}
        datato = self.s.post("https://socialchain.app/api/password_sign_in",headers=self.headers,json=data).json()
        self.access_token = datato["credentials"]["access_token"]
        return datato

    def setup_password(self):
        data = {"phone_number":self.phone,"password":self.password}
        datato = self.s.post("https://socialchain.app/api/setup_password",headers=self.headers,json=data).json()
        self.access_token = datato["credentials"]["access_token"]
        return datato
    
    def profile(self,captcha_token):
        data = {"first_name":self.first_name,"last_name":self.last_name,
                "username":self.username,
                "captcha_token":captcha_token,
                }
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        datato = self.s.post("https://socialchain.app/api/profile",headers=self.headers,json=data).json()
        return datato

    def referral(self):
        data = {"referral_link":self.referral_link}
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        datato = self.s.post("https://socialchain.app/api/referrals/recover",headers=self.headers,json=data).json()
        return datato

    def proof_of_presences(self):
        data = '{"recaptcha_token":null}'
        self.headers["Authorization"] = f"Bearer {self.access_token}"
        datato = self.s.post("https://socialchain.app/api/proof_of_presences",headers=self.headers,data=data).json()
        return datato

# phone = "+84"+random.choice(["58","32","34","39","87"])+str(random.randint(1000000,9999999))
# referral_link = "vanhau6879"
# appapi = API_PI(phone,password=False,referral_link=referral_link)
# to = appapi.users_phone()
# print(to)
# setuppassword = appapi.setup_password()
# print(setuppassword)
# # captcha_token = input("captcha_token:")
# print("Bypass Recaptcha")
# captcha_token = captcha.captcha()
# to = appapi.profile(captcha_token)
# print(to)
# to = appapi.referral()
# print(to)
# to = appapi.proof_of_presences()
# print(to)