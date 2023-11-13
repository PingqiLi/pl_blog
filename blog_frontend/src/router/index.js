import { createRouter, createWebHistory } from 'vue-router'
import Default from '@/layouts/Default.vue'
import Home from '@/views/Home.vue'
import ArticleDetail from '@/views/ArticleDetail.vue'
import SignUp from '@/views/SignUp.vue'
import SignIn from '@/views/SignIn.vue'
import ResetPwd from '@/views/ResetPwd.vue'
import UserProfile from '@/views/UserProfile.vue'

const routes = [
    {
        path: '/',
        component: Default,
        children: [{
            path: '',
            name: 'Home',
            component: Home,
        }],
    },
    {
        path: "/article",
        component: Default,
        children: [{
            path: ':id',
            name: 'ArticleDetail',
            component: ArticleDetail,
        }],
    },
    {
        path: "/account/signup",
        name: 'SignUp',
        component: SignUp,
    },
    {
        path: "/account",
        component: Default,
        children: [
        {
            path: '/account/signin',
            name: 'SignIn',
            component: SignIn,
        },
        {
            path: '/account/reset-password',
            name: 'ResetPassword',
            component: ResetPwd,  // Ensure to import ResetPwd at the top of your file
        }
    ],
    },
    {
        path: "/userProfile",
        name: 'UserProfile',
        component: Default,
        children: [{
            path: ':id',
            component: UserProfile,
        }],
    }
];


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
})

export default router
