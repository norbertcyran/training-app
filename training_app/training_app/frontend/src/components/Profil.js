import React from "react";
import Navbar from "./Navbar";

class Profil extends React.Component {
  render() {
    return (
      <>
        {document.body.classList.remove("dodajcwiczenie_tlo")}
        {document.body.classList.remove("home")}
        {document.body.classList.add("profil")}
        <Navbar />
      </>
    );
  }
}
export default Profil;