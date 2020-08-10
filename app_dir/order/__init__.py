from flask import Blueprint

bp = Blueprint('order', __name__)

from app_dir.order import routes
