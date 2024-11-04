import { createRouter, createWebHistory } from 'vue-router';
import Login from '../components/LoginPage.vue';
import Signup from '../components/SignupPage.vue';
import Upload from '../components/UploadPage.vue';
import DisplayPage from '../components/DisplayPage.vue';

const routes = [
    { path: '/display', component: DisplayPage }, 
    { path: '/login', component: Login }, 
    { path: '/signup', component: Signup },
    { path: '/upload', component: Upload },
    { path: '/', redirect: '/login' },
    { path: '/upload/:username', component: Upload },
  
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
