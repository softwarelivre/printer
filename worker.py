from lib.badge import Badge
from lib.envelope import Envelope

def print_badge(value):
    xid = value['xid']
    name = value.get('name',None)
    company = value.get('organization',None)
    city = value.get('city', None)
    copies = value.get('copies', 1)
    badge    = Badge(xid, name, company, city, copies)
    envelope = Envelope(xid, name, company, city, 1)
    return badge;
