const EASY_MAP = {
    grid: [
        ["empty", "mountain:90", "empty", "empty", "oasis"],
        ["empty", "empty", "empty", "bridge:0", "oasis"],
        ["bridge", "empty", "mountain:180", "empty", "empty"],
        ["empty", "empty", "empty", "oasis", "empty"],
        ["empty", "empty", "mountain:270", "empty", "empty"],
    ],
};

const HARD_MAP = {
    grid: [
        [
            "empty",
            "mountain:90",
            "oasis",
            "oasis",
            "empty",
            "bridge:90",
            "empty",
        ],
        ["bridge", "empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "bridge", "empty", "empty", "empty", "empty"],
        [
            "empty",
            "empty",
            "empty",
            "mountain:270",
            "empty",
            "empty",
            "empty",
        ],
        [
            "mountain:270",
            "empty",
            "mountain:90",
            "empty",
            "bridge:90",
            "empty",
            "oasis",
        ],
        ["empty", "empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "bridge:90", "empty", "empty", "empty"],
    ],
};

const TILE_TYPES = {
    straight_rail: "pics/tiles/straight_rail.png",
    bridge: "pics/tiles/bridge.png",
    bridge_rail: "pics/tiles/bridge_rail.png",
    curve_rail: "pics/tiles/curve_rail.png",
    empty: "pics/tiles/empty.png",
    mountain: "pics/tiles/mountain.png",
    mountain_rail: "pics/tiles/mountain_rail.png",
    oasis: "pics/tiles/oasis.png",
};

const RAIL_TYPES = {
    empty: {
        image: "pics/tiles/empty.png",
        next: "straight_rail",
    },
    straight_rail: {
        image: "pics/tiles/straight_rail.png",
        next: "curve_rail",
        rotations: [0, 90],
    },
    curve_rail: {
        image: "pics/tiles/curve_rail.png",
        next: "empty",
        rotations: [0, 90, 180, 270],
    },
    bridge_rail: {
        image: "pics/tiles/bridge_rail.png",
        next: "bridge",
        rotations: [0, 90],
    },
    mountain_rail: {
        image: "pics/tiles/mountain_rail.png",
        next: "mountain",
        rotations: [0, 90, 180, 270],
    },
};

let selectedDifficulty = null;
let gameTimer;
let startTime;

function selectDifficulty(level) {
    selectedDifficulty = level;
    document.getElementById("easyBtn").classList.remove("selected");
    document.getElementById("hardBtn").classList.remove("selected");
    if (level === "easy") {
        document.getElementById("easyBtn").classList.add("selected");
    } else {
        document.getElementById("hardBtn").classList.add("selected");
    }
}

function showDescription() {
    document.getElementById("descriptionPopup").style.display = "block";
}

function hideDescription() {
    document.getElementById("descriptionPopup").style.display = "none";
}

function showView(viewId) {
    document.querySelectorAll(".view").forEach((view) => {
        view.classList.remove("active");
    });
    document.getElementById(viewId).classList.add("active");
}

function startGame() {
    const playerName = document.getElementById("playerName").value;
    const difficulty = selectedDifficulty;

    if (!playerName || !difficulty) {
        alert("Kérlek, add meg a neved és válassz nehézségi szintet!");
        return;
    }

    showView("gameView");
    initializeGame(playerName, difficulty);
}

function initializeGame(playerName, difficulty) {
    document.getElementById("playerInfo").textContent = playerName;
    const gameBoard = document.getElementById("gameBoard");

    if (difficulty === "easy") {
        gameBoard.style.gridTemplateColumns = `repeat(5, 1fr)`;
        createGrid(gameBoard, EASY_MAP);
    } else {
        gameBoard.style.gridTemplateColumns = `repeat(7, 1fr)`;
        createGrid(gameBoard, HARD_MAP);
    }

    startTimer();
}

function createGrid(gameBoard, mapData) {
    gameBoard.innerHTML = "";

    mapData.grid.forEach((row, i) => {
        row.forEach((cellData, j) => {
            const [cellType, rotation] = cellData.split(":");
            const cell = document.createElement("div");
            cell.className = "game-cell";
            cell.dataset.type = cellType;
            cell.dataset.row = i;
            cell.dataset.col = j;

            if (rotation) {
                cell.dataset.initialRotation = rotation;
                cell.style.transform = `rotate(${rotation}deg)`;
            }

            cell.style.backgroundImage = `url(${TILE_TYPES[cellType]})`;
            gameBoard.appendChild(cell);
        });
    });

    initializeCellHandlers();
}

function initializeCellHandlers() {
    document.querySelectorAll(".game-cell").forEach((cell) => {
        cell.addEventListener("click", handleLeftClick);
        cell.addEventListener("contextmenu", handleRightClick);
        cell.style.transition = "transform 0.3s ease";
    });
}

function handleLeftClick(event) {
    event.preventDefault();
    const cell = event.target;
    const cellType = cell.dataset.type;

    if (cellType === "oasis") {
        return;
    }

    const currentType = cell.dataset.railType || cellType;
    let nextType;

    if (cellType === "bridge" || cellType === "mountain") {
        nextType = currentType === cellType ? `${cellType}_rail` : cellType;
        if (cell.dataset.initialRotation) {
            cell.dataset.rotation = cell.dataset.initialRotation;
            cell.style.transform = `rotate(${cell.dataset.initialRotation}deg)`;
        }
    } else {
        nextType = RAIL_TYPES[currentType].next;
    }

    cell.dataset.railType = nextType;
    cell.style.backgroundImage = `url(${TILE_TYPES[nextType]})`;
    checkGameEnd();
}

function handleRightClick(event) {
    event.preventDefault();
    const cell = event.target;
    const baseType = cell.dataset.type;

    if (baseType === "bridge" || baseType === "mountain") {
        return;
    }

    const currentType = cell.dataset.railType;
    if (!currentType || !RAIL_TYPES[currentType].rotations) return;

    const rotations = RAIL_TYPES[currentType].rotations;
    const currentRotation = parseInt(cell.dataset.rotation || "0");
    const nextRotationIndex =
        (rotations.indexOf(currentRotation) + 1) % rotations.length;
    const nextRotation = rotations[nextRotationIndex];

    cell.dataset.rotation = nextRotation;
    cell.style.transform = `rotate(${nextRotation}deg)`;
    checkGameEnd();
}

function startTimer() {
    startTime = Date.now();
    gameTimer = setInterval(updateTimer, 1000);
}

function updateTimer() {
    const elapsed = Math.floor((Date.now() - startTime) / 1000);
    const minutes = Math.floor(elapsed / 60);
    const seconds = elapsed % 60;
    document.getElementById("gameTimer").textContent = `${minutes
        .toString()
        .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`;
}

function hasUnrailedTiles() {
    const cells = document.querySelectorAll(".game-cell");
    const typesToCheck = ["empty", "mountain", "bridge"];

    for (let cell of cells) {
        const cellType = cell.dataset.type;
        if (typesToCheck.includes(cellType) && !cell.dataset.railType) {
            return true;
        }
    }
    return false;
}

function checkGameEnd() {
    if (!hasUnrailedTiles()) {
        clearInterval(gameTimer);
        const finalTime =
            document.getElementById("gameTimer").textContent;

        alert("Gratulálok, sikeresen összekötötted az összes állomást! Ezzel az idövel: " + finalTime);
        return true;
    }
    return false;
}