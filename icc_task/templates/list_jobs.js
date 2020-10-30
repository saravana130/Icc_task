var List = Vue.extend({
    template: '#Jobs-list',
    data () {
        return {
          jobs: null
        }
      },
      mounted () {
        axios
          .get('http://127.0.0.1:8000/jobs?limit=100')
          .then(response => (this.jobs = response))
      }
  });


//   var router = new VueRouter({
//     routes: [{path: '/', component: List},
//     //   {path: '/invoice/:invoice_id', component: invoice, name: 'invoice'},
//     //   {path: '/invoice-add', component: Addinvoice},
//     //   {path: '/invoice/:invoice_id/edit', component: invoiceEdit, name: 'invoice-edit'},
//     // {path:   '/invoice/:invoice_id/delete', component: invoiceDelete, name: 'invoice-delete'}
//   ]});
  
//   new Vue({
//     el: '#app',
//     router: router,
//     template: '<router-view></router-view>'
//   });
  
new Vue({
    el: '#app',
    data () {
      return {
        info: null
      }
    },
    mounted () {
      axios
        .get('http://127.0.0.1:8000/jobs?limit=100')
        .then(response => (this.info = response.data))
    }
  })


  