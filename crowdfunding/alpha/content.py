from django.http import HttpResponse as response
from django.shortcuts import render
from django.conf import settings

from alpha.app import Alpha
from .models import Promoted,Movement,Project,Event

class Promoteds(Alpha):
    def promote_form(self,request):
        return render(request,'promote.pug',{},content_type='text/html')
    def promote(self,request):
        u = self.current_user(request)
        for k,v in request.REQUEST.iteritems():
            if 'content' in k: content = v
            elif 'id' in k: promotedid = v
            elif 'token' in k: token = v
        move = Movement.objects.filter(cause_id=promotedid)
        if len(move) > 0: p = Promoted(name='$#',prom=promotedid,content=content,user=u); p.save()
        else: s = Promoted(name=token,prom=promotedid,content=content,user=u); s.save()
        mod,pobj = settings.EFFORIA_TOKENS[token].split('.')
        o = globals()[pobj].objects.filter(id=promotedid)[0]
        return response(o.event_id)
    def promoted(self,request):
        u = self.current_user(request)
        ident = request.REQUEST['id']
        p = Promoted.objects.filter(prom=ident)
        mod,pobj = settings.EFFORIA_TOKENS[p[0].name].split('.')
        o = globals()[pobj].objects.filter(id=ident)[0]
        feed = list(p); feed.append(o)
        return self.view_mosaic(request,feed)
