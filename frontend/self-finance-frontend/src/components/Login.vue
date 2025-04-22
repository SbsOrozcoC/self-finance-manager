<template>
    <div class="login-wrapper">
      <div class="login-card">
        <h2>Iniciar sesión</h2>
        <form @submit.prevent="handleLogin">
          <input v-model="username" type="text" placeholder="Usuario" />
          <input v-model="password" type="password" placeholder="Contraseña" />
          <button type="submit">Ingresar</button>
          <p class="error" v-if="error">{{ error }}</p>
        </form>
      </div>
    </div>
  </template>
  
  <script lang="ts">
  import { defineComponent } from 'vue'
  import { login } from '../services/auth'
  import '../assets/login.css'
  
  export default defineComponent({
    name: 'LoginComponent',
    data() {
      return {
        username: '',
        password: '',
        error: ''
      }
    },
    methods: {
      async handleLogin() {
        try {
          await login(this.username, this.password)
          this.$router.push('/dashboard')
        } catch (err) {
          this.error = 'Credenciales incorrectas'
        }
      }
    }
  })
  </script>
  