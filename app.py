from flask import Flask, render_template
from forms import RegistrationForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret'

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        error_count = len(form.errors)
        return render_template('success.html', form=form, errors=error_count)
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
