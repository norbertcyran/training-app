import React from "react";
class Register extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      password: "",
      login: "",
      email: ""
    };
  }
  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
  handleSumbit = e => {
    e.preventDefault();
  };
  render() {
    return (
      <div className="col-sm-6 rejestracja">
        <h1>Zarejestruj się.</h1>
        <form>
          <div class="form-group row">
            <label htmlFor="input" className="col-sm-2 col-form-label">
              login
            </label>
            <div class="col-sm-10">
              <input
                name="login"
                type="text"
                className="form-control"
                id="inputNick"
                placeholder="Login"
                value={this.state.login}
                onChange={e => this.handleChange(e)}
              />
            </div>
          </div>
          <div class="form-group row">
            <label htmlFor="email" className="col-sm-2 col-form-label">
              Email
            </label>
            <div class="col-sm-10">
              <input
                name="email"
                type="Email"
                className="form-control"
                id="Email"
                placeholder="Email"
                value={this.state.email}
                onChange={e => this.handleChange(e)}
              />
            </div>
          </div>
          <div class="form-group row">
            <label htmlFor="password" className="col-sm-2 col-form-label">
              Hasło
            </label>
            <div class="col-sm-10">
              <input
                name="password"
                type="password"
                className="form-control"
                id="inputPassword3"
                placeholder="Hasło"
                value={this.state.password}
                onChange={e => this.handleChange(e)}
              />
            </div>
          </div>
          <div className="form-group row ">
            <div className="col-sm-10 guzik">
              <button type="submit" className="btn btn-primary">
                Zarejestruj
              </button>
            </div>
          </div>
        </form>
      </div>
    );
  }
}
export default Register;
