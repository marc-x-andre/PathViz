import React from 'react';
import { setGridSize } from '../../redux/actions'
import { connect } from 'react-redux';
import './Mazeboard.scss'
import { Grid } from '../../algorithm/types';

const BoxSizePx = 24;
const BoxBorderPx = 1;

interface MazeboardState {
  grid: Grid;
  gridElement: Element;
  dimension: { rows: number, columns: number };
  htmlGrid: any[];
  toggling: boolean;
}

interface MazeboardProps {
  setGridSize: typeof setGridSize
}

class Mazeboard extends React.Component<MazeboardProps, MazeboardState> {

  caseStyle = {
    "width": `${BoxSizePx - (BoxBorderPx * 2)}px`,
    "height": `${BoxSizePx - (BoxBorderPx * 2)}px`,
    "borderWidth": `${BoxBorderPx}px`
  };

  constructor(props: MazeboardProps) {
    super(props);
    this.state = {
      grid: new Grid(0, 0),
      gridElement: (null as any),
      dimension: { rows: 0, columns: 0 },
      htmlGrid: [],
      toggling: false
    };
  }

  handleClick(e: Element) {
    console.log("handleClick");
    if (e.classList.contains("wall"))
      e.classList.remove("wall")
    else
      e.classList.add("wall");
  }

  handleContinuousClick(e: Element, state: "up" | "down") {
    console.log("handleContinuousClick");
    this.setState({ toggling: (state === "up") ? false : true });
  }

  handleMoveClick(e: Element) {
    console.log("handleMoveClick");
  }

  handleMoveHover(e: Element) {
    console.log("handleMoveHover");
    if (this.state.toggling) {
      if (e.classList.contains("wall"))
        e.classList.remove("wall")
      else
        e.classList.add("wall");
    }
  }

  componentDidMount() {
    this.setState({ gridElement: document.getElementById('grid') as Element }, () => this.computeGrid());
    // window.addEventListener('resize', this.computeGrid);
  }

  computeGrid() {
    const columns = Math.ceil(this.state.gridElement.clientHeight / BoxSizePx) - 1;
    const rows = Math.ceil(this.state.gridElement.clientWidth / BoxSizePx) - 1;
    const htmlGrid: any[] = [];
    for (let c = 0; c < columns; c++) {
      const row = [];
      for (let r = 0; r < rows; r++) {
        row.push(
          <td
            id={`${c}-${r}`} key={r}
            style={this.caseStyle}
            onClick={((e) => this.handleClick(e.target as any))}
            onMouseDown={((e) => this.handleContinuousClick(e.target as any, 'down'))}
            onMouseUp={((e) => this.handleContinuousClick(e.target as any, 'up'))}
            onMouseEnter={((e) => this.handleMoveHover(e.target as any))}
          ></td>
        );
      }
      htmlGrid.push(<tr key={c}>{row}</tr>);
    }
    this.props.setGridSize(rows, columns);
    this.setState({ htmlGrid, dimension: { rows, columns } })
  }

  render() {
    return (
      <div className="grid-container">
        <div className="grid" id="grid">
          <table>
            <tbody>
              {this.state.htmlGrid}
            </tbody>
          </table>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state: any) => {
  return { grid: state.grid }
}

const mapDispatchToProps: MazeboardProps = { setGridSize };

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Mazeboard);
