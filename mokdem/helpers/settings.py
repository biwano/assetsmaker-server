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
        for k in request.registry.settings:
            parsed_settings[k] = parse_setting(request.registry.settings, k)

        setattr(request.registry, 'parsed_settings', parsed_settings)

    return request.registry.parsed_settings


def settings_value(request, key):
    return settings(request)[key]
