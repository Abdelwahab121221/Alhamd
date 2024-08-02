import React from "react";
import "../css/style.css";
import { Link } from "react-router-dom";
function Header({ lies }) {
    return (
        <header>
            <nav>
                <ul>
                    {lies.map((li , index) => {
                    return (
                        <li key={index}>
                        <Link
                            to={
                            li === "الطلاب"
                                ? window.location.origin+(window.location.pathname === '/'? '' : window.location.pathname)+"/The students"
                                : li === "المساعدين"
                                ? window.location.origin+(window.location.pathname === '/'? '' : window.location.pathname)+"/The assistants"
                                : li === "الشيوخ"
                                ? window.location.origin+(window.location.pathname === '/'? '' : window.location.pathname)+"/The teachers"
                                : li === "الادارة العامة"
                                ? window.location.origin+(window.location.pathname === '/'? '' : window.location.pathname)+"/management"
                                : li === 'تسجيل الدخول'
                                ? '/login'
                                : li === 'انشاء حساب'
                                ?'/singup'
                                :li === 'تسجيل الخروج'
                                ?'/logout'
                                : window.location.origin
                            }
                            target="_self"
                            >
                        {li}  
                        </Link>
                    </li>
                    );
                })}
                </ul>
            </nav>
            <h1>
            <Link to="/Teacher">الحمد</Link>
            </h1>
        </header>
    );
}

export default Header;
