from django.shortcuts import render
from django.views import View
import bs4
import requests
import threading
from django.http import HttpResponse
# Create your views here.


class ScoreView(View):
    # timer = threading.Timer(0,get)
    # timer.start()

    def get(self,request,*args,**kwargs):
        res = requests.get('https://www.cricbuzz.com/live-cricket-scores/20195/rsa-vs-sl-1st-test-sri-lanka-tour-of-south-africa-2019')
        # soup = bs4.BeautifulSoup(res.text,'html.parser')
        # score = soup.select('.cb-min-bat-rw > .cb-font-20')
        # scr=score[0].text
        print('hello')
        # time = threading.Timer(15,self.get)
        # time.start()
        context = {
             'html':res
        }
        return render(request, 'score.html', context)

