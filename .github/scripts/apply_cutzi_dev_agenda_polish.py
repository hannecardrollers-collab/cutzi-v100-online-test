from pathlib import Path
import hashlib
p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode()+b).hexdigest()

assert blob_sha(s)=='d3a58ec1c641bb35422bd433de5e66f044a8d523', blob_sha(s)

old_text="<div class=\"agenda-closed-state-v1002\"><div><strong>Salon gesloten</strong><span>De uren blijven zichtbaar als referentie. Activeer deze dag bij Instellingen → Openingstijden om afspraken te plannen.</span></div></div>"
new_text="<div class=\"agenda-closed-state-v1002\"><div><strong>Salon gesloten.</strong><span>De uren worden alleen als referentie getoond. Activeer deze dag via Instellingen → Openingstijden om afspraken te kunnen plannen.</span></div></div>"
assert s.count(old_text)==1, s.count(old_text)
s=s.replace(old_text,new_text,1)

polish='''<style id="cutziAgendaDevPolish">\n/* Cutzi dev — stronger glass visibility in agenda fullscreen + closed-day copy/layout polish. */\nbody.agenda-focus-v1006 #view-agenda{\n  background:rgba(7,8,11,.08)!important;\n  backdrop-filter:blur(4px) saturate(112%)!important;\n  -webkit-backdrop-filter:blur(4px) saturate(112%)!important;\n}\nbody.agenda-focus-v1006 #agendaShell.glass{\n  background:linear-gradient(145deg,rgba(255,255,255,.075),rgba(255,255,255,.018))!important;\n  backdrop-filter:blur(16px) saturate(116%)!important;\n  -webkit-backdrop-filter:blur(16px) saturate(116%)!important;\n  border-color:rgba(255,255,255,.13)!important;\n}\nbody.agenda-focus-v1006 #view-agenda .agenda-toolbar{background:rgba(12,13,16,.18)!important;backdrop-filter:blur(18px) saturate(112%)!important;-webkit-backdrop-filter:blur(18px) saturate(112%)!important}\nbody.agenda-focus-v1006 #view-agenda .time-col{background:rgba(13,14,17,.24)!important;backdrop-filter:blur(16px)!important;-webkit-backdrop-filter:blur(16px)!important}\nbody.agenda-focus-v1006 #view-agenda .staff-head{background:rgba(12,13,17,.27)!important;backdrop-filter:blur(18px)!important;-webkit-backdrop-filter:blur(18px)!important}\nbody.agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(4,5,8,.025)!important}\nbody[data-glass="light"].agenda-focus-v1006 #view-agenda{background:rgba(246,241,244,.10)!important}\nbody[data-glass="light"].agenda-focus-v1006 #agendaShell.glass{background:linear-gradient(145deg,rgba(255,255,255,.30),rgba(255,255,255,.11))!important}\nbody[data-glass="light"].agenda-focus-v1006 #view-agenda .agenda-toolbar{background:rgba(255,255,255,.24)!important}\nbody[data-glass="light"].agenda-focus-v1006 #view-agenda .time-col{background:rgba(255,255,255,.25)!important}\nbody[data-glass="light"].agenda-focus-v1006 #view-agenda .staff-head{background:rgba(255,255,255,.30)!important}\nbody[data-glass="light"].agenda-focus-v1006 #view-agenda .grid-canvas{background-color:rgba(255,255,255,.035)!important}\n#view-agenda .agenda-closed-state-v1002>div{display:flex!important;flex-direction:column!important;align-items:center!important;gap:7px!important;max-width:760px!important}\n#view-agenda .agenda-closed-state-v1002 strong{display:block!important;margin:0!important;line-height:1.25!important}\n#view-agenda .agenda-closed-state-v1002 span{display:block!important;line-height:1.55!important}\n</style>'''
assert 'id="cutziAgendaDevPolish"' not in s
s=s.replace('</head>',polish+'\n</head>',1)
p.write_text(s,encoding='utf-8')
print(blob_sha(s))
