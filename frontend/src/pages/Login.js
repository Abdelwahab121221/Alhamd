import React, { useContext, useState } from "react";
import AuthContext from "../services/Context";

function Login() {
  const [passError, setPassError] = useState(false);
  const [user ,setUser] = useState(null)
  const [pass ,setPass] = useState(null)
  const [login] = useContext(AuthContext)
  return (
    <div className="login">
      <div className="box">
        <div className="header">
          <h1>تسجيل الدخول</h1>
        </div>
        <form method="POST">
          <div className="input">
            <input
              className="inp"
              type="text"
              name="user"
              placeholder="اسم المستخدم"
              required
              onChange={(e) => {
                let value = e.target.value
                setUser(value)
              }}
            />
          </div>
          <div className="input">
            <input
              onChange={(e) => {
                let value = e.target.value;
                setPass(value)
                console.log(/.{8,}/gi.test(value));
                if (!/.{8,}/gi.test(value)) {
                  setPassError(true);
                } else {
                  setPassError(false);
                }
              }}
              className="inp"
              name="pass"
              type="password"
              placeholder="كلمة المرور"
              required
            />
          </div>
          {passError && (
            <div style={{ color: "red", textAlign: "center" }}>
              يجب ان تحتوى كلمة المرور على ثمانية احرف او ارقام
            </div>
          )}
          <div className="submit">
            <input onClick={(e) => {
              e.preventDefault()
              if (!passError) {
                if (user !== null && pass !== null) {
                    login(user, pass)
                }
            }
            }} type="submit" value='تسجيل الدخول' className="sub" />
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login;
