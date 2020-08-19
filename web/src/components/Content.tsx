import React from 'react';
import logo from '../logo.svg';
import './Content.scss';

function Content() {
  return (
    <div className="content container-fluid">
      <img src={logo} className="app-logo" alt="logo" />
    </div>
  );
}

export default Content;
