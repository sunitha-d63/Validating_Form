from flask import Flask, render_template, request, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.secret_key = 'your_secret_key' 

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST' and form.validate_on_submit():
        print("Form Data Submitted:")
        for field_name, value in form.data.items():
            if field_name != 'csrf_token':
                print(f"{field_name}: {value}")
        return render_template('success.html', form=form)
    return render_template('form.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
