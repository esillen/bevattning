(window.webpackJsonp=window.webpackJsonp||[]).push([[0],[,,,,,,,,function(e,t,n){e.exports=n.p+"static/media/watering.76cf0a92.gif"},function(e,t,n){e.exports=n(18)},,,,,,function(e,t,n){},function(e,t,n){e.exports=n.p+"static/media/logo.5d5d9eef.svg"},function(e,t,n){},function(e,t,n){"use strict";n.r(t);var a=n(0),o=n.n(a),r=n(7),c=n.n(r),i=(n(15),n(16),n(8)),l=n.n(i),s=(n(17),n(1)),u=n(2),d=n(4),h=n(3),m=n(5),v=function(e){function t(e){return Object(s.a)(this,t),Object(d.a)(this,Object(h.a)(t).call(this,e))}return Object(m.a)(t,e),Object(u.a)(t,[{key:"switchValve",value:function(e){var t=this,n="https://rosenhillgarden.pythonanywhere.com/valve/"+this.props.id+"/action";n+=!0===e?"/on":"/off",fetch(n).then(function(e){return t.props.valves.reloadValves()})}},{key:"render",value:function(){var e=this;return o.a.createElement("div",null,this.props.state?"on":"off",o.a.createElement("button",{onClick:function(){return e.switchValve(!0)}},"Turn On"),o.a.createElement("button",{onClick:function(){return e.switchValve(!1)}},"Turn Off"))}}]),t}(o.a.Component),f=function(e){function t(e){var n;return Object(s.a)(this,t),(n=Object(d.a)(this,Object(h.a)(t).call(this,e))).state={error:null,isLoaded:!1,valves:null},n}return Object(m.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){this.reloadValves()}},{key:"reloadValves",value:function(){var e=this;fetch("https://rosenhillgarden.pythonanywhere.com/valve").then(function(e){return e.json()}).then(function(t){e.setState({isLoaded:!0,valves:t.valves})},function(t){e.setState({isLoaded:!0,error:t})})}},{key:"render",value:function(){var e=this,t=this.state,n=t.error,a=t.isLoaded,r=t.valves;return n?o.a.createElement("div",null,"Error: ",n.message):a?o.a.createElement("ul",null,r.map(function(t){return o.a.createElement("li",{key:t.id},o.a.createElement(v,{id:t.id,state:t.state,valves:e}))})):o.a.createElement("div",null,"Loading...")}}]),t}(o.a.Component),p=function(e){function t(e){var n;return Object(s.a)(this,t),(n=Object(d.a)(this,Object(h.a)(t).call(this,e))).state={error:null,isLoaded:!1,randomImageUrl:null},n}return Object(m.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){this.loadRandomImage()}},{key:"loadRandomImage",value:function(){var e=this;console.log("hejj");var t=Math.floor(20*Math.random()),n="https://api.giphy.com/v1/gifs/search?api_key=".concat("aFFKTuSMjd6j0wwjpFCPXZipQbcnw3vB","&q=").concat("water","&limit=").concat(1,"&offset=").concat(t,"&rating=").concat("g","&lang=").concat("en","&fmt=").concat("json");fetch(n).then(function(e){return e.json()}).then(function(t){console.log(t.data[0].images),e.setState({isLoaded:!0,randomImageUrl:t.data[0].images.original.url})},function(t){e.setState({isLoaded:!0,error:t})})}},{key:"render",value:function(){var e=this.state,t=(e.error,e.isLoaded,e.randomImageUrl);return o.a.createElement("div",null,o.a.createElement("img",{src:t}))}}]),t}(o.a.Component);var g=function(){return o.a.createElement("div",{className:"App"},o.a.createElement("header",{className:"App-header"},o.a.createElement("img",{src:l.a,class:"App-watering"}),o.a.createElement(f,null),o.a.createElement(p,null)))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(o.a.createElement(g,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}],[[9,1,2]]]);
//# sourceMappingURL=main.a459fa1f.chunk.js.map