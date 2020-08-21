import { combineReducers } from 'redux';
import drawingSpeed from './drawingSpeed';
import clear from './clear';
import grid from './grid';

export default combineReducers({
    drawingSpeed,
    clear,
    grid
})