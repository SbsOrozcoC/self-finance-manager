<template>
    <div class="dashboard-container">
      <h1>Bienvenido, {{ user?.username }}</h1>
      <p><strong>Email:</strong> {{ user?.email }}</p>
      <p><strong>Rol:</strong> {{ user?.role }}</p>
  
      <button @click="logoutUser">Cerrar sesión</button>
    </div>
  </template>
  
  <script setup lang="ts">
  import { onMounted, ref } from 'vue'
  import axios from 'axios'
  import { useRouter } from 'vue-router'
  import { getToken, logout } from '../services/auth'
  
  interface User {
    id: number
    username: string
    email: string
    is_active: boolean
    role: string
  }
  
  const user = ref<User | null>(null)
  const router = useRouter()
  
  const fetchUser = async () => {
    try {
      const token = getToken()
      const response = await axios.get('http://localhost:8000/private/me', {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      user.value = response.data
    } catch (error) {
      console.error('Error al obtener usuario:', error)
      logout()
      router.push('/')
    }
  }
  
  const logoutUser = () => {
    logout()
    router.push('/')
  }
  
  onMounted(() => {
    fetchUser()
  })
  </script>
  
  <style scoped>
  .dashboard-container {
    max-width: 500px;
    margin: 60px auto;
    text-align: center;
    padding: 30px;
    border: 1px solid #ddd;
    border-radius: 10px;
    background: #fff;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.05);
  }
  button {
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #ff5c5c;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #e04040;
  }
  </style>
  