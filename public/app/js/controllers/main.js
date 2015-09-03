
function MainController() {
  var self = this;

  /* Initializes the controller, setting up routes and registering the model. */
  this.initialize = function() {
    if (!document.getElementById("main-page")) {
      return;
    }

    // Construct the underlying model and provide it with a fetcher object for
    // the server data.
    self.model = new MainModel(serverComm);
    self.model.initialize();

    // Register the model in the view.
    ko.applyBindings(self.model,
                     document.getElementById("main-page"));

    // Define the controller routes.
    crossroads.addRoute("/", function() {
      self.model.currentView("login");
    });
    crossroads.addRoute("login", function() {
      self.model.currentView("login");
    });
    crossroads.addRoute("home", function() {
      self.model.update();
      self.model.wishListModel.update();
      self.model.currentView("home");
    });
  };

  /* Updates the model and view by fetching data from the server. */
  self.update = function() {
    self.model.update();
  };

}

