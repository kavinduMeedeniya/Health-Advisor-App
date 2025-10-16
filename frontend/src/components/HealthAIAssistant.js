import React from 'react';
import './HealthAIAssistant.css';

const HealthAIAssistant = () => {
  return (
    <div className="health-ai-assistant">
      <section className="health_hero_sec">
        <div className="container">
          <h1>AI Health Assistant<br />Medical Diagnosis<br />Analyser</h1>
          <p>Monitor Your Health and Build Your Personal AI Medical Assistant</p>
          <div className="health_cta_buttons">
            <a href="#start" className="health_btn_primary">Get Started — It's Free</a>
            <a href="#download" className="health_btn_secondary">Download — Mobile App</a>
          </div>
        </div>
      </section>

      <section className="health_feature_section">
        <div className="health_image_background"></div>
      </section>

      <section className="health_partners">
        <div className="health_partners_grid">
          <div className="health_partner_logo">
            <span style={{ fontWeight: '700' }}>Mayo Clinic</span>
          </div>
          <div className="health_partner_logo">
            <div className="health_partner_icon"></div>
            <span>Johns Hopkins</span>
          </div>
          <div className="health_partner_logo">
            <span style={{ fontWeight: '700' }}>Cleveland Clinic</span>
          </div>
          <div className="health_partner_logo">
            <span style={{ fontFamily: 'serif', fontStyle: 'italic' }}>Pfizer</span>
          </div>
          <div className="health_partner_logo">
            <div 
              className="health_partner_icon" 
              style={{ background: 'linear-gradient(45deg, #0061FF, #00A1FF)' }}
            ></div>
            <span>Medtronic</span>
          </div>
        </div>
      </section>
    </div>
  );
};

export default HealthAIAssistant;