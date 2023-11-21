const express = require("express");
const mysql = require("mysql2");
const cors = require("cors");

const app = express();
app.use(cors());

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Abhi@0405",
  database: "football_stats",
});

db.connect((err) => {
  if (err) {
    console.error("Database connection error:", err);
    return;
  }
  console.log("Connected to the database");
});

app.get("/", (req, res) => {
  return res.json("From Backend Side");
});

app.get("/assists", (req, res) => {
  const sql = "SELECT * FROM assists";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});

app.get("/clean_sheets", (req, res) => {
  const sql = "SELECT * FROM clean_sheets";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/goals", (req, res) => {
  const sql = "SELECT * FROM goals";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/inter_club_tour_stats", (req, res) => {
  const sql = "SELECT * FROM inter_club_tour_stats";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/inter_stats", (req, res) => {
  const sql = "SELECT * FROM inter_stats";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/manager", (req, res) => {
  const sql = "SELECT * FROM manager";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/player_stats", (req, res) => {
  const sql = "SELECT * FROM player_stats";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/points_table", (req, res) => {
  const sql = "SELECT * FROM points_table";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
app.get("/join", (req, res) => {
  const sql =
    "SELECT S.Rank, S.Player, S.Country, S.Club_Name, S.Goals, M.MANAGER AS Manager FROM Inter_Club_Tour_Stats S JOIN manager M ON S.Club_Name = M.Club_Name";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});



app.get("/player/count", (req, res) => {
  const sql =
    
    "SELECT inter_club_tour_stats.Player,COUNT(inter_stats.SL_No) as Count FROM inter_stats INNER JOIN inter_club_tour_stats ON inter_stats.SL_No = inter_club_tour_stats.SL_No;";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});

app.get("/nest", (req, res) => {
  const sql =
    
    "select P_Name,Goals from goals WHERE Goals>10 and SL_No IN ( SELECT SL_No from assists where Assists>5 );";
  db.query(sql, (err, data) => {
    if (err) throw err;
    return res.json(data);
  });
});
// Port of server
app.listen(8081, () => {
  console.log(`Server is running on port ${8081}`);
});
