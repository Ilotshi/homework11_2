import json


def load_candidates_from_json():
    with open('candidates.json', encoding='utf-8') as f:
        data = json.load(f)
        return data


def get_candidate(candidate_id):
    candidate_json = load_candidates_from_json()
    for candidate in candidate_json:
        if candidate['id'] == int(candidate_id):
            return candidate


def get_candidates_by_name(candidate_name):
    candidate_json = load_candidates_from_json()
    for candidate in candidate_json:
        if candidate_name in candidate['name']:
            return candidate


def get_candidates_by_skill(skill_name):
    list_of_candidates = []
    candidate_json = load_candidates_from_json()
    for candidate in candidate_json:
        if skill_name.lower() in candidate['skills'].lower():
            list_of_candidates.append(candidate)
    return list_of_candidates


def get_dict():
    candidates_id_dict={}
    loaded_candidates = load_candidates_from_json()
    for candidate in loaded_candidates:
        candidates_id_dict[candidate['id']]=candidate['name']
    return candidates_id_dict

