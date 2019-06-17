import React from "react";
import DataProvider from "./DataProvider";
import Table from "./Table";

const Explore = () => (
  <DataProvider
    endpoint="api/exercises/"
    render={data => <Table data={data} />}
  />
);

export default Explore;
