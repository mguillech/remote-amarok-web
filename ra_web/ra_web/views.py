import telnetlib
import simplejson as json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

def home(request):
    return render_to_response('ra_web/index.html', {},
            context_instance=RequestContext(request))

def run_command(request):
    command = request.GET.get('command', '').encode('utf-8')
    if command:
        command_split = command.split()
        action, params = command_split[0], ' '.join(command_split[1:])
        if action == 'amarok':
            tn = telnetlib.Telnet('localhost', 8000)
            tn.write('%s\r\n' % params)
            tn.close()
        return HttpResponse(json.dumps({'status': True}),
                mimetype='application/json')
