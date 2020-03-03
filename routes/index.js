/* eslint-disable no-unused-vars */
const express = require("express");

const router = express.Router();

const { MongoClient } = require("mongodb");

function addToDB(dbName, collectionName, testInput) {
  const uri =
    "mongodb+srv://devUser:thedumb0nes@uischoolnotifier-kvtkn.gcp.mongodb.net/test?retryWrites=true&w=majority";
  const client = new MongoClient(uri, { useNewUrlParser: true });
  client.connect(err => {
    if (err) {
      console.log("Error connecting to database");
    } else {
      const collection = client.db(dbName).collection(collectionName);
      // perform actions on the collection object
      collection.insertOne({ input: testInput }, err2 => {
        if (err2) {
          console.log("Error adding input to database");
        } else {
          console.log(`added ${testInput} to database`);
        }
      });
    }
    client.close();
  });
}

function fetchDB(dbName, collectionName) {
  // let retStr = "";
  const uri =
    "mongodb+srv://devUser:thedumb0nes@uischoolnotifier-kvtkn.gcp.mongodb.net/test?retryWrites=true&w=majority";
  const client = new MongoClient(uri, {
    useNewUrlParser: true,
    useUnifiedTopology: true
  });
  client.connect(err => {
    if (err) {
      console.log("Error connecting to database");
      client.close();
    } else {
      const collection = client.db(dbName).collection(collectionName);
      // perform actions on the collection object
      collection
        .find()
        .toArray()
        .then(value => {
          console.log(value);
        })
        .catch(err2 => {
          console.log(err2);
          client.close();
        });
    }
  });
}

const path = require("path");
const { spawn } = require("child_process");

// learned how to call python script from node from:
// https://www.ivarprudnikov.com/nodejs-server-running-python-scripts/#run-python-script
function callPiazza() {
  return spawn("python3", ["-u", path.join(__dirname, "piazza.py")]);
}

function attempt() {
  // let curPacket = 0;
  const dataArr = [];
  // console.log("hi");
  const subprocess = callPiazza();
  // print output of script
  subprocess.stdout.on("data", data => {
    // curPacket += 1;
    // console.log(`data:${data}`);
    let datap = data;
    datap = datap.toString();
    datap = datap.slice(0, -1);
    dataArr.push(datap);
    // console.log("hi\n\n");
    // console.log(datap);
    // datap = datap.split("\[*\]", 1);
    // const subject = datap[1].split("'subject': *,");
    // console.log(datap.length);
    // console.log(subject);
  });
  subprocess.stderr.on("data", data => {
    // console.log(`error:${data}`);
  });
  subprocess.on("close", () => {
    // console.log("Closed");
    // console.log(dataArr);
    // let temp = dataarr[0];
    // temp = temp.slice(2,-2);
    // temp.replace("")
    // temp = temp.split(/, (?=[^,]+:)/).map(s => s.split(': '));
    // console.log(temp);
    /*
    let temp = dataarr[0];
    temp = temp.slice(2, -2);
    temp = temp.replace(/'/g, "");
    const table = temp.split(", ").map(pair => pair.split(": "));

    const result = {};
    table.forEach(([key, value]) => {
      result[key] = value;
    });
    console.log(temp);
    console.log(table);
    console.log(result);
    */

    const postArr = [];

    /*
    for (let i = 1; i < dataArr.length; i += 1) {
      let temp = dataArr[i];
      temp = temp.slice(1, -1);
      temp = temp.replace(/'/g, "");
      const table = temp.split(", ").map(pair => pair.split(": "));
      const result = {};
      table.forEach(([key, value]) => {
        result[key] = value;
      });

      postArr.push(result);
    }
    */

    for (let i = 1; i < dataArr.length; i += 1) {
      postArr.push(dataArr[i].slice(1, -1));
    }

    // return postArr;
  });
  // console.log("byte");
}

/* GET home page. */
router.get("/", (req, res, next) => {
  attempt();
  res.render("index");
});

router.post("/testInput", (req, res) => {
  console.log(req.body);
  const { theInput } = req.body;
  // addToDB("test1","testInput", theInput);
  fetchDB("test1", "testInput");
  res.render("testOutput", { output: theInput });
});

module.exports = router;
