      function chooseTab(num) {
        // Dynamically load the appropriate image.
        var html = "Image " + parseInt(num) + "<br>";
        html += "<img src='/static/images/cloud" + num + ".jpg' />";
        $('#tabContent').html(html);
 
        window.location.hash = num;
 
        // Select the current tab
        var tabs = document.querySelectorAll('.tab');
        for (var i = 0; i < tabs.length; i++) {
          if (tabs[i].id == "tab" + parseInt(num)) {
            tabs[i].className = "tab active";
            } else {
            tabs[i].className = "tab";
          }
        }
 
        // Tell parent we've changed the tab
        top.postMessage(self.location.toString(), "*");
      }
 
      window.onload = function() { 
        chooseTab(unescape(self.location.hash.substr(1)) || "1");
      }
 
      // Extra code so that we can communicate with the parent page
      window.addEventListener("message", function(event){
        if (event.source == parent) {
          chooseTab(unescape(self.location.hash.substr(1)));
        }
      }, false);

      $(document).ready(() => {
        $("#tab1").click(function() {
          // Dynamically load the appropriate image.
          //This is the fix
          var html = "Image " + parseInt('1') + "<br>";
          html += "<img src='/static/images/cloud" + '1' + ".jpg' />";
          $('#tabContent').html(html);
   
          window.location.hash = '1';
   
          // Select the current tab
          var tabs = document.querySelectorAll('.tab');
          for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].id == "tab" + parseInt('1')) {
              tabs[i].className = "tab active";
              } else {
              tabs[i].className = "tab";
            }
          }
   
          // Tell parent we've changed the tab
          top.postMessage(self.location.toString(), "*");
        })
        $("#tab2").click(function() {
          // Dynamically load the appropriate image.
          //This is the fix
          var html = "Image " + parseInt('2') + "<br>";
          html += "<img src='/static/images/cloud" + '2' + ".jpg' />";
          $('#tabContent').html(html);
   
          window.location.hash = '2';
   
          // Select the current tab
          var tabs = document.querySelectorAll('.tab');
          for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].id == "tab" + parseInt('2')) {
              tabs[i].className = "tab active";
              } else {
              tabs[i].className = "tab";
            }
          }
   
          // Tell parent we've changed the tab
          top.postMessage(self.location.toString(), "*");
        })
        $("#tab3").click(function() {
          // Dynamically load the appropriate image.
          //This is the fix
          var html = "Image " + parseInt('3') + "<br>";
          html += "<img src='/static/images/cloud" + '3' + ".jpg' />";
          $('#tabContent').html(html);
   
          window.location.hash = '3';
   
          // Select the current tab
          var tabs = document.querySelectorAll('.tab');
          for (var i = 0; i < tabs.length; i++) {
            if (tabs[i].id == "tab" + parseInt('3')) {
              tabs[i].className = "tab active";
              } else {
              tabs[i].className = "tab";
            }
          }
   
          // Tell parent we've changed the tab
          top.postMessage(self.location.toString(), "*");
        })
      })