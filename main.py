from utils import *
from flask import *

diction = get_dict()
app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('list.html', items=diction)


@app.route('/candidate/<uid>')
def candidate_page(uid):
    candidate = get_candidate(uid)
    return render_template('card.html', name=candidate['name'], position=candidate['position'],
                           picture=candidate['picture'], skills=candidate['skills'])


@app.route('/search/<candidate_name>')
def search(candidate_name):
    dict_of_valid = {}
    dict_of_all = get_candidates_by_name(candidate_name)
    dict_of_valid[dict_of_all['id']]=dict_of_all['name']
    return render_template('search.html',count_of_candidates=len(dict_of_valid),items=dict_of_valid)


@app.route('/skill/<skill_name>')
def skill_search(skill_name):
    valid_candidates=get_candidates_by_skill(skill_name)
    valid_candidates_id_dict = {}
    if len(valid_candidates)>1:
        for candidate in valid_candidates:
            valid_candidates_id_dict[candidate['id']]=candidate['name']
    else:
        valid_candidates_id_dict = dict(valid_candidates['id'],valid_candidates['name'])
    return render_template('skill.html',skill=skill_name,skill_count=len(valid_candidates),items=valid_candidates_id_dict)

app.run()
