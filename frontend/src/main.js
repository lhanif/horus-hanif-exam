import { createApp } from "vue"
import { createPinia } from "pinia"

import App from "./App.vue"
import router from "./router"
import "./assets/main.css"

// const authStore = useAuthStore()
// onMounted(() => {
//   if (authStore.user) {
//     authStore.fetchUser()
//   }
// })

createApp(App)
  .use(createPinia())
  .use(router)
  .mount("#app")
