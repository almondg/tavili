
/**
 * LOGIN UTILS
 * */

  // Load the SDK asynchronously
  (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) return;
    js = d.createElement(s); js.id = id;
    js.src = "http://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
  }(document, 'script', 'facebook-jssdk'));

  // This function is called when someone finishes with the Login
  // Button.  See the onlogin handler attached to it in the sample
  // code below.
  function checkLoginState() {
    FB.getLoginStatus(function(response) {
      statusChangeCallback(response);
    });
  }

//once we are logged in, use this function to get the home page of the site!
function loginWithID(response) {
      FB.api('/me?fields=id', function (response) {
          console.log("response is" + response.id);
          //window.location.href = 'home.html?id=' + response.id;
      });
  };

function logout_of_fb(){
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            FB.logout(function(response) {
                console.log("User logged out successfully!!!");
            });
        }
    });
}

  // This is called with the results from from FB.getLoginStatus().
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

function post(path, params, method) {
    method = method || "post"; // Set method to post by default if not specified.

    // The rest of this code assumes you are not using a library.
    // It can be made less wordy if you use one.
    var form = document.createElement("form");
    form.setAttribute("method", method);
    form.setAttribute("action", path);

    for(var key in params) {
        if(params.hasOwnProperty(key)) {
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
  console.log("sucessfully created item: " + item_data.product + " " + item_data.location);
}

// Overall viewmodel for this screen, along with initial state
function WishListViewModel() {
    var self = this;

    // Non-editable catalog data - would come from the server
    self.WishListDataArray = [
        { product: "item1", location: 'Israel'},
        { product: "item2", location: 'USA'},
        { product: "item3", location: 'France'},
        { product: "iphone4", location: 'UK' }
    ];

      /**
   *     self.WishListDataArray = somehow generate the array with source
   */

    // Editable data
    /**
     self.wish_list_items = ko.observableArray([
        new WishListItem({product: "item3", location: 'France'}),
        new WishListItem({product: "item2", location: 'USA'})
    ]);
     */

    self.wish_list_items = [];
    for (var i = 0; i < self.WishListDataArray.length; i++) {
        self.wish_list_items.push(new WishListItem(self.WishListDataArray[i]));
    }
}