const http = require("http");
const hostname = "localhost";
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader("Content-Type", "text/plain");
  res.end("Hello, World!\n");

  if (req.url === "/about") {
    res.end("Acout Page\n");
  } else if (req.url === "/contact") {
    res.end("Contact Page\n");
  } else {
    res.end("Hello, world!\n");
  }
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
