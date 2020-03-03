describe("application", async () => {
  describe("piazza api", async () => {
    it("test login");
    it("get list of classes");
    it("get user feed");
    it("get all posts from a given course");
  });
  describe("mongodb", async () => {
    it("store notification data", async () => {
        /*
      // let's make a dummy notification and dummy user:
      const userName = "dummyUser";
      const notification = "You should probably READ This: not really";
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
      */
    });
    it("fetch notification data", async () => {});
    it("modify notification data", async () => {});
    it("delete notification data", async () => {});
  });
  describe("data sanitization", async () => {
    it("verify escape characters are filtered to prevent javascript injection");
    it(
      "verify escape characters are filtered to prevent json injection (via mongo)"
    );
  });
  describe("correct data display", async () => {
    it("verify correct amount of notifications is displayed");
    it(
      "verify correct messages are displayed, based on time notification arrived"
    );
    it("verify messages update for new notifications");
  });
});
