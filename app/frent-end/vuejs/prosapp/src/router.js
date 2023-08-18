//import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home'
import AddTicket from '@/components/AddTicket'
import EditTicket from '@/components/EditTicket'
import Vue from 'vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode : 'history',
    routes : [
        {   'path': '/', 
            'name' : 'Home',
            'component'  : Home,
        },
        {   'path': '/add', 
            'name' : 'AddTicket',
            'component'  : AddTicket,
            
        },
        {
            'path': '/edit/:ticketId', 
            'name' : 'EditTicket',
            'component'  : EditTicket,
            
        },
    ]
});
