import React from "react";
import Header from "../../components/Header";
import { jwtDecode } from "jwt-decode";
function TeacherPage() {
    let username = jwtDecode(JSON.parse(localStorage.getItem('token')).access).username;
    return (
        <div className="TeacherPage">
            <Header
                lies={["الطلاب", "المساعدين", "الادارة العامة", "تسجيل الخروج"]}
            />
            <div className="content">
                <h1>مرحبا {username}</h1>
            </div>
        </div>
    );
}

export default TeacherPage;
