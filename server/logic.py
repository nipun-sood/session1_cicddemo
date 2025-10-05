from .dao import get_last_names_by_first_name

def get_initials(first_name, last_name):
    # Get first letter of first name and last name
    # first_initial = ''
    # last_initial = ''
    # if first_name is not None and len(first_name) > 0:
    first_initial = first_name[0].upper()
    # if last_name is not None and len(last_name) > 0:
    last_initial = last_name[0].upper()
    return f'{first_initial}{last_initial}'

def get_last_names_logic(conn, first_name):
    last_names = get_last_names_by_first_name(conn, first_name)
    results = []
    for ln in last_names:
        initials = get_initials(first_name, ln)
        results.append(f'{first_name} "{initials}" {ln}')
    return results
