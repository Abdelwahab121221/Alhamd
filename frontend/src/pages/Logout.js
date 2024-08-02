import React from "react";
import { Navigate } from "react-router-dom";
function logout() {
  window.localStorage.removeItem("token");
  return Navigate({to:'/',replace:true});
}

export default logout;
