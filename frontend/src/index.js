import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Student from "./pages/admin/Students";
import Management from "./pages/admin/Management";
import Singup from "./pages/Singup";
import Login from "./pages/Login";
import Logout from "./pages/Logout"
import Teacher from "./pages/admin/Teachers";
import Assistants from "./pages/admin/Assistants";
import TeacherPage from "./pages/Teacher/TeacherPage";
import TeacherAssistants from "./pages/Teacher/TeacherAssistants";
import TeacherManagement from "./pages/Teacher/TeacherManagement";
import TeacherStudents from "./pages/Teacher/TeacherStudents";
import StudentPage from "./pages/StudentPage";
import Protectedurl from "./services/Protectedurl";
import { AuthProvider } from "./services/Context";
import NotFound from "./pages/NotFound";
// Create a BrowserRouter and RouterProvider to use react-router-dom
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="*" Component={NotFound}/>
          <Route path="/" Component={App} />
          <Route path="/singup" Component={Singup} />
          <Route path="/login" Component={Login} />
          <Route path="/logout" Component={Logout}/>
          <Route path="/The students" element={<Protectedurl><Student/></Protectedurl>} />
          <Route path="/management" element={<Protectedurl><Management/></Protectedurl>} />
          <Route path="/The assistants" element={<Protectedurl><Assistants/></Protectedurl>} />
          <Route path="/The teachers" element={<Protectedurl><Teacher/></Protectedurl>} />
          <Route path="/Teacher" element={<Protectedurl><TeacherPage/></Protectedurl>} />
          <Route path="/Teacher/The students" element={<Protectedurl><TeacherStudents/></Protectedurl>} />
          <Route path="/Teacher/The assistants" element={<Protectedurl><TeacherAssistants/></Protectedurl>} />
          <Route path="/Teacher/management" element={<Protectedurl><TeacherManagement/></Protectedurl>} />
          <Route path="/Student/:student" element={<Protectedurl><StudentPage/></Protectedurl>} />
        </Routes>
      </AuthProvider>
    </Router>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
