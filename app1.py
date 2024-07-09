from flask import Flask, render_template, session, request, redirect, url_for

app = Flask(__name__)

app.secret_key = '6074f42e0386bcb42138073803b7d27839e94ed89c920fb287e9729295df3f4c'

@app.route('/')
def index():
    if 'username' in session:
        return render_template('base1.html')
    else:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username') or 'NoName'
        return redirect(url_for('index'))
    return render_template('username_form.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('email', None)
    return redirect(url_for('index'))

@app.errorhandler(404)
def page_not_found(e):
    app.logger.warning(e)
    context = {
        'title': 'Страница не найдена',
        'url': request.base_url,
    }
    return render_template('404.html', **context), 404

if __name__ == '__main__':
    app.run(debug=True)
