let tg = window.Telegram.WebApp;
tg.expand();

const canvas = document.getElementById("gameCanvas");
const ctx = canvas.getContext("2d");

// Hintergrundbild einfügen
let background = new Image();
background.src = "/mnt/data/A_cartoon-style_fantasy_landscape_seen_from_a_firs.png";

// Drachenflügel & Hörner für Ich-Perspektive
let dragon = { x: 350, y: 500, width: 100, height: 100, img: new Image() };
dragon.img.src = "/mnt/data/A_cartoon-style_first-person_perspective_of_a_drag.png";

// Feueranimation
let fire = null;
let fireImg = new Image();
fireImg.src = "fire.png"; // Ersetze mit deiner Feuer-Grafik

// Schatzkisten mit verschiedenen Schadensstufen
let crates = [
    { x: 300, y: 250, width: 60, height: 60, health: 3, img: new Image() },
    { x: 450, y: 250, width: 60, height: 60, health: 3, img: new Image() }
];
crates.forEach(crate => crate.img.src = "/mnt/data/A_cartoon-style_treasure_chest_with_a_fantasy_desi.png");

function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.drawImage(background, 0, 0, canvas.width, canvas.height);
    ctx.drawImage(dragon.img, dragon.x, dragon.y, dragon.width, dragon.height);
    
    crates.forEach(crate => {
        if (crate.health > 0) {
            ctx.drawImage(crate.img, crate.x, crate.y, crate.width, crate.height);
        }
    });
    
    if (fire) {
        ctx.drawImage(fireImg, fire.x, fire.y, fire.width, fire.height);
        fire.y -= 10;
        
        crates.forEach(crate => {
            if (fire && fire.y < crate.y + crate.height && fire.x > crate.x && fire.x < crate.x + crate.width) {
                fire = null;
                crate.health -= 1;
                if (crate.health <= 0) {
                    crate.x = Math.random() * 700;
                    crate.health = 3;
                }
            }
        });
    }
    requestAnimationFrame(draw);
}

document.getElementById("fireButton").addEventListener("click", function() {
    if (!fire) {
        fire = { x: 400, y: 500, width: 20, height: 40 };
    }
});

draw();
