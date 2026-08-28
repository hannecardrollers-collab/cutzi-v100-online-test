from pathlib import Path
import hashlib

p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def git_blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode('ascii')+b).hexdigest()

assert git_blob_sha(s)=='c821ae185126a8a4d5b478ded37dbea4c138c320', 'Unexpected Cutzi base version'

css=r'''<style id="cutziAgendaFullscreenV1006">
/* v100.6 — Agenda focus/fullscreen mode. UI-only: no D1, auth or booking-data changes. */
#view-agenda .agenda-fullscreen-btn-v1006{width:40px;height:40px;min-width:40px;flex:0 0 40px;padding:0;border-radius:12px;border:1px solid rgba(255,255,255,.11);background:rgba(255,255,255,.045);color:rgba(255,255,255,.92);display:grid;place-items:center;cursor:pointer;backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);transition:background .16s ease,border-color .16s ease,transform .16s ease}
#view-agenda .agenda-fullscreen-btn-v1006:hover,#view-agenda .agenda-fullscreen-btn-v1006:focus-visible{color:#fff;background:rgba(255,255,255,.105);border-color:rgba(255,255,255,.20);outline:none}
#view-agenda .agenda-fullscreen-btn-v1006:active{transform:scale(.97)}
#view-agenda .agenda-fullscreen-btn-v1006 svg{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
#view-agenda .agenda-fullscreen-btn-v1006 .agenda-collapse-icon-v1006{display:none}
body.agenda-focus-v1006 #view-agenda .agenda-fullscreen-btn-v1006 .agenda-expand-icon-v1006{display:none}
body.agenda-focus-v1006 #view-agenda .agenda-fullscreen-btn-v1006 .agenda-collapse-icon-v1006{display:block}
body[data-glass="light"] #view-agenda .agenda-fullscreen-btn-v1006{background:rgba(255,255,255,.74);border-color:rgba(91,55,75,.14);color:#4f3945}
body[data-glass="light"] #view-agenda .agenda-fullscreen-btn-v1006:hover,body[data-glass="light"] #view-agenda .agenda-fullscreen-btn-v1006:focus-visible{background:#fff;border-color:rgba(91,55,75,.24);color:#2d1b25}
body.agenda-focus-v1006{overflow:hidden!important}
body.agenda-focus-v1006 #view-agenda{position:fixed!important;inset:0!important;z-index:45!important;display:block!important;width:100vw!important;height:100dvh!important;padding:10px!important;margin:0!important;background:var(--bg)!important;overflow:hidden!important}
body.agenda-focus-v1006 #view-agenda .agenda-shell{width:100%!important;height:calc(100dvh - 20px)!important;min-height:0!important;display:flex!important;flex-direction:column!important;overflow:hidden!important;border-radius:22px!important;box-shadow:0 28px 90px rgba(0,0,0,.34),inset 0 1px 0 rgba(255,255,255,.075)!important}
body.agenda-focus-v1006 #view-agenda .agenda-toolbar{flex:0 0 auto!important}
body.agenda-focus-v1006 #view-agenda .agenda-body{flex:1 1 auto!important;min-height:0!important;max-height:none!important;height:auto!important;overflow:auto!important;-webkit-overflow-scrolling:touch}
body.agenda-focus-v1006 #view-agenda .agenda-body.overview-mode{max-height:none!important;overflow:auto!important}
body.agenda-focus-v1006 .mobile-bottom-nav-v52,body.agenda-focus-v1006 .mobile-quick-actions-v52,body.agenda-focus-v1006 .mobile-more-backdrop-v52,body.agenda-focus-v1006 .pilot-badge-v52{opacity:0!important;visibility:hidden!important;pointer-events:none!important}
@media(max-width:820px){#view-agenda .agenda-actions{order:2!important;margin-left:auto!important;flex:0 0 auto!important;overflow:visible!important}#view-agenda .agenda-view-switch{order:3!important}body.agenda-focus-v1006 #view-agenda{padding:0!important}body.agenda-focus-v1006 #view-agenda .agenda-shell{height:100dvh!important;border-radius:0!important;border-left:0!important;border-right:0!important}body.agenda-focus-v1006 #view-agenda .agenda-toolbar{padding-top:max(10px,env(safe-area-inset-top))!important}body.agenda-focus-v1006 #view-agenda .agenda-body{max-height:none!important}}
</style>'''
assert 'id="cutziAgendaFullscreenV1006"' not in s
s=s.replace('</head>',css+'\n</head>',1)

