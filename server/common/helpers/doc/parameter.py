from drf_yasg import openapi


class IdQueryParameter(openapi.Parameter):
    def __init__(self, name=None, description=None, required=None, schema=None, type=None, format=None, enum=None, pattern=None, items=None, default=None, **extra):
        name = name or 'id'
        in_ = openapi.IN_QUERY
        type = openapi.TYPE_STRING
        super().__init__(name, in_, description, required, schema,
                         type, format, enum, pattern, items, default, **extra)


class EmailQueryParameter(openapi.Parameter):
    def __init__(self, name=None, description=None, required=None, schema=None, type=None, format=None, enum=None, pattern=None, items=None, default=None, **extra):
        name = name or 'email'
        in_ = openapi.IN_QUERY
        type = openapi.TYPE_STRING
        super().__init__(name, in_, description, required, schema,
                         type, format, enum, pattern, items, default, **extra)
