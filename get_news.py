import json
import urllib.parse
import urllib.request
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.poolmanager import PoolManager

"""class MyAdapter(HTTPAdapter):
    def init_poolmanager(self, connections, maxsize, block=False):
        self.poolmanager = PoolManager(num_pools=connections,
                                       maxsize=maxsize,
                                       block=block,
                                       ssl_version=ssl.PROTOCOL_TLSv1"""

def lookup(topic):
    """Looks up articles by topic."""
    #ctx=ssl.create_default_context()
    #ctx.check_hostname = False
    #ctx.verify_mode = ssl.CERT_NONE
    #s = requests.Session()
    #s.mount('https://', MyAdapter())
    feed = requests.get("https://newsapi.org/v2/top-headlines?country=in&category={}&apiKey=be54272d4e6a44999625361ad1a5e8d1".format(urllib.parse.quote(topic, safe="")),verify=False)
    """feed=feed.read()
    feed=feed.decode()
    feed=json.loads(feed)
    dat = feed['articles']#dat is a list of dictionaries
    data=list()#data will be a list of dictionaries
    for item in dat:#item is a dict containing a newsapi
        app_data=dict()
        app_data['title']=item['title']
        app_data['description']=item['description']
        app_data['url']=item['url']
        data.append(app_data)
    return data#returns list of news each is a dictionary with keys
    #'title','description','url' and values string"""
    news=feed.text
    news=json.loads(news)
    news=news['articles']
    output=list()
    for item in news:
        out=dict()
        out['title']=item['title']
        out['description']=item['description']
        out['url']=item['url']
        output.append(out)
    #new_out=list()
    #new_out.append(output[0])
    return output
