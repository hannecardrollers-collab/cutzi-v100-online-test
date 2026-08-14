import {json,readJson,randomSalt,passwordHash,randomToken,sha256,sessionCookie} from '../_lib/auth.js';
export async function onRequestPost(context){
  const b=await readJson(context.request);if(!b)return json({error:'Ongeldige aanvraag.'},400);
  const fullName=String(b.fullName||'').trim(),email=String(b.email||'').trim().toLowerCase(),password=String(b.password||''),salonName=String(b.salonName||'').trim(),phone=String(b.phone||'').trim(),remember=b.remember!==false;
  if(fullName.length<2||!/^\S+@\S+\.\S+$/.test(email)||password.length<8||!/\d/.test(password)||!salonName)return json({error:'Controleer naam, e-mail, wachtwoord en salonnaam.'},400);
  const exists=await context.env.DB.prepare('SELECT id FROM users WHERE email=? LIMIT 1').bind(email).first();if(exists)return json({error:'Er bestaat al een account voor dit e-mailadres.'},409);
  const now=new Date().toISOString(),salonId=crypto.randomUUID(),userId=crypto.randomUUID(),salt=randomSalt(),hash=await passwordHash(password,salt),token=randomToken(),tokenHash=await sha256(token),expiry=new Date(Date.now()+(remember?30:0.5)*86400000).toISOString();
  await context.env.DB.batch([
    context.env.DB.prepare('INSERT INTO salons(id,name,created_at) VALUES(?,?,?)').bind(salonId,salonName,now),
    context.env.DB.prepare('INSERT INTO users(id,email,full_name,phone,role,password_hash,password_salt,salon_id,created_at) VALUES(?,?,?,?,?,?,?,?,?)').bind(userId,email,fullName,phone,'',hash,salt,salonId,now),
    context.env.DB.prepare('INSERT INTO salon_state(salon_id,state_json,revision,updated_at) VALUES(?,?,0,?)').bind(salonId,'{}',now),
    context.env.DB.prepare('INSERT INTO sessions(token_hash,user_id,created_at,expires_at) VALUES(?,?,?,?)').bind(tokenHash,userId,now,expiry)
  ]);
  return json({account:{id:userId,email,fullName,phone,role:'',createdAt:now,salonId,salonName},revision:0},201,{'set-cookie':sessionCookie(context.request,token,remember)});
}
export function onRequest(){return json({error:'Method not allowed'},405)}
