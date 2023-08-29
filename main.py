from flask import Flask, render_template,send_file

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('company_info.html')

@app.route('/preview_document')
def preview_document():
    pdf_path = 'static/corporationRegister.pdf'
    return send_file(pdf_path, mimetype='application/pdf')

if __name__ == "__main__":
    app.run()