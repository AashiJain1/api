from django.db import models
import requests
# Create your models here.

url = "http://www.modyuniversity.ac.in/result-detail.php"
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'en-US,en;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Content-Length': '56',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': '_ga=GA1.3.1288158742.1485665074; sucuri_cloudproxy_uuid_8fc10cefe=5a43c1e5eafa8cd87f99227b7ff4195c; PHPSESSID=fhanavr9hq0eru9kfvrovqrdh1; _gid=GA1.3.586640018.1528599763; _gat=1',
  'Host': 'www.modyuniversity.ac.in',
  'Origin': 'http://www.modyuniversity.ac.in',
  'Referer': 'http://www.modyuniversity.ac.in/results.php',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
    }

class Note(models.Model):
    college = models.CharField(max_length=1)
    course = models.CharField(max_length=5)
    roll_no = models.IntegerField()
    year = models.IntegerField()
    result_type = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
        payload = "college=self.college&course=self.course&roll_no=self.roll_no&year=self.year&result_type=self.result_type"
        response = requests.request("POST", url, data=payload,headers=headers)
        return '%s' % (response.text)