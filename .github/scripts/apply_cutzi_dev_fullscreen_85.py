from pathlib import Path
import hashlib

p=Path('public/index.html')
s=p.read_text(encoding='utf-8')

def blob_sha(text):
    b=text.encode('utf-8')
    return hashlib.sha1((f'blob {len(b)}\0').encode('ascii')+b).hexdigest()

assert blob_sha(s)=='3ce469027bb1ff9477d0a07db2a18582cfaf14ce', blob_sha(s)

repls={
'background:rgba(5,6,9,.95)!important;':'background:rgba(5,6,9,.85)!important;',
'background:linear-gradient(145deg,rgba(18,19,23,.94),rgba(8,9,12,.90))!important;':'background:linear-gradient(145deg,rgba(18,19,23,.86),rgba(8,9,12,.82))!important;',
'background:rgba(12,13,16,.78)!important;':'background:rgba(12,13,16,.72)!important;',
'background:rgba(11,12,15,.82)!important;':'background:rgba(11,12,15,.76)!important;',
'background:rgba(12,13,17,.84)!important;':'background:rgba(12,13,17,.78)!important;',
'background-color:rgba(4,5,8,.70)!important;':'background-color:rgba(4,5,8,.60)!important;'
}
for old,new in repls.items():
    assert s.count(old)>=1, old
    s=s.replace(old,new,1)

p.write_text(s,encoding='utf-8')
print(blob_sha(s))
