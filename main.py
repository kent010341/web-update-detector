import sys
import os
from configparser import ConfigParser
import requests
from bs4 import BeautifulSoup
import smtplib

CFG_PATH = './settings.cfg'
PRE_RESULT_PATH = './pre-result.html'

# cfg string
CFG_DEFAULT = 'default'
CFG_TARGET_URL = 'target.url'
CFG_SENDER_ACCOUNT = 'sender.email.account'
CFG_SENDER_PASSWD = 'sender.email.password'
CFG_RECEIVER_ACCOUNT = 'receiver.email.account'

def argv_parser(argv):
    pass

def read_cfg():
    cfg = ConfigParser()
    cfg.read(CFG_PATH)

    return cfg[CFG_DEFAULT]

def get_web_body(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, features='html.parser')

    return str(soup.find('body'))

def compare(content):
    if os.path.exists(PRE_RESULT_PATH):
        with open(PRE_RESULT_PATH, 'r') as f:
            r = f.read()

        return r == content
    else:
        return True

def overwrite(content):
    with open(PRE_RESULT_PATH, 'w') as f:
        f.write(content)

def send_email(sender_account, sender_password, receiver_account):


def main():
    argv_parser(sys.argv)
    settings = read_cfg()
    body = get_web_body(settings[CFG_TARGET_URL])

    if not compare(body):
        send_email(
            sender_account=settings[CFG_SENDER_ACCOUNT],
            sender_password=settings[CFG_SENDER_PASSWD],
            receiver_account=settings[CFG_RECEIVER_ACCOUNT]
        )
    overwrite(body)

if __name__ == '__main__':
    main()
