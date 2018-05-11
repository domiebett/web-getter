import urllib3
from bs4 import BeautifulSoup
from flask import Blueprint, Markup, render_template

getterBlueprint = Blueprint('getter', __name__, template_folder='templates')
http = urllib3.PoolManager()
mainWeb = None

@getterBlueprint.route('/<website>', methods=['GET'])
def webGetter(website):
    soup = getWebsite(website)
    for a in soup.findAll('a'):
        a['href'] = '{}{}'.format(website, a['href'])
    web = Markup(soup)
    return render_template('getter.html', website=web)

def getWebsite(websiteUrl):
    response = http.request('GET', websiteUrl)
    soup = BeautifulSoup(response.data, 'html.parser')
    return soup.body
