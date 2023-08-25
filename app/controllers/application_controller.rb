from flask_wtf import CSRFProtect
from flask import Flask

app = Flask(__name__)
csrf = CSRFProtect(app)

class ApplicationController:
  def __init__(self):
    csrf.protect()
