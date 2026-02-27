# IoT/appstart.py (최상위 파일)
from my_app import app # 반드시 my_app 폴더에서 app을 가져오도록 설정

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)