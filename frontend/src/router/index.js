import { createRouter, createWebHistory } from "vue-router"
import Login from "@/views/Login.vue"
import Register from "@/views/Register.vue"
import Dashboard from "@/views/Dashboard.vue"
import UpdateUser from "@/views/UpdateUser.vue"

const routes = [
  { path: "/", redirect: "/login", },
  { path: "/login", component: Login , name:"login"},
  { path: "/register", component: Register ,name:"register"},
  { path: "/dashboard", component: Dashboard, name:"dashboard",meta: { requiresAuth: true } },
  { path: "/update/:id", component: UpdateUser, name:"update-user", meta: { requiresAuth: true } },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = localStorage.getItem('user')

  if (to.meta.requiresAuth && !isAuthenticated) {
    next('/login')
  } else if (to.path === '/login' && isAuthenticated) {
    next('/dashboard') 
  } else {
    next()
  }
})

export default router
