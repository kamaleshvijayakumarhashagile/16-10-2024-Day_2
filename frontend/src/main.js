import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import Toast, { POSITION } from 'vue-toastification';
import 'vue-toastification/dist/index.css';

const app = createApp(App);

const options = {
    position: POSITION.TOP_RIGHT,
    timeout: 5000,
};

app.use(Toast, options);
app.use(router);
app.mount('#app');
