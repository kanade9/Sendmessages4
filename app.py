# -*- coding: utf-8 -*-
from flask import *
import PyLineNotify
app = Flask(__name__)

@app.route('/')
def hello():
    st = u"あなたのトークンと送りたいメッセージを入力してください。"
    return render_template("form.html",st=st)

@app.route('/result', methods = ['POST'])
def result():
      tk=request.form["token"]
      ms=request.form["message"]
      PyLineNotify.send_message(token=tk, message=str(ms))
      st=False
      return render_template("form.html",st=st)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)