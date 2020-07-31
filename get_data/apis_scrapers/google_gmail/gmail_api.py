from apiclient.discovery import build
from httplib2 import http
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'

# following the tutorial: https://developers.google.com/gmail/api/guides/threads
store = file.Storage('storage.json')
creds = store.get()

if creds is None or creds.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    creds = tools.run(flow, store)

gmail = build('gmail', 'v1', http=creds.authorize(Http()))

gmail.users().list(userId='livia.clarete@gmail.com').execute()
