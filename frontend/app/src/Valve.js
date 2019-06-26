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
    let content;

    if (this.props.data.state) {
      content = <div>
        On
        <button onClick={() => this.switchValve(false)}>
          Turn Off
        </button> 
        {`Last opened ${this.props.data.last_opened_minutes_ago} minutes and ${this.props.data.last_opened_seconds_ago} seconds ago`}
      </div>
    } else {
      content = <div>
        Off
        <button onClick={() => this.switchValve(true)}>
          Turn On
        </button> 
        {`Last closed ${this.props.data.last_closed_minutes_ago} minutes and ${this.props.data.last_closed_seconds_ago} seconds ago`}
      </div>
    }

    return (
      <div>
        {content}
      </div>
    );
  }
}


export default Valve;
