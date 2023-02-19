def serialize(obj):
    dictionary = dict()
    for key in vars(obj):
        if key.startswith('_'):
            continue
        value = getattr(obj, key)
        if isinstance(value, list):
            dictionary[key] = list(map(serialize, value))
        else:
            dictionary[key] = serialize(value)
    for key, value in vars(type(obj)).items():
        if isinstance(value, property):
            dictionary[key] = getattr(obj, key)
    return dictionary
