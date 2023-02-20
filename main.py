import flask, datetime, sqlite3
app = flask.Flask(__name__)

@app.route("/")
def hello_world():
    return flask.render_template('main.html', time=datetime.datetime.now())

@app.route("/users/", methods=['POST'])
def get_users():
    with sqlite3.connect("users.db") as con:
        cur = con.cursor()
        try:
            statement = ("SELECT * FROM users WHERE name = \'" + flask.request.form['username'] + "\';")
            data = cur.execute(statement).fetchall()
        except Exception as e:
            data = ("Invalid SQL statement: " + str(e))
    if data != []:
        rtn = str(data)
    elif data == []:
        rtn = "Not found"
    return flask.render_template("users.html", active=str(rtn), statement=statement)


if __name__ == "__main__":
    app.run(host='0.0.0.0')