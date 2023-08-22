//import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from './views/Home'
import AddTicket from '@/components/AddTicket'
import EditTicket from '@/components/EditTicket'
import IncidentList from '@/components/IncidentList.vue'
import Vue from 'vue';

Vue.use(VueRouter);

export default new VueRouter({
    mode : 'history',
    routes : [
        {   'path': '/', 
            'name' : 'Root',
            'component'  : Home,
        },
        {   'path': '/home', 
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
        {
            'path': '/tlist',
            'name' : 'IncidentList',
            'component'  : IncidentList,
            
        },
    ]
});
