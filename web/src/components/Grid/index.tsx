import React from 'react';
import { setGridSize } from '../../redux/actions'
import { StoreState } from '../../redux/store';
import { connect } from 'react-redux';
import './Grid.scss'

const BoxSizePx = 24;
const BoxBorderPx = 1;

interface GridState {
  gridElement: Element;
  dimension: { rows: number, columns: number };
  htmlGrid: any[];
}

interface GridProps {
  setGridSize: typeof setGridSize
}

class Grid extends React.Component<GridProps, GridState> {

  caseStyle = {
    "width": `${BoxSizePx - (BoxBorderPx * 2)}px`,
    "height": `${BoxSizePx - (BoxBorderPx * 2)}px`,
    "borderWidth": `${BoxBorderPx}px`
  };

  constructor(props: GridProps) {
    super(props);
    this.state = {
      gridElement: (null as any),
      dimension: { rows: 0, columns: 0 },
      htmlGrid: []
    };
  }

  handleClick(e: Element) {
    console.log(e);
    if (e.classList.contains("wall"))
      e.classList.remove("wall")
    else
      e.classList.add("wall");
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

const mapStateToProps = (state: StoreState) => {
  return { state: state.drawingSpeed }
}

const mapDispatchToProps: GridProps = { setGridSize };

export default connect(
  mapStateToProps,
  mapDispatchToProps
)(Grid);
