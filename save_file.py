import json

def write_file (high_score, ai_settings):
    with open(ai_settings.file_name,'w') as file_object:
        json.dump(high_score,file_object)

def read_file(ai_settings):
    try:
        with open(ai_settings.file_name)as file_object:
            high_score = json.load(file_object)
    except FileNotFoundError:
        return 0
    else: return high_score