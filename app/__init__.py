from flask import Flask

app = Flask(__name__)
app.config['SECRET KEY'] = 'BUDI-LNIK'

from app import routes