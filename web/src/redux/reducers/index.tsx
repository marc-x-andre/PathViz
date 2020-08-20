import { combineReducers } from 'redux';
import drawingSpeed from './drawingSpeed';
import clear from './drawingSpeed';

export default combineReducers({
    drawingSpeed,
    clear
})