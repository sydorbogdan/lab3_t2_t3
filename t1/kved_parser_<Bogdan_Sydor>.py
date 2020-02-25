import json


def open_json(path: str):
    """
    (str) -> dict
    open jsop file
    """
    with open('kved.json') as f:
        data = json.load(f)
    return data


def create_json(path: str, rez: dict):
    """
    (str, dict) -> None
    write data to file
    """
    with open(path, 'w') as f:
        json.dump(rez, f, ensure_ascii=False, indent=2)


def transform_data(data: dict):
    """
    (dict) -> list
    return transformed data
    """
    rez = []
    sec_ch = len(data['sections'][0])
    for sections in data['sections'][0]:
        div_ch = len(sections['divisions'])
        for divisions in sections['divisions']:
            gr_ch = len(divisions['groups'])
            for groups in divisions['groups']:
                for classes in groups['classes']:
                    a = {"classCode": classes['classCode'],
                         "name": classes['className'],
                         "type": 'classes',
                         "parent": {
                        "name": groups['groupName'],
                        "type": 'groups',
                        "num_children": gr_ch,
                        "parent": {
                            "name": divisions['divisionName'],
                            "type": 'divisions',
                            "num_children": div_ch,
                            "parent": {
                                "name": sections['sectionName'],
                                "type": 'sections',
                                "num_children": sec_ch
                            }
                        }
                    }
                    }
                    rez.append(a)
    return rez


def find_class(data: dict, klass: str):
    """
    (dict, str)
    return dict where ke 'name' == input(), from data
    """
    if_check = 0
    for i in data:
        if i['classCode'] == klass:
            del i['classCode']
            create_json('kved_results.json', i)
            if_check += 1
    if if_check == 0:
        print('Input error')


def main():
    """
    run program
    """
    try:
        classCode = input()
        data = open_json('kved.json')
        data = transform_data(data)
        find_class(data, classCode)
    except:
        print('Input error')


if __name__ == '__main__':
    main()
