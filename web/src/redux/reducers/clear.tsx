import { Action } from '../actions'
import { initialState, StoreState } from '../store'

const clear = (state: StoreState = initialState, action: { type: Action, clearType: string }) => {
    if (action.type === Action.CLEAR)
        return { ...state }
    return { ...state }
}

export default clear;