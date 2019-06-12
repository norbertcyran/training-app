import Navbar from "./Navbar";

class Profil extends React.Component {
  render() {
    return (
      <>
        {document.body.classList.add("profil")}
        <Navbar />
      </>
    );
  }
}
