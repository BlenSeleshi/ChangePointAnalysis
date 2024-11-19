import React from 'react';
import './styles.css';
import TrendsChart from './components/TrendsChart';
import EventCorrelation from './components/EventCorrelation';
import MetricsDisplay from './components/MetricsDisplay';

function App() {
  return (
    <div className="app-container">
      <h1>Brent Oil Price Dashboard</h1>
      <MetricsDisplay />
      <TrendsChart />
      <EventCorrelation />
    </div>
  );
}

export default App;
