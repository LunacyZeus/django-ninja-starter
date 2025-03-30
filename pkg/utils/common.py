import json


def record_data(file_path, data, is_parse=False):
    if isinstance(data, str):
        if is_parse:
            save_data = json.loads(data)
            save_data = json.dumps(save_data, ensure_ascii=False, indent=4)
        else:
            save_data = data
    else:
        save_data = json.dumps(data, ensure_ascii=False, indent=4)

    open(file_path, "w", encoding="utf8").write(save_data)


def get_record_data(file_path, is_json=True):
    data = open(file_path, encoding="utf8").read()
    if is_json:
        data = json.loads(data)

    return data
