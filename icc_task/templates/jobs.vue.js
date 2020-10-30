var List = {
	data () {
		return {
		  data:null
		}
	  },
	  mounted () {
		axios
		  .get('http://127.0.0.1:8000/jobs?limit=100')
		  .then(response => (this.data = response.data))
	  },
	
	  template: '<template> <section className="section">'+
	  '<div className="container">'+
		  '<div className="row">'+
			  '<div  className="col s12">'+
				 '<h5 className="center">Jobs</h5>'+
				 '<div v-for="state in data" className="card-panel">'+
					 '<div>'+
					 '<div class="divider #26c6da cyan lighten-1"></div>'+
					//  '<router-link to=/job/state.id>'+
					 '<router-link :to="{ name: '+'job'+', params: { job_id:state.id } }">'+
						 '<p><b>{{state.jobTitel}}</b></p>'+
						 '<p><b>{{state.ShortDescription}}</b></p>'+		 				 
						 '<div className="row">'+
							 '<div className="col s12 m6 offset-m3">'+
								 '<table>'+
									 
									 '<tbody>'+
										 '<tr>'+
											 '<td>Job Location</td>'+
											 '<td>{{state.job_location}}</td>'+
										 '</tr>'+
										
									 '</tbody>'+
								 '</table>'+
							 '</div>'+
						 '</div>'+
						 '<div className="center">'+
						 '</router-link >'+
							
						 '</div>'+
					 '</div>'+
				 '</div>'+
			  '</div>'+
		  '</div>'+
	  '</div>'+
 '</section> </template>'
	 
  };
