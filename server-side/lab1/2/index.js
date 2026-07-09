const express = require("express");
const app = express();
const PORT = 3000;

app.get("/", (req, res) => {
  res.send(`
    <h1>สวัสดีครับ จากภายใน Docker Container</h1>
    <p><b>ชื่อขนามสกุล:</b> นายพิสิษฐ์ภณ จันทร</p>
    <p><b>รหัสนักศ฿กษา:</b> 67070119</p>
  `);
});

app.listen(PORT, () => console.log(`http:localhost:${PORT}`));
