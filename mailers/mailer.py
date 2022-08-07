from flask import Flask, render_template, request
from flask_mail import Mail, Message
app = Flask(__name__)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'natsmu78@gmail.com'
app.config['MAIL_PASSWORD'] = 'password'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

@app.route('/')
def index():
   return render_template('mailer_home.html')


@app.route('/send_message', methods = ['POST', 'GET'])
def send_message():
   if request.method == 'POST':
      email = request.form['email']
      subject = request.form['subject']
      msg = request.form['message']

      message = Message(subject, sender="natsmu78@gmail.com", recipients=[email])
      message.body = msg

      mail.send(message)
      success = "Message sent"

      return render_template("mailer_result.html", success=success)

if __name__ == '__main__':
   app.run(debug = True)

