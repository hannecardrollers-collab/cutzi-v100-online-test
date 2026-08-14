import {json,parseCookies,sha256,clearSessionCookie} from '../_lib/auth.js';
export async function onRequestPost(context){const token=parseCookies(context.request).cutzi_session;if(token){const h=await sha256(token);await context.env.DB.prepare('DELETE FROM sessions WHERE token_hash=?').bind(h).run()}return json({ok:true},200,{'set-cookie':clearSessionCookie(context.request)})}
export function onRequest(){return json({error:'Method not allowed'},405)}
