
var job = {
    
	data () {
		return {
            id: this.$route.params.job_id,
            state:null
           
		}
	  },
	  mounted () {
		axios
		  .get('http://127.0.0.1:8000/job/'+this.id+'')
		  .then(response => (this.state = response.data))
	  },
	  template: '<template> <section className="section">'+
	  '<div className="container">'+
		  '<div className="row">'+
		//   '<router-link to=/jobapply/state.id>'+
		//   '<router-link :to="{ name: '+'jobapply'+', params: { jobid:state.id } }">'+
		  '<a class="waves-effect waves-light btn right">Apply</a>'+
		//   '</router-link >'+
			  '<div  className="col s12">'+
				 '<h5 className="center">{{state.jobTitel}}</h5>'+
				
				 '<div  className="card-panel">'+
					 '<div>'+
					 '<div class="divider #26c6da cyan lighten-1"></div>'+
				                      
						 '<p><b>{{state.ShortDescription}}</b></p>'+
						 '<p><b>Job Description : </b>{{state.job_Description}}</p>'+
						 				 
						 '<div className="row">'+
							 '<div className="col s12 m6 offset-m3">'+
								 '<table>'+
									 
									 '<tbody>'+
										 '<tr>'+
											 '<td>Job Location</td>'+
											 '<td>{{state.job_location}}</td>'+
										 '</tr>'+
										 '<tr>'+
											 '<td>Walkin Date</td>'+
											 '<td>{{state.walkin_date}}</td>'+
										 '</tr>'+
										 '<tr>'+
											 '<td>Emplayment Type</td>'+
											 '<td>{{state.employment_type}}</td>'+
										 '</tr>'+
									
									 '</tbody>'+
								 '</table>'+
							 '</div>'+
						 '</div>'+
						 '<div className="center">'+
						 '</div>'+
					 '</div>'+
				 '</div>'+
			  '</div>'+
		  '</div>'+
	  '</div>'+
 '</section> </template>'
	 
  };
