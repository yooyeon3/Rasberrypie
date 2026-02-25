from flask import Flask, render_template
try:
    from urllib.request import urlopen # python 3
    from urllib.error import HTTPError, URLError
except ImportError:
    from urllib2 import urlopen # python 2
    from urllib2 import HTTPError, URLError
#import json

# 사용자 설정 부분
deviceIp = "192.168.0.12"  # ESP8266 장치의 실제 IP 주소로 수정하세요
portnum = "80"

base_url = "http://" + deviceIp + ":" + portnum
events_url = base_url + "/events"

app = Flask(__name__, template_folder="templates")

@app.route('/events')
def getevents():
    u = urlopen(events_url)
    data = ""
    try:
        data = u.read()
    except HTTPError as e:
        print("HTTP error: %d" % e.code)
    except URLError as e:
        print("Network error: %s" % e.reason.args[1])
    return data

@app.route('/')
def dht22chart():
    return render_template("dhtchart.html")

if __name__ == '__main__':
    # 서버 IP와 포트를 설정하세요 (예: host='0.0.0.0', port=5000)
    app.run(host="0.0.0.0", port=5000,debug=True)