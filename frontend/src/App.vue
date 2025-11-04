<template>
  <div id="app">
    <nav>
      <router-link to="/pacientes">Pacientes</router-link>
      <router-link to="/laboratoristas">Laboratoristas</router-link>
      <router-link to="/resultados">Resultados</router-link>
    </nav>
    <router-view />
  </div>
</template>

<script setup>
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

nav {
  background: #42b983;
  padding: 20px;
  display: flex;
  gap: 20px;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
  padding: 10px 20px;
  border-radius: 4px;
  transition: background 0.3s;
}

nav a:hover,
nav a.router-link-active {
  background: rgba(255, 255, 255, 0.2);
}
</style>