setTimeout(function() { 
    console.log($('[name="next"]'))
    next = $('[name="nextdata"]').attr("content")
    next = next.substring(0, next.length-1)
    console.log(next)
    window.location = next; 
}, 1000);