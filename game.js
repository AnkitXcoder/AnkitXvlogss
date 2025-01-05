const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");
const GRAVITY = 0.25;
let birdY = canvas.height / 2;
let birdVelocity = 0;
const birdSize = 20;
const pipeWidth = 60;
const pipeGap = 150;
let score = 0;
let pipes = [];
let gameRunning = true;


function createPipe() {
      const pipeHeight = Math.random() * (canvas.height - pipeGap - 100) + 50;
     pipes.push({
         x: canvas.width,
         topHeight: pipeHeight,
        bottomHeight: canvas.height - pipeHeight - pipeGap,
    });
}
function drawBird() {
      ctx.fillStyle = "yellow";
       ctx.beginPath();
        ctx.arc(50, birdY, birdSize, 0, Math.PI * 2);
      ctx.fill();
}

function drawPipes() {
      pipes.forEach((pipe) => {
          ctx.fillStyle = "green";
             ctx.fillRect(pipe.x, 0, pipeWidth, pipe.topHeight);
          ctx.fillRect(pipe.x, canvas.height - pipe.bottomHeight, pipeWidth, pipe.bottomHeight);
    });
}
function movePipes() {
      pipes.forEach((pipe) => {
          pipe.x -= 2;
      });
      pipes = pipes.filter((pipe) => pipe.x + pipeWidth > 0);
}

function checkCollision() {
       if (birdY - birdSize <= 0 || birdY + birdSize >= canvas.height) {
        return true;
    }

    for (let pipe of pipes) {
        if (
            50 + birdSize > pipe.x &&
            50 - birdSize < pipe.x + pipeWidth &&
            (birdY - birdSize < pipe.topHeight || birdY + birdSize > canvas.height - pipe.bottomHeight)
        ) {
            return true;
        }
    }
    return false;
}
function gameLoop() {
    if (!gameRunning) return;

    ctx.clearRect(0, 0, canvas.width, canvas.height);
    birdVelocity += GRAVITY;
      birdY += birdVelocity;
      drawBird();
    drawPipes();
      movePipes();
      if (checkCollision()) {
          gameRunning = false;
           alert(`Game Over! Your score: ${score}`);
        document.location.reload();
    }
         if (pipes.length === 0 || pipes[pipes.length - 1].x < canvas.width - 200) {
        createPipe();
    }

    pipes.forEach((pipe) => {
        if (pipe.x === 50) {
            score++;
        }
    });
    ctx.fillStyle = "black";
     ctx.font = "20px Arial";
    ctx.fillText(`Score: ${score}`, 10, 20);

      requestAnimationFrame(gameLoop);
}
document.addEventListener("keydown", (e) => {
    if (e.code === "Space") {
        birdVelocity = -6;
    }
});
gameLoop();
