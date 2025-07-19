const express = require("express");
const app = express();
app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ status: "Lyra.Stack online" });
});

app.post("/logDecision", (req, res) => {
  const decision = req.body;
  console.log("Logged decision:", decision);
  res.json({ status: "logged", input: decision });
});

app.listen(8081, () => {
  console.log("Lyra.Stack running on port 8081");
});