import React,{useState} from 'react'
import {toast} from "react-toastify"
import {useNavigate} from 'react-router-dom'
import axios from 'axios'



const Login = () => {
  
  const navigate=useNavigate()
  const [formdata,SetFormData]=useState({
    email:"",
    password:"",
    })
  const [error,SetError]=useState("")
  
  const handleOnChange=(e)=>{
    SetFormData({...formdata,[e.target.name]:e.target.value})
  }
  const {email,password}=formdata
  const handleOnSubmit=async(e)=>{
    e.preventDefault()
    const response=await axios.post("http://localhost:8000/auth/user/login/",formdata)
      
   
    const message=response.data.message
    const data=response.data.data
    console.log(response)
    if (response.status==200||response.status==201){
      toast.success(message)
      console.log(data)
      localStorage.setItem("user_id", JSON.stringify(data.full_name))
      localStorage.setItem("access_token",JSON.stringify(data.access_token))
      localStorage.setItem("refresh_token", JSON.stringify(data.refresh_token))
      navigate("/dashboard")
    }else{
      toast.error(error)
    }
  }
  
  return (
    <div className="signup">
				<form onSubmit={handleOnSubmit} >
					<label htmlFor="chk" aria-hidden="true">Login</label>
					<input type="email" name="email" placeholder="Email" value={email} onChange={handleOnChange}/>
					<input type="password" name="password" placeholder="Password"  value={password} onChange={handleOnChange}/>          
					<button>Login</button>
				</form>
			</div>
  )
}

export default Login