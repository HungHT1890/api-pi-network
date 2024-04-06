import API_PI,captcha
import random,threading


def runnow(l):
    dem = 0
    sl = 400
    while True:
        if dem==sl:
            break
        try:
            phone = "+84"+random.choice(["58","32","34","39","87"])+str(random.randint(1000000,9999999))
            referral_link = "haduchau2209"
            appapi = API_PI.API_PI(phone,password=False,referral_link=referral_link)
            users = appapi.users_phone()
            if users["continue_in_webview_ui"]["path"] != "/signin/phone-number-password":
                continue
            appapi.setup_password()
            print("Bypass Recaptcha")
            captcha_token = captcha.captcha()
            if captcha_token == False:
                continue
            appapi.profile(captcha_token)
            recovercheck = appapi.referral()
            if recovercheck["message"] != "Referral successfully recovered":
                continue
            presences = appapi.proof_of_presences()
            presences = presences["proof_of_presence"]["created_at"]
            toacc = f"{appapi.id}|{appapi.username}|{appapi.phone}|{appapi.password}|{appapi.referral_link}|{presences}"
            open("AccPI.txt","a+").write(toacc+"\n")
            print(toacc)
            dem+=1
        except Exception as e:
            print(e)

thread  = []
for l in  range(20):
    thread+=[threading.Thread(target=runnow,args={l},)]
for t in thread:
    t.start()
for t in thread:
    t.join()