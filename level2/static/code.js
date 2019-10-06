function Post(message) { 
    this.message = message;
    this.date = (new Date()).getTime();
  }
   
function PostDB(defaultMessage) {
  // Initial message to display to users
  this._defaultMessage = defaultMessage || "";
  
  this.setup = function() {
    var defaultPost = new Post(defaultMessage);
    window.localStorage["postDB"] = JSON.stringify({
      "posts" : [defaultPost]
    });
  }
  
  this.save = function(message, callback) {
    var newPost = new Post(message);
    var allPosts = this.getPosts();
    allPosts.push(newPost);
    window.localStorage["postDB"] = JSON.stringify({
      "posts" : allPosts
    });
  
    callback();
    return false;
  }
  
  this.clear = function(callback) {
    this.setup();
  
    callback();
    return false;
  }
  
  this.getPosts = function() {
    return JSON.parse(window.localStorage["postDB"]).posts;
  }
  
  if(!window.localStorage["postDB"]) { 
    this.setup();
  }
}

  var defaultMessage = "Welcome!<br><br>This is your <i>personal</i>"
    + " stream. You can post anything you want here, especially "
    + "<span style='color: #f00ba7'>madness</span>.";

  var DB = new PostDB(defaultMessage);

  function displayPosts() {
    var containerEl = document.getElementById("post-container");
    containerEl.innerHTML = "";

    var posts = DB.getPosts();
    for (var i=0; i<posts.length; i++) {
      var html = '<table class="message"> <tr> <td valign=top> '
        + '</td> <td valign=top '
        + ' class="message-container"> <div class="shim"></div>';

      html += '<b>You</b>';
      html += '<span class="date">' + new Date(posts[i].date) + '</span>';
      html += "<blockquote>" + posts[i].message + "</blockquote";
      html += "</td></tr></table>"
      containerEl.innerHTML += html; 
    }
  }

  window.onload = function() { 
    document.getElementById('clear-form').onsubmit = function() {
      DB.clear(function() { displayPosts() });
      return false;
    }

    document.getElementById('post-form').onsubmit = function() {
      var message = document.getElementById('post-content').value;
      DB.save(message, function() { displayPosts() } );
      document.getElementById('post-content').value = "";
      return false;
    }

    displayPosts();
  }
