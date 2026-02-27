# appstart.py 수정
from my_app import app  

if __name__ == '__main__':
    # host='0.0.0.0'으로 설정해야 라즈베리 파이 외부에서도 접속이 가능합니다.
    app.run(host='0.0.0.0', port=8080)