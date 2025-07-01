import json


def readJson(file):
    with open(file, "r", encoding="utf8") as f:
        return json.load(f)


def writeJson(file, data, indent=2):
    with open(file, "w", encoding="utf8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=indent)


target_path = "localized_data/text_data_dict.json"
target = readJson(target_path)
skill_data = readJson("skill_data_dict.json")
target["48"] = skill_data["48"]
writeJson(target_path, target)
