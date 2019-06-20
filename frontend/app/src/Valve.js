import React from 'react';

class Valve extends React.Component {
  constructor(props) {
    super(props);
  }

  switchValve(newstate) {
    let url = "http://localhost:5000/valve/" + this.props.index + "/action";
    if (newstate === true) {
      url += '/on';
    } else {
      url += '/off';
    }
    fetch(url);
  }

  
  render() {
    return (
      <div>
        {this.props.state ? 'on' : 'off'}
        <button onClick={() => this.switchValve(true)}>
          Turn On
        </button>
        <button onClick={() => this.switchValve(false)}>
          Turn Off
        </button>
      </div>
    );
  }
}


export default Valve;
