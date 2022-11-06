# WOKO_alert
##### Any feedback or contribution would be appreciated. Don't forget to give a STAR :star2:
##### Currently, this is a code base with minimum condition requirements. CS guys could help if something more sophisticated is needed. ;)
It is crucial to be the first who contacts the room subtenant, because they get 100s emails/day. This script checks the [WOKO](http://www.woko.ch) website for student accommodation in Zurich, Switzerland for new room entries repeatedly once in a specified time interval and sends you an email alert if a new room is **available**.

Version: 11.2022

## Usage

### 0. Clone this repository 
Open your favourite command line tool (Terminal etc) and run this line to clone the repository on your machine:
```
git clone git@github.com:KalinNonchev/WOKO_alert.git
```

Please, navigate to the **WOKO_alert** folder

### 1. Install dependencies 

Open your favourite command line tool (Terminal etc) and run this line to install the missing dependencies:
```
pip install -r requirements.txt
```

### 2. Fill out the config file

Open and fill out the config.yaml file.

```python
content: "New WOKO room!"
receiver_email: "pass" # email to send to 
sender_email: "pass" # email to send from @gmail
password: "pass" # password of the sender_email email @gmail
keyword: "Zürich" # Choose between Zürich and Winterthur
url_woko: "https://www.woko.ch/en/nachmieter-gesucht"
```

You can use the same **receiver_email** and **sender_email**.  
Since May 30: You have to enable 2-step verification and set up app password for this app and set it the config file so that this app is allowed to login, else it will be considered a less secure app and gmail won't allow it to login. See this for more info: https://support.google.com/accounts/answer/6010255, https://support.google.com/accounts/answer/185833?hl=en.
**The script doesn't store and share your privacy data!**

You can choose the appropriate url_woko depending on the city and whether you want sublets or not. For eg, "https://www.woko.ch/en/nachmieter-gesucht" only contains longterm listings while "https://www.woko.ch/en/zimmer-in-zuerich" contains both.

### 3. Run

Open your favourite command line tool (Terminal etc) and run the script as: 

```python
python3 queryWOKO.py
```

If everything is fine, you should see something like:
```
Still: 2 rooms...
Sleep for: 3min.
```
Leave the script running in the background. The script will update itself every 3 to 6 min and if a new room is available, it will notify you by email. Enjoy! \
**Good luck!**
