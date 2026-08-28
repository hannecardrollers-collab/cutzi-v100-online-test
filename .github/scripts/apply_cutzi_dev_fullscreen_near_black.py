from pathlib import Path
import hashlib

p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode('ascii')+b).hexdigest()

assert blob_sha(s)=='423ccbdff52cb27bb9326a8a1f31a179e9e32e61', blob_sha(s)

repls={
'''body.agenda-focus-v1006 #view-agenda{\n  background:rgba(7,8,11,.08)!important;\n  backdrop-filter:blur(4px) saturate(112%)!important;\n  -webkit-backdrop-filter:blur(4px) saturate(112%)!important;\n}''':'''body.agenda-focus-v1006 #view-agenda{\n  background:rgba(5,6,9,.95)!important;\n  backdrop-filter:blur(8px) saturate(108%)!important;\n  -webkit-backdrop-filter:blur(8px) saturate(108%)!important;\n}''',
'''body.agenda-focus-v1006 #agendaShell.glass{\n  background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018))!important;\n  backdrop-filter:blur(16px) saturate(116%)!important;\n  -webkit-backdrop-filter:blur(16px) saturate(116%)!important;\n  border-color:rgba(255,255,255,.13)!important;\n}''':'''body.agenda-focus-v1006 #agendaShell.glass{\n  background:linear-gradient(145deg,rgba(18,19,23,.94),rgba(8,9,12,.90))!important;\n  backdrop-filter:blur(14px) saturate(110%)!important;\n  -webkit-backdrop-filter:blur(14px) saturate(110%)!important;\n  border-color:rgba(255,255,255,.11)!important;\n}''',
'''body.agenda-focus-v1006 #view-agenda .agenda-toolbar{background:rgba(12,13,16,.18)!important;backdrop-filter:blur(18px) saturate(112%)!important;-webkit-backdrop-filter:blur(18px) saturate(112%)!important}''':'''body.agenda-focus-v1006 #view-agenda .agenda-toolbar{background:rgba(12,13,16,.78)!important;backdrop-filter:blur(16px) saturate(108%)!important;-webkit-backdrop-filter:blur(16px) saturate(108%)!important}''',
'''body.agenda-focus-v1006 #view-agenda .time-col{background:rgba(13,14,17,.24)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}''':'''body.agenda-focus-v1006 #view-agenda .time-col{background:rgba(11,12,15,.82)!important;backdrop-filter:blur(14px)!important;-webkit-backdrop-filter:blur(14px)!important}''',
'''body.agenda-focus-v1006 #view-agenda .staff-head{background:rgba(12,13,17,.27)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important}''':'''body.agenda-focus-v1006 #view-agenda .staff-head{background:rgba(12,13,17,.84)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}''',
'''body.agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(4,5,8,.025)!important}''':'''body.agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(4,5,8,.70)!important}'''
}
for old,new in repls.items():
    assert old in s, old
    s=s.replace(old,new,1)

p.write_text(s,encoding='utf-8')
print(blob_sha(s))