old_actions='<div class="agenda-actions"><button class="secondary smart-btn-v38" id="smartBtn"'
new_actions='''<div class="agenda-actions"><button class="agenda-fullscreen-btn-v1006" id="agendaFullscreenBtnV1006" type="button" aria-label="Agenda op volledig scherm" aria-pressed="false" title="Volledig scherm"><svg class="agenda-expand-icon-v1006" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 3H3v5M16 3h5v5M21 16v5h-5M8 21H3v-5"/></svg><svg class="agenda-collapse-icon-v1006" viewBox="0 0 24 24" aria-hidden="true"><path d="M9 4v5H4M15 4v5h5M20 15h-5v5M4 15h5v5"/></svg></button><button class="secondary smart-btn-v38" id="smartBtn"'''
assert s.count(old_actions)==1
s=s.replace(old_actions,new_actions,1)

old_go="function goView(name){document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));"
new_go="function goView(name){if(name!=='agenda'&&document.body.classList.contains('agenda-focus-v1006'))exitAgendaFocusV1006(false);document.querySelectorAll('.view').forEach(v=>v.classList.remove('active'));"
assert s.count(old_go)==1
s=s.replace(old_go,new_go,1)

anchor="const navBtns=document.querySelectorAll('.date-nav .iconbtn');if(navBtns[0])navBtns[0].onclick=()=>shiftAgendaRange(-1);if(navBtns[1])navBtns[1].onclick=()=>shiftAgendaRange(1);\n"
assert s.count(anchor)==1
js=r'''const agendaFocusStateV1006={windowY:0,bodyTop:0,bodyLeft:0};
function updateAgendaFullscreenButtonV1006(){const btn=document.getElementById('agendaFullscreenBtnV1006');if(!btn)return;const active=document.body.classList.contains('agenda-focus-v1006'),fr=document.documentElement.lang==='fr';btn.setAttribute('aria-pressed',active?'true':'false');btn.setAttribute('aria-label',active?(fr?'Quitter le plein écran':'Volledig scherm sluiten'):(fr?'Ouvrir l’agenda en plein écran':'Agenda op volledig scherm'));btn.title=active?(fr?'Quitter le plein écran':'Volledig scherm sluiten'):(fr?'Plein écran':'Volledig scherm')}
function setAgendaFocusV1006(active,announce=true){const agendaBody=document.querySelector('#view-agenda .agenda-body');if(active===document.body.classList.contains('agenda-focus-v1006'))return;if(active){agendaFocusStateV1006.windowY=window.scrollY||0;agendaFocusStateV1006.bodyTop=agendaBody?.scrollTop||0;agendaFocusStateV1006.bodyLeft=agendaBody?.scrollLeft||0;document.body.classList.add('agenda-focus-v1006')}else{if(agendaBody){agendaFocusStateV1006.bodyTop=agendaBody.scrollTop;agendaFocusStateV1006.bodyLeft=agendaBody.scrollLeft}document.body.classList.remove('agenda-focus-v1006')}updateAgendaFullscreenButtonV1006();requestAnimationFrame(()=>{const bodyNow=document.querySelector('#view-agenda .agenda-body');if(bodyNow){bodyNow.scrollTop=agendaFocusStateV1006.bodyTop;bodyNow.scrollLeft=agendaFocusStateV1006.bodyLeft}if(!active)window.scrollTo({top:agendaFocusStateV1006.windowY,left:0,behavior:'auto'})});if(announce)showToast(document.documentElement.lang==='fr'?(active?'Agenda en plein écran':'Plein écran fermé'):(active?'Agenda op volledig scherm':'Volledig scherm gesloten'))}
function exitAgendaFocusV1006(announce=true){setAgendaFocusV1006(false,announce)}
document.getElementById('agendaFullscreenBtnV1006')?.addEventListener('click',()=>setAgendaFocusV1006(!document.body.classList.contains('agenda-focus-v1006')));
document.addEventListener('keydown',e=>{if(e.key!=='Escape'||!document.body.classList.contains('agenda-focus-v1006'))return;if(document.querySelector('.modal-backdrop.show,.drawer-backdrop.show,.mobile-more-backdrop-v52.show'))return;exitAgendaFocusV1006()});
updateAgendaFullscreenButtonV1006();
'''
s=s.replace(anchor,anchor+js,1)

assert git_blob_sha(s)=='3764551e13823d1ebe2ba9d87d30649731b2cb94', git_blob_sha(s)
p.write_text(s,encoding='utf-8')
