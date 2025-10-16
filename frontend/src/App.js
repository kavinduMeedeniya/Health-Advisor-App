import React from 'react';
import './App.css';
import ChatBot from './components/ChatBot';
import HealthFootSonicJourney from './components/HealthFootSonicJourney';
import HealthAIAssistant from './components/HealthAIAssistant';

function App() {
  return (
    <div className="App">

      <HealthAIAssistant />
      <ChatBot />

      <HealthFootSonicJourney />
    </div>
  );
}

export default App;