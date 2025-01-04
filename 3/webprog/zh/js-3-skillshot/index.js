const canvas = document.querySelector("canvas");
const ctx = canvas.getContext("2d");

const mage = {
  x: 200,
  y: 400,
  width: 100,
  height: 100,
  img: new Image(),
};

const target = {
  x: 0,
  vx: 50,
  y: 50,
  width: 40,
  height: 60,
  rootedUntil: null,
  img: new Image(),
};

mage.img.src = "mage.png";
target.img.src = "target.png";

function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function update(dt) {
}

let last = performance.now();

function next() {
  const now = performance.now();
  const dt = (now - last) / 1000;
  update(dt);
  render();
  last = now;
  requestAnimationFrame(next);
}

next();

function getInitialProjectileData(e) {
  return {
    x: 250,
    y: 400,
    r: 15,
    vx:
      300 *
      Math.cos(Math.atan((400 - e.offsetY) / (250 - e.offsetX))) *
      (e.offsetX < 250 ? -1 : 1),
    vy:
      300 *
      Math.sin(Math.atan((400 - e.offsetY) / (250 - e.offsetX))) *
      (e.offsetX < 250 ? -1 : 1),
  };
}

function checkCollision(circle, rectangle) {
  const closestX = Math.max(
    rectangle.x,
    Math.min(circle.x, rectangle.x + rectangle.width)
  );
  const closestY = Math.max(
    rectangle.y,
    Math.min(circle.y, rectangle.y + rectangle.height)
  );
  const distanceX = circle.x - closestX;
  const distanceY = circle.y - closestY;
  return distanceX ** 2 + distanceY ** 2 <= circle.r ** 2;
}