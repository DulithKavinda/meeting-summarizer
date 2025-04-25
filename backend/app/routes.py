from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/test')
def test_route():
    return {"status": "SUCCESS", "message": "It's working now!"}