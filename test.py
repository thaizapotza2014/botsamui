from flask import Flask
app = Flask(__name__)
@app.route('/')
def MainFunction():
    return 'สวัสดี ประพจน์ รักษานวน'
if __name__ == '__main__':
    app.run()