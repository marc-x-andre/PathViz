import { Action, DrawingSpeed } from '../actions'
import { initialGridState, GridStoreState } from '../store'
import { Grid } from '../../algorithm/types';

const grid = (state: GridStoreState = initialGridState, action: { type: Action, rows: number, columns: number, speed: DrawingSpeed }) => {
    if (action.type === Action.SET_GRID_SIZE) {
        return {
            ...state,
            dimension: { rows: action.rows, columns: action.columns },
            grid: new Grid(action.rows, action.columns)
        };
    }
    else if (action.type === Action.UPDATE_SPEED)
        switch (action.speed) {
            case DrawingSpeed.SLOW:
                return { ...state, drawingSpeed: DrawingSpeed.SLOW }
            case DrawingSpeed.NORMAL:
                return { ...state, drawingSpeed: DrawingSpeed.NORMAL }
            case DrawingSpeed.FAST:
                return { ...state, drawingSpeed: DrawingSpeed.FAST }
            default:
                return { ...state, drawingSpeed: DrawingSpeed.NORMAL }
        }
    return state
}

export default grid;