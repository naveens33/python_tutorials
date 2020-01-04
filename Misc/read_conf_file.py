import configparser

config = configparser.ConfigParser()
config.read('db.ini')

host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
db = config['mysql']['db']

print('MySQL configuration:')
print(user)