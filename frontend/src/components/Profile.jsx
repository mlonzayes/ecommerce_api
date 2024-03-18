import React from 'react'

const Profile = () => {
  const user=JSON.parse(localStorage.getItem('user_id'))

  return (
    <div>
      <h2>hi {user} </h2>
      <p>welcome to your profile</p>
      <button>Logout</button>
    </div>
  )
}

export default Profile