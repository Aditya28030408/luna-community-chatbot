import axios from 'axios'
const base = import.meta.env.VITE_API_BASE || 'http://localhost:8000'


export const api = {
classify: (messages: string[]) => axios.post(`${base}/classify/`, { messages }).then(r=>r.data),
summarize: (text: string, max_words=120) => axios.post(`${base}/summarize/`, { text, max_words }).then(r=>r.data),
createPoll: (question: string, options: string[]) => axios.post(`${base}/polls/create`, { question, options }).then(r=>r.data),
vote: (poll_id: string, option: number) => axios.post(`${base}/polls/vote`, { poll_id, option }).then(r=>r.data),
getPoll: (poll_id: string) => axios.get(`${base}/polls/${poll_id}`).then(r=>r.data),
trends: () => axios.get(`${base}/trends/`).then(r=>r.data),
}