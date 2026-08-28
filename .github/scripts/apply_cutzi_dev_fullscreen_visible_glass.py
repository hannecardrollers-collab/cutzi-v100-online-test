from pathlib import Path
import hashlib

p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode('ascii')+b).hexdigest()

assert blob_sha(s)=='e16c256adc1232cd95a4dc187652522f9f5d191d', blob_sha(s)
old='''body.agenda-focus-v1006 #view-agenda{\n  background:rgba(5,6,9,.85)!important;\n  backdrop-filter:blur(8px) saturate(108%)!important;\n  -webkit-backdrop-filter:blur(8px) saturate(108%)!important;\n}'''
new='''body.agenda-focus-v1006 #view-agenda{\n  background:\n    radial-gradient(circle at 78% 18%,rgba(239,93,168,.085),transparent 34%),\n    radial-gradient(circle at 25% 80%,rgba(96,118,255,.065),transparent 38%),\n    rgba(5,6,9,.62)!important;\n  backdrop-filter:blur(8px) saturate(112%)!important;\n  -webkit-backdrop-filter:blur(8px) saturate(112%)!important;\n}'''
assert s.count(old)==1, s.count(old)
s=s.replace(old,new,1)
p.write_text(s,encoding='utf-8')
print(blob_sha(s))
