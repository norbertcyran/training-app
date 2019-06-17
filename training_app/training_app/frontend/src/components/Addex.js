import React from "react";
import { BrowserRouter as Router, Link, Route } from "react-router-dom";
import "./styles.css";

class Addex extends React.Component {
  state = {
    name: "",
    description: "",
    muscles: "",
    obrazek: []
  };
  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
  render() {
    return (
      <>
        {document.body.classList.remove("home")}
        {document.body.classList.remove("profil")}
        {document.body.classList.add("dodajcwiczenie_tlo")}
        <div className="container dodajcwiczenie_okienko">
          <h1>Dodaj ćwiczenie</h1>
          <div className="container dodajcwiczenie_form">
            Angażowany mięsień
            <div className="input-group mb-3">
              <div className="input-group-prepend">
                <span
                  className="input-group-text"
                  id="inputGroup-sizing-default"
                />
              </div>
              <input
                type="text"
                name="muscles"
                className="form-control"
                aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default"
                value={this.state.muscles}
                onChange={e => this.handleChange(e)}
              />
            </div>
            Nazwa ćwiczenia
            <div className="input-group mb-3">
              <div className="input-group-prepend">
                <span
                  className="input-group-text"
                  id="inputGroup-sizing-default"
                />
              </div>
              <input
                type="text"
                name="name"
                className="form-control"
                aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default"
                value={this.state.name}
                onChange={e => this.handleChange(e)}
              />
            </div>
            Opis ćwiczenia
            <div className="input-group mb-3">
              <div className="input-group-prepend">
                <span
                  className="input-group-text"
                  id="inputGroup-sizing-default"
                />
              </div>
              <input
                type="text"
                name="description"
                className="form-control"
                aria-label="Sizing example input"
                aria-describedby="inputGroup-sizing-default"
                value={this.state.description}
                onChange={e => this.handleChange(e)}
              />
            </div>
            Dodaj obrazek
            <div className="input-group mb-3">
              <div className="input-group-prepend">
                <span className="input-group-text" id="inputGroupFileAddon01" />
              </div>
              <div className="custom-file">
                <input
                  type="file"
                  name="obrazek"
                  className="custom-file-input"
                  id="inputGroupFile01"
                  aria-describedby="inputGroupFileAddon01"
                  value={this.state.obrazek}
                  onChange={e => this.handleChange(e)}
                />
                <label className="custom-file-label" for="inputGroupFile01">
                  Wybierz plik
                </label>
              </div>
            </div>
            <button type="button" className="btn btn-light">
              Dodaj
            </button>
            <button type="button" className="btn btn-light btn_cofnij">
              <Link to="/profil">Cofnij</Link>
            </button>
          </div>
        </div>
      </>
    );
  }
}
export default Addex;
