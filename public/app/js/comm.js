function request(resource, options) {
  return $.ajax(options)
      .fail(function(jqXHR, textStatus, errorThrown) {
        var code = jqXHR.status;
        if (code == 401 || code == 403) {
          // Find the role of the login according to the path.
          var roleMatch = /^\/([a-zA-Z]*).*/.exec(
              document.location.pathname);
          var role = roleMatch ? roleMatch[1] : "user";

          // Determine the login app parameters.
          var next = exports.encodeURIComp(document.location.href);
          var err = "";
          if (code == 401) {
            err = exports.encodeURIComp(
                "Your session timed out.<br>" +
                "Please retype your credentials to continue.");
          } else if (code == 403) {
            err = exports.encodeURIComp(
                "You don't have the proper permission to view this.<br>" +
                "Please retype your credentials to enter.");
          }

          // Redirect to the correct login page.
          var url = ("/auth/" + role + "/#login" +
                     "?err=" + err + "&next=" + next);
          document.location.href = url;
        }
      });
};

// Initialize the server communications REST client.
var serverComm = new $.RestClient(
    "/api/", { request: request });

// Add the relevant paths.
serverComm.add("user");
serverComm.user.add("info");
serverComm.add("get_wishlist");

