from flask import Flask, render_template, request

app = Flask(__name__)
app.debug = True
user_data = {}

@app.route('/view/<username>', methods=['GET','POST'])
def view_page(username):
    if username not in user_data:
        user_data[username] = [0, 1000000]

    if request.method == 'POST':
        buy_count = request.form['buy_count']
        if buy_count:
            user_data[username][0] += int(buy_count)
            user_data[username][1] -= int(buy_count)*10000

        sell_count = request.form['sell_count']
        if sell_count:
            user_data[username][0] -= int(sell_count)
            user_data[username][1] += int(sell_count)*10000

    shares = user_data[username][0]
    money = user_data[username][1]
    return render_template('view.html',
            name=username,
            share_cnt=shares,
            dollars=money/100)

@app.route('/')
def hello_world():
    return 'Hello world!'

if __name__ == '__main__':
    app.run()

