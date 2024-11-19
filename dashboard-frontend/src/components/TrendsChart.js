import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

function TrendsChart() {
  const [trends, setTrends] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/trends')
      .then(response => {
        setTrends(response.data.data);
      })
      .catch(error => console.error('Error fetching trends:', error));
  }, []);

  return (
    <div className="chart-container">
      <h2>Historical Price Trends</h2>
      <ResponsiveContainer width="100%" height={400}>
        <LineChart data={trends}>
          <Line type="monotone" dataKey="Price" stroke="#8884d8" />
          <CartesianGrid stroke="#ccc" />
          <XAxis dataKey="Date" />
          <YAxis />
          <Tooltip />
        </LineChart>
      </ResponsiveContainer>
    </div>
  );
}

export default TrendsChart;
