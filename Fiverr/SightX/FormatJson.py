import json

with open('../../input.json', encoding='utf-8-sig') as f:
    d = json.load(f)

for i in d:
    if i == 'responses':
        for k, e in enumerate(d[i]):
            if k == 0:
                for l in e:
                    if l == 'answers':
                        for s, v in e[l].items():
                            dict1 = {'questionId': s, 'na': v['na'] if 'na' in v else None, 'values': v['values']}
                            print({k: v for k, v in dict1.items() if v is not None})


