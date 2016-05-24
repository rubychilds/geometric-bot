import datetime

def footline( p ):
    result = p['name']+' | '
    for key in list(p['params']):
        result += key +':'+str(p['params'][key])[0:6]+' '
    print('footline: '+result)
    return result

def filename( p ):
    now_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    result = p['name']+'-'+now_str
    for key in list(p['params']):
        result += '-'+ key +str(p['params'][key])[0:6]
    result += '.png'
    print('filename: '+result)
    return result
