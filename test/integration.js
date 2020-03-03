describe("application", async () => {
  describe("piazza api", async () => {
    it("test login");
    it("get list of classes");
    it("get user feed");
    it("get all posts from a given course");
  });
  describe("mongodb", async () => {
    it("store notification data", async () => {});
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
