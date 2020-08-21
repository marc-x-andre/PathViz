export enum CaseStatus {
    VISITED = "visited",
    UNVISITED = "unvisited",
}

export enum CaseType {
    WALL = "wall",
    START = "start",
    END = "end",
}

export interface Case {
    status: CaseStatus;
    type: CaseType;
}

export class Grid {
    cases: { [x: number]: { [y: number]: Case; }; } = {};
    dimensionX: number = 0;
    dimensionY: number = 0;

    constructor(dimensionX: number, dimensionY: number) {
        this.dimensionX = dimensionX;
        this.dimensionY = dimensionY;
        this.createCaseList();
        this.cases[9][2]
    }

    updateCase(x: number, y: number, status?: CaseStatus, type?: CaseType) {

    }

    private createCaseList() {
        for (let y = 0; y < this.dimensionY; y++) {
            for (let x = 0; x < this.dimensionX; x++) {
                // TODO
            }
        }
    }
}

