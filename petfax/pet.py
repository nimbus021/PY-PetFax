from flask import Blueprint, render_template, json


bp = Blueprint('pet', __name__, url_prefix="/pets")


@bp.route('/')
def index():
    pets = json.load(open('../pets.json'))
    return render_template('index.html', pets=pets)
