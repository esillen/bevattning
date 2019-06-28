import React from 'react';

class LastAccess extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          error: null,
          isLoaded: false,
          health: null
        };
    }

    componentDidMount() {
      this.reloadHealth();
    }

    reloadHealth() {
      fetch(
        "https://rosenhillgarden.pythonanywhere.com/health")
      .then((result) => result.json())
      .then((json) => {
          this.setState({
            isLoaded: true,
            health: json
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

    render() {
      const { error, isLoaded, health } = this.state;
      if (error) {
        return <div>Error: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading health...</div>;
      } else {
        return (
          <div>System last heartbeat {`${health.last_access_minutes} minutes and ${health.last_access_seconds} seconds ago.`}</div>
        );
      }
    }
}
export default LastAccess;
