(window.webpackJsonp=window.webpackJsonp||[]).push([[0],{129:function(e,t,a){e.exports=a.p+"static/media/watering.76cf0a92.gif"},164:function(e,t,a){e.exports=a(349)},169:function(e,t,a){},170:function(e,t,a){e.exports=a.p+"static/media/logo.5d5d9eef.svg"},171:function(e,t,a){},349:function(e,t,a){"use strict";a.r(t);var n=a(1),r=a.n(n),o=a(51),l=a.n(o),c=(a(169),a(170),a(129)),s=a.n(c),i=(a(171),a(10)),u=a(11),d=a(13),h=a(12),m=a(14),p=function(e){function t(e){return Object(i.a)(this,t),Object(d.a)(this,Object(h.a)(t).call(this,e))}return Object(m.a)(t,e),Object(u.a)(t,[{key:"switchValve",value:function(e){var t=this,a="https://rosenhillgarden.pythonanywhere.com/valve/"+this.props.data.id,n={password:this.props.password};n.action=!0===e?"on":"off",fetch(a,{headers:{Accept:"application/json","Content-Type":"application/json"},method:"POST",body:JSON.stringify(n)}).then(function(e){return t.props.valves.reloadValves()})}},{key:"render",value:function(){var e,t=this;return e=this.props.data.state?r.a.createElement("div",null,"On",r.a.createElement("button",{onClick:function(){return t.switchValve(!1)}},"Turn Off"),"Last opened ".concat(this.props.data.last_opened_minutes_ago," minutes and ").concat(this.props.data.last_opened_seconds_ago," seconds ago")):r.a.createElement("div",null,"Off",r.a.createElement("button",{onClick:function(){return t.switchValve(!0)}},"Turn On"),"Last closed ".concat(this.props.data.last_closed_minutes_ago," minutes and ").concat(this.props.data.last_closed_seconds_ago," seconds ago")),r.a.createElement("div",null,e)}}]),t}(r.a.Component),v=function(e){function t(e){var a;return Object(i.a)(this,t),(a=Object(d.a)(this,Object(h.a)(t).call(this,e))).state={error:null,isLoaded:!1,valves:null,password:""},a}return Object(m.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){this.reloadValves()}},{key:"reloadValves",value:function(){var e=this;fetch("https://rosenhillgarden.pythonanywhere.com/valve").then(function(e){return e.json()}).then(function(t){e.setState({isLoaded:!0,valves:t.valves})},function(t){e.setState({isLoaded:!0,error:t})})}},{key:"updatePassword",value:function(e){this.setState({password:e})}},{key:"render",value:function(){var e=this,t=this.state,a=t.error,n=t.isLoaded,o=t.valves;return a?r.a.createElement("div",null,"Error: ",a.message):n?r.a.createElement("ul",null,r.a.createElement("li",null,"Password:",r.a.createElement("input",{value:this.state.password,onChange:function(t){return e.updatePassword(t.target.value)}})),o.map(function(t){return r.a.createElement("li",{key:t.id},r.a.createElement(p,{data:t,valves:e,password:e.state.password}))})):r.a.createElement("div",null,"Loading...")}}]),t}(r.a.Component),f=function(e){function t(e){var a;return Object(i.a)(this,t),(a=Object(d.a)(this,Object(h.a)(t).call(this,e))).state={error:null,isLoaded:!1,randomImageUrl:null},a}return Object(m.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){this.loadRandomImage()}},{key:"loadRandomImage",value:function(){var e=this;console.log("hejj");var t=Math.floor(20*Math.random()),a="https://api.giphy.com/v1/gifs/search?api_key=".concat("aFFKTuSMjd6j0wwjpFCPXZipQbcnw3vB","&q=").concat("water","&limit=").concat(1,"&offset=").concat(t,"&rating=").concat("g","&lang=").concat("en","&fmt=").concat("json");fetch(a).then(function(e){return e.json()}).then(function(t){console.log(t.data[0].images),e.setState({isLoaded:!0,randomImageUrl:t.data[0].images.original.url})},function(t){e.setState({isLoaded:!0,error:t})})}},{key:"render",value:function(){var e=this.state,t=(e.error,e.isLoaded,e.randomImageUrl);return r.a.createElement("div",null,r.a.createElement("img",{src:t}))}}]),t}(r.a.Component),E=a(7),g=function(e){function t(e){var a;return Object(i.a)(this,t),(a=Object(d.a)(this,Object(h.a)(t).call(this,e))).state={error:null,isLoaded:!1,data:null},a}return Object(m.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){this.reloadCharts()}},{key:"reloadCharts",value:function(){var e=this;fetch("https://rosenhillgarden.pythonanywhere.com/miflora").then(function(e){return e.json()}).then(function(t){e.setState({isLoaded:!0,data:t})},function(t){e.setState({isLoaded:!0,error:t})})}},{key:"render",value:function(){var e=this.state,t=e.error,a=e.isLoaded,n=e.data;return t?r.a.createElement("div",null,"Error Loading Charts: ",t.message):a?r.a.createElement("div",null,r.a.createElement(E.d,{width:600,height:300,data:n},r.a.createElement(E.c,{type:"monotone",dataKey:"temperature",stroke:"#FF6347"}),r.a.createElement(E.a,{strokeDasharray:"3 3"}),r.a.createElement(E.f,{interval:9}),r.a.createElement(E.g,null),r.a.createElement(E.b,null),r.a.createElement(E.e,null)),r.a.createElement(E.d,{width:600,height:300,data:n},r.a.createElement(E.c,{type:"monotone",dataKey:"light",stroke:"#FFFF00"}),r.a.createElement(E.a,{strokeDasharray:"3 3"}),r.a.createElement(E.f,{interval:9}),r.a.createElement(E.g,null),r.a.createElement(E.b,null),r.a.createElement(E.e,null)),r.a.createElement(E.d,{width:600,height:300,data:n},r.a.createElement(E.c,{type:"monotone",dataKey:"moisture",stroke:"#FF6347"}),r.a.createElement(E.a,{strokeDasharray:"3 3"}),r.a.createElement(E.f,{interval:9}),r.a.createElement(E.g,null),r.a.createElement(E.b,null),r.a.createElement(E.e,null)),r.a.createElement(E.d,{width:600,height:300,data:n},r.a.createElement(E.c,{type:"monotone",dataKey:"battery",stroke:"#ADFF2F"}),r.a.createElement(E.a,{strokeDasharray:"3 3"}),r.a.createElement(E.f,{interval:9}),r.a.createElement(E.g,null),r.a.createElement(E.b,null),r.a.createElement(E.e,null))):r.a.createElement("div",null,"Loading Charts...")}}]),t}(r.a.Component),y=function(e){function t(e){var a;return Object(i.a)(this,t),(a=Object(d.a)(this,Object(h.a)(t).call(this,e))).state={error:null,isLoaded:!1,health:null},a}return Object(m.a)(t,e),Object(u.a)(t,[{key:"componentDidMount",value:function(){this.reloadHealth()}},{key:"reloadHealth",value:function(){var e=this;fetch("https://rosenhillgarden.pythonanywhere.com/health").then(function(e){return e.json()}).then(function(t){e.setState({isLoaded:!0,health:t})},function(t){e.setState({isLoaded:!0,error:t})})}},{key:"render",value:function(){var e=this.state,t=e.error,a=e.isLoaded,n=e.health;return t?r.a.createElement("div",null,"Error: ",t.message):a?r.a.createElement("div",null,"System last heartbeat ","".concat(n.last_access_minutes," minutes and ").concat(n.last_access_seconds," seconds ago.")):r.a.createElement("div",null,"Loading health...")}}]),t}(r.a.Component);var w=function(){return r.a.createElement("div",{className:"App"},r.a.createElement("header",{className:"App-header"},r.a.createElement(y,null),r.a.createElement("img",{src:s.a,class:"App-watering"}),r.a.createElement(v,null),r.a.createElement(f,null),r.a.createElement(g,null)))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));l.a.render(r.a.createElement(w,null),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then(function(e){e.unregister()})}},[[164,1,2]]]);
//# sourceMappingURL=main.ce017f29.chunk.js.map