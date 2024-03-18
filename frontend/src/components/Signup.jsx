import React from 'react'
import { useState } from 'react'
import { FaGoogle } from "react-icons/fa";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import {toast} from "react-toastify"


const Signup = () =>{
  const navigate=useNavigate()
  const [formdata,SetFormData]=useState({
    email:"",
    first_name:"",
    last_name:"",
    password:"",
    password2:""
    })
  const [error,SetError]=useState("")
  
  const handleOnChange=(e)=>{
    SetFormData({...formdata,[e.target.name]:e.target.value})
  }
  const {email,first_name,last_name,password,password2}=formdata

  const hadleSubmit =async (e) => {
    e.preventDefault();
    
    if (!email || !password || !first_name || !last_name || !password2) {
      SetError("Please fill all the fields");
    } else if (password !== password2) {
      SetError("Password do not match");
    } else{
      //make call to api
      //check our response
      //redirect to verify email
      
      const res = await axios.post("http://localhost:8000/auth/user/register/",formdata)

      const response=res.data.data
      const message=res.data.message
      if (res.status==200||res.status==201){
        navigate("/otp/verify")
        toast.success(message)

      }else{
        SetError("Something went wrong")
      }


    }
  }

  
  return (
	<div className="main">  	
		<input type="checkbox" id="chk" aria-hidden="true" />
        
			<div className="signup">
				<form onSubmit={hadleSubmit}>
                <p style={{color:"red",padding:"1px"}}>{error ? error : ""}</p>
					<label htmlFor="chk" aria-hidden="true">Sign up</label>
					<input type="email" name="email" placeholder="Email" value={email} onChange={handleOnChange}/>
					<input type="text" name="first_name" placeholder="First name"  value={first_name} onChange={handleOnChange}/>
                    <input type="text" name="last_name" placeholder="Last name"  value={last_name} onChange={handleOnChange}/>
					<input type="password" name="password" placeholder="Password"  value={password} onChange={handleOnChange}/>
                    <input type="password" name="password2" placeholder="Confirm password"  value={password2} onChange={handleOnChange}/>
					<button>Sign up</button>
				</form>
			</div>
     
            
               
            
	</div>
    
  )
}

export default Signup