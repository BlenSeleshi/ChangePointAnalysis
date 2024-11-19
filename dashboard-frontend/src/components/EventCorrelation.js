import React, { useEffect, useState } from 'react';
import axios from 'axios';

function EventCorrelation() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/events')
      .then(response => {
        setEvents(response.data.data);
      })
      .catch(error => console.error('Error fetching event correlations:', error));
  }, []);

  return (
    <div className="events-container">
      <h2>Event Correlations</h2>
      <table>
        <thead>
          <tr>
            <th>Event</th>
            <th>Date</th>
            <th>Correlation</th>
          </tr>
        </thead>
        <tbody>
          {events.map((event, index) => (
            <tr key={index}>
              <td>{event.Event}</td>
              <td>{event.Date}</td>
              <td>{event.Correlation}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default EventCorrelation;
