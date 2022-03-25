from flask import Flask
import json

app = Flask(__name__)


def get_candidates(json_file):
    with open(json_file, encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def page_index():
    candidates = get_candidates("candidates.json")

    response_string = "<pre>"
    for candidate in candidates:
        response_string += f"<a href='/candidate/{candidate['id']}/'>Имя кандидата - {candidate['name']}<br>"
        response_string += f"Позиция кандидата {candidate['position']}<br>"
        response_string += f"Навыки через запятую {candidate['skills']}</a><br>"
        response_string += f"<br>"
    response_string += "</pre>"
    return response_string


@app.route('/candidate/<int:candidate_id>/')
def page_candidate(candidate_id):
    candidates = get_candidates("candidates.json")

    response_string = f"<pre>"
    for candidate in candidates:
        skills = candidate['skills'].lower().split(", ")
        skills_link = []
        if candidate['id'] == candidate_id:
            response_string += f"<img src=\"{candidate['picture']}\"<br><br>"
            response_string += f"Имя кандидата - {candidate['name']}<br>"
            response_string += f"Позиция кандидата {candidate['position']}<br>"
            response_string += f"Навыки через запятую "
            for skill in skills:
                skills_link.append(f"<a href='/skill/{skill}/'>{skill}</a>")
            response_string += ", ".join(skills_link)
            response_string += f"<br>"
            break

    response_string += "</pre>"
    return response_string


@app.route('/skill/<skill>/')
def page_skill(skill):
    candidates = get_candidates("candidates.json")

    response_string = f"<pre>"
    for candidate in candidates:
        skills = candidate['skills'].lower().split(", ")
        if skill.lower() in skills:
            response_string += f"Имя кандидата - {candidate['name']}<br>"
            response_string += f"Позиция кандидата {candidate['position']}<br>"
            response_string += f"Навыки через запятую {candidate['skills']}<br>"
            response_string += f"<br>"

    response_string += f"</pre>"
    return response_string


app.run()
