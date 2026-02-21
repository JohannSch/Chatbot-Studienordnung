<script setup>
import Main from './components/main.vue'
</script>

<template>
  <main>
    <Main/>
  </main>
</template>

<style scoped>

main {
  margin: 0;
  width: 128%;
  height: 100vh;
}

@media (min-width: 1024px) {
  main {
    margin: 0 4rem;
  }
}
</style>
