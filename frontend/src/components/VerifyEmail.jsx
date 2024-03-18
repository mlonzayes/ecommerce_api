import React, { useState } from 'react'
import axios from 'axios'
import {useNavigate} from 'react-router-dom'
import {toast } from 'react-toastify'

const VerifyEmail = () => {
  const [otp,setOtp]=useState("")
  const navigate=useNavigate()
  const handleSubmit=async (e)=>{
    e.preventDefault()
    if (otp){
      const response= await axios.post("http://localhost:8000/auth/user/verify-email/", {"otp":otp})
      if (response.status==200||response.status==201){
        const message=response.data.message
        toast.success(message)
        navigate("/login")
        
      }
    }
  }
  return (
    <div className="main">  	
		<input type="checkbox" id="chk" aria-hidden="true" />
        
			<div className="signup">
				<form onSubmit={handleSubmit}>
                <p style={{color:"red",padding:"1px"}}></p>
					<label htmlFor="chk" aria-hidden="true">Verify Email</label>
					<input type="number" name="otp_code" placeholder="Please put your otp code" onChange={(e)=>setOtp(e.target.value)} />

					<button>Verify</button>
				</form>
			</div>


            
               
            
	</div>
  )
}

export default VerifyEmail