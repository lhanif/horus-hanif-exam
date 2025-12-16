<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/store/auth";

const username = ref("");
const password = ref("");
const error = ref("");
const router = useRouter();
const auth = useAuthStore();

const submit = async () => {
  error.value = "";
  try {
    await auth.login({
      username: username.value,
      password: password.value,
    });
    router.push("/dashboard");
  } catch (err) {
    error.value = "Username atau password salah";
  }
};
</script>

<template>
  <div
    style="
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    "
  >
    <div class="card" style="width: 420px">
      <h2 style="text-align: center; margin-bottom: 30px">LOGIN PAGE</h2>

      <div>
        <input
          v-model="username"
          placeholder="Username"
          @keyup.enter="submit"
          style="display: block; width: 100%; margin-bottom: 10px"
        />

        <input
          type="password"
          v-model="password"
          placeholder="Password"
          @keyup.enter="submit"
          style="display: block; width: 100%; margin-bottom: 10px"
        />

        <p
          v-if="error"
          style="color: red; text-align: center; margin-bottom: 10px"
        >
          {{ error }}
        </p>

        <button
          type="button"
          class="btn-primary"
          @click="submit"
          style="width: 100%"
        >
          LOGIN
        </button>
      </div>

      <div
        class="link"
        @click="$router.push('/register')"
        style="text-align: center; margin-top: 15px; cursor: pointer"
      >
        Belum memiliki akun? Daftar Sekarang
      </div>
    </div>
  </div>
</template>
