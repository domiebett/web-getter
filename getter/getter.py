import urllib3
from bs4 import BeautifulSoup
from flask import Blueprint, Markup, render_template, session

getterBlueprint = Blueprint('getter', __name__, template_folder='templates')
http = urllib3.PoolManager()
count = 0

@getterBlueprint.route('/<domainName>')
@getterBlueprint.route('/<domainName>/<path:url>', methods=['GET'])
def webGetter(domainName, url=''):
    webUrl = '{}/{}'.format(domainName, url)
    soup = getWebsite(webUrl)
    web = Markup(soup)
    return render_template('getter.html', website=web)

def getWebsite(websiteUrl):
    response = http.request('GET', websiteUrl)
    soup = BeautifulSoup(response.data, 'html.parser')
    return soup.body
