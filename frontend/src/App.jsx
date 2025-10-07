import { BrowserRouter, Route, Routes } from "react-router";
import Home from "./pages/Home";
import About from "./pages/About";

function App() {
  return (
    <BrowserRouter basename="/mentorx">
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/about" element={<About/>} />
      </Routes>
    </BrowserRouter>
  );
}
