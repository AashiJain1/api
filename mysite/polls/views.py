from django.shortcuts import render
from django.http import HttpResponse
import requests
url = "http://www.modyuniversity.ac.in/result-detail.php"

payload = "college=1&course=bce&roll_no=150158&year=3&result_type=m"
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '56',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_ga=GA1.3.1288158742.1485665074; sucuri_cloudproxy_uuid_8fc10cefe=5a43c1e5eafa8cd87f99227b7ff4195c; _gid=GA1.3.586640018.1528599763; sucuri_cloudproxy_uuid_0e4f27f2b=dff626dd6859a8248b2beac56bf70bf6; PHPSESSID=gjdrlas9dfr1av9grjoh817777; _gat=1',
    'Host': 'www.modyuniversity.ac.in',
    'Origin': 'http://www.modyuniversity.ac.in',
    'Referer': 'http://www.modyuniversity.ac.in/results.php',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'  
    }
def index(request):
    response = requests.request("POST", url, data=payload, headers=headers)
    r=response.text
    return HttpResponse(r)


