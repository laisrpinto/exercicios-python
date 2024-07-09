import urllib
import urllib.request

try:
    site = urllib.request.urlopen('https://www.youtube.com/')
except:
    print('\033[31mO site Pudim não está acessível no momento.')
else:
    print('\033[33mConsegui acessar o site pudim com sucesso!')