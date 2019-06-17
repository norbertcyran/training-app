import React from "react";
import DataProvider from "./DataProvider";
import Table from "./Table";
import Navbar from "./Navbar";

const Explore = () => (
  <>
    <Navbar />
    <DataProvider
      endpoint="api/exercises/"
      render={data => <Table data={data} />}
    />
  </>
);

export default Explore;
