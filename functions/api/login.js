import {json,readJson,passwordHash,safeEqual,randomToken,sha256,sessionCookie} from '../_lib/auth.js';
export async function onRequestPost(context){
  const b=await readJson(context.request),email=String(b?.email||'').trim().toLowerCase(),password=String(b?.password||''),remember=!!b?.remember;if(!email||!password)return json({error:'Vul e-mailadres en wachtwoord in.'},400);
  const row=await context.env.DB.prepare(`SELECT u.id AS user_id,u.email,u.full_name,u.phone,u.role,u.password_hash,u.password_salt,u.created_at,u.salon_id,s.name AS salon_name FROM users u JOIN salons s ON s.id=u.salon_id WHERE u.email=? LIMIT 1`).bind(email).first();if(!row)return json({error:'E-mailadres of wachtwoord klopt niet.'},401);
  const hash=await passwordHash(password,row.password_salt);if(!safeEqual(hash,row.password_hash))return json({error:'E-mailadres of wachtwoord klopt niet.'},401);
  const token=randomToken(),tokenHash=await sha256(token),now=new Date().toISOString(),expiry=new Date(Date.now()+(remember?30:0.5)*86400000).toISOString();await context.env.DB.prepare('INSERT INTO sessions(token_hash,user_id,created_at,expires_at) VALUES(?,?,?,?)').bind(tokenHash,row.user_id,now,expiry).run();
  return json({account:{id:row.user_id,email:row.email,fullName:row.full_name,phone:row.phone||'',role:row.role||'',createdAt:row.created_at,salonId:row.salon_id,salonName:row.salon_name}},200,{'set-cookie':sessionCookie(context.request,token,remember)});
}
export function onRequest(){return json({error:'Method not allowed'},405)}
