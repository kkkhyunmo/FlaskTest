from flask import Blueprint, render_template

bp = Blueprint('chatbot', __name__, url_prefix='/chatbot')

@bp.route('/')
def chatbot():
    return render_template('chatBot/chatbot_test.html')