function MainModel(source) {
  var self = this;

  // Set the model source from the given one.
  self.source = source;
  // Flag for blocking double initializations.
  self.isInitialized = false;

  /* -- Public Methods -- */

  /* Sets up the fields and models. */
  self.initialize = function () {
    // Prevent double initializations.
    if (self.isInitialized) {
      return;
    }

    self.userData = ko.observable();

    self.currentUserId = ko.observable();

    self.product = ko.observable();

    self.location = ko.observable();

    self.wishListModel = new WishListViewModel(self.source, self.currentUserId);

    // The current view to display.
    self.currentView = ko.observable("login");

    self.currentViewTitle = ko.pureComputed(function () {
      var title = self.currentView();
      title = title.split("_").join(" ");

      return title;
    });

    // The current User to display and pass on to other views.
    self.user = ko.observable(null);

    // Done initializing.
    self.isInitialized = true;
  };

  /* Fetches new data from the server and updates the model. */
  self.update = function () {
    initMainControllerUserData();
    getUserData();
    console.log("User Data Is: ");
    console.log(self.userData());

    finalCountry.subscribe(function () {
      console.log(extractUserData());
      self.source.user.login.create(extractUserData())
          .fail(function (error) {
            console.log("Error send login");
            console.log(error);
          })
          .done(function (data) {
            console.log("Success send login");
            console.log(data);
          })
    });
  };

  self.addWishItem = function () {
    self.source.add_to_wishlist.create({product: self.product, location: self.location, fb_id: self.userData().userId})
        .fail(function (error) {
          console.log(error);
        })
        .done(function (data) {
          if (!data || !data.result) {
            console.log("Error");
            return;
          }
          self.wishListModel.WishListDataArray(data.result);
        });
  };

  self.removeFromWishList = function (item) {
    var item_id = item.item_id;
    console.log("in removeFromWishList: " + item_id);
    self.source.remove_from_wishlist.create({item_id: item_id, fb_id: self.userData().userId})
        .fail(function (error) {
          console.log(error);
        })
        .done(function (data) {
          if (!data || !data.result) {
            console.log("Error");
            return;
          }
          self.wishListModel.WishListDataArray(data.result);
        });
    };

  function extractUserData() {
    var data = self.userData();
    var js =  {
      friendIds: String(data.friendIds()),
      posts: data.posts(),
      userId: data.userId(),
      numOfPosts: data.numOfPosts(),
      country: data.country(),
      address: data.address(),
      email: data.email(),
      name: data.name(),
    };

    console.log("!!!!!");
    console.log(js);
    console.log("!!!!!");
    return js
  }

  /**
   * LOGIN UTILS
   * */

  // Load the SDK asynchronously


  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {
    console.log("Inside Check Login State");
    FB.getLoginStatus(function (response) {
      self.statusChangeCallback(response);
    });
  };


  // This is called with the results from from FB.getLoginStatus().
  function statusChangeCallback(response) {
    /**if (response.status==='connected'){
        FB.logout(function(response) {
          // user is now logged out
          console.log("User logged out");
        });
      }*/

    console.log('statusChangeCallback');
    console.log(response);
    // The response object is returned with a status field that lets the
    // app know the current login status of the person.
    // Full docs on the response object can be found in the documentation
    // for FB.getLoginStatus().
    if (response.status === 'connected') {
      // Logged into your app and Facebook.

      loginWithID(response);

      //testAPI();
    } else if (response.status === 'not_authorized') {
      // The person is logged into Facebook, but not your app.
      //document.getElementById('status').innerHTML = 'Please log ' +
      //  'into this app.';
    } else {
      // The person is not logged into Facebook, so we're not sure if
      // they are logged into this app or not.
      //document.getElementById('status').innerHTML = 'Please log ' +
      //  'into Facebook.';
    }
  }

  function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for (var key in params) {
      if (params.hasOwnProperty(key)) {
        var hiddenField = document.createElement("input");
        hiddenField.setAttribute("type", "hidden");
        hiddenField.setAttribute("name", key);
        hiddenField.setAttribute("value", params[key]);

        form.appendChild(hiddenField);
      }
    }

    document.body.appendChild(form);
    form.submit();
  }


//////////////////////////////////////////////////////////////////////////////////////

// Class to represent a row in the wishlist
  function WishListItem(item_data) {
    var self = this;
    self.product = item_data.product;
    self.location = item_data.location;
    self.item_id = item_data.itemId;
    console.log("sucessfully created item: " + item_data.product + " " + item_data.location + " " + item_data.itemId);
  }

// Overall viewmodel for this screen, along with initial state
  function WishListViewModel(source, currentUserId) {
    var self = this;

    self.source = source;

    self.currentUserId = currentUserId;

    self.WishListDataArray = ko.observableArray([
      {product: "item1", location: 'Israel', item_id: "1"},
      {product: "item2", location: 'USA', item_id: "2"},
      {product: "item3", location: 'France', item_id: "3"},
      {product: "iphone4", location: 'UK', item_id: "4"}
    ]);

    self.update = function () {
      self.source.get_wishlist.read(String(self.currentUserId()))
        .fail(function (error) {
          console.log("Error occurred on: /api/get_wishlist on id: " + self.currentUserId());
          console.log(error);
        })
        .done(function (data) {
          if (!data || !data.result) {
            console.log("Error on data from: /api/get_wishlist with: " + self.currentUserId());
            console.log(data);
          }
          self.WishListDataArray(data.result);
        });

      self.wish_list_items = self.WishListDataArray().map(function (wish_item) {
        return new WishListItem(wish_item);
      });

      console.log(self.wish_list_items);

      self.WishListDataArray(self.wish_list_items);
    }

  }
}

//once we are logged in, use this function to get the home page of the site!
function loginWithID(response) {
  console.log("In loginWithID");
  getUserData();
  console.log(response);
  FB.api('/me?fields=id', function (response) {
    console.log(response);
    console.log("response is: " + response.id);
    window.location.href = "#home";
    mainController.model.currentUserId(response.id);
  });
}

function logout_of_fb() {
  FB.getLoginStatus(function (response) {
    if (response.status === 'connected') {
      FB.logout(function (response) {
        console.log("User logged out successfully!!!");
        window.location.href = "#login";
      });
    }
  });
  //window.location.href = 'templates/Login.html';
}

// This function is called when someone finishes with the Login
// Button.  See the onlogin handler attached to it in the sample
// code below.
function checkLoginState() {
  console.log("Inside Check Login State");
  FB.getLoginStatus(function (response) {
    self.statusChangeCallback(response);
  });
}


function statusChangeCallback(response) {

  console.log('statusChangeCallback');
  console.log(response);

  if (response.status === 'connected') {
    // Logged into your app and Facebook.
    loginWithID(response);
    //testAPI();
  } else if (response.status === 'not_authorized') {
    // The person is logged into Facebook, but not your app.
    //document.getElementById('status').innerHTML = 'Please log ' +
    //  'into this app.';
  } else {
    // The person is not logged into Facebook, so we're not sure if
    // they are logged into this app or not.
    //document.getElementById('status').innerHTML = 'Please log ' +
    //  'into Facebook.';
  }
}

