import { DrawingSpeed, Action } from '../actions'
import { initialState, StoreState } from '../store'

const drawingSpeed = (state: StoreState = initialState, action: { type: Action, speed: DrawingSpeed }) => {
    console.log(state);
    if (action.type === Action.UPDATE_SPEED)
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
    return { ...state, drawingSpeed: DrawingSpeed.NORMAL }
}

export default drawingSpeed;