export enum Action {
    UPDATE_SPEED = "UPDATE_SPEED",
    CLEAR = "CLEAR",
}

export enum DrawingSpeed {
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
    type: 'UPDATE_SPEED',
    speed
})
