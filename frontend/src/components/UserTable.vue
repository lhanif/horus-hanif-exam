<template>
  <table>
    <thead>
      <tr>
        <th>ID</th>
        <th>Username</th>
        <th>Nama</th>
        <th>Email</th>
        <th>Aksi</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.nama }}</td>
        <td>{{ user.email }}</td>
        <td class="actions">
          <button class="update" @click="$emit('update', user)">
            <i class="fa-solid fa-pen-to-square"></i>
          </button>
          <button class="delete" @click="$emit('delete', user.id)">
            <i class="fa-solid fa-trash"></i>
          </button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps({
  users: {
    type: Array,
    required: true,
  },
});
</script>

<style scoped>
table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  padding: 14px;
  text-align: left;
}

thead {
  background: #dcfce7;
}

.actions button {
  margin-right: 8px;
  padding: 6px 12px;
  border-radius: 6px;
  border: none;
  cursor: pointer;
}

.update {
  background: #22c55e;
  color: white;
}

.delete {
  background: #ef4444;
  color: white;
}
</style>
