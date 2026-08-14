const enc=new TextEncoder();
export function json(data,status=200,extraHeaders={}){return new Response(JSON.stringify(data),{status,headers:{'content-type':'application/json; charset=utf-8','cache-control':'no-store',...extraHeaders}})}
export async function readJson(request){try{return await request.json()}catch(_){return null}}
function bytesToB64(bytes){let s='';for(const b of bytes)s+=String.fromCharCode(b);return btoa(s)}
function b64ToBytes(value){const s=atob(value);const out=new Uint8Array(s.length);for(let i=0;i<s.length;i++)out[i]=s.charCodeAt(i);return out}
export function randomToken(bytes=32){const a=new Uint8Array(bytes);crypto.getRandomValues(a);return bytesToB64(a).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'')}
export function randomSalt(){const a=new Uint8Array(16);crypto.getRandomValues(a);return bytesToB64(a)}
export async function passwordHash(password,saltB64){const key=await crypto.subtle.importKey('raw',enc.encode(password),'PBKDF2',false,['deriveBits']);const bits=await crypto.subtle.deriveBits({name:'PBKDF2',hash:'SHA-256',salt:b64ToBytes(saltB64),iterations:100000},key,256);return bytesToB64(new Uint8Array(bits))}
export async function sha256(value){const bits=await crypto.subtle.digest('SHA-256',enc.encode(value));return bytesToB64(new Uint8Array(bits))}
export function safeEqual(a,b){a=String(a||'');b=String(b||'');if(a.length!==b.length)return false;let diff=0;for(let i=0;i<a.length;i++)diff|=a.charCodeAt(i)^b.charCodeAt(i);return diff===0}
export function parseCookies(request){const raw=request.headers.get('cookie')||'';const out={};for(const part of raw.split(';')){const i=part.indexOf('=');if(i<0)continue;out[part.slice(0,i).trim()]=decodeURIComponent(part.slice(i+1).trim())}return out}
export function sessionCookie(request,token,remember){const secure=new URL(request.url).protocol==='https:'?'; Secure':'';const age=remember?'; Max-Age=2592000':'';return `cutzi_session=${encodeURIComponent(token)}; Path=/; HttpOnly; SameSite=Lax${secure}${age}`}
export function clearSessionCookie(request){const secure=new URL(request.url).protocol==='https:'?'; Secure':'';return `cutzi_session=; Path=/; HttpOnly; SameSite=Lax${secure}; Max-Age=0`}
export async function getSession(context){const token=parseCookies(context.request).cutzi_session;if(!token)return null;const tokenHash=await sha256(token),now=new Date().toISOString();const row=await context.env.DB.prepare(`SELECT s.token_hash,s.expires_at,u.id AS user_id,u.email,u.full_name,u.phone,u.role,u.created_at,u.salon_id,sa.name AS salon_name FROM sessions s JOIN users u ON u.id=s.user_id JOIN salons sa ON sa.id=u.salon_id WHERE s.token_hash=? AND s.expires_at>? LIMIT 1`).bind(tokenHash,now).first();return row||null}
export function accountFromRow(row){return {id:row.user_id,email:row.email,fullName:row.full_name,phone:row.phone||'',role:row.role||'',createdAt:row.created_at,salonId:row.salon_id,salonName:row.salon_name}}
