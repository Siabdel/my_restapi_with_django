import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home'
import Login from './views/Login'
import AddPost from './views/AddPost'
import Post from './views/Post'

Vue.use(VueRouter);

export default new VueRouter({
    mode : 'history',
    routes : [
        {   'path': '/', 
            'name' : 'Home',
            'component'  : Home,
        },
        {   'path': '/login', 
            'name' : 'Login',
            'component'  : Login,
        },
        {   'path': '/add', 
            'name' : 'AddPost',
            'component'  : AddPost,
        },
        {   'path': '/get/:postId', 
            'name' : 'UPost',
            'component' : Post,
        },
    ]
});
