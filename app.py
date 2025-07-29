from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/blog')
def blog():
    # Sample blog posts (you can replace with a database later)
    posts = [
        {'title': 'My First Blog Post', 'content': 'This is my first blog post!', 'date': 'July 28, 2025'},
        {'title': 'Learning Web Development', 'content': 'Sharing my journey in web dev.', 'date': 'July 27, 2025'}
    ]
    return render_template('blog.html', posts=posts)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        msg = Message(
            subject=f'New Contact Form Message from {name}',
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[app.config['MAIL_USERNAME']],
            body=render_template('email_template.html', name=name, email=email, message=message)
        )
        try:
            mail.send(msg)
            flash('Message sent successfully!', 'success')
        except Exception as e:
            flash(f'Error sending message: {str(e)}', 'error')
        return render_template('contact.html')
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)