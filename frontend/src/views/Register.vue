<script setup>
import { ref } from "vue"
import { useRouter } from "vue-router"
import api from "@/services/api"

const router = useRouter()
const error = ref("")
const form = ref({
  nama: "",
  email: "",
  username: "",
  password: ""
})

const submit = async () => {
  error.value = ""

  if (!form.value.nama || !form.value.email || !form.value.username || !form.value.password) {
    error.value = "Semua field wajib diisi"
    return
  }

  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(form.value.email)) {
    error.value = "Format email tidak valid"
    return
  }

  try {
    await api.post("/users/register/", form.value)
    router.push("/login")
  } catch (err) {
    error.value = err.response?.data?.message || "Registrasi gagal (username/email sudah digunakan)"
  }
}


</script>

<template>
  <div style="min-height:100vh;display:flex;align-items:center;justify-content:center;">
    <div class="card" style="width:460px;">
      <h2 style="text-align:center;margin-bottom:30px;">REGISTRASI AKUN</h2>

      <input v-model="form.nama" placeholder="Nama Lengkap" />
      <input v-model="form.email" placeholder="Email" />
      <input v-model="form.username" placeholder="Username" />
      <input v-model="form.password" type="password" placeholder="Password" />

      <p v-if="error" style="color:red;text-align:center">{{ error }}</p>

      <button class="btn-primary" @click="submit">REGISTRASI</button>
    <div class="link" @click="$router.push('/login')">
        Kembali ke login
      </div>
    </div>
  </div>
</template>
