import React from 'react';

class Valve extends React.Component {
  constructor(props) {
    super(props);
  }

  switchValve(newstate) {
    let url = "https://rosenhillgarden.pythonanywhere.com/valve/" + this.props.data.id + "/action";
    if (newstate === true) {
      url += '/on';
    } else {
      url += '/off';
    }
    fetch(url)
    .then((_) =>
      this.props.valves.reloadValves()
    );
    
  }
  
  render() {
    return (
      <div>
        {this.props.data.state ? 'on' : 'off'}
        <button onClick={() => this.switchValve(true)}>
          Turn On
        </button>
        <button onClick={() => this.switchValve(false)}>
          Turn Off
        </button> 
        {`Last opened: ${this.props.data.last_opened_minutes_ago} minutes and ${this.props.data.last_opened_seconds_ago} seconds ago`}
      </div>
    );
  }
}


export default Valve;
