import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import svgLoader from 'vite-svg-loader'

// --------------------------
// import basicSsl from '@vitejs/plugin-basic-ssl'
// --------------------------


// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(), vueJsx(), svgLoader(),
    // --------------------------
    // basicSsl()
    // --------------------------
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  server: {
    proxy: {
      '/graphql': 'http://127.0.0.1:8000',
      '/uploads': 'http://127.0.0.1:8000',
      '/admin': 'http://127.0.0.1:8000',
      '/static': 'http://127.0.0.1:8000',
    },
  },
})
