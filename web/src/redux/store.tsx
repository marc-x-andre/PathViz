import { DrawingSpeed, PathfindingAlgorithms, MazeAlgorithms } from "./actions";
import { Grid } from "../algorithm/types";

export interface GridStoreState {
    grid: Grid;
    dimension: { rows: number, columns: number };
}

export interface ConfigStoreState {
    drawingSpeed: DrawingSpeed;
    pathfindingAlgorithms: PathfindingAlgorithms;
    mazeAlgorithms: MazeAlgorithms;

}

export const initialGridState: GridStoreState = {
    grid: new Grid(0, 0),
    dimension: { rows: 0, columns: 0 }
};


export const initialConfigState: ConfigStoreState = {
    drawingSpeed: DrawingSpeed.NORMAL,
    pathfindingAlgorithms: PathfindingAlgorithms.UNKNOWN,
    mazeAlgorithms: MazeAlgorithms.UNKNOWN,
};
