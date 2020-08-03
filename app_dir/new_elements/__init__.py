from flask import Blueprint

bp = Blueprint('new_elements', __name__)

from app_dir.new_elements import routes
