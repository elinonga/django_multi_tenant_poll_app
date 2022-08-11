from django.db import connection

def hostname_from_request(request):
    # split on `:` to remove port
    return request.get_host().split(':')[0].lower()


def tenant_schema_from_request(request):
    hostname = hostname_from_request(request)
    tenants_map = get_tenants_map()
    return tenants_map.get(hostname)


def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f"SET search_path to {schema}")

        
"""
    Now when we get a request to dart.polls.local we need to read from the schema dart, 
    and when we get a request to agricomm.polls.local we need to read from schema agricomm.
"""
def get_tenants_map():
    return {
        "dart.polls.local": "dart",
        "agricomm.polls.local": "agricomm",
    }
