# WOKO_alert - DEPRECATED!!!
##### Any feedback or contribution would be appreciated. Don't forget to give a STAR :star2:
##### Currently, this is a code base with minimum condition requirements. CS guys could help if something more sophisticated is needed. ;)
It is crucial to be the first who contacts the room subtenant, because they get 100s emails/day. This script checks the [WOKO](http://www.woko.ch) website for student accommodation in Zurich, Switzerland for new room entries every 3 to 6 min and sends you an email alert if a new room is **available**.

Version: 07.2021

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
```

You can use the same **receiver_email** and **sender_email**.  
I recommend creating a second special email (sender_email) for the purpose of this app. \
You **have** to use gmail and you **have** to turn **Less secure app access** feature **on**. Read more [here](https://support.google.com/accounts/answer/6010255?hl=en#zippy=%2Cif-less-secure-app-access-is-on-for-your-account). \
**The script doesn't store and share your privacy data!**

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
