import React from 'react'
import '../css/style.css'
function Header() {
    return (
        <header>
            <nav>
                <ul>
                    <li><a href="/The teachers">الشيوخ</a></li>
                    <li><a href="/The students">الطلاب</a></li>
                    <li><a href="/The assists">المساعدين</a></li>
                    <li><a href="/The management">الادارة العامة</a></li>
                </ul>
            </nav>
            <h1><a href="#">الحمد</a></h1>
        </header>
    )
}

export default Header