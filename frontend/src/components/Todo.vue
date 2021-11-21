<template>
  <h1> My TODO List</h1>
  <ul v-if="list">
    <li v-for="(l, index) in list" :key="index">
      <h2> {{l.title}}</h2>
      <p> {{l.description}} </p>
      </li>
  </ul>
</template>

<script>
import axios from '../plugins/axios_plugin'
export default {
  data() {
    return {
      list: [],
    }
  },
  mounted() {
    axios.get('http://127.0.0.1:8000/api/')
    .then(response => {
      this.list = response.data
    })
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
