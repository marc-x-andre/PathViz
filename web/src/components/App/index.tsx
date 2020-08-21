import React from 'react';
import './App.scss';
import Drawer from '../Drawer';
import Infobox from '../Infobox';
import Grid from '../Grid';


class App extends React.Component {
  render() {
    return (
      <div className="drawer-layout">
        <Drawer></Drawer>
        <Grid></Grid>
        <Infobox></Infobox>
      </div>
    );
  }
}

export default App;
