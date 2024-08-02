import React, { createContext, useState } from "react";
import { Navigate } from "react-router-dom";
import axios from "axios";
let AuthContext = createContext();
let api = axios.create({
  baseURL: "http://127.0.0.1:8000",
});
api.interceptors.request.use(
  (conf) => {
    const token = JSON.parse(localStorage.getItem("token"));
    if (token && token.access) {
      conf.headers.Authorization = `Bearer ${token}`;
    }
    return conf;
  },
  (error) => {
    return Promise.reject(error);
  }
);
export const AuthProvider = ({ children }) => {
  const [redirect, setRedirect] = useState(null);

  const login = async (username, password) => {
    let res = await api.post("/token/", {
      username: username,
      password: password,
    });
    localStorage.setItem("token", JSON.stringify(res.data));
    setRedirect("/Teacher");
  };
  const Sign_up = async (
    username = String,
    password = String,
    first_name = String,
    last_name = String
  ) => {
    await api.post("/users/create", {
      username: username,
      password: password,
    });

    await api.post("/Teachers/create", {
      first_name: first_name,
      last_name: last_name,
    });
    let res = await api.post("/token/", {
      username: username,
      password: password,
    });
    localStorage.setItem("token", JSON.stringify(res.data));
    setRedirect("/Teacher");
  };
  if (redirect) {
    return <Navigate to={redirect} replace />;
  }
  return (
    <AuthContext.Provider value={[login, Sign_up, api]}>
      {children}
    </AuthContext.Provider>
  );
};

export default AuthContext;
