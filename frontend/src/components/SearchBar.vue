<template>
  <div class="search-bar">
    <input
      v-model="keyword"
      type="text"
      placeholder="Cari berdasarkan nama atau username"
    />
    <button @click="emitSearch">Cari</button>
  </div>
</template>

<script setup>
import { ref } from "vue"

const keyword = ref("")
const emit = defineEmits(["search"])

const emitSearch = () => {
  emit("search", keyword.value)
}
</script>

<style scoped>
.search-bar {
  display: flex;
  gap: 12px;
  margin-bottom: 24px;
}

input {
  flex: 1;
  padding: 12px 18px;
  border-radius: 999px;
  border: 1px solid #bbf7d0;
  outline: none;
}

button {
  padding: 0px 24px;
  border-radius: 999px;
  border: 1px solid transparent;
  background: #22c55e;
  color: white;
  cursor: pointer;
  height: auto;
  margin-bottom:20px;
}
</style>    