import React from 'react';
import logo from './logo.svg';
import watering from './watering.gif';
import './App.css';
import Valves from './Components/Valves.js';
import RandomImage from './Components/RandomImage.js'
import FlowerSensorCharts from './Components/FlowerSensorCharts.js'
import LastAccess from './Components/LastAccess.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <LastAccess />
        <img src={watering} class="App-watering"/>
        <Valves />
        <RandomImage />
        <FlowerSensorCharts />
      </header>
    </div>
  );
}

export default App;
