import React from "react";
class Login extends React.Component {
  state = {
    password: "",
    login: "",
    email: "",
    remind: false
  };
  handleChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };
  handleSumbit = e => {
    e.preventDefault();
  };
  handleRemind = () => {
    this.setState({ remind: !this.state.remind });
  };
  render() {
    return (
      <>
        <div className="col-sm-6 login">
          <h1>Zaloguj się.</h1>
          <form onSumbit={this.handleSumbit}>
            <div className="form-group row">
              <label htmlFor="login" className="col-sm-2 col-form-label">
                Login
              </label>
              <div className="col-sm-10">
                <input
                  className="form-control"
                  name="login"
                  type="text"
                  value={this.state.login}
                  onChange={e => this.handleChange(e)}
                  placeholder="Login"
                />
              </div>
            </div>
            <div className="form-group row">
              <label htmlFor="password" className="col-sm-2 col-form-label">
                Hasło
              </label>
              <div className="col-sm-10">
                <input
                  className="form-control"
                  name="password"
                  type="password"
                  value={this.state.password}
                  onChange={e => this.handleChange(e)}
                  placeholder="Hasło"
                />
              </div>
            </div>
            <div className="form-group row ">
              <div className="col-sm-2 ">
                <button type="submit" className="btn btn-primary">
                  Zaloguj
                </button>
              </div>
            </div>
          </form>
          <div className="form-group row ">
            <div className="col-sm-4">
              <button
                onClick={this.handleRemind}
                className="btn btn-primary przypomnij"
              >
                Zapomniałeś hasło?
              </button>
            </div>
          </div>
          {this.state.remind ? (
            <Remind email={this.state.email} onClick={this.handleChange} />
          ) : (
            false
          )}
        </div>
      </>
    );
  }
}

const Remind = props => {
  return (
    <div className="Odzysk">
      <div className="odzyskaj container">
        <h1>Odzyskiwanie hasła!</h1>
        <p>
          Poniżej wpisz mail na któy zakładane było konto, a przyślemy na niego
          przypisane do konta hasło.
        </p>
        <form>
          <div className="form-group row">
            <label for="email" className="col-sm-2 col-form-label">
              Email
            </label>
            <div className="col-sm-10">
              <input
                name="email"
                type="Email"
                className="form-control"
                id="Email"
                placeholder="jankowalski@poczta.pl"
                value={props.email}
                onChange={e => props.onClick(e)}
              />
            </div>
            <div className="form-group row ">
              <div className="col-sm-10">
                <button
                  type="submit"
                  className="przypomnij_btn btn btn-primary"
                >
                  Przypomnij
                </button>
              </div>
            </div>
          </div>
        </form>
      </div>
    </div>
  );
};
export default Login;
