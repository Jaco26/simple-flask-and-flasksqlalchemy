Vue.component('container', {
  template: //html
  `
    <div :class="classObj">
      <slot></slot>
    </div>
  `,
  props: {
    fillHeight: Boolean,
  },
  computed: {
    classObj: function() {
      return this.fillHeight ? 'container-fluid fill-height' : 'container'
    }
  }
});

Vue.component('row', {
  template: //html
  `
    <div class="row">
      <slot></slot>
    </div>
  `,
});

Vue.component('b-col', {
  template: //html
  `
    <div class="col">
      <slot></slot>
    </div>
  `,
});
