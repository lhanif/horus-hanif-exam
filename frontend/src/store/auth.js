import { defineStore } from "pinia";
import api from "@/services/api";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    user: JSON.parse(localStorage.getItem("user")) || null,
  }),

  getters: {
    isAuthenticated: (state) => !!state.user,
  },

  actions: {
    async login(payload) {
      const res = await api.post("/users/login", payload);

      this.user = res.data.user;
      localStorage.setItem("user", JSON.stringify(this.user));
    },

    async logout() {
      try {
        await api.post("/users/logout");
      } catch (error) {
        console.error("Gagal logout di server:", error);
      } finally {
        this.user = null;
        localStorage.removeItem("user");
        
        localStorage.removeItem("token"); 
        
      }
    },

    async fetchUser() {
      try {
        const res = await api.get("/users/me");
        this.user = res.data;
        localStorage.setItem("user", JSON.stringify(this.user));
      } catch (error) {
        this.user = null;
        localStorage.removeItem("user");
      }
    },
  },
});