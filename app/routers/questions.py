from flask import Blueprint, request



questions_bp = Blueprint('questions', __name__)

@questions_bp.route('/', methods=['GET', 'POST'])
def questions():
    if request.method == "GET":
        return 'List of questions'
    if request.method == "POST":
        return 'Add question'


@questions_bp.route('/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def question(id):
    if request.method == "GET":
        return f'Question {id}'
    if request.method == "PUT":
        return f'Update question {id}'
    if request.method == "DELETE":
        return f'Delete question {id}'