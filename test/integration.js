describe('application', async () => {
    describe('blackboard api', async() => {
        it("oauth blackboard authentication");
        it("make announcements GET request");
        it("make calendar GET request");
        it("make course announcements GET request");
        it("make course content GET request");
    });
    describe('mongodb', async() => {
        it("store notification data");
        it("fetch notification data");
        it("modify notification data");
        it("delete notification data");
    });
    describe('data sanitization', async() => {
        it("verify escape characters are filtered to prevent javascript injection");
        it("verify escape characters are filtered to prevent json injection (via mongo)")
    });
    describe('correct data display', async() => {
        it("verify correct amount of notifications is displayed");
        it("verify correct messages are displayed, based on time notification arrived");
        it("verify messages update for new notifications");
    });
});