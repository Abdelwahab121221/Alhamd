import React from "react";
import ReactDOM from "react-dom/client";
import "./css/style.css";
import App from "./App";
import Teachers from "./pages/Teachers";
import Students from "./pages/Students"
import Assists from "./pages/Assists"
import Management from "./pages/Management"

// Create a BrowserRouter and RouterProvider to use react-router-dom
import { createBrowserRouter, RouterProvider } from "react-router-dom";
const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: ".....sorry this page is not found",
  },
  // Add more routes as needed
  {
    path: "The teachers",
    element: <Teachers />,
  },
  {
    path: "The students",
    element: <Students />,
  },
  {
    path: "The assists",
    element: <Assists />
  },
  {
    path: "The management",
    element: <Management />
  }
]);
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
