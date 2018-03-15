from flask import Flask, flash, redirect, render_template, request, session, url_for
from get_news import lookup
from Sentiment import sentiment
import time
app = Flask(__name__)

#ssl_dir: str =os.path.dirname(__file__).replace('src','ssl')
#key_path: str =os.path.join(ssl_path, 'server.key')
#crt_path: str =os.path.join(ssl_path, 'server.crt')
#ssl_context: tuple =(crt_path, key_path)
#app.run('0.0.0.0', 8000, debug=False, ssl_context=ssl_context)

@app.route('/')
def homepage():
  return render_template('homepage.html')

@app.route('/politics')
def politics():
    news=lookup('politics')
    output=list()
    for ne in news:
        sent=sentiment(ne['title'])
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url'] =ne['url']
        out['sentiment']=sent[0]['sentiment']
        output.append(out)
        """words=ne['title'].split()
        query=words[0]+" "+words[1]+" "+words[2]
        t_reviews=tweet(query)#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            time.sleep(0.2)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)"""
    return render_template('news.html',output=output,topic='politics')

@app.route('/sports')
def sports():
    news=lookup('sports')
    output=list()
    for ne in news:
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url'] =ne['url']
        out['sentiment']=sent[0]['sentiment']
        output.append(out)
        """t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)"""
    return render_template('news.html',output=output,topic='sports')

@app.route('/entertainment')
def entertainment():
    news=lookup('entertainment')
    output=list()
    for ne in news:
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url'] =ne['url']
        out['sentiment']=sent[0]['sentiment']
        output.append(out)
        """t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)"""
    return render_template('news.html',output=output,topic='entertainment')

@app.route('/technology')
def technology():
    news=lookup('technology')
    output=list()
    for ne in news:
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url'] =ne['url']
        out['sentiment']=sent[0]['sentiment']
        output.append(out)
        """t_reviews=tweet(ne['title'])#t_reviews is a list of tweets
        out=dict()
        out['title']=ne['title']
        out['description']=ne['description']
        out['url']=ne['url']
        out['reviews']=list()
        for rev in t_reviews:
            sent=sentiment(rev)
            if sent[0]["sentiment"] != 0:
                sen=dict()
                sen['tweet']=rev
                sen['sentiment']=sent[0]['sentiment']
                out['reviews'].append(sen)
        output.append(out)"""
    return render_template('news.html',output=output,topic='Tech')

if __name__ == '__main__':
  app.run()
