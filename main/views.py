from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
  html = '''
  <!DOCTYPE html>
  <html lang="en">
    <head>
      <meta charset="UTF-8" />
      <title>Main Page</title>
    </head>
    <body>
    <h1>Welcome to the Main Page!<br/>
      This is a simple web page created using Django.</h1><br/>
    </body>
    </html>
  '''
  return HttpResponse(html)