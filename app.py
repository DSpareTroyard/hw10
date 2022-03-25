from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def page_index():
    with open("candidates.json", encoding='utf-8') as f:
        candidates = json.load(f)

    response_string = "<pre>"
    for candidate in candidates:
        response_string += f"<a href='/candidate/{candidate['id']}/'>Имя кандидата - {candidate['name']}<br>"
        response_string += f"Позиция кандидата {candidate['position']}<br>"
        response_string += f"Навыки через запятую {candidate['skills']}</a><br>"
        response_string += f"<br>"
    response_string += "<pre>"
    return response_string


@app.route('/candidate/<int:candidate_id>/')
def page_candidate(candidate_id):
    with open("candidates.json", encoding='utf-8') as f:
        candidates = json.load(f)

    response_string = f"<pre>"
    for candidate in candidates:
        if candidate['id'] == candidate_id:
            response_string += f"Имя кандидата - {candidate['name']}<br>"
            response_string += f"Позиция кандидата {candidate['position']}<br>"
            response_string += f"Навыки через запятую {candidate['skills']}<br>"
            response_string += f"<br>"
            break

    response_string += "<pre>"
    return response_string


app.run()
