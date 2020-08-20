import { DrawingSpeed, PathfindingAlgorithms, MazeAlgorithms } from "./actions";


export interface StoreState {
    drawingSpeed: DrawingSpeed;
    pathfindingAlgorithms: PathfindingAlgorithms;
    mazeAlgorithms: MazeAlgorithms;
}

export const initialState: StoreState = {
    drawingSpeed: DrawingSpeed.NORMAL,
    pathfindingAlgorithms: PathfindingAlgorithms.UNKNOWN,
    mazeAlgorithms: MazeAlgorithms.UNKNOWN,
};
