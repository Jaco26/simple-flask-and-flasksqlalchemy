Vue.component('container', {
  template: //html
  `
    <div :class="classObj">
      <slot></slot>
    </div>
  `,
  props: {
    'fillHeight': Boolean 
  },
  computed: {
    classObj: function() {
      return {
        'fill-height': this.fillHeight,
        container: true,
      };
    },
  },
});


Vue.component('row', {
  template: //html
  `
    <div class="row" :style="styleObj">
      <slot></slot>
    </div>
  `,
  props: {
    m: String,
    p: String,
    height: {
      default: 0,
    },
    width: {
      default: 0,
    },
    justifyStart: Boolean,
    justifyEnd: Boolean,
    justifyCenter: Boolean,
    alignStart: Boolean,
    alignEnd: Boolean, 
    alignCenter: Boolean,
  },
  computed: {
    styleObj: function() {
      const margin = this.m ? this.m.split(' ').map(item => item += 'px').join(' ') : '';
      const padding = this.p ? this.p.split(' ').map(item => item += 'px').join(' ') : '';
      const justifyContent = this.justifyCenter ? 'center' : this.justifyEnd ? 'flex-end' : this.justifyStart ? 'flex-start' : '';
      const alignItems = this.alignCenter ? 'center' : this.alignEnd ? 'flex-end' : this.alignStart ? 'flex-start' : '';
      return {
        height: Number(this.height) + 'px',
        widht: Number(this.width) + 'px',
        margin,
        padding,
        justifyContent,
        alignItems,
      };
    },
  },
});

Vue.component('flex', {
  template: //html
  `
    <div :style="styleObj">
      <slot></slot>
    </div>
  `,
  props: {
    m: String,
    p: String,
    f: {
      default: 1,
    },
    justifyStart: Boolean,
    justifyEnd: Boolean,
    justifyCenter: Boolean,
    alignStart: Boolean,
    alignEnd: Boolean, 
    alignCenter: Boolean,
    dFlex: Boolean,
  },
  computed: {
    styleObj: function() {
      const margin = this.m ? this.m.split(' ').map(item => item += 'px').join(' ') : '';
      const padding = this.p ? this.p.split(' ').map(item => item += 'px').join(' ') : '';
      const justifyContent = this.justifyCenter ? 'center' : this.justifyEnd ? 'flex-end' : this.justifyStart ? 'flex-start' : '';
      const alignItems = this.alignCenter ? 'center' : this.alignEnd ? 'flex-end' : this.alignStart ? 'flex-start' : '';
      return {
        display: this.dFlex ? 'flex' : '',
        margin,
        padding,
        flex: this.f + ' 1 auto',
        justifyContent,
        alignItems
      };
    },
  },
});
