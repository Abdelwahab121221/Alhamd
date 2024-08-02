import React, { useEffect, useState } from "react";
import Header from "../../components/Header";
import { Link } from "react-router-dom";
function TeacherManagement() {
  const [students, setStudents] = useState([]);
  const [student, setStudent] = useState({});
  useEffect(() => {
    const getStudents = async () => {
      let data = await fetch("http://127.0.0.1:8000/Students");
      data = await data.json();
      setStudents(data);
    };
    getStudents();
  }, []);
  const updateStudent = async () => {
    if (student.id === undefined) {
      console.log("not now");
    } else {
      await fetch(`http://127.0.0.1:8000/Students/update/${student.id}`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(student),
      });
    }
  };
  useEffect(() => {
    updateStudent();
  }, [student]);
  return (
    <div className="management">
      <Header lies={[]} />
      <div className="content">
        <div className="students">
          <h2>Students</h2>
          <div className="student-list">
            <table>
              <thead>
                <tr>
                  <th>الاسم</th>
                  <th>ID</th>
                  <th>الحضور</th>
                  <th>التاريخ</th>
                  <th>السورة</th>
                </tr>
              </thead>
              {students.map((student) => {
                let date = new Date().getDate();
                return (
                  <tbody>
                    <tr>
                      <td
                        onClick={(e) => {
                          console.log(e.target.textContent);
                        }}
                      >
                        <Link to={`/Student/${student.first_name} ${student.last_name}`}>
                        {student.first_name} {student.last_name}
                        </Link>
                      </td>
                      <td>
                        <span>{student.id}</span>
                      </td>
                      <td>
                        <input type="checkbox" />
                      </td>
                      <td>{date}</td>
                      <td>{student.al_syera}</td>
                    </tr>
                  </tbody>
                );
              })}
            </table>
          </div>
        </div>
        <div className="assistants">
          <h2>Assistants</h2>
        </div>
      </div>
    </div>
    // Add your Management page content here
  );
}

export default TeacherManagement;
