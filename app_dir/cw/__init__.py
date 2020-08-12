from flask import Blueprint

bp = Blueprint('cw', __name__)

from app_dir.cw import routes
