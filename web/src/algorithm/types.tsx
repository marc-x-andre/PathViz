
export enum CaseStatus {
    UNVISITED = "unvisited",
    VISITED = "visited",
    WALL = "wall",
    START = "start",
    END = "end",
}

export interface Case {
    status: CaseStatus;
}

export class Grid {
    cases: { [x: number]: { [y: number]: Case; }; } = {};
    dimensionX: number = 0;
    dimensionY: number = 0;

    constructor(dimensionX: number, dimensionY: number) {
        this.dimensionX = dimensionX;
        this.dimensionY = dimensionY;
        this.initCaseList();
    }

    updateCase(x: number, y: number, status?: CaseStatus) {

    }

    private initCaseList() {
        for (let y = 0; y < this.dimensionY; y++) {
            if (!this.cases[y])
                this.cases[y] = []
            for (let x = 0; x < this.dimensionX; x++) {
                this.cases[y][x] = { status: CaseStatus.UNVISITED }
            }
        }
    }
}

