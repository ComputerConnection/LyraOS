const express = require("express");
const axios = require("axios");

const PORT = 8081;
const CORE_URL = process.env.CORE_URL || "http://lyra-core:8080";

const app = express();
app.use(express.json());

app.get("/health", (req, res) => {
  res.json({ status: "Lyra.Stack online" });
});

app.post("/runQuote", async (req, res) => {
  try {
    const response = await axios.post(`${CORE_URL}/generateQuote`, req.body);
    res.json(response.data);
  } catch (err) {
    console.error(err.response?.data || err.message);
    res.status(err.response?.status || 500).json({
      error: "Quote generation failed",
      detail: err.response?.data || err.message
    });
  }
});

app.listen(PORT, () =>
  console.log(`Lyra.Stack listening on http://localhost:${PORT}`)
);
