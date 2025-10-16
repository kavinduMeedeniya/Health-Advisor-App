import React, { useState, useRef } from 'react';
import './ChatBot.css';

const ChatBot = () => {
  const [messages, setMessages] = useState([
    { text: "Hello! I'm your AI Health Advisor. Tell me about your disease (e.g., 'I have diabetes'), and I'll provide some advice.", sender: 'bot' }
  ]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  

  const handleSend = async () => {
    if (!input.trim()) return;

    const userMessage = { text: input, sender: 'user' };
    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const response = await fetch('https://health-advisor-application.onrender.com/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: input })
      });

      if (!response.ok) {
        throw new Error('Failed to get response');
      }

      const data = await response.json();
      const botMessage = { text: data.response || data.error || 'Sorry, something went wrong.', sender: 'bot' };
      setMessages(prev => [...prev, botMessage]);
    } catch (error) {
      const errorMessage = { text: 'Error connecting to the advisor. Please try again.', sender: 'bot' };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="app-container">
      {/* Left Side - HealthAI Information */}
      <div className="health_ai_container">
        <div className="health_ai_content">
          <div className="health_ai_left_section">
            <h1 className="health_ai_logo">HealthAI</h1>
          </div>
          
          <div className="health_ai_right_section">
            <div className="health_ai_blob"></div>
            <div className="health_ai_description">
              <p>HealthAI Assistant is an advanced AI-powered platform that provides personalized health insights, symptom analysis, and wellness recommendations based on your unique health profile and medical history.</p>
              <div className="health_ai_line"></div>
            </div>
          </div>
        </div>
      </div>

      {/* Right Side - Chat Interface */}
      <div className="chat-panel">
        <div className="chat-container">
          <div className="messages">
            {messages.map((msg, index) => (
              <div key={index} className={`message ${msg.sender}`}>
                <div className="message-text">{msg.text}</div>
              </div>
            ))}
            {isLoading && (
              <div className="message bot">
                <div className="message-text">Thinking...</div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>
          <div className="input-container">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your message here..."
              className="input-field"
              disabled={isLoading}
            />
            <button onClick={handleSend} disabled={isLoading || !input.trim()} className="send-button">
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ChatBot;
