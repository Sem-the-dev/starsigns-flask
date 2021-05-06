
''' Signs controller '''

signs = [
    {'id': 1, 'sign': 'Aquarius'},
    {'id': 2, 'sign': 'Pisces'},
    {'id': 3, 'sign': 'Aries'},
    {'id': 4, 'sign': 'Taurus'},
    {'id': 5, 'sign': 'Gemini'},
    {'id': 6, 'sign': 'Cancer'},
    # {'sign': 'Leo'},
    # {'sign': 'Virgo'},
    # {'sign': 'Scorpio'},
    # {'sign': 'Saggitarius'},
    # {'sign': 'Capricorn'},
     ]

def index(req):
    return [c for c in signs], 200

def create(req):
    new_sign = req.get_json()
    new_sign['id'] = sorted([c['id'] for c in signs])[-1] + 1
    signs.append(new_sign)
    return new_sign, 201

def show(req, uid):
    return find_by_uid(uid), 200

def update(req, uid):
    sign = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        sign[key] = val
    return sign, 200

def destroy(req, uid):
    sign = find_by_uid(uid)
    signs.remove(sign)
    return sign, 204


def find_by_uid(uid):
    try:
        return next(sign for sign in signs if sign['id'] == uid)
    except:
        raise Exception