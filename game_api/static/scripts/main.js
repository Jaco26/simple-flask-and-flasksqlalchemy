
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
    </container>
  `,
  components: {
    MenuBar,
  }
}).$mount('#app');