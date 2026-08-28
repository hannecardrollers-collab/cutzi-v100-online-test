from pathlib import Path
import hashlib
p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode()+b).hexdigest()

assert blob_sha(s)=='f27da6c82980593d8bd29cc64cb14151b1498429', blob_sha(s)
old="body.agenda-focus-v1006 #view-agenda{position:fixed!important;inset:0!important;z-index:45!important;display:block!important;width:100vw!important;height:100dvh!important;padding:10px!important;margin:0!important;background:var(--bg)!important;overflow:hidden!important}"
new="body.agenda-focus-v1006 #view-agenda{position:fixed!important;inset:0!important;z-index:45!important;display:block!important;width:100vw!important;height:100dvh!important;padding:10px!important;margin:0!important;background:rgba(13,11,13,.72)!important;backdrop-filter:blur(18px) saturate(112%)!important;-webkit-backdrop-filter:blur(18px) saturate(112%)!important;overflow:hidden!important}body[data-glass=\"light\"].agenda-focus-v1006 #view-agenda{background:rgba(246,241,244,.72)!important}"
assert s.count(old)==1, s.count(old)
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print(blob_sha(s))
