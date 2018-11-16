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
    <div class="col" :class="classObj">
      <slot></slot>
    </div>
  `,
  props: {
    'd-flex': Boolean,
    'justify-start': Boolean,
    'justify-end': Boolean,
    'justify-center': Boolean,
    'justify-between': Boolean,
    'justify-around': Boolean,
    'justify-sm-start': Boolean,
    'justify-sm-end': Boolean,
    'justify-sm-center': Boolean,
    'justify-sm-between': Boolean,
    'justify-sm-around': Boolean,
    'justify-md-start': Boolean,
    'justify-md-end': Boolean,
    'justify-md-center': Boolean,
    'justify-md-between': Boolean,
    'justify-md-around': Boolean,
    'justify-lg-start': Boolean,
    'justify-lg-end': Boolean,
    'justify-lg-center': Boolean,
    'justify-lg-between': Boolean,
    'justify-lg-around': Boolean,
    'justify-xl-start': Boolean,
    'justify-xl-end': Boolean,
    'justify-xl-center': Boolean,
    'justify-xl-between': Boolean,
    'justify-xl-around': Boolean,
    'align-start': Boolean,
    'align-end': Boolean,
    'align-center': Boolean,
    'align-baseline': Boolean,
    'align-stretch': Boolean,
    'align-sm-start': Boolean,
    'align-sm-end': Boolean,
    'align-sm-center': Boolean,
    'align-sm-baseline': Boolean,
    'align-sm-stretch': Boolean,
    'align-md-start': Boolean,
    'align-md-end': Boolean,
    'align-md-center': Boolean,
    'align-md-baseline': Boolean,
    'align-md-stretch': Boolean,
    'align-lg-start': Boolean,
    'align-lg-end': Boolean,
    'align-lg-center': Boolean,
    'align-lg-baseline': Boolean,
    'align-lg-stretch': Boolean,
    'align-xl-start': Boolean,
    'align-xl-end': Boolean,
    'align-xl-center': Boolean,
    'align-xl-baseline': Boolean,
    'align-xl-stretch': Boolean,
    'align-self-start': Boolean,
    'align-self-end': Boolean,
    'align-self-center': Boolean,
    'align-self-baseline': Boolean,
    'align-self-stretch': Boolean,
    'align-self-sm-start': Boolean,
    'align-self-sm-end': Boolean,
    'align-self-sm-center': Boolean,
    'align-self-sm-baseline': Boolean,
    'align-self-sm-stretch': Boolean,
    'align-self-md-start': Boolean,
    'align-self-md-end': Boolean,
    'align-self-md-center': Boolean,
    'align-self-md-baseline': Boolean,
    'align-self-md-stretch': Boolean,
    'align-self-lg-start': Boolean,
    'align-self-lg-end': Boolean,
    'align-self-lg-center': Boolean,
    'align-self-lg-baseline': Boolean,
    'align-self-lg-stretch': Boolean,
    'align-self-xl-start': Boolean,
    'align-self-xl-end': Boolean,
    'align-self-xl-center': Boolean,
    'align-self-xl-baseline': Boolean,
    'align-self-xl-stretch': Boolean,
  },
  computed: {
    classObj: function() {
      return Object.keys(this.$props).reduce((a, b) => {
        const capsRe = /[A-Z]/g;
        if (this.$props[b]) {          
          const capsIs = b.split('').map((c, i) => capsRe.test(c) ? i : '').filter(c => c);
          let newB = capsIs.reduce((accum, capI) => {            
            accum = accum.replace(b[capI], `-${b[capI].toLowerCase()}`);            
            return accum;
          }, b);
          if (newB.includes('align-self')) {
            newB = newB;
          } else if (b.includes('justify')) {
            newB = 'justify-content' + newB.slice(newB.indexOf('y') + 1).toLowerCase();
          } else if (newB === 'd-flex') {
            newB = newB
          } else {
            newB = 'align-items' + newB.slice(newB.indexOf('n') + 1).toLowerCase();
          }
          a[newB] = newB;          
        }
        return a;
      }, {})
    }
  }
})


// Vue.component('container', {
//   template: //html
//   `
//     <div :class="classObj">
//       <slot></slot>
//     </div>
//   `,
//   props: {
//     'fillHeight': Boolean 
//   },
//   computed: {
//     classObj: function() {
//       return {
//         'fill-height': this.fillHeight,
//         container: true,
//       };
//     },
//   },
// });


// Vue.component('row', {
//   template: //html
//   `
//     <div class="row" :style="styleObj">
//       <slot></slot>
//     </div>
//   `,
//   props: {
//     m: String,
//     p: String,
//     height: {
//       default: 0,
//     },
//     width: {
//       default: 0,
//     },
//     justifyStart: Boolean,
//     justifyEnd: Boolean,
//     justifyCenter: Boolean,
//     alignStart: Boolean,
//     alignEnd: Boolean, 
//     alignCenter: Boolean,
//   },
//   computed: {
//     styleObj: function() {
//       const margin = this.m ? this.m.split(' ').map(item => item += 'px').join(' ') : '';
//       const padding = this.p ? this.p.split(' ').map(item => item += 'px').join(' ') : '';
//       const justifyContent = this.justifyCenter ? 'center' : this.justifyEnd ? 'flex-end' : this.justifyStart ? 'flex-start' : '';
//       const alignItems = this.alignCenter ? 'center' : this.alignEnd ? 'flex-end' : this.alignStart ? 'flex-start' : '';
//       return {
//         height: Number(this.height) + 'px',
//         widht: Number(this.width) + 'px',
//         margin,
//         padding,
//         justifyContent,
//         alignItems,
//       };
//     },
//   },
// });

// Vue.component('flex', {
//   template: //html
//   `
//     <div :style="styleObj">
//       <slot></slot>
//     </div>
//   `,
//   props: {
//     m: String,
//     p: String,
//     f: {
//       default: 1,
//     },
//     justifyStart: Boolean,
//     justifyEnd: Boolean,
//     justifyCenter: Boolean,
//     alignStart: Boolean,
//     alignEnd: Boolean, 
//     alignCenter: Boolean,
//     dFlex: Boolean,
//   },
//   computed: {
//     styleObj: function() {
//       const margin = this.m ? this.m.split(' ').map(item => item += 'px').join(' ') : '';
//       const padding = this.p ? this.p.split(' ').map(item => item += 'px').join(' ') : '';
//       const justifyContent = this.justifyCenter ? 'center' : this.justifyEnd ? 'flex-end' : this.justifyStart ? 'flex-start' : '';
//       const alignItems = this.alignCenter ? 'center' : this.alignEnd ? 'flex-end' : this.alignStart ? 'flex-start' : '';
//       return {
//         display: this.dFlex ? 'flex' : '',
//         margin,
//         padding,
//         flex: this.f + ' 1 auto',
//         justifyContent,
//         alignItems
//       };
//     },
//   },
// });
