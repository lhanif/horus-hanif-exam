import { fileURLToPath, URL } from "node:url";

import { defineConfig, loadEnv } from "vite"; 
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";


export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), '');
  return {
    plugins: [vue(), vueDevTools()],
    resolve: {
      alias: {
        "@": fileURLToPath(new URL("./src", import.meta.url)),
      },
    },
    server: {
      proxy: {
        "/api": {
          // 4. Panggil variable dari env
          target: env.VITE_API_URL,
          changeOrigin: true,
          secure: false,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
  };
});