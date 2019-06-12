import React from "react";

const Navbar = () => {
  return (
    <nav className="navbar navbar-expand-lg navbar-dark bg-dark navbar-fixed-bottom">
      <button
        className="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarTogglerDemo03"
        aria-controls="navbarTogglerDemo03"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span className="navbar-toggler-icon" />
      </button>
      <a className="navbar-brand" href="#">
        <span className="badge badge-secondary">NPNG</span> 🐗
      </a>

      <div className="collapse navbar-collapse" id="navbarTogglerDemo03">
        <ul className="navbar-nav mr-auto mt-2 mt-lg-0">
          <li className="nav-item active">
            <a className="nav-link" href="/Profil">
              Profil <span className="sr-only">(current)</span>
            </a>
          </li>
          <li className="nav-item active">
            <a className="nav-link" href="/Treninigi">
              Treningi <span class="sr-only">(current)</span>
            </a>
          </li>
          <li className="nav-item active">
            <a className="nav-link" href="/Cwiczenia">
              Ćwiczenia<span class="sr-only">(current)</span>
            </a>
          </li>
          <li className="nav-item active">
            <a className="nav-link" href="/Onas">
              O nas
            </a>
          </li>
          <li className="nav-item active">
            <a className="nav-link" href="/Kontakt">
              Kontakt
            </a>
          </li>
        </ul>
      </div>
    </nav>
  );
};
export default Navbar;
