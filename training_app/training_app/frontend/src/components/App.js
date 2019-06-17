import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router, Link, Route } from "react-router-dom";
import Home from "./Home";
import Profil from "./Profil";
import Addex from "./Addex";
import Explore from "./Explore";

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="container">
          <Route exact path="/" component={Home} />
          <Route path="/Profil" component={Profil} />
          <Route path="/Dodaj" component={Addex} />
          <Route path="/Przegladaj" component={Explore} />
        </div>
      </Router>
    );
  }
}

const wrapper = document.getElementById("app");

wrapper ? ReactDOM.render(<App />, wrapper) : null;

export default App;
