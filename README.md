## TeamDexGram
MADE WITH ❤ BY ```[@Akki_ThePro⚡]```

### Support - ```@Dexgram_Official```

### Installing 📊
Contact [Me](https://telegram.dog/Akki_ThePro) to report bug or error.


### The Easy Way
[![Deploy To Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Akshat7678/DexGram/)

Take Sting session from Replit
[![Run on Repl.it](https://repl.it/badge/github/Akshat7678/DexGram)](https://replit.com/@AkshatKumar6/DexGram#main.py)
-------------------------------------------------

🔺 How to Deploy your UserBot to Heroku 🔺

So I have Updated This Things For Api Id Just GO To This Bot Click There t.me/ceoappid_bot
- Take APP ID AND HASH FROM HERE https://my.telegram.org
- For String Session [👉Click here 👈](https://replit.com/@AkshatKumar6/DexGram#main.py)
- Wait For 2 Mins Until It Asks API ID 
- When It Ask Api Id And Hash Go To That Bot Which I Gived In Step 1 
- Then After That Enter Your Phone Number 
- It will Send A OTP Enter The Otp There
- Boom 💣 Your String Session Has Been Generated 
- Now Copy String Session
- Make login to your heroku Account. 

- Then Fill 

🔹 App name - with any name you want 
       
🔹 API_HASH  - Put Your Hash In It which you get from my.telegram.org

🔹 APP_ID - Put your Api In It which you get from my.telegram.org

🔹 HEROKU_API_KEY - Get Api Key From https://dashboard.heroku.com/account and reveal it ( This will help in update )

🔹 HEROKU_APP_NAME - Put same name as of App name

🔹 STRING_SESSION - Put String Session In It 

🔹 TG_BOT_TOKEN_BF_HER - Make new bot from botfather and put token here

🔹 TG_BOT_USER_NAME_BF_HER - Put bot Username here ( e.g.  @MyUser_bot )

### The Normal Way 👨‍💻

Simply clone the repository and run the main file:
```sh
git clone https://github.com/Akshat7678/DexGram
virtualenv -p /usr/bin/python3 venv
. ./venv/bin/activate
pip install -r requirements.txt
# <Create local_config.py with variables as given below>
python3 -m userbot
```

An example `local_config.py` file could be:

**Not All of the variables are mandatory**

__The Userbot should work by setting only the first two variables__

```python3
from heroku_config import Var

class Development(Var):
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"
```

### UniBorg Configuration

The UniBorg Config is situated in `userbot/uniborgConfig.py`.

