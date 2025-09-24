import React, { useState } from 'react'
import { api } from '../lib/api'


export default function PollWidget(){
const [qid, setQid] = useState<string | null>(null)
const [poll, setPoll] = useState<any>(null)
const [q, setQ] = useState('What should we build next?')
const [opts, setOpts] = useState('Feature A, Feature B, Bug Bash')


const create = async() => {
const res = await api.createPoll(q, opts.split(',').map(s=>s.trim()))
setQid(res.poll_id)
setPoll(await api.getPoll(res.poll_id))
}
const vote = async(i:number)=>{
if(!qid) return
await api.vote(qid, i)
setPoll(await api.getPoll(qid))
}
return (
<div className="card space-y-2">
{!qid ? (
<>
<input className="w-full p-2 rounded bg-gray-800" value={q} onChange={e=>setQ(e.target.value)} />
<input className="w-full p-2 rounded bg-gray-800" value={opts} onChange={e=>setOpts(e.target.value)} />
<button className="btn" onClick={create}>Create Poll</button>
</>
) : (
<div>
<div className="text-lg font-semibold">{poll.q}</div>
<div className="mt-2 grid gap-2">
{poll.opt.map((o:string, i:number)=> (
<button key={i} className="btn flex justify-between" onClick={()=>vote(i)}>
<span>{o}</span>
<span className="badge">{poll.votes[i]}</span>
</button>
))}
</div>
</div>
)}
</div>
)
}