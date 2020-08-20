import React from 'react';
import './Drawer.scss';
import { connect } from 'react-redux';
import { updateSpeed, DrawingSpeed } from '../redux/actions'
import { StoreState } from '../redux/store'
import Icon from '../components/Icon';

interface DrawerProps {
  updateSpeed: Function
}

const mapStateToProps = (state: StoreState) => {
  return { state: state.drawingSpeed }
}

const mapDispatchToProps: DrawerProps = { updateSpeed };

class Drawer extends React.Component<DrawerProps> {

  handleUpdateSpeed = () => {
    this.props.updateSpeed(DrawingSpeed.FAST);
  };

  render() {
    return (
      <div className="drawer container-fluid">
        <h1>Welcome to PathViz</h1>
        <p>Create, Solve, Enjoy</p>
        <hr />
        {/* TODO create router */}
        <a href="#1" className="drawer-item">
          <Icon type="map-marker-path"></Icon>
          <span className="item-text">Algorithms</span>
        </a>
        <a href="#1" className="drawer-item">
          <Icon type="checkerboard"></Icon>
          <span className="item-text">Maze</span>
        </a>
        <a href="#1" className="drawer-item" onClick={this.handleUpdateSpeed}>
          <Icon type="speedometer"></Icon>
          <span className="item-text">Speed</span>
        </a>
        <a href="#1" className="drawer-item">
          <Icon type="nuke"></Icon>
          <span className="item-text">Clear</span>
        </a>
        <a href="#1" className="drawer-item primary">
          <Icon type="arrow-decision"></Icon>
          <span className="item-text">Resolve</span>
        </a>

        <div className="bottom-section mt-auto w-100">
          <a href="#1" className="drawer-item">
            <Icon type="cog"></Icon>
            <span className="item-text">Settings</span>
          </a>
          <hr />
          <div className="socials">
            <a href="#1" className="socials-link">
              <Icon type="github"></Icon>
            </a>
            <a href="#1" className="socials-link">
              <Icon type="account-group"></Icon>
            </a>
          </div>
        </div>
      </div>
    );
  }
}

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Drawer);
