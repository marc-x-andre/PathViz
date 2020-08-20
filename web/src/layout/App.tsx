import React from 'react';
import './App.scss';
import Drawer from './Drawer';
import Content from './Content';
import Infobox from './Infobox';


class App extends React.Component {
  render() {
    return (
      <div className="drawer-layout">
        <Drawer></Drawer>
        <Content></Content>
        <Infobox></Infobox>
      </div>
    );
  }
}

export default App;
