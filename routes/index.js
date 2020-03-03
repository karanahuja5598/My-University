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
    } 
    else {
      const collection = client.db(dbName).collection(collectionName);
      // perform actions on the collection object
      collection.insertOne({ input: testInput }, err2 => {
        if (err2) {
          console.log("Error adding input to database");
        } 
        else {
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
    } 
    else {
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

/* GET home page. */
router.get("/", (req, res, next) => {
  res.render("index");
});

router.post("/testInput", (req, res) => {
  console.log(req.body);
  const { theInput } = req.body;
  // addToDB("test1","testInput", theInput);
  fetchDB("test1","testInput");
  res.render("testOutput", { output: theInput });
});

module.exports = router;
