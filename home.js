const el = document.getElementById('rainbow-js');
    let hue = 0;

    setInterval(() => {
      hue = (hue + 1) % 360; // 0–359
      el.style.color = `hsl(${hue}, 100%, 50%)`;
    }, 20);
