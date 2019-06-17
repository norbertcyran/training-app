import React from "react";
import { BrowserRouter as Router, Link, Route } from "react-router-dom";
import "../App.css";
import Home from "./Home";
import Profil from "./Profil";
import Addex from "./Addex";

class App extends React.Component {
  render() {
    return (
      <Router>
        <div className="container">
          <Route exact path="/" component={Home} />
          <Route path="/Profil" component={Profil} />
          <Route path="/Dodaj" component={Addex} />
        </div>
      </Router>
    );
  }
}
export default App;
