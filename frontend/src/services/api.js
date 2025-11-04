import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000/api'

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// ====== PACIENTES ======
export const getPacientes = () => api.get('/pacientes/')
export const getPaciente = (id) => api.get(`/pacientes/${id}/`)
export const createPaciente = (data) => api.post('/pacientes/', data)
export const updatePaciente = (id, data) => api.put(`/pacientes/${id}/`, data)
export const deletePaciente = (id) => api.delete(`/pacientes/${id}/`)

// ====== LABORATORISTAS ======
export const getLaboratoristas = () => api.get('/laboratoristas/')
export const getLaboratorista = (id) => api.get(`/laboratoristas/${id}/`)
export const createLaboratorista = (data) => api.post('/laboratoristas/', data)
export const updateLaboratorista = (id, data) => api.put(`/laboratoristas/${id}/`, data)
export const deleteLaboratorista = (id) => api.delete(`/laboratoristas/${id}/`)

// ====== RESULTADOS ======
export const getResultados = () => api.get('/resultados/')
export const getResultado = (id) => api.get(`/resultados/${id}/`)
export const createResultado = (data) => api.post('/resultados/', data)
export const updateResultado = (id, data) => api.put(`/resultados/${id}/`, data)
export const deleteResultado = (id) => api.delete(`/resultados/${id}/`)

export default api