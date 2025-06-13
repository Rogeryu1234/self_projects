import React from "react";

function Success({ user, onLogout }) {
  return (
    <div className="success-container">
      <h1> Welcome Back {user.last_name}{user.first_name || "User"}!</h1>

      <div className="video-wrapper">
        <iframe
          width="560"
          height="315"
          src="https://www.youtube.com/embed/dQw4w9WgXcQ?autoplay=1"
          title="YouTube video"
          frameBorder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowFullScreen
        ></iframe>
      </div>
    </div>
  );
}

export default Success;
