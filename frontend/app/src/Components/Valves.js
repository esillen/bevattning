import React from 'react';
import Valve from './Valve.js';

class Valves extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          error: null,
          isLoaded: false,
          valves: null,
          password: ''
        };
    }

    componentDidMount() {
      this.reloadValves();
    }

    reloadValves() {
      fetch("https://rosenhillgarden.pythonanywhere.com/valve")
      //.then(res => res.json())
      .then((result) => result.json())
      .then((json) => {
          this.setState({
            isLoaded: true,
            valves: json.valves
          });
        },
        // Note: it's important to handle errors here
        // instead of a catch() block so that we don't swallow
        // exceptions from actual bugs in components.
        (error) => {
          this.setState({
            isLoaded: true,
            error: error
          });
        }
      )
    }

    updatePassword(password) {
      this.setState({password: password});
    }

    render() {
      const { error, isLoaded, valves } = this.state;
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading...</div>;
      } else {
        return (
          <ul>
            <li>
              Password: 
              <input value={this.state.password} onChange={evt => this.updatePassword(evt.target.value)}/>
            </li>
            {valves.map(valve => (
              <li key={valve.id}>
                <Valve data = {valve} valves={this} password = {this.state.password}/>
              </li>
            ))}

          </ul>
        );
      }
    }
}
export default Valves;
