function cleanSpam() {
  var threads = GmailApp.search('in:spam older_than:7d');
  for (var i = 0; i < threads.length; i++) {
    threads[i].moveToTrash();
}
}

function cleanUnsubscribe() {
  var threads = GmailApp.search('label:unsubscribe older_than:7d');
  for (var i = 0; i < threads.length; i++) {
    threads[i].moveToTrash();
}
}

function archiveInbox() {
var threads = GmailApp.search('label:inbox is:read older_than:7d');
  for (var i = 0; i < threads.length; i++) {
    threads[i].moveToArchive();
}
}

function mailFunction(){
  cleanSpam();
  cleanUnsubscribe();
  archiveInbox();
}
