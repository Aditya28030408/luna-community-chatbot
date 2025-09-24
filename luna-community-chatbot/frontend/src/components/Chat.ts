import React, { useEffect, useRef, useState } from 'react'
import { api } from '../lib/api'
import Message from './Message'
import Toast from './Toast'
import RoleBadges from './RoleBadges'


export default function Chat(){
const [msgs, setMsgs] = useState<{who:string,text:string,label?:string}[]>([])
const [input, setInput] = useState('')
const [toast, setToast] = useState<string>('')
const wsRef = useRef<WebSocket | null>(null)


useEffect(()=>{
const ws = new WebSocket((location.protocol==='https:'?'wss':'ws')+`://${location.host.replace(':5173',':8000')}/ws`)
ws.onmessage = (e)=>{ /* echo demo */ }
wsRef.current = ws
return ()=> ws.close()
},[])


const send = async()=>{
if(!input.trim()) return
const text = input.trim()
const { labels } = await api.classify([text])
const label = labels?.[0] || 'casual'
setMsgs(m=>[...m, { who:'you', text, label }])
setInput('')
setToast(`Tagged as ${label}`)
setTimeout(()=>setToast(''), 1500)
}


const summarize = async()=>{
const long = msgs.map(m=>m.text).join('\n')
const { summary } = await api.summarize(long, 100)
setMsgs(m=>[...m, { who:'luna', text: summary, label: 'summary' }])
}


return (
<div className="space-y-3">
<div className="flex items-center gap-2">
<RoleBadges role="Contributor" />
<button className="btn" onClick={summarize}>Summarize Thread</button>
</div>
<div className="grid gap-3">
{msgs.map((m,i)=> <Message key={i} who={m.who} text={m.text} label={m.label} />)}
</div>
<div className="flex gap-2">
<input className="flex-1 p-3 rounded-xl bg-gray-800" value={input} onChange={e=>setInput(e.target.value)} placeholder="Type a message..." />
<button className="btn" onClick={send}>Send</button>
</div>
{toast && <Toast text={toast} />}
</div>
)
}