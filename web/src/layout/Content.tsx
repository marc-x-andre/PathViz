import React from 'react';
import './Content.scss';
import Grid from '../components/Grid';

function Content() {
  return (
    <div className="content container-fluid">
      {/* <img src={logo} className="app-logo" alt="logo" /> */}
      <Grid></Grid>
    </div>
  );
}

export default Content;
