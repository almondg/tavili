var comm_utils = require("../../common/app/lib/comm_utils");

// Initialize the server communications REST client.
var serverComm = new $.RestClient(
    "/api/", { request: comm_utils.request });

// Add the relevant paths.
serverComm.add("user");
serverComm.user.add("info");

module.exports = serverComm;
