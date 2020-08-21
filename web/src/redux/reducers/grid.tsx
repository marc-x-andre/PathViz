import { Action } from '../actions'
import { initialState, StoreState } from '../store'

const grid = (state: StoreState = initialState, action: { type: Action, rows: number, columns: number }) => {
    if (action.type === Action.SET_GRID_SIZE) {
        console.log(action);
        return { ...state, dimension: { rows: action.rows, columns: action.columns } };
    }
    return { ...state };
}

export default grid;