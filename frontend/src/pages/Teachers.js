import React from 'react'
import { useState, useEffect } from 'react'
import '../css/style.css'
function Teachers() {
    const [teachers, setTeachers] = useState([])
    async function getTeachers() {
        let data = await fetch('http://127.0.0.1:8000/Teachers')
        data = await data.json()
        setTeachers(data)
    }
    useEffect(() => { 
        getTeachers()
    }, [])
    console.log(teachers)
    return (
        <div className='Teachers'>
            <h2>The number of teachers is {teachers.length}</h2>
            <div className='cards'>
            {teachers.map((teacher) => {
                return (
                    <div key={teacher.id} className='card'>
                        <h2><a href='/login'>{teacher.first_name} {teacher.last_name} </a></h2>
                    </div> 
                )
            })}
            </div>
        </div>
    )
}

export default Teachers