import time


def notfound_404(environ, start_response):
    start_response('404 Not Found', [('Content-type', 'text/plain')])
    return [b'Not Found']

_hello_resp = (
               '    <html>\n'
               '        <head>\n'
               '            <title>Hello {names}</title>\n'
               '        </head>\n'
               '        <body>\n'
               '            <h1>Hello {names}!</h1>\n'
               '        </body>\n'
               '    </html>')


def hello_world(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    params = environ['params']
    resp = _hello_resp.format(names = params.getvalue('name'))
    yield resp.encode('utf-8')


_localtime_resp = ('<?xml version="1.0"?>\n'
                   '        <time>\n'
                   '            <year>{t.tm_year}</year>\n'
                   '            <month>{t.tm_mon}</month>\n'
                   '            <day>{t.tm_mday}</day>\n'
                   '            <hour>{t.tm_hour}</hour>\n'
                   '            <minute>{t.tm_min}</minute>\n'
                   '            <second>{t.tm_sec}</second>\n'
                   '        </time>')


def localtime(environ, start_response):
    start_response('200 OK', [('Content-type', 'application/xml')])
    resp = _localtime_resp.format(t=time.localtime())
    yield resp.encode('utf-8')


#html code to display image in browser
_img_resp =('<html xmlns="http://www.w3.org/1999/xhtml">\n'
                   '        <head>\n'
                   '            <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n'
                   '            <title>Image to server</title>\n'
                   '            <link rel="stylesheet" type="text/css" href="css/style.css" media="screen" />\n'
                   '            </head>\n'
                   '            <body>\n'
                   '            <img src="{img_net}" alt="Image to server" />\n'
                   '            <iframe width="420" height="315" src="https://www.youtube.com/watch?v=xqBdTn3_0Rw></iframe>'
                   '       </body></html>')

def image(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/html')])
    resp = _img_resp.format(img_net='http://logosolusa.com/wp-content/uploads/parser/Elvis-Logo-1.jpg')
    yield resp.encode('utf-8')


