from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
import logging


# Create your views here.
class IndexView(View):

    def get(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.error('MAIN PAGE ENTERED')
        return HttpResponse(
                            '<!DOCTYPE html>'
                            '<html>'
                            '<body>'
                            
                            '<h1>Heading</h1>'
                            '<p>First paragraph.</p>'
                            
                            '</body>'
                            '</html>')


class AboutMeView(View):
    def get(self, request, *args, **kwargs):
        logger = logging.getLogger(__name__)
        logger.error('ABOUT PAGE ENTERED')
        return HttpResponse(
                            '<!DOCTYPE html>'
                            '<html>'
                            '<body>'
                            '<h1>About Gojo</h1>'
                            '<p>Satoru is a complex individual. He is normally seen to be nonchalant and playful towards his students, close colleagues, and friends. However, he is unsympathetic and cruel towards sorcerer executives, an example being his blatant disrespect towards Principal Gakuganji, and his enemies.</p>'
                
                            '</body>'
                            '</html>')
