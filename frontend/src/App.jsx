import { useState } from 'react'
import { BrowserRouter as Router,Routes,Route } from 'react-router-dom'
import {
  Signup,
  Login,
  Profile,
  VerifyEmail,
  ForgetPassword
} from "./components"
import './App.css'
import {ToastContainer} from "react-toastify"
import "react-toastify/dist/ReactToastify.css"; 


function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Router>
        <ToastContainer position="top-right"
          autoClose={5000}
          hideProgressBar={false}
          newestOnTop={false}
          closeOnClick
          rtl={false}
          pauseOnFocusLoss
          draggable
          pauseOnHover
          theme="light"
          /> 
          <Routes>
             
            <Route path="/" element={<Signup />} />
            <Route path="/login" element={<Login />} />
            <Route path="/dashboard" element={<Profile />} />
            <Route path="/otp/verify" element={<VerifyEmail />} />
            <Route path="/forget_password" element={<ForgetPassword />} />
          </Routes>
    
      </Router>
    </>
  )
}

export default App
