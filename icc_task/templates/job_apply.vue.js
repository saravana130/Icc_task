var jobaplly = {
    
	data () {
		return {
            id: this.$route.params.jobid,
            state:null
           
		}
	  },
	  mounted () {
		axios
		  .get('http://127.0.0.1:8000/job/'+this.id+'/apply')
          .then(response => (this.state = response.data))
          self.$router.push('/');
	  }
}