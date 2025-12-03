from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    return render_template('result.html', username=username, email=email, phone=phone)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)