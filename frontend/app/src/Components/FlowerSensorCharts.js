import React from 'react';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Legend, Tooltip } from 'recharts';

const data = [{x: 1, y: 400}, {x:2, y: 500}];

class FlowerSensorCharts extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      data: null
    };
}

componentDidMount() {
  this.reloadCharts();
}

reloadCharts() {
  fetch("https://rosenhillgarden.pythonanywhere.com/miflora")
  //.then(res => res.json())
  .then((result) => result.json())
  .then((json) => {
      this.setState({
        isLoaded: true,
        data: json
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
      const { error, isLoaded, data } = this.state;
      if (error) {
        return <div>Error Loading Charts: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Loading Charts...</div>;
      } else {
        return (
          <div>
          <LineChart width={600} height={300} data={data}>
            <Line type="monotone" dataKey="temperature" stroke="#FF6347" />
            <CartesianGrid stroke="#ccc" />
            <XAxis />
            <YAxis />
            <Legend />
            <Tooltip />
          </LineChart>
          <LineChart width={600} height={300} data={data}>
          <Line type="monotone" dataKey="light" stroke="#FFFF00" />
            <CartesianGrid stroke="#ccc" />
            <XAxis />
            <YAxis />
            <Legend />
            <Tooltip />
          </LineChart>
          <LineChart width={600} height={300} data={data}>
            <Line type="monotone" dataKey="moisture" stroke="#FF6347" />
            <CartesianGrid stroke="#ccc" />
            <XAxis />
            <YAxis />
            <Legend />
            <Tooltip />
          </LineChart>
          <LineChart width={600} height={300} data={data}>
            <Line type="monotone" dataKey="battery" stroke="#ADFF2F" />
            <CartesianGrid stroke="#ccc" />
            <XAxis />
            <YAxis />
            <Legend />
            <Tooltip />
          </LineChart>
          </div>
        );
      }
  }

}


export default FlowerSensorCharts;