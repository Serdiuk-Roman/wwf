from flask import Blueprint

bp = Blueprint('sketch', __name__)

from app_dir.sketch import routes
