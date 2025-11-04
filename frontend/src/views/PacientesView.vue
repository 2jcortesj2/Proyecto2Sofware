<template>
  <div class="pacientes-container">
    <h1>Gestión de Pacientes</h1>
    
    <!-- Formulario para crear/editar -->
    <div class="form-container">
      <h2>{{ editMode ? 'Editar' : 'Crear' }} Paciente</h2>
      <form @submit.prevent="submitForm">
        <input v-model="form.paciente_id" placeholder="ID Paciente" :disabled="editMode" required />
        <input v-model="form.codigo_ingreso" placeholder="Código Ingreso" required />
        <input v-model="form.nombre" placeholder="Nombre" required />
        <input v-model="form.apellidos" placeholder="Apellidos" required />
        <input v-model="form.direccion" placeholder="Dirección" required />
        <input v-model="form.telefono" placeholder="Teléfono" required />
        <input v-model="form.insurance" placeholder="EPS" required />
        <input v-model="form.fecha_registro" type="date" required />
        
        <button type="submit">{{ editMode ? 'Actualizar' : 'Crear' }}</button>
        <button v-if="editMode" type="button" @click="cancelEdit">Cancelar</button>
      </form>
    </div>

    <!-- Lista de pacientes -->
    <div class="list-container">
      <h2>Lista de Pacientes</h2>
      <table v-if="pacientes.length > 0">
        <thead>
          <tr>
            <th>ID</th>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Teléfono</th>
            <th>EPS</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="paciente in pacientes" :key="paciente.paciente_id">
            <td>{{ paciente.paciente_id }}</td>
            <td>{{ paciente.nombre }}</td>
            <td>{{ paciente.apellidos }}</td>
            <td>{{ paciente.telefono }}</td>
            <td>{{ paciente.insurance }}</td>
            <td>
              <button @click="editPaciente(paciente)">Editar</button>
              <button @click="removePaciente(paciente.paciente_id)" class="delete">Eliminar</button>
            </td>
          </tr>
        </tbody>
      </table>
      <p v-else>No hay pacientes registrados</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { getPacientes, createPaciente, updatePaciente, deletePaciente } from '@/services/api'

const pacientes = ref([])
const editMode = ref(false)
const form = ref({
  paciente_id: '',
  codigo_ingreso: '',
  nombre: '',
  apellidos: '',
  direccion: '',
  telefono: '',
  insurance: '',
  fecha_registro: ''
})

// Cargar pacientes
const loadPacientes = async () => {
  try {
    const response = await getPacientes()
    pacientes.value = response.data.Pacientes || []
  } catch (error) {
    console.error('Error al cargar pacientes:', error)
    alert('Error al cargar pacientes')
  }
}

// Crear o actualizar
const submitForm = async () => {
  try {
    if (editMode.value) {
      await updatePaciente(form.value.paciente_id, form.value)
      alert('Paciente actualizado exitosamente')
    } else {
      await createPaciente(form.value)
      alert('Paciente creado exitosamente')
    }
    resetForm()
    loadPacientes()
  } catch (error) {
    console.error('Error:', error)
    alert('Error al guardar paciente')
  }
}

// Editar paciente
const editPaciente = (paciente) => {
  form.value = { ...paciente }
  editMode.value = true
}

// Eliminar paciente
const removePaciente = async (id) => {
  if (confirm('¿Estás seguro de eliminar este paciente?')) {
    try {
      await deletePaciente(id)
      alert('Paciente eliminado exitosamente')
      loadPacientes()
    } catch (error) {
      console.error('Error:', error)
      alert('Error al eliminar paciente')
    }
  }
}

// Cancelar edición
const cancelEdit = () => {
  resetForm()
}

// Resetear formulario
const resetForm = () => {
  form.value = {
    paciente_id: '',
    codigo_ingreso: '',
    nombre: '',
    apellidos: '',
    direccion: '',
    telefono: '',
    insurance: '',
    fecha_registro: ''
  }
  editMode.value = false
}

onMounted(() => {
  loadPacientes()
})
</script>

<style scoped>
.pacientes-container {
  padding: 20px;
  max-width: 1200px;
  margin: 0 auto;
}

.form-container, .list-container {
  background: white;
  padding: 20px;
  margin-bottom: 20px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

form {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
}

input {
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background: #42b983;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background: #359268;
}

button.delete {
  background: #e74c3c;
  margin-left: 5px;
}

button.delete:hover {
  background: #c0392b;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  padding: 12px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}

th {
  background: #f5f5f5;
  font-weight: bold;
}
</style>