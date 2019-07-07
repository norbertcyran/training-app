import React from "react";
import Login from "./Login";
import { BrowserRouter as Router, Link, Route } from "react-router-dom";
import Register from "./Register";
import "./styles.css";
class Home extends React.Component {
  state = {};
  render() {
    return (
      <>
        {document.body.classList.remove("dodajcwiczenie_tlo")}
        {document.body.classList.remove("profil")}
        {document.body.classList.add("home")}
        <div className="container-fluids">
          <h1>
            <span className="badge badge-secondary">NPNG </span>🐗
          </h1>
        </div>
        <section id="Log_cart">
          <div class="container-fluids">
            <div class="container-fluids ltop">
              <h1>Dołącz do nas!</h1>
            </div>
            <div className="row">
              <Login />
              <Register />
            </div>
          </div>
        </section>
        <button>
          <Link to="/Profil"> Dalej</Link>{" "}
        </button>
      </>
    );
  }
}
export default Home;
