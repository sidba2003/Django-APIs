<template>
    <div>
        <h1>API Client</h1>
        <pre>Response: {{ message }}</pre>
    </div>
  </template>
  
<script>
export default {
    data() {
        return {
            message: '',
        }
    },
    async mounted() {
        const response = await fetch('http://localhost:8000/api/sample/')
        const data = await response.json()
        this.message = data.message
    }
}
</script>
