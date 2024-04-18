import pickle
from pathlib import Path
from httplib2 import Authentication
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
with open('setcredential.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)


authenticator = Authentication(
config['credentials'],
config['cookie']['name'],
config['cookie']['key'],
config['cookie']['expiry_days'],
config['preauthorized'],
content='Any',
http='Any'
)
name, authentication_status, username = stauth.Authenticate.login({'Form name':"Login"},location="main")
