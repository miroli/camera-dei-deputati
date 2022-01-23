import json


def merge_data():
    with open('positions.json') as f:
        positions = json.loads(f.read())

    with open('statements.json') as f:
        statements = json.loads(f.read())


    data = []

    for statement in statements:
        entry = {'item': statement['item'], 'st': statement['st'], "code": statement['code']}
        for position in positions:
            p_code = position['persona']['value'].split('/')[-1][1:]
            s_code = statement['code']
            if p_code == s_code:
                start = position['startMandato']['value']
                end = position['fineMandato']['value']
                start = f'{start[:4]}-{start[4:6]}-{start[6:8]}'
                end = f'{end[:4]}-{end[4:6]}-{end[6:8]}'
                entry['start'] = start
                entry['end'] = end
        data.append(entry)

    with open('merged_data.json', 'w') as f:
        f.write(json.dumps(data))


if __name__ == '__main__':
    merge_data()
