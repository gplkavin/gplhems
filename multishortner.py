import requests

import pyshorteners


SHORTENER = 'tnlink.in'
SHORTENER_API = '85a34b0ad8254c6d93e3a83c13148a2254c3014c'



def short_url(longurl):
    if "shorte.st" in SHORTENER:
        disable_warnings()
        return requests.get(f'http://api.shorte.st/stxt/{SHORTENER_API}/{longurl}', verify=False).text
    elif "linkvertise" in SHORTENER:
        url = quote(base64.b64encode(longurl.encode("utf-8")))
        linkvertise = [
            f"https://link-to.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}",
            f"https://up-to-down.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}",
            f"https://direct-link.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}",
            f"https://file-link.net/{SHORTENER_API}/{random.random() * 1000}/dynamic?r={url}"]
        return random.choice(linkvertise)
    elif "bitly.com" in SHORTENER:
        s = pyshorteners.Shortener(api_key=SHORTENER_API)
        return s.bitly.short(longurl)
    elif "ouo.io" in SHORTENER:
        disable_warnings()
        return requests.get(f'http://ouo.io/api/{SHORTENER_API}?s={longurl}', verify=False).text
    elif "du-link.in" in SHORTENER: 
        api = SHORTENER_API
        params = {'api': api, 'url': longurl}
        duli= f'https://dulink.in/api'
        get_url = requests.get(duli,params)
        get_url =  get_url.json()['shortenedUrl']
        return 
    else:
        return requests.get(f'https://{SHORTENER}/api?api={SHORTENER_API}&url={longurl}&format=text').text
