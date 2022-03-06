import requests, time

def main():
    channelId = str(input("Identifiant du salon ou envoyer le message -> "))
    auth = str(input("Authorization -> "))
    
    headers = {
      "authorization": f"{auth}",
    }
    
    payload = {
      "content": "!d bump"
    }
    
    while True:
      r = requests.post(f"https://canary.discord.com/api/v9/channels/{channelId}/messages", headers=headers, data=payload)
      if r.ok:
        print("!d bump sent")
      else:
        print("Status code : ", r.status_code)
        break
      time.sleep(7200)
       
main()
