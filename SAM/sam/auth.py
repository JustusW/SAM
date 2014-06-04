from imapclient import IMAPClient

HOST = 'mail.kw-it.info'

USERS = {
    'wingert@kw-it.info': 'admin',
}
GROUPS = {
    'admin': ['group:admins'],
    'default': ['group:default'],
}

def groupFinder(userID, request):
    if userID in USERS:
        return GROUPS.get(userID, [])
    elif userID is not None:
        return GROUPS.get('default', [])

    return None

def login(user, password):
    server = IMAPClient(HOST, use_uid=True, ssl=True)
    server.login(user, password)
    pass