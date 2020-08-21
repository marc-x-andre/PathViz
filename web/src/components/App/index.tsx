import React from 'react';
import './App.scss';
import Drawer from '../Drawer';
import Infobox from '../Infobox';
import Mazeboard from '../Mazeboard';


class App extends React.Component {
  render() {
    return (
      <div className="drawer-layout">
        <Drawer></Drawer>
        <Mazeboard></Mazeboard>
        <Infobox></Infobox>
      </div>
    );
  }
}

export default App;
