/**
 * main.js
 *
 * Bootstraps Vuetify and other plugins then mounts the App`
 */

import App from './App.vue'
import { createApp } from 'vue'
import { registerPlugins } from '@/plugins'
import router from "@/router";
import { createPinia } from 'pinia';

URLSearchParams.prototype.appendIfExists = function (key, value) {
    if (value !== null && value !== undefined) {
        this.append(key, value)
    }
};



const app = createApp(App)
app.mixin({
    methods: {
      formattedTime(iso_date_string) {
        const date = new Date(iso_date_string);
        return date.toLocaleDateString("en-US")
      }
    }
})

registerPlugins(app)
// app.use(router)
app.use(createPinia());

app.mount('#app')



