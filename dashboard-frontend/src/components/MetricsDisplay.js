import React, { useEffect, useState } from 'react';
import axios from 'axios';

function MetricsDisplay() {
  const [metrics, setMetrics] = useState({});

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/metrics')
      .then(response => {
        setMetrics(response.data.data);
      })
      .catch(error => console.error('Error fetching metrics:', error));
  }, []);

  return (
    <div className="metrics-container">
      <h2>Model Metrics</h2>
      <ul>
        <li>RMSE: {metrics.rmse}</li>
        <li>MAE: {metrics.mae}</li>
        <li>Forecast Accuracy: {metrics.forecast_accuracy}</li>
      </ul>
    </div>
  );
}

export default MetricsDisplay;
