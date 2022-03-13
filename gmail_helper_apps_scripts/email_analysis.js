
function get_raw_data() {
  var counts = {};
  
  var threads = GmailApp.search('older_than:300d newer_than:400d', 0, 400);
  for( var i = 0; i < threads.length; i++ ) {
    messages = threads[i].getMessages();
    for( var j = 0; j < messages.length; j++ ) {
      from_eml = messages[j].getFrom();
      counts[ from_eml ] = counts[ from_eml ] ? counts[ from_eml ] + 1 : 1;
    }
  }
  console.log( counts );
}

