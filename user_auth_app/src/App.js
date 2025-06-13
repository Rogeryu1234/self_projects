import './App.css';
import { useState, useEffect } from 'react';
import Signup from './Signup';
import Signin from './Signin';
import Success from './Success';

function App() {
  const [mode, setMode] = useState("signup");
  const [loggedInUser, setLoggedInUser] = useState(null);

  // Load user from localStorage on mount
  useEffect(() => {
    const savedUser = localStorage.getItem("loggedInUser");
    if (savedUser) {
      setLoggedInUser(JSON.parse(savedUser));
    }
  }, []);

  // Save to localStorage on login
  const handleLogin = (user) => {
    setLoggedInUser(user);
    localStorage.setItem("loggedInUser", JSON.stringify(user));
  };

  // Clear localStorage on logout
  const handleLogout = () => {
    setLoggedInUser(null);
    localStorage.removeItem("loggedInUser");
    setMode("signin");
  };

  return (
    <div className="App">
      <div className="top-bar">
        {!loggedInUser && (
          <div className="toggle-buttons">
            <button onClick={() => setMode("signup")} className={mode === "signup" ? "active" : ""}>
              Sign Up
            </button>
            <button onClick={() => setMode("signin")} className={mode === "signin" ? "active" : ""}>
              Sign In
            </button>
          </div>
        )}
        {loggedInUser && (
          <button className="logout-button" onClick={handleLogout}>Log Out</button>
        )}
      </div>
      <div className="center-container">
      {loggedInUser ? (
        <Success user={loggedInUser} />
      ) : mode === "signup" ? (
        <Signup />
      ) : (
        <Signin setLoggedInUser={handleLogin} />
      )}
      </div>
    </div>
  );
}

export default App;
