import { Action } from '../actions'
import { initialConfigState, ConfigStoreState } from '../store'

const config = (state: ConfigStoreState = initialConfigState, action: { type: Action, clearType: string }) => {
    if (action.type === Action.CLEAR)
        return { ...state }
    return state
}

export default config;