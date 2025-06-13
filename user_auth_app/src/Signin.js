import React, { useState } from "react";

function Signin({ setLoggedInUser }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSignIn = async (e) => {
    e.preventDefault();
    const payload = { email, password };

    const res = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      const data = await res.json();
      setLoggedInUser(data); // <== Save to app and localStorage
    } else {
      const error = await res.json();
      alert("Login failed: " + error.error);
    }
  };

  return (
    <form onSubmit={handleSignIn}>
      <fieldset>
        <h2>Sign In</h2>
        <div className="Field">
          <label>Email address</label>
          <input
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Email address"
          />
        </div>
        <div className="Field">
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
        </div>
        <button type="submit">Sign In</button>
      </fieldset>
    </form>
  );
}

export default Signin;
