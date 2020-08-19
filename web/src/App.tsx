import React from 'react';
import './App.scss';
import Drawer from './components/Drawer';
import Content from './components/Content';
import Infobox from './components/Infobox';

function App() {
  return (
    <div className="drawer-layout">
      <Drawer></Drawer>
      <Content></Content>
      <Infobox></Infobox>
    </div>
  );
}

export default App;
