import { useState } from "react";
import './login.css';

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

const handleSubmit = async (e) => {
  e.preventDefault();
  const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/login/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ username, password }),
  });

  const data = await res.json();
  console.log(data);
};


  return (
    <div class="login_container">
        <div class="bg-shape-top"></div>
        <div class="bg-illustration">
            <img src="/resources/student-illus.png" alt="Student Illustration" />
        </div>

        <div class="login-card">
            <h1>Join</h1>
            
            <form onSubmit={handleSubmit}>
                <div class="input-group">
                    <label for="username">Username</label>
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} id="username" placeholder="example@school.com" />
                </div>

                <div class="input-group">
                    <label for="password">Password</label>
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} id="password" placeholder="••••••••••••" />
                </div>

                <button type="submit" class="btn-primary">Sign Up</button>
                
                <div class="divider">or</div>
                
                <button type="button" class="btn-primary">Sign Up</button>
            </form>
        </div>
    </div>

  );
}
