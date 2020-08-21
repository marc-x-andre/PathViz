import { DrawingSpeed, PathfindingAlgorithms, MazeAlgorithms } from "./actions";


export interface StoreState {
    drawingSpeed: DrawingSpeed;
    pathfindingAlgorithms: PathfindingAlgorithms;
    mazeAlgorithms: MazeAlgorithms;
    dimension: { rows: number, columns: number };
}

export const initialState: StoreState = {
    drawingSpeed: DrawingSpeed.NORMAL,
    pathfindingAlgorithms: PathfindingAlgorithms.UNKNOWN,
    mazeAlgorithms: MazeAlgorithms.UNKNOWN,
    dimension: { rows: 0, columns: 0 }
};
