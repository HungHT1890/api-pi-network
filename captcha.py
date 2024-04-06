import requests

clientKey = "efd75bcd89c24218b428647be3d395d7"

def captcha():
    data = {
	"clientKey": clientKey,
	"task": {
		"type": "RecaptchaV3TaskProxyless",
		"websiteURL": "https://app-cdn.minepi.com",
		"websiteKey": "6LeZEGwbAAAAAO4FZkn63hJD5w8-YVIOMDe48un2",
		"minScore": 0.3,
		"pageAction": "verify",
		"isEnterprise": False
	    }
    }
    datato = requests.post("https://api.anycaptcha.com/createTask",json=data,headers={'Content-Type': 'application/json'}).json()
    data = {
        "clientKey": clientKey,
        "taskId": datato["taskId"]
        }
    while True:
        datato = requests.post("https://api.anycaptcha.com/getTaskResult",json=data,headers={'Content-Type': 'application/json'}).json()
        if datato["status"] ==  "ready":
            captcha_token = datato["solution"]["gRecaptchaResponse"]
            return captcha_token
        if datato["errorId"] ==  1:
            return False
# print(captcha())
# input("..")
