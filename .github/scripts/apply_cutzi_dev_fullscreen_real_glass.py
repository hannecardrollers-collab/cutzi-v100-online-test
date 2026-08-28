from pathlib import Path
import hashlib

p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode('ascii')+b).hexdigest()

expected='c132ab51bf799b6624cb440d24dd914d64bb130d'
assert blob_sha(s)==expected, (blob_sha(s), expected)
repls={
'''    rgba(5,6,9,.62)!important;''':'''    rgba(5,6,9,.16)!important;''',
'''  background:linear-gradient(145deg,rgba(18,19,23,.86),rgba(8,9,12,.82))!important;''':'''  background:linear-gradient(145deg,rgba(18,19,23,.42),rgba(8,9,12,.26))!important;''',
'''body.agenda-focus-v1006 #view-agenda .agenda-toolbar{background:rgba(12,13,16,.72)!important;''':'''body.agenda-focus-v1006 #view-agenda .agenda-toolbar{background:rgba(12,13,16,.36)!important;''',
'''body.agenda-focus-v1006 #view-agenda .time-col{background:rgba(11,12,15,.76)!important;''':'''body.agenda-focus-v1006 #view-agenda .time-col{background:rgba(11,12,15,.40)!important;''',
'''body.agenda-focus-v1006 #view-agenda .staff-head{background:rgba(12,13,17,.78)!important;''':'''body.agenda-focus-v1006 #view-agenda .staff-head{background:rgba(12,13,17,.42)!important;''',
'''body.agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(4,5,8,.70)!important}''':'''body.agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(4,5,8,.10)!important}'''
}
for old,new in repls.items():
    assert s.count(old)==1, (old, s.count(old))
    s=s.replace(old,new,1)
# Make the underlying Cutzi scene slightly more visible only in focus mode.
needle='''body.agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(4,5,8,.10)!important}\n'''
insert=needle+'''body.agenda-focus-v1006 .bg-scene{filter:brightness(1.12) saturate(1.12)!important}\n'''
assert s.count(needle)==1
s=s.replace(needle,insert,1)
p.write_text(s,encoding='utf-8')
print(blob_sha(s))
