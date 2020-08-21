export enum Action {
    UPDATE_SPEED = "UPDATE_SPEED",
    SET_GRID_SIZE = "SET_GRID_SIZE",
    CLEAR = "CLEAR",
}

export enum DrawingSpeed {
    INSTANT = "INSTANT",
    SLOW = "SLOW",
    NORMAL = "NORMAL",
    FAST = "FAST"
}

export enum PathfindingAlgorithms {
    UNKNOWN = "UNKNOWN",
}

export enum MazeAlgorithms {
    UNKNOWN = "UNKNOWN",
}

export const updateSpeed = (speed: DrawingSpeed) => ({
    type: Action.UPDATE_SPEED,
    speed
});

export const setGridSize = (rows: number, columns: number) => ({
    type: Action.SET_GRID_SIZE,
    rows,
    columns,
});