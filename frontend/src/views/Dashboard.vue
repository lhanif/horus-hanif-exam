

<script setup>
import { ref, computed, onMounted } from "vue"
import { useRouter } from "vue-router"
import api from "@/services/api"
import SearchBar from "@/components/SearchBar.vue"
import UserTable from "@/components/UserTable.vue"
import { useAuthStore } from "@/store/auth"


const users = ref([])
const keyword = ref("")
const router = useRouter()
const authStore = useAuthStore()
const fetchUsers = async () => {
  const res = await api.get("/users")
  users.value = res.data
}

onMounted(fetchUsers)

const handleSearch = (value) => {
  keyword.value = value.toLowerCase()
}

const handleLogout = async () => {
    await authStore.logout()
    router.push("/login")
}
const filteredUsers = computed(() => {
  return users.value.filter(u =>
    u.username.toLowerCase().includes(keyword.value) ||
    u.nama.toLowerCase().includes(keyword.value)
  )
})

const goToUpdate = (user) => {
  router.push({ name: "update-user", params: { id: user.id } })
}

const deleteUser = async (id) => {
  if (!confirm("Apakah Anda yakin?")) return
  await api.delete(`/users/${id}`)
  fetchUsers()
}

const user = computed(() => authStore.user)


</script>
<template>
  <div class="dashboard">
    <div class="header-container">
      <h1>DASHBOARD PENGGUNA</h1>
      
      <button @click="handleLogout" class="btn-logout">LOGOUT</button>
    </div>

    <h2 v-if="user">Hi, {{ user.nama }}</h2>
    <h2 v-else>Loading...</h2>

    <SearchBar @search="handleSearch" />

    <UserTable
      :users="filteredUsers"
      @update="goToUpdate"
      @delete="deleteUser"
    />
  </div>
</template>

<style scoped>
.dashboard {
  padding: 40px;
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
}

h1 {
  margin: 0; 
}


.btn-logout {
  background-color: #dc3545; 
  color: white;
  border: none;
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
  font-weight: bold;
  transition: background 0.3s;
}

.btn-logout:hover {
  background-color: #c82333; 
}
</style>
