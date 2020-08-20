import React from 'react';
import { updateSpeed } from '../../redux/actions'
import { StoreState } from '../../redux/store';
import { connect } from 'react-redux';
import './Grid.scss'

const BoxSizePx = 24;

interface GridState {
  gridElement: Element
}

interface GridProps {
  updateSpeed: Function
}

class Grid extends React.Component<GridProps, GridState> {

  componentDidMount() {
    this.setState({ gridElement: document.getElementById('grid') as Element }, () => this.computeGrid());
    window.addEventListener('resize', this.computeGrid);
  }

  computeGrid() {
    const rows = Math.ceil(this.state.gridElement.clientHeight / BoxSizePx);
    const colunms = Math.ceil(this.state.gridElement.clientWidth / BoxSizePx);
    console.log({ rows, colunms });

  }

  render() {
    return (
      <div className="grid" id="grid">
        <div className="box" style={{ "width": "24px", "height": "24px" }}></div>
      </div>
    );
  }
}

const mapStateToProps = (state: StoreState) => {
  return { state: state.drawingSpeed }
}

const mapDispatchToProps: GridProps = { updateSpeed };

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Grid);
