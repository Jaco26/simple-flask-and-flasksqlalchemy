
const DropDown = {
  template: //html
  `<div class="dropdown" @mouseleave="show = false">
      <button @mouseenter="show = true" class="btn btn-light dropdown-toggle">
        Options
      </button>
      <div v-if="show" class="dropdown-menu">
        <div 
          v-for="(item, i) in menuItems"
          :key="i"  
          @click="item.action"
          class="dropdown-item pointer"
        >
          {{item.text}}
        </div>
      </div>
    </div>
  `,
  props: {
    menuItems: Array,
  },
  data: function() {
    return {
      show: false,
    }
  },
}

const MenuBar = {
  template: //html
  `
    <row>
      <nav class="col navbar navbar-light bg-light">
        <DropDown :menuItems="menuItems" />
      </nav>
    </row>
  `,
  components: {
    DropDown,
  },
  data: function() {
    return {
      showMenu: false,
      menuItems: [
        {
          text: 'Add Player',
          action: this.showAddPlayer,
        }
      ]
    }
  },
  methods: {
    showAddPlayer() {
      console.log('show add player form');
      
    }
  }
};

const PlayerList = {
  template: //html
  ` <row>
      <ul class="list-group col">
        <li 
          class="list-group-item" 
          v-for="item in users" 
          :key="item.id"
          @dblclick="deletePlayer(item.id)"
        >{{item.name}}</li>
      </ul>
    </row>
  `,
  props: {
    users: Array,
    deletePlayer: Function,
  },
};

const NewPlayer = {
  template: //html
  ` <row>
      <form @submit.prevent="handleSubmit" class="col">
        <div class="form-group">
          <label for="new-player">New Player</label>
          <input 
            type="text" 
            class="form-control" 
            id="new-player" 
            placeholder="Player name" 
            v-model="newPlayer"
          >
          <small class="form-text text-muted">Enter the name of a new player</small>
        </div>
      </form>
    </row>
  `,
  props: {
    addPlayer: Function,
  },
  data: function() {
    return {
      newPlayer: '',
    }
  },
  methods: {
    handleSubmit() {
      this.addPlayer(this.newPlayer);
      this.newPlayer = '';
    }
  }

}


const app = new Vue({
  template: //html
  `
    <container fill-height> 
      <MenuBar />
      <NewPlayer :addPlayer="addPlayer" />
      <PlayerList :users="users" :deletePlayer="deletePlayer" />
    </container>
  `,
  components: {
    MenuBar,
    PlayerList,
    NewPlayer,
  }, 
  data: function() {
    return {
      users: [],
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
          this.users = res.data.users
        })
        .catch(err => {
          console.log(err);
          
        })
    },
    addPlayer: function(player) {
      console.log(player);
      
      axios.post('/user', { name: player})
        .then(res => {
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