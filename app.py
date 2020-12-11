import os
# splite3をimportする
import sqlite3
# flaskをimportしてflaskを使えるようにする
from flask import Flask, render_template, request, redirect, session
# appにFlaskを定義して使えるようにしています。Flask クラスのインスタンスを作って、 app という変数に代入しています。
app = Flask(__name__)

# Flask では標準で Flask.secret_key を設定すると、sessionを使うことができます。この時、Flask では session の内容を署名付きで Cookie に保存します。
app.secret_key = 'tama'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/scene_1")
def scene_1():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from greetings ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_1.html", html_word_info=word_info)


@app.route("/scene_2")
def scene_2():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from shopping ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_2.html", html_word_info=word_info)


@app.route("/scene_3")
def scene_3():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from eatingout ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_3.html", html_word_info=word_info)


@app.route("/scene_4")
def scene_4():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from directions ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_4.html", html_word_info=word_info)


@app.route("/scene_5")
def scene_():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from conversation ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_5.html", html_word_info=word_info)


@app.route("/scene_6")
def scene_6():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from sick_emergency ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_6.html", html_word_info=word_info)


@app.route("/scene_7")
def scene_7():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute('SELECT id, english, japanese, pronunciation from numbers ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_7.html", html_word_info=word_info)


@app.route("/scene_8")
def scene_8():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from time_date ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_8.html", html_word_info=word_info)


@app.route("/scene_9")
def scene_9():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute('SELECT id, english, japanese, pronunciation from dating ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_9.html", html_word_info=word_info)


@app.route("/scene_10")
def scene_10():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute('SELECT id, english, japanese, pronunciation from colors ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_10.html", html_word_info=word_info)


@app.route("/scene_11")
def scene_11():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute('SELECT id, english, japanese, pronunciation from places ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_11.html", html_word_info=word_info)


@app.route("/scene_12")
def scene_12():
    # flasktest.dbに接続します
    conn = sqlite3.connect("scene_words.db")
    c = conn.cursor()
    word_info = []
    c.execute(
        'SELECT id, english, japanese, pronunciation from foods_drinks ORDER BY id')
    for row in c.fetchall():
        word_info.append(
            {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
    c.close()
    print(word_info)
    return render_template("scene_12.html", html_word_info=word_info)


@app.route('/register', methods=["GET", "POST"])
def register():
    #  登録ページを表示させる
    if request.method == "GET":
        if 'user_id' in session:
            return redirect('/bookmark')
        else:
            return render_template("register.html")

    # ここからPOSTの処理
    else:
        # 登録ページで登録ボタンを押した時に走る処理
        name = request.form.get("name")
        password = request.form.get("password")

        conn = sqlite3.connect('scene_words.db')
        c = conn.cursor()
        c.execute("insert into user values(null,?,?)", (name, password))
        conn.commit()
        conn.close()
        return redirect('/bookmark')


# GET  /login => ログイン画面を表示
# POST /login => ログイン処理をする
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        if 'user_id' in session:
            return redirect("/register")
        else:
            return render_template("login.html")
    else:
        # ブラウザから送られてきたデータを受け取る
        name = request.form.get("name")
        password = request.form.get("password")

        # ブラウザから送られてきた name ,password を userテーブルに一致するレコードが
        # 存在するかを判定する。レコードが存在するとuser_idに整数が代入、存在しなければ nullが入る
        conn = sqlite3.connect('scene_words.db')
        c = conn.cursor()
        c.execute(
            "select id from user where name = ? and password = ?", (name, password))
        user_id = c.fetchone()
        conn.close()
        # DBから取得してきたuser_id、ここの時点ではタプル型
        print(type(user_id))
        # user_id が NULL(PythonではNone)じゃなければログイン成功
        if user_id is None:
            # ログイン失敗すると、ログイン画面に戻す
            return render_template("login.html")
        else:
            session['user_id'] = user_id[0]
            return redirect("/bookmark")


@app.route("/logout")
def logout():
    session.pop('user_id', None)
    # ログアウト後はログインページにリダイレクトさせる
    return redirect("/login")


@app.route('/bookmark')
def bookmark():
    if 'user_id' in session:
        user_id = session['user_id']
        conn = sqlite3.connect('scene_words.db')
        c = conn.cursor()
        # # DBにアクセスしてログインしているユーザ名と投稿内容を取得する
        # クッキーから取得したuser_idを使用してuserテーブルのnameを取得
        c.execute("select name from user where id = ?", (user_id,))
        # fetchoneはタプル型
        user_info = c.fetchone()
        # user_infoの中身を確認
        word_info = []

        c.execute(
            "SELECT id, english, japanese, pronunciation from bookmark where user_id = ? ORDER BY id", (user_id,))
        comment_list = []
        for row in c.fetchall():
            word_info.append(
                {"id": row[0], "english": row[1], "japanese": row[2], "pronunciation": row[3]})
        c.close()
        print(word_info)
        return render_template('bookmark.html', user_info=user_info, html_word_info=word_info)
    else:
        return redirect("/login")


@app.route('/add', methods=["POST"])
def add():
    user_id = session['user_id']

    # POSTアクセスならDBに登録する
    # フォームから入力されたアイテム名の取得(Python2ならrequest.form.getを使う)
    id = request.form.get("id")
    english = request.form.get("english")
    japanese = request.form.get("japanese")
    pronunciation = request.form.get("pronunciation")
    conn = sqlite3.connect('scene_words.db')

    c = conn.cursor()
    # 現在の最大ID取得(fetchoneの戻り値はタプル)

    c.execute("insert into bookmark values(?,?,?,?,?)",
              (id, english, japanese, pronunciation, user_id))
    conn.commit()
    conn.close()
    return redirect('/bookmark')


@app.errorhandler(403)
def mistake403(code):
    return 'There is a mistake in your url!'


@app.errorhandler(404)
def notfound404(code):
    return "404だよラッキーちゃん(*'▽')ノ"


# __name__ というのは、自動的に定義される変数で、現在のファイル(モジュール)名が入ります。 ファイルをスクリプトとして直接実行した場合、 __name__ は __main__ になります。
if __name__ == "__main__":
    # Flask が持っている開発用サーバーを、実行します。
    app.run(debug=True)
    # app.run()
