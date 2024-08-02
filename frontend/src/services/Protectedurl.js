import React, { useContext, useEffect, useState } from "react";
import { Navigate } from "react-router-dom";
import { jwtDecode } from "jwt-decode";
import AuthContext from "./Context";
const Protectedurl = ({ children }) => {
  const token = localStorage.getItem("token");
  const [is_Auth, setIs_Auth] = useState(null);
  let [, , api] = useContext(AuthContext);
  useEffect(() => {
    auth();
  }, []);
  const refreshToken = async () => {
    console.log("refresh");
    try {
      let res = await api.post("/token/refresh/", {
        refresh: JSON.parse(token).refresh,
      });
      localStorage.setItem("token", JSON.stringify(res.data));
      setIs_Auth(true);
    } catch (error) {
      console.log(error);
      setIs_Auth(false);
    }
  };
  const auth = async () => {
    if (!token) {
      setIs_Auth(false);
      return;
    }
    let jwt_exp = jwtDecode(JSON.parse(token).access).exp;
    let now = Date.now() / 1000;
    console.log(jwt_exp < now);
    if (jwt_exp < now) {
      console.log("starting refresh");
      await refreshToken();
    } else {
      setIs_Auth(true);
    }
  };
  if (is_Auth === null) {
    return <div>loading ...</div>;
  }
  return is_Auth !== null ? (
    is_Auth ? (
      children
    ) : (
      <Navigate to={"/login"} />
    )
  ) : null;
};
export default Protectedurl;
