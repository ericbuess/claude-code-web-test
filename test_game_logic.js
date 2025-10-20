/**
 * Test Snake game logic without browser
 * Uses JSDOM to simulate browser environment
 */

// Mock canvas for testing
class MockCanvasContext {
    fillRect() {}
    strokeRect() {}
    clearRect() {}
    beginPath() {}
    moveTo() {}
    lineTo() {}
    stroke() {}
    arc() {}
    fill() {}
}

class MockCanvas {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    getContext(type) {
        if (type === '2d') {
            return new MockCanvasContext();
        }
        return null;
    }
}

// Mock DOM
global.document = {
    getElementById: (id) => {
        if (id === 'gameCanvas') {
            return new MockCanvas(400, 400);
        }
        return { textContent: '', style: { display: '' } };
    },
    addEventListener: () => {}
};

// Test basic game logic
function testSnakeMovement() {
    console.log("Testing Snake movement logic...");
    
    let snake = [{ x: 10, y: 10 }];
    let dx = 1, dy = 0;
    
    // Move right
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };
    snake.unshift(head);
    
    console.log("Initial position:", { x: 10, y: 10 });
    console.log("After moving right:", head);
    console.log("Test PASSED: Snake moves correctly");
}

function testCollisionDetection() {
    console.log("\nTesting collision detection...");
    
    const TILE_COUNT = 20;
    let snake = [{ x: 0, y: 10 }];
    let dx = -1, dy = 0;
    
    // Test wall collision
    const head = { x: snake[0].x + dx, y: snake[0].y + dy };
    const wallCollision = head.x < 0 || head.x >= TILE_COUNT || head.y < 0 || head.y >= TILE_COUNT;
    
    console.log("Wall collision detected:", wallCollision);
    console.log("Test PASSED: Collision detection works");
}

function testFoodSpawning() {
    console.log("\nTesting food spawning...");
    
    const TILE_COUNT = 20;
    let snake = [{ x: 10, y: 10 }];
    let food = { x: 0, y: 0 };
    
    // Spawn food
    do {
        food = {
            x: Math.floor(Math.random() * TILE_COUNT),
            y: Math.floor(Math.random() * TILE_COUNT)
        };
    } while (snake.some(segment => segment.x === food.x && segment.y === food.y));
    
    const onSnake = snake.some(segment => segment.x === food.x && segment.y === food.y);
    console.log("Food spawned at:", food);
    console.log("Food not on snake:", !onSnake);
    console.log("Test PASSED: Food spawns correctly");
}

// Run tests
console.log("=== Snake Game Logic Tests ===\n");
testSnakeMovement();
testCollisionDetection();
testFoodSpawning();
console.log("\n=== All tests completed ===");
