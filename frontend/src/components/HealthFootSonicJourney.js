import React from 'react';
import './HealthFootSonicJourney.css';

const HealthFootSonicJourney = () => {
  const handleExploreClick = () => {
    console.log('Explore More button clicked');
    // Add your navigation or action logic here
  };

  return (
    <div className="health_foot-body">
      <div className="health_foot-container">
        {/* Large Inspirational Card */}
        <div className="health_foot-card health_foot-card-large">
          <div className="health_foot-card-top-text">Start Your AI Journey.</div>
          <div>
            <div className="health_foot-card-quote">"I Believe Intelligence Can Change Health."</div>
            <div className="health_foot-card-author">Eglion KXZ, Developer</div>
          </div>
        </div>

        {/* Stats Card */}
        <div className="health_foot-card health_foot-card-small health_foot-card-stats">
          <div className="health_foot-stats-label">Clients</div>
          <div className="health_foot-stats-number">350K+</div>
          <div className="health_foot-stats-description">350 Thousend Requests And Counting</div>
        </div>

        {/* Action Card */}
        <div className="health_foot-card health_foot-card-small health_foot-card-action">
          <div className="health_foot-action-title">Shape Your Intelligent Health Universe.</div>
          <button 
            className="health_foot-action-button"
            onClick={handleExploreClick}
          >
            Explore More
          </button>
        </div>
      </div>
    </div>
  );
};

export default HealthFootSonicJourney;