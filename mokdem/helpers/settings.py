def parse_setting(settings, key):
    value = None
    if (key in settings):
        value = settings[key]
        if value == 'True':
            return True
        if value == 'False':
            return False
    return value


def settings(request):
    if 'parsed_settings' not in request.registry:
        parsed_settings = {}
        for k, v in request.registry.settings:
            parsed_settings[k] = parse_setting(request.registry.settings, k)

        setattr(request.registry, 'parsed_settings', request.registry.parsed_setting)

    return request.registry.parsed_settings
