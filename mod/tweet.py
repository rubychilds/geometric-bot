from TwitterAPI import TwitterAPI

import yaml
config = yaml.load(open('./config.yml'))

CONSUMER_KEY        = config['TwitterAPI']['CONSUMER_KEY']
CONSUMER_SECRET     = config['TwitterAPI']['CONSUMER_SECRET']
ACCESS_TOKEN_KEY    = config['TwitterAPI']['ACCESS_TOKEN_KEY']
ACCESS_TOKEN_SECRET = config['TwitterAPI']['ACCESS_TOKEN_SECRET']

def withImage( filepath, text ):
    api = TwitterAPI(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)
    print('Tw:'+filepath)
    print('Tw:'+text)
    file = open( filepath, 'rb')
    img_data = file.read()
    r = api.request('statuses/update_with_media', {'status': text }, {'media[]':img_data})
    print( 'Twitter status:' + str(r.status_code) )
