import {json,getSession,accountFromRow} from '../_lib/auth.js';
export async function onRequestGet(context){const s=await getSession(context);if(!s)return json({error:'Niet ingelogd.'},401);return json({account:accountFromRow(s)})}
export function onRequest(){return json({error:'Method not allowed'},405)}
