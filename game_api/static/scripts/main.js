
const MenuBar = {
  template: //html
  `
    <div>
      <row align-center height="50">
        <flex d-flex justify-center> <h1>Hello</h1></flex>
      </row>
    </div>
  `,
};

const app = new Vue({
  template: //html
  `
    <container fill-height> 
      <MenuBar />
      <row>
        <flex f="3"></flex>
        <flex height="50" style="background-color: blue;">
          <ul style="list-style: none;">
            <li v-for="(item, i) in user" :key="i" @dblclick="deletePlayer(item.id)">{{item.name}}</li>
          </ul>
          <input type="text" v-model="newPlayer" />
          <button @click="addPlayer">Add</button>
        </flex>
      </row>
    </container>
  `,
  components: {
    MenuBar,
  }, 
  data: function() {
    return {
      user: '',
      newPlayer: ''
    };
  },
  mounted: function() {
    this.getPlayers();
  },
  methods: {
    ...apiCalls(),
  }
}).$mount('#app');



function apiCalls() {
  return {
    getPlayers: function() {
      return axios.get('/user')
        .then(res => {
          console.log(res);
          
          this.user = res.data.users
          
        })
        .catch(err => {
          console.log(err);
          
        })
    },
    addPlayer: function() {
      axios.post('/user', { name: this.newPlayer })
        .then(res => {
          this.newPlayer = '';
          this.getPlayers();
        })
        .catch(err => {
          console.log(err);
        });
    },
    deletePlayer: function(id) {
      axios.delete('/user/' + id)
        .then(() => this.getPlayers())
        .catch(err => {
          console.log(err);
          
        });
    }
  }
}