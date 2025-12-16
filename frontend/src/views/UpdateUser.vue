<script setup>
import { ref, onMounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import api from "@/services/api"

const route = useRoute()
const router = useRouter()
const form = ref({})

onMounted(async () => {
  const res = await api.get("/users/")
  form.value = res.data.find(u => u.id == route.params.id)
})

const submit = async () => {
  await api.put(`/users/${route.params.id}`, form.value)
  router.push("/dashboard")
}
</script>

<template>
  <div style="min-height:100vh;display:flex;align-items:center;justify-content:center;">
    <div class="card" style="width:460px;">
      <h2 style="text-align:center">UPDATE USER</h2>

      <input v-model="form.nama" />
      <input v-model="form.email" />
      <input v-model="form.username" />

      <button class="btn-primary" @click="submit">Update</button>
      <div class="link" @click="router.push('/dashboard')">Kembali</div>
    </div>
  </div>
</template>
