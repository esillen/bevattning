import React from 'react';
import logo from './logo.svg';
import watering from './watering.gif';
import './App.css';
import Valves from './Valves.js';
import RandomImage from './RandomImage.js'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={watering} class="App-watering"/>
        <Valves />
        <RandomImage />
        
      </header>
    </div>
  );
}

export default App;
