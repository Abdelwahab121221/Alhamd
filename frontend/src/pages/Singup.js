import React, { useContext, useState } from "react";
import AuthContext from "../services/Context";

function Singup() {
  const [user, setUser] = useState(null);
  const [pass, setPass] = useState(null);
  const [first, setFirst] = useState(null);
  const [last, setLast] = useState(null);
  const [passError, setPassError] = useState(false);
  const [userError, setUserError] = useState(false);
  let [, sing_up, api] = useContext(AuthContext);
  const checkUser = async () => {
    let res = await api
      .post("/users/check user", {
        username: user,
      })
      .then(
        (res) => {
          sing_up(user,pass,first,last);
        },
        (rej) => {
          return setUserError(true);
        }
      );
  };
  return (
    <div className="singup">
      <div className="box">
        <div className="header">
          <h1>انشاء حساب</h1>
        </div>
        <form method="POST">
          <div className="info">
            <input
              type="text"
              onChange={(e) => {
                setLast(e.target.value);
              }}
              className="inp"
              placeholder="الاسم الاخير"
            />
            <input
              type="text"
              onChange={(e) => {
                setFirst(e.target.value);
              }}
              className="inp"
              placeholder="الاسم الاول"
            />
          </div>
          <div className="input">
            <input
              className="inp"
              type="email"
              name="user"
              placeholder="اسم المستخدم"
              required
              onChange={(e) => {
                setUser(e.target.value);
              }}
            />
          </div>
          {userError && (
            <div style={{ color: "red", textAlign: "center" }}>
              اسم المستخدم موجود مسبقا
            </div>
          )}
          <div className="input">
            <input
              className="inp"
              name="pass"
              type="password"
              placeholder="كلمة السر"
              required
              onChange={(e) => {
                let value = e.target.value;
                setPass(value);
                if (!/.{8,}/gi.test(value)) {
                  setPassError(true);
                } else {
                  setPassError(false);
                }
              }}
            />
          </div>
          {passError && (
            <div style={{ color: "red", textAlign: "center" }}>
              يجب ان تحتوى كلمة المرورة على ثمانية احرف او ارقام
            </div>
          )}
          <div className="submit">
            <input
              type="submit"
              onClick={(e) => {
                e.preventDefault();
                if (!passError) {
                  if (
                    user !== null &&
                    pass !== null &&
                    first !== null &&
                    last !== null
                  ) {
                    checkUser()
                  }
                }
              }}
              value="انشاء حساب"
              className="sub"
            />
          </div>
        </form>
      </div>
    </div>
  );
}

export default Singup;
