import React from "react";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Navbar from "./Navbar";
import "./styles.css";

const Explore = () => (
  <>
    <Navbar />
    <div className="table">
      <DataProvider
        endpoint="api/exercises/"
        render={data => <Table data={data} />}
      />
    </div>
  </>
);

export default Explore;
